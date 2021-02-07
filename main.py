import tkinter as tk
from tkinter import filedialog
from tkinter import *
import ImageToAscii as i


def options():
  print(option.get())
  return option.get()

def create_image():
    img = i.ImageToAscii()
    path = tk.filedialog.askopenfilename()
    img.create_image(path,options())

window = tk.Tk()

window.title('ImageToAscii')

window.configure(bg='#1d1d1d')

window.geometry('200x100')

option = IntVar()

create_image = tk.Button(window, text='Create Image', font='Roboto',
                         command=create_image).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

png = tk.Radiobutton(window, activebackground='#1d1d1d', selectcolor='#2d2d2d',highlightbackground='#1d1d1d', fg='white',
                     text='PNG', variable=option, value=1, bg='#1d1d1d', command=options).pack(side=tk.BOTTOM)

txt = tk.Radiobutton(window, activebackground='#1d1d1d', selectcolor='#2d2d2d',highlightbackground='#1d1d1d',
                     fg='white', text='TXT', variable=option, value=0, bg='#1d1d1d', command=options).pack()


window.mainloop()
