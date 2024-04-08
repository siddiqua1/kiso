Kiso (基礎) is a strongly opinioned methodology for organizing notes in Obsidian. This document will walk through the rationale behind the foundation this structure lays out.

## Why Kiso?

Kiso is heavily inspired by the Zettelkasten and PARA methodologies. While they contain many important personal knowledge management insights, they leave a lot of headway that can be paralyzing. Kiso intends to close this gap by augmenting these methods with two techniques: templates and workflows.

Kiso is intended to make notes and ideas more actionable by offering golden path(s) to note taking. This is largely inspired by the current surge of platforming engineering. I recommend [Hazel Weakly's talk at InfoQ](https://www.infoq.com/presentations/platforms-social-engineering/) to learn more about what makes platforms great. The TLDR would be platforms are a force multiplier to users. In the end, platforms are to be evolved to meet the user's needs, so be sure to always check in and see what areas could be improved on.

## Intended Users

In the end, the ultimate user for this is myself, but I hope this platform could inspire your own workflow. Going into this, my intended areas of study are for computer science and mathematics, so you may see parts optimized for those use cases.

## Structure 

The structure of Kiso reflect a lot of the design decisions of this platform. Kiso is intended to be relatively flat, relying mostly on links to build up a knowledge base. The folders are supposed to group "meta" concepts surrounding notetaking. We will talk about each concept below.

### Inbox

This is where every new note starts. This initial folder is to act a scratch area. For example, creating a note to quickly write down some useful references to go thorough later and process. 

The intent is to rapidly capture new sources of information down, so that in a daily maintenance period you can filter out what may be relevant.

### Calendar 

This is a standard journaling section. Journaling has been a useful concept and including it by default is a good value add.

### Fleeting

These are unprocessed notes that are filtered from the inbox and worthwhile to delve more into. Very typical from the Zettelkasten system. These notes are intended to not be deleted unless the information judged from them seems irrelevant at a later point. 

### Literature 

These are in-depth research notes on a given piece of media, like a book, video, or article. They often "process" a fleeting note. 

### Concepts

Concepts are "one idea" notes and often stem out of literature notes. They should be considered as "context-free" as possible, that is the information about them should not require background knowledge to the whatever reasonable extent possible.

### Maps

Maps, or Maps of Content (MOC), are the linking methodology recommended by this platform. Folders are to strict, making notes difficult to share between areas of interest without duplication. Tags are too free form. Adding a tag requires you to edit multiple files if you need to apply them retroactively. MOCs are a good upgrade to tags, as on top of being able to group notes, you can additional context around them, helping the linking process. Tags are still used, but mainly to provide automation to the vault.

Maps are also useful to group other maps, allowing you have multiple views on a topic depending on the level of specificity you would want.

### Projects

As an engineer, side projects are an excellent idea to develop your skills and passion. By including projects as first class, we can both track projects but also extract useable information out of them. Projects should be thought as a subclass of MOCs. They link to relevant concepts, providing some contextual information with the given projects. I have also opted to included Kanban directly in the project to provide a "single source of truth" type view of the project.

I have opted for three "views" on projects. Active, completed, and backlogged. This is simply so that you can context switch to the appropriate area quickly.

### Practice Problems

Practice is key, thus having your practice problems as a first class member is important to your knowledge. While rediscovery is great and really shows understanding, when building understanding for the first time, the ability to have a section to reference for all the relevant problems will prove invaluable for refreshing on skill sets.

### Maintenance

Maintenance can be thought of as a recurring type of project. 


### Workflow

Workflows are one of the key concepts Kiso brings to the table. They are intended to be a personalized methodology for handling different types of note taking. This is so that when presented with new and challenging ideas, the burden of how to digest them are already thought out ahead of time and just need to done. The key is to give starting velocity.

### References

These are a section of notes dedicated for reference material.

### Resources

This section is dedicated to resources used by the vault, mainly intended for screenshots.

### Templates

This is the other key concept Kiso intends to provide. Templates are often used in daily note taking, but in Kiso, we want to expand to as many work types as possible. Again the key is starting velocity. On top of this we want to introduce the ability to automate as much of our workflow. This will require the usage of metadata that is a hassle to add intentionally every time, and thus should be left to the platform where possible. 


```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
## Setup 




This is your new *vault*.

Make a note of something, [[create a link]], or try [the Importer](https://help.obsidian.md/Plugins/Importer)!

When you're ready, delete this note and make the vault your own.