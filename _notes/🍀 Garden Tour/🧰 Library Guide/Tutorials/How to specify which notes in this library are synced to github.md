---
created: '2022-09-03'
cssclasses: ''
modified: '2023-03-14'
permalink: /🍀 Garden Tour/🧰 Library Guide/Tutorials/How to specify which notes in
  this library are synced to github.md
publish: true
published: '2025-07-09T02:06:30.218+08:00'
title: How to specify which notes in this library are synced to github
---
Discuss scenarios based on 2 dimensions:

- Whether the github repository is private or public.
- Whether the scope of note upload is specified by a whitelist mechanism or a blacklist mechanism.

This library, or rather myself, uses a public repository because I want to share it with you. Secondly, I want to share far more notes than I don't want to share, so it's a blacklist mechanism: by default, all notes are uploaded and shared, and only a few notes involving personal privacy are not uploaded.

The method is very simple, just use the .gitignore file. You can directly open this library with vscode, and there is a .gitignore file in the root directory. For the syntax, see: [[gitignore syntax]]

If you want to use a whitelist mechanism: the most intuitive and simple idea is to only perform git add, commit and push operations on these notes. 