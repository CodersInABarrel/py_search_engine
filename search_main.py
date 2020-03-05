from tkinter import *
import tkinter
import webbrowser
from links import *
from funcs import *
from pygame import mixer  # Load the popular external library
import time
mixer.init()
mixer.music.load('yo.mp3')



color = 'white'
top = tkinter.Tk()
squery = StringVar()

def getsquery():
    http = 'https://www.google.com/search?q='
    if squery.get().startswith('www.'):
        http = 'http://'
    webbrowser.open(http + squery.get())# need http://
    sbar.delete(first=0,last=1000)

def engchange():
    print('')
    
def ing():
    color = 'black'
    mixer.music.play()
    time.sleep(4.5)
    top.configure(background=color)

senbut = tkinter.Button(top, text ='patreon', activebackground = 'red', command = pat, activeforeground = 'red')
senbut2 = tkinter.Button(top, text ='discord', activebackground = 'red', command = disc, activeforeground = 'red')
engbut = tkinter.Button(top, text ='incognito', activebackground = 'red', command = ing, activeforeground = 'red')
sbut = tkinter.Button(top, text ='search', command  = getsquery , activebackground = 'red', activeforeground = 'red')
sbar = tkinter.Entry(top, textvariable = squery , bd =5)

senbut.grid(row = 2, column = 3, pady = 0)
senbut2.grid(row = 2, column = 2, pady = 0)
engbut.grid(row = 2, column = 1, pady = 0)
sbar.grid(row = 1, column = 2, pady = 0)
sbut.grid(row = 1, column = 1, pady = 0)


top.configure(background=color) 
top.title('poogle')
top.mainloop()


