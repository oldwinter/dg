#!/usr/bin/env python3
"""
数字花园笔记同步脚本
自动从 dg3 仓库同步 content 目录到当前仓库的 _notes 目录
并自动处理 frontmatter 添加 title 字段
"""

import os
import sys
import shutil
import subprocess
import re
import yaml
from pathlib import Path
import tempfile
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class NotesSync:
    def __init__(self, source_repo="https://github.com/oldwinter/dg3.git", target_dir="_notes"):
        self.source_repo = source_repo
        self.target_dir = Path(target_dir)
        self.temp_dir = None
        
    def __enter__(self):
        self.temp_dir = tempfile.mkdtemp(prefix="dg3_sync_")
        logger.info(f"创建临时目录: {self.temp_dir}")
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.temp_dir and os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
            logger.info(f"清理临时目录: {self.temp_dir}")
    
    def clone_source_repo(self):
        """克隆源仓库到临时目录"""
        if not self.temp_dir:
            logger.error("临时目录未初始化")
            return False
            
        logger.info(f"克隆源仓库: {self.source_repo}")
        try:
            subprocess.run([
                "git", "clone", "--depth", "1", 
                self.source_repo, 
                os.path.join(self.temp_dir, "source")
            ], check=True, capture_output=True)
            logger.info("源仓库克隆成功")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"克隆失败: {e.stderr.decode()}")
            return False
    
    def get_title_from_filename(self, filepath):
        """从文件名提取标题"""
        filename = Path(filepath).stem  # 去掉扩展名
        # 直接使用完整的文件名作为标题，保留所有特殊前缀
        return filename
    
    def parse_frontmatter(self, content):
        """解析 frontmatter"""
        # 检查是否有 frontmatter
        if not content.startswith('---'):
            return {}, content
        
        # 找到第二个 ---
        try:
            end_index = content.index('---', 3)
            frontmatter_text = content[3:end_index].strip()
            body = content[end_index + 3:].lstrip('\n')
            
            # 解析 YAML
            if frontmatter_text:
                # 处理特殊的 JSON 格式 frontmatter
                if frontmatter_text.startswith('{') and frontmatter_text.endswith('}'):
                    import json
                    frontmatter = json.loads(frontmatter_text)
                else:
                    frontmatter = yaml.safe_load(frontmatter_text) or {}
            else:
                frontmatter = {}
                
            return frontmatter, body
        except (ValueError, yaml.YAMLError, json.JSONDecodeError) as e:
            logger.warning(f"解析 frontmatter 失败: {e}")
            return {}, content
    
    def add_title_to_frontmatter(self, filepath, content):
        """为 frontmatter 添加 title 字段"""
        frontmatter, body = self.parse_frontmatter(content)
        
        # 如果已经有 title 字段，保持不变
        if 'title' not in frontmatter or not frontmatter['title']:
            frontmatter['title'] = self.get_title_from_filename(filepath)
            logger.debug(f"为 {filepath} 添加标题: {frontmatter['title']}")
        
        # 重新构建文件内容
        if frontmatter:
            yaml_content = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False)
            new_content = f"---\n{yaml_content}---\n{body}"
        else:
            # 如果没有 frontmatter，创建一个新的
            title = self.get_title_from_filename(filepath)
            new_content = f"---\ntitle: {title}\n---\n{content}"
        
        return new_content
    
    def process_markdown_file(self, source_path, target_path):
        """处理单个 markdown 文件"""
        try:
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 添加或更新 title 字段
            processed_content = self.add_title_to_frontmatter(source_path, content)
            
            # 确保目标目录存在
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入处理后的内容
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(processed_content)
            
            logger.debug(f"处理文件: {source_path} -> {target_path}")
            return True
            
        except Exception as e:
            logger.error(f"处理文件失败 {source_path}: {e}")
            return False
    
    def sync_content(self):
        """同步内容从源仓库到目标目录（增量同步）"""
        if not self.temp_dir:
            logger.error("临时目录未初始化")
            return False
            
        source_content_dir = Path(self.temp_dir) / "source" / "content"
        
        if not source_content_dir.exists():
            logger.error(f"源内容目录不存在: {source_content_dir}")
            return False
        
        logger.info(f"开始增量同步内容到: {self.target_dir}")
        
        # 确保目标目录存在
        self.target_dir.mkdir(parents=True, exist_ok=True)
        
        # 统计计数器
        total_files = 0
        processed_files = 0
        copied_files = 0
        updated_files = 0
        deleted_files = 0
        
        # 收集源目录中的所有文件路径（相对路径）
        source_files = set()
        for source_file in source_content_dir.rglob('*'):
            if source_file.is_file():
                rel_path = source_file.relative_to(source_content_dir)
                source_files.add(rel_path)
        
        # 收集目标目录中的所有文件路径（相对路径）
        target_files = set()
        if self.target_dir.exists():
            for target_file in self.target_dir.rglob('*'):
                if target_file.is_file():
                    rel_path = target_file.relative_to(self.target_dir)
                    target_files.add(rel_path)
        
        # 找出需要删除的文件（在目标目录中存在，但源目录中不存在）
        files_to_delete = target_files - source_files
        
        # 删除不再存在的文件
        for rel_path in files_to_delete:
            target_file = self.target_dir / rel_path
            try:
                target_file.unlink()
                deleted_files += 1
                logger.info(f"删除文件: {rel_path}")
                
                # 如果父目录变空了，也删除它
                parent = target_file.parent
                if parent != self.target_dir and not any(parent.iterdir()):
                    parent.rmdir()
                    logger.debug(f"删除空目录: {parent.relative_to(self.target_dir)}")
            except Exception as e:
                logger.error(f"删除文件失败 {rel_path}: {e}")
        
        # 处理需要同步的文件
        for source_file in source_content_dir.rglob('*'):
            if source_file.is_file():
                total_files += 1
                
                # 计算相对路径
                rel_path = source_file.relative_to(source_content_dir)
                target_file = self.target_dir / rel_path
                
                # 检查文件是否需要更新
                need_update = True
                if target_file.exists():
                    # 比较修改时间
                    source_mtime = source_file.stat().st_mtime
                    target_mtime = target_file.stat().st_mtime
                    
                    # 对于markdown文件，还要比较内容（因为我们会修改frontmatter）
                    if source_file.suffix.lower() == '.md':
                        need_update = True  # markdown文件总是需要处理（可能需要更新frontmatter）
                    else:
                        need_update = source_mtime > target_mtime
                
                if need_update:
                    if source_file.suffix.lower() == '.md':
                        # 处理 markdown 文件
                        if self.process_markdown_file(source_file, target_file):
                            processed_files += 1
                            if target_file.relative_to(self.target_dir) in target_files:
                                updated_files += 1
                                logger.debug(f"更新文件: {rel_path}")
                            else:
                                copied_files += 1
                                logger.debug(f"新增文件: {rel_path}")
                    else:
                        # 直接复制其他文件
                        target_file.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(source_file, target_file)
                        processed_files += 1
                        if target_file.relative_to(self.target_dir) in target_files:
                            updated_files += 1
                            logger.debug(f"更新文件: {rel_path}")
                        else:
                            copied_files += 1
                            logger.debug(f"新增文件: {rel_path}")
                else:
                    processed_files += 1  # 文件未变更，但计入处理数量
        
        logger.info(f"同步完成: 总文件 {total_files}, 成功处理 {processed_files}")
        logger.info(f"统计: 新增 {copied_files}, 更新 {updated_files}, 删除 {deleted_files}")
        return processed_files == total_files
    
    def run(self):
        """执行完整的同步流程"""
        logger.info("开始笔记同步流程")
        
        # 1. 克隆源仓库
        if not self.clone_source_repo():
            return False
        
        # 2. 同步内容
        if not self.sync_content():
            return False
        
        logger.info("笔记同步完成！")
        return True


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="数字花园笔记同步脚本")
    parser.add_argument("--source", default="https://github.com/oldwinter/dg3.git",
                       help="源仓库地址")
    parser.add_argument("--target", default="_notes",
                       help="目标目录")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="详细日志输出")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        with NotesSync(args.source, args.target) as sync:
            success = sync.run()
            sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        logger.info("用户中断操作")
        sys.exit(1)
    except Exception as e:
        logger.error(f"发生未预期错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 