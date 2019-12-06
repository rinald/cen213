from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Converter')
entry = Entry(root)
entry.grid(row=0, column=1)
Label(text='inches').grid(row=0, column=2)
Label(text='is equivalent to').grid(row=1, column=0)
label = Label(text='')
label.grid(row=1, column=1)
Label(text='cm').grid(row=1, column=2)


def convert():
    try:
        value = float(entry.get())
    except:
        messagebox.showerror('Error', 'Error: you should enter a number')
    else:
        value *= 2.54
        label.config(text=str(value))


def reset():
    entry.delete(0, 'end')
    label.config(text='')


button1 = Button(text='Calculate', command=convert)
button1.grid(row=2, column=0)
button2 = Button(root, text='Reset', command=reset)
button2.grid(row=2, column=1)
button3 = Button(root, text='Quit', command=root.destroy)
button3.grid(row=2, column=2)

mainloop()
