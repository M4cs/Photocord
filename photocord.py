import os
import glob
from pathlib import Path
import shutil
from sys import platform

home = str(Path.home())

if "win" in platform():
    FILEPATHS = [
        os.path.realpath(f'{home}/AppData/Roaming/discord/Cache'),
        os.path.realpath(f'{home}/AppData/Roaming/discordcanary/Cache'),
        os.path.realpath(f'{home}/AppData/Roaming/discordptb/Cache')
    ]

elif "linux" in platform():
    FILEPATHS = [
        os.path.realpath(f'{home}/.config/discord/Cache'),
        os.path.realpath(f'{home}/.config/discordcanary/Cache'),
        os.path.realpath(f'{home}/.config/discordptb/Cache')
    ]

EXISTINGFILEPATHS = []

def grabArchives(lol):
    print("Grabbing Files...")
    for i in range(3):
        if os.path.exists(FILEPATHS[i]) == True:
            EXISTINGFILEPATHS.append(FILEPATHS[i])

    pictures = []

    for i in range(len(EXISTINGFILEPATHS)):
        for x in glob.glob(EXISTINGFILEPATHS[i] + "/*"):
            if ".png" not in x:
                print(f"Found: {x}.png")
                pictures.append(x)

    for i in pictures:
        if ".png" not in i and "data" not in i and "index" not in i:
            out = i + ".png"
            os.rename(i, out)

    
    if lol == True:
        for f in range(len(EXISTINGFILEPATHS)):
            shutil.make_archive(f"archives/{f}", "bztar", EXISTINGFILEPATHS[f])
            test = os.listdir(EXISTINGFILEPATHS[f])
            for item in test:
                if item.endswith(".png"):
                    os.remove(os.path.join(EXISTINGFILEPATHS[f], item))
    elif lol == False:
        for f in range(len(EXISTINGFILEPATHS)):
            shutil.make_archive(f"archive/{f}", "bztar", EXISTINGFILEPATHS[f])


print("""
Welcome To Photocord

I made this tool because I saw on twitter that Discord saves every
photo you've viewed in their Cache (most Electron apps do). So this
will allow you to grab all those and put them into a .tar.bz2 archive
for easy storage. Enjoy :)

Archive Key:

0.tar.bz2 = Normal Discord
1.tar.bz2 = Discord Canary
2.tar.bz2 = Discord PTB

Developed by @maxbridgland under the GPLv3 License.
    """)


def main():
    msg = """
What would you like to do?

1. Archive All Cached Photos

2. Archive And Delete All Cache

2. Exit"""
    term = "[photocord]> "
    print(msg)
    terminal = str(input(term))
    if terminal == "1":
        grabArchives(lol=True)
        main()
    elif terminal == "2":
        grabArchives(lol=False)
        main()
    elif terminal == "3":
        exit()
    else:
        print("Please choose an option.")
        main()

main()




