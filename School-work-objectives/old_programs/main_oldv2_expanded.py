"""
look at change_logs.txt to see if the wanted program is finished
DO NOT CHANGE main.py or any file in /change
"""

import os
clear = lambda: os.system("clear")
un = [".upm", "extra", ".git", "change"]


def send(__, _, x):
    clear()
    os.system("python " + __[_] + "/" + os.listdir(__[_])[x - 2])
    _ = ("" if input(
        "\npress enter to go to rerun\nor input anything else to return\n") !=
         "" else "1\n" + str(_) + "\n" + str(x))
    f = open("update.txt", "w")
    f.write(_)
    f.close()
    os.system("python main.py")


def paths():
    return sorted([(i) for i in list(
        filter(os.path.isdir, os.listdir("/home/runner/obs-all")))
                   if i not in un])


def main():
    clear()
    __ = paths()
    [print(x + 1, "--", __[x]) for x in range(len(__))]
    _ = int(
        input(
            "what objective do you want to run?, enter then number next to the objective\nnote that the programs in the 'extra' directory is just extra, it is not to be used for marking as it doesnt follow the spec\n"
        )) - 1
    clear()
    [
        print(f + 1, "--",
              os.listdir(__[_])[f - 1]) for f in range(len(os.listdir(__[_])))
    ]
    send(__, _,
         int(input("input the number of the project you want to run\n")))


exec(
    'try:f=open("update.txt","r");f=f.read().splitlines();main() if f[0]=="0" else send(paths(),int(f[1]),int(f[2]))\nexcept:f=open("update.txt","w");f.write("0");f.close()\nos.system("python main.py")'
)