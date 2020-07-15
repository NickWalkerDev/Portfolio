
import tkinter
from tkinter import *
import tkinter.filedialog
import os
import shutil
import sqlite3
import time


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(800,650))
        self.master.title('File Helper')
        

        self.varfromfiles = StringVar()
        self.vartofiles = StringVar()
        self.varfileext = StringVar()
        self.varfromdir = StringVar()
        self.varlistfield = StringVar()
        self.varmovefileext = StringVar()


        self.txtF1name = Entry(self.master,text=self.varfromfiles, font=("Times New Roman", 12),fg='black', bg='white', width=60)
        self.txtF1name.grid(row=0,column=1, columnspan=3, padx=(20,0), pady=(40,0))


        self.txtF2name = Entry(self.master,text=self.varmovefileext, font=("Times New Roman", 12),fg='black', bg='white', width=60)
        self.txtF2name.grid(row=1, column=1, columnspan=3, padx=(20,0), pady=(10,0))

        self.lbl_fname = Label(self.master,text='File type: ')
        self.lbl_fname.grid(row=1,column=0,padx=(27,0),pady=(10,0),sticky=N)


        self.txtF2name = Entry(self.master,text=self.vartofiles, font=("Times New Roman", 12),fg='black', bg='white', width=60)
        self.txtF2name.grid(row=2, column=1, columnspan=3, padx=(20,0), pady=(10,0))


        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=lambda: ask_quit())
        self.btnCancel.grid(row=15, column=6, padx=(0,0), pady=(20,0), sticky=NE)


        self.btnCancel = Button(self.master, text="Move Recently Modified", width=20, height=2, command=lambda: move_files())
        self.btnCancel.grid(row=3, column=0, columnspan=2, padx=(30,0), pady=(10,20), sticky=W)

        
        self.btnSubmit = Button(self.master, text="From...", width=10, command=lambda: fromFiles())
        self.btnSubmit.grid(row=0, column=0, padx=(30,0), pady=(40,0), sticky=N)


        self.btnSubmit = Button(self.master, text="To...", width=10, command=lambda: toFiles())
        self.btnSubmit.grid(row=2, column=0, padx=(30,0), pady=(10,0), sticky=N)


        self.txtF1name = Entry(self.master,text=self.varfromdir, font=("Times New Roman", 12),fg='black', bg='white', width=60)
        self.txtF1name.grid(row=4,column=1, columnspan=3, padx=(20,0), pady=(10,0))


        self.txtF2name = Entry(self.master,text=self.varfileext, font=("Times New Roman", 12),fg='black', bg='white', width=60)
        self.txtF2name.grid(row=5, column=1, columnspan=3, padx=(20,0), pady=(10,20))


        self.btnSubmit = Button(self.master, text="Browse...", width=10, command=lambda: browseDir())
        self.btnSubmit.grid(row=4, column=0, padx=(30,0), pady=(10,0), sticky=N)

        self.lbl_fname = Label(self.master,text='File type: ')
        self.lbl_fname.grid(row=5,column=0,padx=(27,0),pady=(10,0),sticky=N)


        self.btnCancel = Button(self.master, text="Search", width=10, height=2, command=lambda: search_files())
        self.btnCancel.grid(row=6, column=0, padx=(30,0), pady=(0,0), sticky=N)

        self.btnOpen = Button(self.master, text="Open", width=10, height=2, command=lambda: open_file())
        self.btnOpen.grid(row=7, column=0, padx=(30,0), pady=(0,0), sticky=N)


        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList1 = Listbox(self.master,exportselection=0,width=100,height=15,yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.lstList1.yview)
        self.scrollbar1.grid(row=6,column=7,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
        self.lstList1.grid(row=6,column=1,rowspan=7,columnspan=6,padx=(20,0),pady=(0,0),sticky=N+E+S+W)
    

  
        def fromFiles():
            file = tkinter.filedialog.askdirectory()
            self.varfromfiles.set(file)

        def toFiles():
            file = tkinter.filedialog.askdirectory()
            self.vartofiles.set(file)

        def ask_quit():
            self.master.destroy()
            os._exit(0)

        def browseDir():
            file = tkinter.filedialog.askdirectory()
            self.varfromdir.set(file)

        
        def search_files():
            self.lstList1.delete(0,END)
            directory = self.varfromdir.get()
            counter = 0
            fileext = self.varfileext.get()
            self.lstList1.insert(END, 'Searching for {} files...'.format(fileext))
            for f in os.listdir(directory):
                if f.endswith(fileext):
                    self.lstList1.insert(END, directory + '/' + f)
                    counter = (counter + 1)
                    continue
                else:
                    continue

            self.lstList1.insert(END, "{} {} files in this directory.".format(counter,fileext))

        def move_files():
            self.lstList1.delete(0,END)
            directory = self.varfromfiles.get()
            counter = 0
            fileext = self.varmovefileext.get()
            todirectory = self.vartofiles.get()
            self.lstList1.insert(END, "Moving {} files...".format(fileext))
            conn = sqlite3.connect('drill_step_124.db')
            for f in os.listdir(directory):
                if f.endswith(fileext):
                    time1 = int(os.path.getmtime(directory + '\\' + f))
                    now = int(time.time())
                    diff = int(now / 60 - time1 / 60)
                    print('Modified {} minutes ago'.format(diff))
                    if diff < 1440:
                        self.lstList1.insert(END, directory + '/' + f)
                        shutil.move(directory + '\\' + f, todirectory + '\\' + f)
                        self.lstList1.insert(END, 'TimeStamp: ' + str(os.path.getmtime(todirectory + '\\' + f)))
                        self.lstList1.insert(END, 'Last Modified: {} minutes ago. File transfered.'.format(diff))
                        with conn:
                            cur = conn.cursor()
                            cur.execute('INSERT INTO tbl_changes(col_docName,col_timestamp) VALUES ("' + todirectory + '/' + f + '", "' + str(os.path.getmtime(todirectory + '\\' + f)) + '")')
                            conn.commit()
                        counter = (counter + 1)
                        continue
                    else:
                        self.lstList1.insert(END, directory + '/' + f)
                        self.lstList1.insert(END, 'File not modified in last 24 hours. File was not transferred')
                        continue
                else:
                    continue
            conn.close()
            if counter < 1:
                self.lstList1.insert(END, "0 files moved.")
            else:
                self.lstList1.insert(END, "{} {} files from {} were".format(counter,fileext,directory))
                self.lstList1.insert(END, "successfully moved to {}.".format(todirectory))
                self.lstList1.insert(END, "{} new entries to database".format(counter))

        def open_file():
            file = self.lstList1.get(self.lstList1.curselection())
            self.lstList1.delete(0,END)
            read = open(file,'r')
            with read as f:
                for line in f:
                    self.lstList1.insert(END, line)
            
            
            
  


if __name__ == "__main__":
    conn = sqlite3.connect('drill_step_124.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_changes(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_docName TEXT, \
            col_timestamp TEXT \
            )")
        conn.commit()
    conn.close()  
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
