# Photocord
Discord Photo Cache Archiver and Manager

Discord is an Electron app which means it caches your images in its local storage in order to incread load times in the future. This is also a security risk since even deleted photos you've seen get cached. Therefore any image that has been loaded into Discord is available on Windows at least in your AppData. This program allows you to archive those images and then delete if you'd like to. **Windows only unless somebody can send the link to MacOS and Linux Cache Directories**

# Usage
Run `python3 photocord.py` from the directory of photocord. It will create a directory in that one named "archives". In this folder will be up to 3 archives with all the cached images saved in the `.tar.bz2` archive format.

# Archive Key

0.tar.bz2 = Discord Normal

1.tar.bz2 = Discord Canary

2.tar.bz2 = Discord PTB
