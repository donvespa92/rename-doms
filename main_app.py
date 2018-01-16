import tkinter as tk
import rename_doms


class MainApp(tk.Frame):
    def __init__(self,master):       
        tk.Frame.__init__(self,master)
        self.master = master
        self.master.option_add("*Font", "Arial 12")
        
        self.button_rename_doms = tk.Button(
                self.master,
                text='Rename domains',
                command=self.cmd_rename_doms)
                
        self.button_rename_doms.pack()
        
    def cmd_rename_doms(self):
        self.window_rename_doms = tk.Toplevel(self.master)
        rename_doms.AppRenameDoms(self.window_rename_doms).pack()

root = tk.Tk()
root.title('Rename domains')
MainApp(root).pack()
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()

