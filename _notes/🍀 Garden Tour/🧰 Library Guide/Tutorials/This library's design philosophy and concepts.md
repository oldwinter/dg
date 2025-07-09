---
created: '2022-06-29'
cssclasses: ''
modified: '2023-03-14'
permalink: /🍀 Garden Tour/🧰 Library Guide/Tutorials/This library's design philosophy
  and concepts.md
publish: true
published: '2025-07-09T13:07:49.961+08:00'
title: This library's design philosophy and concepts
---
up:: [[🍀 Garden Tour/🧰 Library Guide/🧰 Library Usage Guide]]
x: [[🍀 Garden Tour/🧰 Library Guide/Tutorials/Core principles to follow when using this library]]

## Design Philosophy and Concepts

- Focus on [[Reading, Note-taking and Writing]], not information clipping, not schedule management, not cloud collaboration, not [[Cards/all in one]].
- [[🍀 Garden Tour/🧰 Library Guide/Tutorials/Link first]]. Try to make every file have a link with other files. The file size can be as small as an atomic sentence or as large as a long article.
- Only use the standard syntax of markdown + `[[` syntax, and pay attention to the text content itself. Try not to use callout, try not to use aliases, try not to use [[block reference]], and try not to introduce css for layout and beautification.
	- Update, callout syntax is a markdown syntax extension that Microsoft also uses. Even if other md platforms do not support it, it will at most be downgraded to a reference format, and to a certain extent, it enriches and beautifies the layout, so I started to use it.
- Out of the box and progressive mastery. This library can be opened in safe mode to turn off all third-party plugins, and at least 90% of the functions are still available. This is out of the box. Then you can turn on the plugins in turn and use them with [[🍀 Garden Tour/🧰 Library Guide/Tutorials/∑ This library's ACCESS workflow summary]] to progressively master the remaining 20%. My philosophy follows [[80% default first, 20% deep customization]].
- Unify the use logic of [[Comparison and selection of shortcut keys, icons, and command lines]]. Only remember the super high-frequency shortcut keys, try to achieve the purpose through the command line, and use icons less.
- Unless necessary, do not customize. For example, emoji and snippet both use system-level input solutions, for example, text editing shortcut keys are consistent with [[Spaces/3-Resource/Software-Sorting/macos-software/VSCode]], for example, regular git backup uses system-level scheduled tasks, for example, translation uses system-level translation software.
- Follow the traditional [[folders and tags]] note organization method to give yourself a sense of security. Use the modern [[Atlas/MOCs/∑ MOCs]] note organization method to reduce the pressure of structuring. See [[5 elements of organizing notes in obsidian]] and [[ACCESS Note Organization Method]].
- [[Use heavy tools lightly]], for more detailed analysis, see [[The unavoidable shortcomings of obsidian and their solutions]].
	- At present, obsidian's batch editing and batch file management capabilities are very weak, and they are still weak even with plugins installed, so I use [[Spaces/3-Resource/Software-Sorting/macos-software/VSCode]] to open the library for processing. vscode's capabilities in this area are already quite mature.
	- Do not do any iframe embedding, because iframe has no substantial linkage, and can essentially be better replaced by the system's window management capabilities.
	- For [[mind map]], epub and pdf reading, audio and video, pictures, etc., obsidian related plugins are not as easy to use as independent software. It can be linked with obsidian through [[Cards/URL scheme]]. 