from tkinter import *
import qrcode
from PIL import Image,ImageTk

class Appwin(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master,width=300,height=400)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text="hello",command=self.genQrcode)
        self.alertButton.pack()
        self.label = Label(self)
        self.label.pack()

    def genQrcode(self):
        text = self.nameInput.get() or "没有输入"
        self.img = qrcode.make(text)
        self.tkImage = ImageTk.PhotoImage(image=self.img)
        self.label.config(image=self.tkImage)
        self.label.image=self.tkImage

root = Appwin()
root.master.title('二维码')
root.mainloop()
