#! python3

from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("This is my first tkinter app")
        self.pack(fill=BOTH, expand=1)

        # menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Save', command=self.client_samp)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImage)
        edit.add_command(label='Show Text', command=self.showText)
        edit.add_command(label='Undo', command=self.client_samp)
        menu.add_cascade(label='Edit', menu=edit)
        

        # buttons
        sampButton = Button(self, text="Sample button", command=self.client_samp)
        sampButton.place(x=10, y=10)

        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=100, y=10)

    def showImage(self):
        print('Show image')
        load = Image.open('foto.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showText(self):
        print('show text')
        text = Label(self, text='Hello World')
        text.pack()
        

    def client_samp(self):
        print('Click log...')

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
