# Photocord
Discord Photo Cache Archiver and Manager

Discord is an Electron app which means it caches your images in its local storage in order to incread load times in the future. This is also a security risk since even deleted photos you've seen get cached. Therefore any image that has been loaded into Discord is available on Windows at least in your AppData. This program allows you to archive those images and then delete if you'd like to. **Windows and Linux only atm unless somebody can provide MacOS paths. Shoutout to ByteCommander in the PyDis for the Linux Locations.**

# Getting Started

**On Windows:**
`pip install python-magic-win64`

**On Linux:**
`pip install python-magic`

Photocord uses the libmagic library to read what type of file it is before conversion so you aren't just naming every file a png and having some be corrupted.

***Make sure you have all instances of Discord closed in the background not just the window.***

# Usage
Run `python3 photocord.py` from the directory of photocord. It will create a directory in that one named "archives". In this folder will be up to 3 archives with all the cached images saved in the `.tar.bz2` archive format.

# Archive Key

0.tar.bz2 = Discord Normal

1.tar.bz2 = Discord Canary

2.tar.bz2 = Discord PTB

# Changelog

#### Update 2:

- Sorts through more filetypes (.mov, .gif, .gz (these are usually .js files inside), .mpeg, .jpeg, .png)

#### Update 1:

- Added libmagic functionality to only convert .pngs.

#### Hotfix 2:

- Fixed bug with numbers in menu.

#### Hotfix 1:

- Added options to delete or save cache.
