# 数字花园笔记自动同步

这个系统可以自动从 `https://github.com/oldwinter/dg3.git` 仓库的 `content` 目录同步内容到当前仓库的 `_notes` 目录，并自动处理frontmatter添加title字段。

## 功能特性

- ✅ 自动克隆源仓库获取最新内容
- ✅ 批量处理markdown文件，自动添加title字段到frontmatter
- ✅ 支持JSON和YAML格式的frontmatter
- ✅ 保持现有title字段不变，仅为缺失title的文件添加
- ✅ 自动检测源仓库更新，避免重复同步
- ✅ GitHub Actions自动化工作流
- ✅ 完整的日志记录和错误处理

## 本地使用

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 手动执行同步

```bash
# 基本同步
python sync_notes.py

# 详细日志输出
python sync_notes.py --verbose

# 自定义源仓库和目标目录
python sync_notes.py --source https://github.com/your-repo.git --target custom_notes
```

### 3. 脚本参数

- `--source`: 源仓库地址 (默认: `https://github.com/oldwinter/dg3.git`)
- `--target`: 目标目录 (默认: `_notes`)
- `--verbose` / `-v`: 启用详细日志输出

## 自动化部署

### GitHub Actions 配置

本系统包含了完整的 GitHub Actions 工作流配置 (`.github/workflows/sync-notes.yml`)，支持：

1. **定时同步**: 每小时自动检查源仓库更新
2. **手动触发**: 在GitHub Actions页面手动运行
3. **代码变更触发**: 当同步脚本或配置文件更改时自动运行

### 配置要求

**🎉 零配置！** 由于源仓库是公开的，无需任何额外配置：

- ✅ 使用 HTTPS 克隆，无需 SSH 密钥
- ✅ GitHub Actions 自动使用内置 GITHUB_TOKEN
- ✅ 开箱即用，推送后立即生效

## 工作原理

### 1. 同步流程

1. **检查更新**: 获取源仓库最新commit hash，与上次同步记录比较
2. **克隆源仓库**: 使用shallow clone减少下载时间
3. **处理文件**: 
   - 对所有`.md`文件解析frontmatter
   - 为缺失title字段的文件从文件名生成title
   - 支持JSON和YAML两种frontmatter格式
4. **同步内容**: 将处理后的文件复制到目标目录
5. **提交变更**: 自动提交并推送到当前仓库

### 2. Title生成规则

- 使用文件名（去除扩展名）作为基础title
- 移除特殊前缀字符: `∑»§_` 和数字、日期前缀
- 保持现有title字段不变
- 如果清理后为空，使用原始文件名

### 3. 安全特性

- 使用临时目录，自动清理
- 完整的错误处理和日志记录
- 仅在检测到实际变更时才提交
- 支持增量同步，避免重复工作

## 目录结构

同步后的目录结构会保持源仓库的组织方式：

```
_notes/
├── 📥 Inbox/
├── 🍀 花园导览/
├── 🍀 Garden Tour/
├── Spaces/
├── Sources/
├── Extras/
├── Cards/
├── Calendar/
├── Atlas/
└── 其他文件...
```

## 故障排除

### 常见问题

1. **Python依赖问题**
   - 使用 `pip install -r requirements.txt` 安装依赖
   - 确保Python版本 >= 3.8

2. **Git权限问题**
   - 确保GitHub Token有仓库写入权限
   - 检查工作流权限设置

3. **网络连接问题**
   - 检查是否能访问 GitHub
   - 确认源仓库地址正确

### 调试步骤

1. 查看GitHub Actions运行日志
2. 本地运行 `python sync_notes.py --verbose` 获取详细输出
3. 检查 `.last_sync_commit` 文件内容
4. 验证网络连接和仓库地址

## 定制化

### 修改同步频率

在 `.github/workflows/sync-notes.yml` 中修改 cron 表达式：

```yaml
schedule:
  - cron: '0 */6 * * *'  # 每6小时同步一次
```

### 修改Title生成规则

在 `sync_notes.py` 的 `get_title_from_filename` 方法中自定义规则。

### 添加文件过滤

在 `sync_content` 方法中添加文件过滤逻辑，跳过特定文件或目录。 