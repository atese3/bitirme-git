from Tkinter import *
import webbrowser

def Wopen():
    webbrowser.open("***Path of Html File****")
           
class MainProcess(object):
    def __init__(self):

        self._button1 = Button(arka,image= img2,compound="bottom",command= Wopen )
        self._button1.pack(side=LEFT)

        self._frame = Frame()
        self._frame.pack(padx=5)

        self._button2 = Button(arka,image=img3,compound="bottom")
        self._button2.pack(side=RIGHT)

       
_window = Tk()

img1 = PhotoImage(file="***path of photo file***")
img2 = PhotoImage(file="***path of photo file***")
img3 = PhotoImage(file="***path of photo file***")


_background = Label(image=img1)
_background.pack(fill='both',expand='yes')


_window.geometry("640x480")
_process = MainProcess()
mainloop()
