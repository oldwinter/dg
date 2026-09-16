# oldwinter 的公开数字花园

这是 [oldwinter/dg](https://github.com/oldwinter/dg) 的 Jekyll 发布仓，不是上游模板演示站。第一次进来请先本地预览，再从 `_notes/` 和 [🍀 花园导览](_notes/🍀%20花园导览/🍀%20花园导览.md) 往下走。

不要把上游模板预览当成这个花园。

## 本地预览

需要 Ruby（可用 mise）和 Bundler：

```bash
brew install mise
mise install ruby
bundle
bundle exec jekyll serve
```

更短的本机命令也写在 [README-new.md](README-new.md)。

## 笔记在哪

- [`_notes/`](_notes/)：花园正文
- [`_pages/index.md`](_pages/index.md)：站点首页（时间线）
- [🍀 花园导览](_notes/🍀%20花园导览/🍀%20花园导览.md)：逛花园的地图

笔记从 [oldwinter/dg3](https://github.com/oldwinter/dg3) 的 `content` 同步进 `_notes/`。

## 怎么同步

步骤在 [SYNC_README.md](SYNC_README.md)：

```bash
pip install -r requirements.txt
python sync_notes.py
```

## 模板致谢

站点壳来自 [Maxime Vaillancourt 的 Jekyll digital garden 模板](https://github.com/maximevaillancourt/digital-garden-jekyll-template)。通用教程只说明壳怎么来的，不是本仓入口。

## License

源码沿用 [MIT](LICENSE)。
