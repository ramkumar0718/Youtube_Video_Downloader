from pytube import YouTube
import tkinter 
from tkinter import *
from PIL import ImageTk, Image
 
root = tkinter.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Video Downloader") 

# Youtube Logo
my_pic = Image.open("youtube.png")
resized = my_pic.resize((80, 80), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
my_pic = ImageTk.PhotoImage(file="youtube.png")
my_label = Label(root, image=new_pic)
my_label.place(x= 50, y = 10)

tkinter.Label(root, text =' Video Downloader', font ='arial 20 bold').place(x= 140, y = 35)
# Input Link
link = tkinter.StringVar() 
tkinter.Label(root, text ='Paste Link Here:', font ='arial 15 bold').place(x= 170, y = 100)
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 140)
 
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download()
    tkinter.Label(root, fg="green", text ='Sucessfully Downloaded !', font ='arial 16').place(x= 130, y = 245)
 
tkinter.Button(root, text ='DOWNLOAD', font ='arial 15 bold',padx = 2, command = Downloader).place(x=180, y = 190)
tkinter.Label()
root.mainloop()





