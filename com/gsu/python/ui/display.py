'''
Created on Nov 11, 2015

@author: Rajkiran, Ashwin, Vishesh, Kshitij
'''
from tkinter import *
from os import listdir
from random import choice
from com.gsu.python.algo.tfidf import TFIDF
from os.path import dirname,isfile,join
from os import getcwd

class Display():  #The display class
    
    mypath=dirname(getcwd())+"\\resource"
        
    def __init__(self,allfiles):  #Constructor: creates the window
        window=Tk()
        window.title("GoF Search")
        self.tfidf=TFIDF(allfiles)

        self.frame=Frame(window,width=600,height=400,bg="white")
        self.frame.pack()
        window.bind('<Return>',self.returnKey)
        self.mainPage()
        window.mainloop()

    def mainPage(self):
        self.image=PhotoImage(file=self.mypath+"\\"+choice(listdir(path=self.mypath)))
        self.background=Label(self.frame, image=self.image)
        self.background.image=self.image
        self.background.place(x=0,y=0,relwidth=1, relheight=1)
        self.input=StringVar()
        self.logo=Label(self.background,text="GoF Search",font=("Helvetica", "20", "bold"),bg="grey")
        self.logo.pack(side="top",pady=150)
        Entry(self.background,textvariable=self.input,relief="sunken",width=50).place(x=150,y=200)
        Button(self.background,text="Search",command=self.search).place(x=500,y=200)

    def clear(self):
        self.background.destroy()
        self.prevInput=self.input.get()
        self.input.set('')

    def resPage(self,resLst):
        self.topbar=Label(self.frame, image=self.image)
        self.topbar.place(x=0,y=0,relwidth=1, relheight=0.2)
        self.logoSmall=Label(self.topbar,text="GoF Search",font=("Helvetica", "12", "bold"),bg="grey")
        self.logoSmall.place(x=10,y=25)
        self.logoSmall.bind("<Button-1>", self.mouseClick)

        self.searchBar=Entry(self.topbar,textvariable=self.input,relief="sunken",width=42)
        self.searchBar.place(x=100,y=20)
        self.searchBar.insert(0,self.prevInput)
        Button(self.topbar,text="Search",command=self.search).place(x=500,y=20)
        scrollbar = Scrollbar(self.frame,orient=VERTICAL)
        scrollbar.place(x=590,y=110,relheight=0.70)

        text = Text(self.frame, width = 40, height = 10, wrap = WORD,yscrollcommand = scrollbar.set,bg='grey')
        text.configure(state='normal')
        text.insert('end',resLst)
        text.configure(state='disabled')
        Label(self.frame,text="Search results:",font="bold").place(x=10,y=90)
        text.place(x=10,y=110,relwidth=0.96,relheight=0.70)
        scrollbar.config(command = text.yview)
        #self.resCanvas.create_text(x=20,y=100,text=resLst)

    def search(self):
        lst=self.input.get()
        self.clear()
        self.resPage(self.tfidf.searchRelevantDocument(lst))

    def mouseClick(self,event):
        self.clear()
        self.mainPage()

    def returnKey(self,event):
        self.search()

def main():
    mypath = dirname(getcwd())+'\\data'
    docfile_list = [f for f in listdir(path=mypath) if isfile(join(mypath,f))]
    d=Display(docfile_list)
    
#main()