from tkinter import *


class _Frame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.build()

    def build(self):
        pass


class RadioButtons(_Frame):
    def build(self):
        self.button1 = Radiobutton(
            self,
            text='Blue',
            padx=10,
            variable=self.master.color_var,
            value=1,
            command=self.master.update_label
        )
        self.button1.pack(anchor=W)
        self.button2 = Radiobutton(
            self,
            text='Red',
            padx=10,
            variable=self.master.color_var,
            value=2,
            command=self.master.update_label
        )
        self.button2.pack(anchor=W)
        self.button3 = Radiobutton(
            self,
            text='Green',
            padx=10,
            variable=self.master.color_var,
            value=3,
            command=self.master.update_label
        )
        self.button3.pack(anchor=W)


class CheckBoxes(_Frame):
    def build(self):
        self.check1 = Checkbutton(
            self,
            text='Bold',
            padx=10,
            variable=self.master.bold_var,
            command=self.master.update_label
        )
        self.check1.pack()
        self.check2 = Checkbutton(
            self,
            text='Italic',
            padx=10,
            variable=self.master.italic_var,
            command=self.master.update_label
        )
        self.check2.pack()


class BottomButtons(_Frame):
    def build(self):
        self.button1 = Button(
            self,
            text='Verdana',
            padx=20,
            command=lambda: self.master.set_font('Verdana')
        )
        self.button1.pack(side=LEFT)
        self.button2 = Button(
            self,
            text='Times',
            padx=20,
            command=lambda: self.master.set_font('Times')
        )
        self.button2.pack(side=LEFT)
        self.button3 = Button(
            self,
            text='Quit',
            padx=20,
            command=self.master.master.destroy
        )
        self.button3.pack(side=LEFT)


class App(_Frame):
    def set_font(self, font):
        self.font = font
        self.update_label()

    def update_label(self):
        color_var = self.color_var.get()
        bold_var = self.bold_var.get()
        italic_var = self.italic_var.get()

        font = self.font + self.font_size

        if color_var == 1:
            color = 'blue'
        elif color_var == 2:
            color = 'red'
        elif color_var == 3:
            color = 'green'
        else:
            color = 'black'

        if bold_var:
            font += ' bold'
        if italic_var:
            font += ' italic'

        self.label.config(fg=color, font=font)

    def build(self):
        self.font = 'Times'
        self.font_size = ' 16'
        self.color_var = IntVar()
        self.bold_var = BooleanVar()
        self.italic_var = BooleanVar()

        self.label = Label(
            self,
            text='Python GUI Programming',
            font=self.font+self.font_size,
            padx=30,
            pady=30
        )
        self.bottom_buttons = BottomButtons(self)
        self.bottom_buttons.pack(side=BOTTOM)

        self.radio_buttons = RadioButtons(self)
        self.radio_buttons.pack(side=LEFT)
        self.label.pack(side=LEFT)
        self.check_boxes = CheckBoxes(self)
        self.check_boxes.pack(side=LEFT)


root = Tk()
root.title('Button Demo')
App(root).pack()
mainloop()
