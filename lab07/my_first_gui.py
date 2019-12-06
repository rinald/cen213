from tkinter import *


class _Frame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.build()

    def build(self):
        pass


class App(_Frame):
    def greet(self):
        self.label.config(text='GREETINGS!!!')

    def build(self):
        self.label = Label(self, text='This is our first GUI!')
        self.label.pack()
        self.button1 = Button(self, width=15, text='Greet', command=self.greet)
        self.button1.pack(side=LEFT)
        self.button2 = Button(self, width=15, text='Close',
                              command=self.master.destroy)
        self.button2.pack(side=LEFT)


root = Tk()
root.title('My first GUI')
App(root).pack()
mainloop()
