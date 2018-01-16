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
        self.button_selectinput = tk.Button(self.frame_filepaths,text='Select')
        self.button_selectoutput = tk.Button(self.frame_filepaths,text='Select')     
    
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
                height=2)
        self.button_view = tk.Button(
                self.frame_tags,
                text='View file',
                height=2)
             
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
        self.tags.button_write.grid(row=5,column=1,sticky='NSEW')
        self.tags.button_view.grid(row=6,column=1,sticky='NSEW')
        
        self.fp.button_selectinput.config(command=self.cmd_selectinput)
        self.fp.button_selectoutput.config(command=self.cmd_selectoutput)
        self.tags.button_write.config(command=self.cmd_write)
        self.tags.button_view.config(command=self.cmd_view)
                
    def cmd_selectinput(self):
        selected = tk.filedialog.askopenfilename(
                title='Choose the .ccl file with default domains',
                filetypes=(("CFX Command file", "*.ccl"),("All files", "*.*")))
        
        if selected:
            self.inputfile_fullpath = selected
            self.inputfile_name = os.path.basename(self.inputfile_fullpath)
            self.inputfile_dir_name = os.path.dirname(self.inputfile_fullpath)
            self.inputfile_ext = os.path.splitext(self.inputfile_fullpath)[1]
            
            self.fp.entry_inputfile.delete(0,'end')
            self.fp.entry_inputfile.insert(0,selected)
        else:
            return
    
    def cmd_selectoutput(self):
        selected = filedialog.asksaveasfilename(parent=self.master,
                                    initialdir=self.inputfile_dir_name,
                                    title="Selet a file for export",
                                    filetypes=[('All files', '.*')]) 
    
        if selected:
            self.outpufile_fullpath = selected
            self.fp.entry_outputfile.delete(0,'end')
            self.fp.entry_outputfile.insert(0,selected)
        else:
            return
    
    def cmd_write(self):
        self.check_entries()
        
    def cmd_view(self):
        pass

    def check_entries(self):
        self.check = True
        if not os.path.isfile(self.fp.entry_inputfile.get()):
            self.check = False
            print ('Path of inputfile is invalid!')
            return
        if not os.path.isdir(os.path.dirname(self.fp.entry_outputfile.get())):
            self.check = False
            print ('Path of outputfile is invalid!')
            return
        if not self.fp.entry_outputfile:
            self.check = False
            print ('Choose the outpufile!')
            return
        if not self.tags.entry_tagfluid.get():
            self.check = False
            print ('Define tag for fluid domains!')
            return
        if not self.tags.entry_tagsolid.get():
            self.check = False
            print ('Define tag for solid domains!')
            return

                        


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Rename domains')
    AppRenameDoms(root).pack()
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()
