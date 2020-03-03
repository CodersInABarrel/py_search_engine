from tkinter import *
import tkinter
import webbrowser
from links import *
top = tkinter.Tk()

squery = StringVar()

def getsquery():
    http = 'https://www.google.com/search?q='
    if squery.get().startswith('www.'):
        http = 'http://'
    webbrowser.open(http + squery.get())# need http://
    sbar.delete(first=0,last=1000)

senbut = tkinter.Button(top, text ='patreon', activebackground = 'red', command = pat, activeforeground = 'red')
senbut2 = tkinter.Button(top, text ='discord', activebackground = 'red', command = disc, activeforeground = 'red')

sbut = tkinter.Button(top, text ='search', command  = getsquery , activebackground = 'red', activeforeground = 'red')
sbar = tkinter.Entry(top, textvariable = squery , bd =5)

senbut.pack(side = 'bottom')
senbut2.pack(side = 'bottom')

sbar.pack(side = 'left')
sbut.pack(side = 'right')
top.title('poogle')
top.mainloop()


