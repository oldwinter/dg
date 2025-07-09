---
created: '2022-08-09'
cssclasses: ''
modified: '2023-03-14'
permalink: /🍀 Garden Tour/🧰 Library Guide/Tutorials/∑ Basic configuration of this
  library's obsidian and reasons.md
publish: true
published: '2025-07-09T09:41:28.656+08:00'
tags:
- moc
title: ∑ Basic configuration of this library's obsidian and reasons
---
Only select the configuration items that I personally think are important and explain the reasons.

## Editor

- Default view: Editing view
- Default editing mode: Live Preview
	- Use the what-you-see-is-what-you-get editing mode in 90% of scenarios. Switch to source mode for scenarios such as viewing dataview code and editing tables.
	- There is a user skill that has to be mentioned. In preview mode, clicking a link opens it in the current page, while using the cmd modifier key to click a link opens it in a new tab. However, there is a more common usage scenario: the current page is used as a MOC, clicking a link opens it in another tab, and clicking other links will not create a new tab page. You only need to "pin" the current file.
- Readable line length: On
	- This is the style of major mainstream websites such as sspai and notion. We don't want to be mavericks. And this width does provide a better reading experience.
- Strict line breaks: On
	- The habit of using 2 spaces + enter at the end of a markdown line has been passed down and cannot be changed. And if it is turned on, there will be no format problems when markdown is directly pasted to any other website. If it is turned off, some websites may not be compatible.

## Files and Links

- Automatically update internal links: On
	- One of the fundamental reasons for the smooth use of two-way links. Please do not rename files outside of obsidian, such as in the system file manager, as this will cause the links that refer to the file to not be automatically modified and become invalid.
- Default location for new notes: In the same folder as the current file.
	- [[🍀 Garden Tour/🧰 Library Guide/Tutorials/∑ This library's ACCESS workflow summary]] mentions that in order to avoid creating isolated files, it is only recommended to create new files directly in files (such as DailyNote and MOC files) through the two-way link syntax. In this way, the newly generated file is at least connected to the current file, and the newly generated file is in the same folder as the current file, making the file organization more orderly. So this configuration item is needed.
- New link format: Shortest path when possible
	- This form guides us to ignore the path and let the link become the first citizen of our notes, that is, [[🍀 Garden Tour/🧰 Library Guide/Tutorials/Link first]]. If you are reluctant to part with the traditional folder, that is, the [[folder first]] mode, then change to other options.
- Use wikilinks: On
	- That is, the form of [[Cards/wikilink]]: `[[]]`. It is more convenient to use. You can search for everything in the library with two square brackets, which is cool. However, traditional blogs such as hugo, jekyll, gatsby, etc. still mainly support the `[]()` format. But don't worry, if you need to use it, you can always switch to an automatic conversion solution.
- Default location for new attachments: In the folder specified below
	- When taking notes, please let the text be the first citizen with 99% occupancy. After other pictures, videos, pdfs, etc. are placed in one place, you can give full play to the specialty of obsidian's [[Cards/local first]], for example, use software such as devonthink or billfish to uniformly manage these non-md files.

## Appearance

- For theme usage, see [[🍀 Garden Tour/🧰 Library Guide/Tutorials/Themes used in this library and why]].
- Font usage.
	- I have passed the age of tossing and turning. For me, the default font is often the most suitable for me. [[80% default first, 20% deep customization]].
- CSS snippets.
	- Menu bar customization: At present, the forward and back buttons in the upper left corner of the menu bar are mainly removed, because this group of buttons is more logical to use in the page menu bar.
		- [[2023-02-27]]: The 1.0 version of ob really removed the forward and back buttons in the upper left corner, which is exactly the same as my original idea.
	- Hide xx files: There are some LICENSE files or other dependencies in the root directory that you don't want to see at ordinary times.
	- supercharged-links-gen: The plugin automatically generates emoji and colors for various specific internal links, which can help you find important content faster when searching.

## Shortcut keys

- See [[🍀 Garden Tour/🧰 Library Guide/Tutorials/Commonly used shortcut keys and their functions in this library]]

## Core plugins

- [[🍀 Garden Tour/🧰 Library Guide/Tutorials/Obsidian core plugins enabled in this library and why]]

## Third-party plugins

> If you are confused and don't know where to start, you might as well turn off the safe mode first, and then you will find that this library seems to be able to be used normally without third-party plugins. Hahaha.

- [[🍀 Garden Tour/🧰 Library Guide/Tutorials/Third-party obsidian plugins used in this library and why]]
- [[🍀 Garden Tour/🧰 Library Guide/Tutorials/Plugins that need to be configured separately in this library]] 