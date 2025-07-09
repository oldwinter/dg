---
created: '2022-07-16'
cssclasses: ''
modified: '2023-03-14'
permalink: /🍀 Garden Tour/🧰 Library Guide/Tutorials/Plugins that need to be configured
  separately in this library.md
publish: true
published: '2025-07-09T02:09:25.061+08:00'
title: Plugins that need to be configured separately in this library
---
up:: [[🍀 Garden Tour/🧰 Library Guide/🧰 Library Usage Guide]]

- [[Cards/Remotely Save]] plugin, it is strongly recommended to use it with [[S3 - Object Storage Service]], [[Alibaba Cloud]], [[Tencent Cloud]] are all acceptable, the synchronization speed is extremely fast, it can be completed within 2 seconds daily, and the cost is only a few cents a month. The S3 bucket can also be used as an image bed. My configuration screenshot is as follows, and the parameters outside the screenshot are all set to the default values.
	- [[2022-10-05]] update, I have switched to using the official sync, so this plugin is deleted from the library. If you need to continue using it, please download it yourself.
	- ![](<https://img2.oldwinter.top/截屏2022-08-29 下午7.59.39.png>)
- [[Cards/Weread Plugin]] plugin, after synchronizing the notes on WeChat Reading, you can directly use `[[` to complete the quick input in daily writing, and you no longer have to type the book title or author name of the book you have read word by word. Since the configuration file contains sensitive token information, I cannot upload it. The personal related configuration is as follows, and the template used is [[WeChat Reading Sync Template]].
	- ![](<https://img2.oldwinter.top/截屏2022-08-29 下午7.57.01.png>)
- [[🍀 花园导览/🧰 本库指南/Obsidian/Plugins/Image auto upload Plugin]] plugin, linked with [[Spaces/3-Resource/Software-Sorting/macos-software/PicGo]]. Automatically upload the pictures in the clipboard to the image bed. If you need to use an image bed, you don't need to change the plugin, you just need to download [[Spaces/3-Resource/Software-Sorting/macos-software/PicGo]] and configure it accordingly.
- [[local RESTApi]] plugin, expose obsidian as a server, other software can actively send requests to it, so as to automatically complete operations such as creating notes, updating notes, etc. in the background. At present, I mainly use it to be called by [[Sources/GithubStarsSync/simpread]]. If you don't understand what I said above, just ignore this plugin. 