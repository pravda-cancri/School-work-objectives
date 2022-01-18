"""
this page has now been made to be readable
feel lucky you didn't have to read the compressed versions that came before
please see School-work-objectives/old_programs/

note all files that need to be accessed can be accessed in the /files folder
"""

import os
os.system("python crawl.py")
input()
def writes(x):
    #writes to file loc.txt
    f = open("loc.txt", "w")
    f.write(x)
    f.close()


def reads():
    #reads from file returning the directory
    try:
        f = open("loc.txt", "r")
        f = f.read()
    except:
        f = ""
    if f != "":
        _ = f
    else:
        _ = "/home/runner/all"
    return _


def pick_dir():
    #allows yoy to navigate back folders after program has run
    time.sleep(0.5)
    y = reads()
    y = y.split("/")
    for x in range(3):
        del y[0]
    print(
        "what folder/script do you want to return to?\nplease either input a number or enter anything else to return to the main folder\n"
    )
    y.reverse()
    for x in range(len(y)):
        print(x, "----", y[x])
    try:
        str = ""
        y.reverse()
        p = int(input())
        for x in range(p):
            del y[-1]
        for x in y:
            str += "/" + x
        str = "/home/runner" + str
    except:
        str = "/home/runner/all"
    writes(str)
    clear()
    main()


def paths(x):
    #returns all directories /files along a path
    return sorted([
        (i) for i in list(os.listdir(x)) if i not in
        ".upm.gitextrasmain.py.breakpointsREADME.mdpoetry.lockpyproject.toml._runhelp.py__pycache__errors.pyfilefiles"
        if not i.endswith((".json", ".txt"))
    ])


def read_description(x):
    f = open(x, "r")
    f = f.read().splitlines()
    v = []
    try:
        for x in range(len(f)):
            if f[x] == '"""':
                for i in range(len(f)):
                    if f[i + 1] != '"""':
                        v.append(f[x + 1])
                    else:
                        raise StopIteration
    except:
        clear()
        print(v[0])

    input("\ninput anything to carry on\n")


def send(x):
    #runs the program selected
    writes(x)
    print("please press ctrl + c at any time to exit\n")
    os.system("python " + x)
    print("\n\n")
    p = input("would you like to read the task description?\nyes/no\n")
    if p == "yes":
        read_description(x)
    pick_dir()


def recursion(x):
    #displays the output of paths() in a structured way
    v = paths(x)
    writes(x)
    print("folder:{}\n".format(x))
    [print(str(x) + " --- " + v[x]) for x in range(len(v))]
    try:
        _ = input(
            "\nwhat file do you want to open / run?\n or press enter to pick directory\n or enter any string to go to main directory\n"
        )
        _ = x + "/" + str(v[int(_)])
    except ValueError:
        if not _:
            clear()
            _ = pick_dir()
        else:
            writes("")
            main()
    except IndexError:
        clear()
        recursion(x)
    return _

def find_similar(x):
    #if file/directory is not found then this function will search for the nearest string similar to the path returned by paths()
    str = ""
    x = x.split("/")
    v = x[-1]
    del x[-1]
    del x[0]
    for t in x:
        str += "/" + t
    words = paths(str)
    b = difflib.get_close_matches(v, words, cutoff=0.05, n=1)
    str += "/" + b[0]
    writes(str)
    main()


def main():
    #checks if directory given is a file, if its a file it is run, else it runs recursion() to get to the location you want
    p = True
    path = reads()
    if path == "/home/runner" or path == "/home":
        writes("")
        main()
    while p:
        try:
            clear()
            path = recursion(path)
        except NotADirectoryError:
            send(path)
            p = False
        except FileNotFoundError:
            find_similar(path)


def check_reset():
    #checks for different args
    if len(sys.argv) > 1:
        if sys.argv[1] == "reset":
            pick_dir()


import os
import time
import difflib
import sys

clear = lambda: os.system("clear")

try:
    check_reset()
    main()
except:
    os.system("python main.py")