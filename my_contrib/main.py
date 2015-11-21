from save_data import Data_index
from search_img import Searcher
from Tkinter import *
import requests
from tkFont import Font
from bs4 import BeautifulSoup
import tkMessageBox

def call_index():
	path= z.get()
	if path== '':
		tkMessageBox.showinfo('ERROR','Please folder path!!!')
	elif path != '':
		di=Data_index(path)
		di.insert_data()



def call_search():
	info = v.get()
	if info=='':
		tkMessageBox.showinfo('ERROR','Please enter image name!!!')
	elif info !='':
		s=Searcher(info)
		s.search_image()


def cleartext():
	addr.delete(0,'end')
	srch_text.delete(0,'end')



#GUI


root = Tk().geometry("750x450")
v=StringVar()
z=StringVar()
tframe=Frame(root)
tframe.pack(side=TOP,pady=10,fill=X)
addrc=Label(tframe,text="CONTENT BASED IMAGE RETREIVAL SYSTEM",font=('bold'))
addrc.pack(pady=10)
addrc=Label(tframe,text="Enter the Path of Image folder",font=('bold'))
addrc.pack(pady=10)
addr=Entry(tframe,textvariable=z)
addr.pack(fill=X,padx=30)
btn=Button(tframe,text="Index DB",fg="red",bg="white",command=call_index)
btn.pack(pady=10,padx=300,side=LEFT)


#search

frame=Frame(root)
frame.pack()
srch=Label(frame,text="Enter query image name",font=('bold'))
srch.pack(pady=10)
srch_text=Entry(frame,textvariable=v)
srch_text.pack(fill=X,padx=30)
btn_ss=Button(frame,text="Search",fg="blue",bg="white",command=call_search)
btn_ss.pack(pady=10,padx=90,side=LEFT)

lframe=Frame(root)
lframe.pack()
cbtn=Button(lframe,text="Clear fields",fg="green",bg="white",command=cleartext)
cbtn.pack(pady=10,padx=20,side=LEFT)

mainloop()
