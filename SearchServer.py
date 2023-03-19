import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import re
import os
import subprocess
# Frame
gui = tk.Tk()
gui.state('zoomed')
gui.title("SCQM Search Server App v0.1")
gui.configure(background='white')

# out=tk.Label(gui, text= "")
# comm=tk.Label(gui, text= "")
# gui.geometry('1500x1500')
#gui.attributes("-fullscreen", True)

text_widget = tk.Text(gui)
scroll_bar = tk.Scrollbar(gui, command=text_widget.yview, orient="vertical")
text_widget.configure(yscrollcommand=scroll_bar.set)


scroll_bar.pack(side=tk.RIGHT, fill='y')
text_widget.pack(side=tk.BOTTOM, fill ='both',expand=1)
#logo_image = 'flash.icns'
#gui.iconbitmap(logo_image)
#gui.resizable(0, 0)


def getFolderPath():
    folder_selected = tk.filedialog.askdirectory()
    folderPath.set(folder_selected)

# def remove_label(): 
# #     out.pack_forget()
# #     comm.pack_forget()
# #     output.pack_forget()
#     text.delete(1.0,END)


    
def doStuff():
    global comm
    global output
    folder = folderPath.get()
    pattern=getKeyword.get()
    depth=getDepth.get()
    cmd = 'find '+ folder + ' -maxdepth ' + depth + ' -type d -path "*/.*" -prune -o -not -name ".*" -type f -iname ' + pattern 
    #find . -not -path '*/.*' -type f -name '*some text*'
    #cmd = 'find '+ folder + ' -maxdepth ' + depth + ' -path ""*/.* "+ -type d -path "*/.*" -prune -o -not -name ".*" -type f -name ' + pattern 
    #cmd =     'find '+ folder + ' -maxdepth ' + depth +  ' -iname ' + pattern
    #cmd =     'fd '+ pattern +' '+ folder
#find . -not -path '*/.*' -type f -iname '*patient*'     
    output = subprocess.check_output(cmd, shell=True)

    comm=tk.Label(gui, text= cmd)
    comm.pack()
    text_widget.insert(tk.END, output)
    scroll_bar.config(command=text_widget.yview)


folderPath = tk.StringVar()
getKeyword = tk.StringVar()
getDepth = tk.StringVar()

wordlabel = tk.Label(gui ,text="Keyword")
wordlabel.pack()

wordactual = tk.Entry(gui,textvariable=getKeyword)
wordactual.pack()

dirlabel = tk.Label(gui ,text="Choose directory")
dirlabel.pack()

foldeactual = tk.Entry(gui,textvariable=folderPath)
foldeactual.pack()

btnFind = tk.Button(gui, text="Browse Folder",command=getFolderPath)
btnFind.pack()

depthlabel = tk.Label(gui ,text="Choose maxdepth")
depthlabel.pack()

depthactual = tk.Entry(gui,textvariable=getDepth)
depthactual.pack()


btnSearch = tk.Button(gui ,text="Search", command=doStuff)
btnSearch.pack()


# Delete Button
btn = tk.Button(gui, text='Delete', command=lambda: text_widget.delete(1.0,tk.END))
btn.pack()

gui.mainloop()