import tkinter as tk
import re
import template_for_default_domains as template
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
        if self.check_entries() == True:
            self.tag_fluid = self.tags.entry_tagfluid.get()
            self.tag_solid = self.tags.entry_tagsolid.get()
            
            self.read_data_from_ccl()
            self.get_indices()
            self.get_domain_names()
            self.get_domain_types()
            self.write_ccl_file()
        else:
            return        
       
    def cmd_view(self):
        pass

    def check_entries(self):
        if not os.path.isfile(self.fp.entry_inputfile.get()):
            print ('Path of inputfile is invalid!')
            return False
        if not os.path.isdir(os.path.dirname(self.fp.entry_outputfile.get())):
            self.check = False
            print ('Path of outputfile is invalid!')
            return False
        if not self.fp.entry_outputfile:
            self.check = False
            print ('Choose the outpufile!')
            return False
        if not self.tags.entry_tagfluid.get():
            self.check = False
            print ('Define tag for fluid domains!')
            return False
        if not self.tags.entry_tagsolid.get():
            self.check = False
            print ('Define tag for solid domains!')
            return False
        else:
            return True
        
    def read_data_from_ccl(self):
        self.inputdata = []
        with open(self.inputfile_fullpath) as f:
            for line in f:
                
                self.inputdata.append(line.strip())
    
    def get_indices(self):
        for idx,line in enumerate(self.inputdata):
            if 'Domain Type = ' in line:
                self.fidx = idx+1
            elif 'BOUNDARY: ' in line:
                self.lidx = idx

    def get_domain_names(self):
        inputdata_cut = self.inputdata[self.fidx:self.lidx]
        joined = ''.join(inputdata_cut)
        joined = joined.replace('\\','')
        joined = joined.split(' = ')[1]
        self.domains_orig = joined.split(",")
        
    def get_domain_types(self):
        self.domains_fluid = []
        self.domains_solid = []
        for domain in self.domains_orig:
            if self.tag_fluid.lower() in domain.lower():
                if re.search(r'[0-9]{3}$',domain):
                    domain = domain.split(' ')[0]
                    self.domains_fluid.append(domain)
                else:
                    self.domains_fluid.append(domain)
            elif self.tag_solid.lower() in domain.lower():
                if re.search(r'[0-9]{3}$',domain):
                    domain = domain.split(' ')[0]
                    self.domains_solid.append(domain)
                else:
                    self.domains_solid.append(domain)
                
    def write_ccl_file(self):
        f = open(self.outpufile_fullpath,'w')
        for domain in self.domains_fluid:
            s = template.templates('fluid')
            s = s.replace('!DOMAIN_NAME!',domain.upper())
            s = s.replace('!DOMAIN_TYPE!','Fluid')
            s = s.replace('!DOMAIN_LOCATION!',domain)
            s = s.replace('!DOMAIN_MATERIAL!','Water')
            f.write(s)

        for domain in self.domains_solid:
            s = template.templates('fluid')
            s = s.replace('!DOMAIN_NAME!',domain.upper())
            s = s.replace('!DOMAIN_TYPE!','Solid')
            s = s.replace('!DOMAIN_LOCATION!',domain)
            s = s.replace('!DOMAIN_MATERIAL!','Aluminium')
            f.write(s)
        f.close()
                                                                          

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Rename domains')
    AppRenameDoms(root).pack()
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()
