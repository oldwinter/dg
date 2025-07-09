---
aliases: non-md resource file management attachment management
created: '2022-08-07'
cssclasses: ''
modified: '2023-03-14'
permalink: /🍀 Garden Tour/🧰 Library Guide/Tutorials/» This library's non-md resource
  file management workflow.md
publish: true
published: '2025-07-09T02:00:46.570+08:00'
tags:
- AI-generated
- workflow
- file-management
title: » This library's non-md resource file management workflow
---
# Non-MD Resource File Management Workflow

This guide aims to provide you with a clear and efficient method for managing non-Markdown format resource files (such as images, PDFs, videos, audio, scripts, etc.) in your Obsidian repository.

The core goal is to leverage Obsidian's powerful linking and backlinking features to ensure that every resource can be effectively tracked and its specific reference location within the knowledge base can be understood.

## 1. Core Principles

- **Unified storage**: Store most non-MD resource files centrally in the `Extras/Attachments/` directory.
- **Categorized management**: Create subfolders within `Extras/Attachments/` based on file type, such as `Images`, `PDFs`, `Videos`, `Audio`, `Scripts`, etc.
- **Link first**: Always use Markdown links `[[]]` or embed `![[]]` to reference resources, instead of copying files.
- **Clear naming**: Set a clear and readable name for the file for easy searching and identification.

## 2. Storage Location Strategy

### a. Main repository: `Extras/Attachments/`

This is the "central station" for all general resource files in your repository.

- **`Extras/Attachments/Images/`**: Stores general images.
- **`Extras/Attachments/PDFs/`**: Stores PDF documents.
- **`Extras/Attachments/Videos/`**: Stores video files.
- **`Extras/Attachments/Audio/`**: Stores audio files.
- **`Extras/Attachments/Scripts/`**: Stores code scripts.
- **`Extras/Attachments/Icons/`**: Stores icon files, which you are already practicing.
- **`Extras/Attachments/Other/`**: Stores other uncategorized files.

**Automation configuration suggestion**:
In Obsidian's settings, find `Files & Links` -> `Default location for new attachments`, set it to `In the folder specified below`, and fill in the path `Extras/Attachments` below. In this way, when you paste an image or drag and drop a file, it will be automatically saved to this location.

### b. Specific context storage

For resources that are highly bound to a specific project or theme, they can be stored in their corresponding directory.

- **`Atlas/Draws/`**: Used to store Excalidraw or Canvas drawing files, which are part of your core knowledge map.
- **`Spaces/1-Project/Project Name/assets/`**: If a resource is **only** used for a specific project, it can be stored with the project, which is convenient for the overall migration or archiving of the project.

## 3. Reference Method

To make backlinks work, be sure to use the following methods to reference your resources:

- **Embed image**: `![[my-image.png]]`
- **Embed a specific page of a PDF**: `![[my-document.pdf#page=3]]`
- **Link to file**: `[[my-document.pdf]]`
- **Link and set display text**: `[[my-document.pdf|View my document]]`

In this way, you can clearly see which notes each resource file is referenced by in the "Backlinks" panel on the right.

## 4. Create "Metadata Notes" for Resource Files (Optional but Recommended)

For some important resource files (such as a complex design draft, an important PDF report), you can create a `.md` note with the same name to record its metadata.

**Example**:
You have an important chart file `2025-market-analysis.png`.

1.  Create a `2025-market-analysis.md` file next to it.
2.  In this Markdown file, you can record:
    - The source and author of the file.
    - A brief description of the file.
    - Related thoughts and comments.
    - Use `tags` and `aliases` to increase discoverability.
    - Finally, embed the image `![[2025-market-analysis.png]]`.

```markdown
---
tags: [report, market-analysis, AI-generated]
aliases: [2025 Market Analysis Chart]
source: "A certain research institution"
---
# 2025 Market Analysis Chart

This chart shows the expected market share distribution of the AI market in 2025.

**Core viewpoints**:
- The growth in field A is the most significant.
- Field B is tending towards saturation.

![[2025-market-analysis.png]]

---
*Related notes: [[AI Industry Observation]]*
```

The advantage of this is that your resource file itself has become a knowledge node that can be deeply searched and associated, not just an attachment.

## 5. Summary

| Scenario | Recommended practice |
| :--- | :--- |
| General images, PDFs, audio and video | Store them in the classified folders under `Extras/Attachments/` and reference them through `
# Non-MD Resource File Management Workflow

This guide aims to provide you with a clear and efficient method for managing non-Markdown format resource files (such as images, PDFs, videos, audio, scripts, etc.) in your Obsidian repository.

The core goal is to leverage Obsidian's powerful linking and backlinking features to ensure that every resource can be effectively tracked and its specific reference location within the knowledge base can be understood.

## 1. Core Principles

- **Unified storage**: Store most non-MD resource files centrally in the `Extras/Attachments/` directory.
- **Categorized management**: Create subfolders within `Extras/Attachments/` based on file type, such as `Images`, `PDFs`, `Videos`, `Audio`, `Scripts`, etc.
- **Link first**: Always use Markdown links `[[]]` or embed `![[]]` to reference resources, instead of copying files.
- **Clear naming**: Set a clear and readable name for the file for easy searching and identification.

## 2. Storage Location Strategy

### a. Main repository: `Extras/Attachments/`

This is the "central station" for all general resource files in your repository.

- **`Extras/Attachments/Images/`**: Stores general images.
- **`Extras/Attachments/PDFs/`**: Stores PDF documents.
- **`Extras/Attachments/Videos/`**: Stores video files.
- **`Extras/Attachments/Audio/`**: Stores audio files.
- **`Extras/Attachments/Scripts/`**: Stores code scripts.
- **`Extras/Attachments/Icons/`**: Stores icon files, which you are already practicing.
- **`Extras/Attachments/Other/`**: Stores other uncategorized files.

**Automation configuration suggestion**:
In Obsidian's settings, find `Files & Links` -> `Default location for new attachments`, set it to `In the folder specified below`, and fill in the path `Extras/Attachments` below. In this way, when you paste an image or drag and drop a file, it will be automatically saved to this location.

### b. Specific context storage

For resources that are highly bound to a specific project or theme, they can be stored in their corresponding directory.

- **`Atlas/Draws/`**: Used to store Excalidraw or Canvas drawing files, which are part of your core knowledge map.
- **`Spaces/1-Project/Project Name/assets/`**: If a resource is **only** used for a specific project, it can be stored with the project, which is convenient for the overall migration or archiving of the project.

## 3. Reference Method

To make backlinks work, be sure to use the following methods to reference your resources:

- **Embed image**: `![[my-image.png]]`
- **Embed a specific page of a PDF**: `![[my-document.pdf#page=3]]`
- **Link to file**: `[[my-document.pdf]]`
- **Link and set display text**: `[[my-document.pdf|View my document]]`

In this way, you can clearly see which notes each resource file is referenced by in the "Backlinks" panel on the right.

## 4. Create "Metadata Notes" for Resource Files (Optional but Recommended)

For some important resource files (such as a complex design draft, an important PDF report), you can create a `.md` note with the same name to record its metadata.

**Example**:
You have an important chart file `2025-market-analysis.png`.

1.  Create a `2025-market-analysis.md` file next to it.
2.  In this Markdown file, you can record:
    - The source and author of the file.
    - A brief description of the file.
    - Related thoughts and comments.
    - Use `tags` and `aliases` to increase discoverability.
    - Finally, embed the image `![[2025-market-analysis.png]]`.

```markdown
---
tags: [report, market-analysis, AI-generated]
aliases: [2025 Market Analysis Chart]
source: "A certain research institution"
---
# 2025 Market Analysis Chart

This chart shows the expected market share distribution of the AI market in 2025.

**Core viewpoints**:
- The growth in field A is the most significant.
- Field B is tending towards saturation.

![[2025-market-analysis.png]]

---
*Related notes: [[AI Industry Observation]]*
```

The advantage of this is that your resource file itself has become a knowledge node that can be deeply searched and associated, not just an attachment.

## 5. Summary

| Scenario | Recommended practice |
| :--- | :--- |
| General images, PDFs, audio and video | Store them in the classified folders under `Extras/Attachments/` and reference them through `
# Non-MD Resource File Management Workflow

This guide aims to provide you with a clear and efficient method for managing non-Markdown format resource files (such as images, PDFs, videos, audio, scripts, etc.) in your Obsidian repository.

The core goal is to leverage Obsidian's powerful linking and backlinking features to ensure that every resource can be effectively tracked and its specific reference location within the knowledge base can be understood.

## 1. Core Principles

- **Unified storage**: Store most non-MD resource files centrally in the `Extras/Attachments/` directory.
- **Categorized management**: Create subfolders within `Extras/Attachments/` based on file type, such as `Images`, `PDFs`, `Videos`, `Audio`, `Scripts`, etc.
- **Link first**: Always use Markdown links `[[]]` or embed `![[]]` to reference resources, instead of copying files.
- **Clear naming**: Set a clear and readable name for the file for easy searching and identification.

## 2. Storage Location Strategy

### a. Main repository: `Extras/Attachments/`

This is the "central station" for all general resource files in your repository.

- **`Extras/Attachments/Images/`**: Stores general images.
- **`Extras/Attachments/PDFs/`**: Stores PDF documents.
- **`Extras/Attachments/Videos/`**: Stores video files.
- **`Extras/Attachments/Audio/`**: Stores audio files.
- **`Extras/Attachments/Scripts/`**: Stores code scripts.
- **`Extras/Attachments/Icons/`**: Stores icon files, which you are already practicing.
- **`Extras/Attachments/Other/`**: Stores other uncategorized files.

**Automation configuration suggestion**:
In Obsidian's settings, find `Files & Links` -> `Default location for new attachments`, set it to `In the folder specified below`, and fill in the path `Extras/Attachments` below. In this way, when you paste an image or drag and drop a file, it will be automatically saved to this location.

### b. Specific context storage

For resources that are highly bound to a specific project or theme, they can be stored in their corresponding directory.

- **`Atlas/Draws/`**: Used to store Excalidraw or Canvas drawing files, which are part of your core knowledge map.
- **`Spaces/1-Project/Project Name/assets/`**: If a resource is **only** used for a specific project, it can be stored with the project, which is convenient for the overall migration or archiving of the project.

## 3. Reference Method

To make backlinks work, be sure to use the following methods to reference your resources:

- **Embed image**: `![[my-image.png]]`
- **Embed a specific page of a PDF**: `![[my-document.pdf#page=3]]`
- **Link to file**: `[[my-document.pdf]]`
- **Link and set display text**: `[[my-document.pdf|View my document]]`

In this way, you can clearly see which notes each resource file is referenced by in the "Backlinks" panel on the right.

## 4. Create "Metadata Notes" for Resource Files (Optional but Recommended)

For some important resource files (such as a complex design draft, an important PDF report), you can create a `.md` note with the same name to record its metadata.

**Example**:
You have an important chart file `2025-market-analysis.png`.

1.  Create a `2025-market-analysis.md` file next to it.
2.  In this Markdown file, you can record:
    - The source and author of the file.
    - A brief description of the file.
    - Related thoughts and comments.
    - Use `tags` and `aliases` to increase discoverability.
    - Finally, embed the image `![[2025-market-analysis.png]]`.

```markdown
---
tags: [report, market-analysis, AI-generated]
aliases: [2025 Market Analysis Chart]
source: "A certain research institution"
---
# 2025 Market Analysis Chart

This chart shows the expected market share distribution of the AI market in 2025.

**Core viewpoints**:
- The growth in field A is the most significant.
- Field B is tending towards saturation.

![[2025-market-analysis.png]]

---
*Related notes: [[AI Industry Observation]]*
```

The advantage of this is that your resource file itself has become a knowledge node that can be deeply searched and associated, not just an attachment.

## 5. Summary

| Scenario | Recommended practice |
| :--- | :--- |
| General images, PDFs, audio and video | Store them in the classified folders under `Extras/Attachments/` and reference them through `
# Non-MD Resource File Management Workflow

This guide aims to provide you with a clear and efficient method for managing non-Markdown format resource files (such as images, PDFs, videos, audio, scripts, etc.) in your Obsidian repository.

The core goal is to leverage Obsidian's powerful linking and backlinking features to ensure that every resource can be effectively tracked and its specific reference location within the knowledge base can be understood.

## 1. Core Principles

- **Unified storage**: Store most non-MD resource files centrally in the `Extras/Attachments/` directory.
- **Categorized management**: Create subfolders within `Extras/Attachments/` based on file type, such as `Images`, `PDFs`, `Videos`, `Audio`, `Scripts`, etc.
- **Link first**: Always use Markdown links `[[]]` or embed `![[]]` to reference resources, instead of copying files.
- **Clear naming**: Set a clear and readable name for the file for easy searching and identification.

## 2. Storage Location Strategy

### a. Main repository: `Extras/Attachments/`

This is the "central station" for all general resource files in your repository.

- **`Extras/Attachments/Images/`**: Stores general images.
- **`Extras/Attachments/PDFs/`**: Stores PDF documents.
- **`Extras/Attachments/Videos/`**: Stores video files.
- **`Extras/Attachments/Audio/`**: Stores audio files.
- **`Extras/Attachments/Scripts/`**: Stores code scripts.
- **`Extras/Attachments/Icons/`**: Stores icon files, which you are already practicing.
- **`Extras/Attachments/Other/`**: Stores other uncategorized files.

**Automation configuration suggestion**:
In Obsidian's settings, find `Files & Links` -> `Default location for new attachments`, set it to `In the folder specified below`, and fill in the path `Extras/Attachments` below. In this way, when you paste an image or drag and drop a file, it will be automatically saved to this location.

### b. Specific context storage

For resources that are highly bound to a specific project or theme, they can be stored in their corresponding directory.

- **`Atlas/Draws/`**: Used to store Excalidraw or Canvas drawing files, which are part of your core knowledge map.
- **`Spaces/1-Project/Project Name/assets/`**: If a resource is **only** used for a specific project, it can be stored with the project, which is convenient for the overall migration or archiving of the project.

## 3. Reference Method

To make backlinks work, be sure to use the following methods to reference your resources:

- **Embed image**: `![[my-image.png]]`
- **Embed a specific page of a PDF**: `![[my-document.pdf#page=3]]`
- **Link to file**: `[[my-document.pdf]]`
- **Link and set display text**: `[[my-document.pdf|View my document]]`

In this way, you can clearly see which notes each resource file is referenced by in the "Backlinks" panel on the right.

## 4. Create "Metadata Notes" for Resource Files (Optional but Recommended)

For some important resource files (such as a complex design draft, an important PDF report), you can create a `.md` note with the same name to record its metadata.

**Example**:
You have an important chart file `2025-market-analysis.png`.

1.  Create a `2025-market-analysis.md` file next to it.
2.  In this Markdown file, you can record:
    - The source and author of the file.
    - A brief description of the file.
    - Related thoughts and comments.
    - Use `tags` and `aliases` to increase discoverability.
    - Finally, embed the image `![[2025-market-analysis.png]]`.

```markdown
---
tags: [report, market-analysis, AI-generated]
aliases: [2025 Market Analysis Chart]
source: "A certain research institution"
---
# 2025 Market Analysis Chart

This chart shows the expected market share distribution of the AI market in 2025.

**Core viewpoints**:
- The growth in field A is the most significant.
- Field B is tending towards saturation.

![[2025-market-analysis.png]]

---
*Related notes: [[AI Industry Observation]]*
```

The advantage of this is that your resource file itself has become a knowledge node that can be deeply searched and associated, not just an attachment.

## 5. Summary

| Scenario | Recommended practice |
| :--- | :--- |
| General images, PDFs, audio and video | Store them in the classified folders under `Extras/Attachments/` and reference them through `
# Non-MD Resource File Management Workflow

This guide aims to provide you with a clear and efficient method for managing non-Markdown format resource files (such as images, PDFs, videos, audio, scripts, etc.) in your Obsidian repository.

The core goal is to leverage Obsidian's powerful linking and backlinking features to ensure that every resource can be effectively tracked and its specific reference location within the knowledge base can be understood.

## 1. Core Principles

- **Unified storage**: Store most non-MD resource files centrally in the `Extras/Attachments/` directory.
- **Categorized management**: Create subfolders within `Extras/Attachments/` based on file type, such as `Images`, `PDFs`, `Videos`, `Audio`, `Scripts`, etc.
- **Link first**: Always use Markdown links `[[]]` or embed `![[]]` to reference resources, instead of copying files.
- **Clear naming**: Set a clear and readable name for the file for easy searching and identification.

## 2. Storage Location Strategy

### a. Main repository: `Extras/Attachments/`

This is the "central station" for all general resource files in your repository.

- **`Extras/Attachments/Images/`**: Stores general images.
- **`Extras/Attachments/PDFs/`**: Stores PDF documents.
- **`Extras/Attachments/Videos/`**: Stores video files.
- **`Extras/Attachments/Audio/`**: Stores audio files.
- **`Extras/Attachments/Scripts/`**: Stores code scripts.
- **`Extras/Attachments/Icons/`**: Stores icon files, which you are already practicing.
- **`Extras/Attachments/Other/`**: Stores other uncategorized files.

**Automation configuration suggestion**:
In Obsidian's settings, find `Files & Links` -> `Default location for new attachments`, set it to `In the folder specified below`, and fill in the path `Extras/Attachments` below. In this way, when you paste an image or drag and drop a file, it will be automatically saved to this location.

### b. Specific context storage

For resources that are highly bound to a specific project or theme, they can be stored in their corresponding directory.

- **`Atlas/Draws/`**: Used to store Excalidraw or Canvas drawing files, which are part of your core knowledge map.
- **`Spaces/1-Project/Project Name/assets/`**: If a resource is **only** used for a specific project, it can be stored with the project, which is convenient for the overall migration or archiving of the project.

## 3. Reference Method

To make backlinks work, be sure to use the following methods to reference your resources:

- **Embed image**: `![[my-image.png]]`
- **Embed a specific page of a PDF**: `![[my-document.pdf#page=3]]`
- **Link to file**: `[[my-document.pdf]]`
- **Link and set display text**: `[[my-document.pdf|View my document]]`

In this way, you can clearly see which notes each resource file is referenced by in the "Backlinks" panel on the right.

## 4. Create "Metadata Notes" for Resource Files (Optional but Recommended)

For some important resource files (such as a complex design draft, an important PDF report), you can create a `.md` note with the same name to record its metadata.

**Example**:
You have an important chart file `2025-market-analysis.png`.

1.  Create a `2025-market-analysis.md` file next to it.
2.  In this Markdown file, you can record:
    - The source and author of the file.
    - A brief description of the file.
    - Related thoughts and comments.
    - Use `tags` and `aliases` to increase discoverability.
    - Finally, embed the image `![[2025-market-analysis.png]]`.

```markdown
---
tags: [report, market-analysis, AI-generated]
aliases: [2025 Market Analysis Chart]
source: "A certain research institution"
---
# 2025 Market Analysis Chart

This chart shows the expected market share distribution of the AI market in 2025.

**Core viewpoints**:
- The growth in field A is the most significant.
- Field B is tending towards saturation.

![[2025-market-analysis.png]]

---
*Related notes: [[AI Industry Observation]]*
```

The advantage of this is that your resource file itself has become a knowledge node that can be deeply searched and associated, not just an attachment.

## 5. Summary

| Scenario | Recommended practice |
| :--- | :--- |
| General images, PDFs, audio and video | Store them in the classified folders under `Extras/Attachments/` and reference them through `![[]]` or `[[]]`. |
| Project-specific files | Store them in the `assets` subdirectory within the project folder. |
| Core knowledge map, drawings | Store them in `Atlas/Draws/`. |
| Want to add more instructions to resources | Create a `.md` file with the same name as a "metadata note". |

By following this workflow, you will be able to maximize the advantages of Obsidian and make every piece of knowledge (regardless of format) a traceable and manageable part of your knowledge network. `. |
| Project-specific files | Store them in the `assets` subdirectory within the project folder. |
| Core knowledge map, drawings | Store them in `Atlas/Draws/`. |
| Want to add more instructions to resources | Create a `.md` file with the same name as a "metadata note". |

By following this workflow, you will be able to maximize the advantages of Obsidian and make every piece of knowledge (regardless of format) a traceable and manageable part of your knowledge network. `. |
| Project-specific files | Store them in the `assets` subdirectory within the project folder. |
| Core knowledge map, drawings | Store them in `Atlas/Draws/`. |
| Want to add more instructions to resources | Create a `.md` file with the same name as a "metadata note". |

By following this workflow, you will be able to maximize the advantages of Obsidian and make every piece of knowledge (regardless of format) a traceable and manageable part of your knowledge network. `. |
| Project-specific files | Store them in the `assets` subdirectory within the project folder. |
| Core knowledge map, drawings | Store them in `Atlas/Draws/`. |
| Want to add more instructions to resources | Create a `.md` file with the same name as a "metadata note". |

By following this workflow, you will be able to maximize the advantages of Obsidian and make every piece of knowledge (regardless of format) a traceable and manageable part of your knowledge network. `. |
| Project-specific files | Store them in the `assets` subdirectory within the project folder. |
| Core knowledge map, drawings | Store them in `Atlas/Draws/`. |
| Want to add more instructions to resources | Create a `.md` file with the same name as a "metadata note". |

By following this workflow, you will be able to maximize the advantages of Obsidian and make every piece of knowledge (regardless of format) a traceable and manageable part of your knowledge network. 