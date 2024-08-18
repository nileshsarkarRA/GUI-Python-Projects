## A useful and simple GUI Python File Manager by Team Achievers

from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


def window():
    value = easygui.fileopenbox()
    return value


def file():
    w1 = window()
    try:
        os.startfile(w1)
    except:
        mb.showinfo('failed!',"File not found!")


def copy_file():
    file1 = window()
    file2 = filedialog.askdirectory()
    shutil.copy(file1, file2)
    mb.showinfo('congrats', "File Copied")


def delete_file():
    file1 = window()
    if os.path.exists(file1):
        os.remove(file1)
    else:
        mb.showinfo('failed!',"File not found !")


def rename_file():
    file1 = window()
    path1 = os.path.dirname(file1)
    ext = os.path.splitext(file1)[1]
    print("Enter new name ")
    name = input()
    path = os.path.join(path1, name + ext)
    print(path)
    os.rename(file1, path)
    mb.showinfo('congrats', "File Renamed !")


def new_folder():
    folder1 = filedialog.askdirectory()
    print("Enter name")

    name = input()
    path = os.path.join(folder1, name)

    os.mkdir(path)
    mb.showinfo('congrats', "Folder created !")


def remove_folder():
    folder1 = filedialog.askdirectory()
    os.rmdir(folder1)
    mb.showinfo('congrats', "Folder Deleted !")


def list_files():
    flist = filedialog.askdirectory()
    sorts = sorted(os.listdir(flist))
    j = 0
    print("Files in ", flist, "are-")
    while j < len(sorts):
        print(sorts[j] + '\n')
        j += 1


manager = Tk()
manager.geometry('500x600')
manager.title('File Manager by Team Achievers')


frame = Frame(manager)
frame.pack(pady=20)
Label(frame, text="File Manager by Team Achievers",font = ("Ariel 14 bold"),bg="lightgreen").pack()

frame1 = Frame(manager)
frame1.pack(pady=20)

Button(frame1, text="Open", command=file, bd=1, bg="lightblue", cursor="hand2", font = ("Times_New_Roman 10")).pack(pady=10)

Button(frame1, text="Copy", command=copy_file,bg="lightblue", bd=1, cursor="hand2",font = ("Times_New_Roman 10")).pack(pady=10)

Button(frame1, text="Delete", command=delete_file,bg="lightblue", bd=1, cursor="hand2",font = ("Times_New_Roman 10")).pack(pady=10)

Button(frame1, text="Rename", command=rename_file, bd=1, cursor="hand2",bg="lightblue", font = ("Times_New_Roman 10")).pack(pady=10)

frame2 = Frame(manager)
frame2.pack(pady=15)

Button(frame2, text="New Folder", command=new_folder, bd=1, cursor="hand2",bg="lightblue",font = ("Times_New_Roman 10")).pack(pady=10)

Button(frame2, text="Remove a Folder", command=remove_folder,bg="lightblue", bd=1, cursor="hand2",font = ("Times_New_Roman 10")).pack(pady=10)

Button(frame2, text="List all Files", command=list_files, bd=1,bg="lightblue", cursor="hand2",font = ("Times_New_Roman 10")).pack(pady=10)

manager.mainloop()
