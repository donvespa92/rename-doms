import tkinter as tk
import re
from tkinter import ttk
from tkinter import filedialog
from tkinter.font import Font
from tkinter import messagebox
from tkinter import simpledialog
import shutil
from shutil import copyfile
import math
import os

class filepaths(tk.Frame):
    def __init__(self,master):       
        tk.Frame.__init__(self,master)
        self.master = master
        self.frame_filepaths = tk.Frame(self.master)
        
        self.label_inputfile = tk.Label(self.frame_filepaths,text='Inputfile')
        self.entry_inputfile = tk.Entry(self.frame_filepaths,width=50)
        self.label_outputfile = tk.Label(self.frame_filepaths,text='Outputfile')
        self.entry_outputfile = tk.Entry(self.frame_filepaths,width=50)
        
        self.button_selectinput = tk.Button(
                self.frame_filepaths,
                text='Select',
                command=self.cmd_selectinput)
        self.button_selectoutput = tk.Button(
                self.frame_filepaths,
                text='Select',
                command=self.cmd_selectoutput)    
        
    def cmd_selectinput(self):
        pass
    
    def cmd_selectoutput(self):
        pass

class define_tags(tk.Frame):
    def __init__(self,master):       
        tk.Frame.__init__(self,master)
        self.master = master 
        self.frame_tags = tk.Frame(self.master)
        
        self.label_tagsolid = tk.Label(self.frame_tags,text='Solid domain tag')
        self.entry_tagsolid = tk.Entry(self.frame_tags,width=50)
        self.label_tagfluid = tk.Label(self.frame_tags,text='Fluid domain tag')
        self.entry_tagfluid = tk.Entry(self.frame_tags,width=50)
        
        self.button_write = tk.Button(
                self.frame_tags,
                text='Write',
                height=2,
                command=self.cmd_write)
        self.button_view = tk.Button(
                self.frame_tags,
                text='View file',
                height=2,
                command=self.cmd_view)
        
    def cmd_write(self):
        pass
    
    def cmd_view(self):
        pass
    
    
class AppRenameDoms(tk.Frame):
    def __init__(self,master):       
        tk.Frame.__init__(self,master)
        self.master = master
        self.master.option_add("*Font", "Arial 12")
        self.mainframe = tk.Frame(self.master)
        self.mainframe.pack(fill='both',expand=1)
        
        self.fp = filepaths(self)
        self.fp.frame_filepaths.grid(row=1,column=1,sticky='NSEW',padx=5,pady=5)
        self.fp.label_inputfile.grid(row=2,column=1,sticky='W')
        self.fp.entry_inputfile.grid(row=3,column=1,sticky='NSEW') 
        self.fp.label_outputfile.grid(row=4,column=1,sticky='W')
        self.fp.entry_outputfile.grid(row=5,column=1,sticky='NSEW')
        self.fp.button_selectinput.grid(row=3,column=2,sticky='NSEW')
        self.fp.button_selectoutput.grid(row=5,column=2,sticky='NSEW')

        self.tags = define_tags (self)
        self.tags.frame_tags.grid(row=2,column=1,sticky='NSEW',padx=5,pady=5)
        self.tags.label_tagfluid.grid(row=1,column=1,sticky='W') 
        self.tags.entry_tagfluid.grid(row=2,column=1,sticky='NSEW')
        self.tags.label_tagsolid.grid(row=3,column=1,sticky='W') 
        self.tags.entry_tagsolid.grid(row=4,column=1,sticky='NSEW')
        self.tags.button_write.grid(row=5,column=1,sticky='NSEW',padx=5,pady=5)
        self.tags.button_view.grid(row=6,column=1,sticky='NSEW',padx=5,pady=5)            
    

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Rename domains')
    AppRenameDoms(root).pack()
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()
