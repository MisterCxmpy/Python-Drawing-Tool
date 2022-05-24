
from tkinter import *
from tkinter import colorchooser
from tkinter.colorchooser import askcolor
import tkinter as tk
from tkinter import ttk
import os, sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

root = Tk()

root.title("Drawing")
root.geometry("1050x570+150+20")
root.configure(bg="#f2f2f2")
root.resizable(False, False)

currentX = 0
currentY = 0
colour = "black"
_colour = "white"

def LocateXY(work):
    global currentX, currentY

    currentX = work.x
    currentY = work.y 

def AddLine(work):
    global currentX, currentY

    canvas.create_line((currentX, currentY, work.x, work.y), width=GetCurrentValue(), fill=colour, capstyle=ROUND, smooth=True)
    currentX, currentY = work.x, work.y

def ShowColour(newColour):
    global colour

    colour = newColour

def NewCanvas():
    canvas.delete("all")
    DisplayPallete()

imageIcon = PhotoImage(file="Images\\logo.png")
root.iconphoto(False, imageIcon)

colorBox = PhotoImage(file="Images\\color section.png")
Label(root, image=colorBox, bg="#f2f2f2").place(x=10, y=10)

eraser = PhotoImage(file="Images\\eraser.png")
Button(root, image=eraser, bg="#f2f2f2", command=NewCanvas).place(x=30, y=400)

colours = Canvas(root, bg="#ffffff", width=37, height=305, bd=0)
colours.place(x=30, y=60)

def ColourPicker():
    global _colour

    _colour = colorchooser.askcolor()
    ShowColour(_colour[1])

    id = colours.create_rectangle((10, 280, 30, 300), fill=_colour[1])
    colours.tag_bind(id, "<Button-1>", lambda x: ColourPicker())

def DisplayPallete():
    id = colours.create_rectangle((10, 10, 30, 30), fill="black")
    colours.tag_bind(id, "<Button-1>", lambda x: ShowColour("black"))

    id = colours.create_rectangle((10, 40, 30, 60), fill="gray")
    colours.tag_bind(id, "<Button-1>", lambda x: ShowColour("gray"))

    id = colours.create_rectangle((10, 70, 30, 90), fill="brown4")
    colours.tag_bind(id, "<Button-1>", lambda x: ShowColour("brown4"))

    id = colours.create_rectangle((10, 100, 30, 120), fill="red")
    colours.tag_bind(id, "<Button-1>", lambda x: ShowColour("red"))

    id = colours.create_rectangle((10, 130, 30, 150), fill="orange")
    colours.tag_bind(id, "<Button-1>", lambda x: ShowColour("orange"))

    id = colours.create_rectangle((10, 160, 30, 180), fill="yellow")
    colours.tag_bind(id, "<Button-1>", lambda x: ShowColour("yellow"))

    id = colours.create_rectangle((10, 190, 30, 210), fill="green")
    colours.tag_bind(id, "<Button-1>", lambda x: ShowColour("green"))

    id = colours.create_rectangle((10, 220, 30, 240), fill="blue")
    colours.tag_bind(id, "<Button-1>", lambda x: ShowColour("blue"))

    id = colours.create_rectangle((10, 250, 30, 270), fill="purple")
    colours.tag_bind(id, "<Button-1>", lambda x: ShowColour("purple"))

    id = colours.create_rectangle((10, 280, 30, 300), fill="white")
    colours.tag_bind(id, "<Button-1>", lambda x: ColourPicker())

DisplayPallete()

canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind("<Button-1>", LocateXY)
canvas.bind("<B1-Motion>", AddLine)

currentValue = tk.DoubleVar()

def GetCurrentValue():
    return '{: .0f}'.format(currentValue.get())

def SliderChanged(event):
    valueLabel.configure(text=GetCurrentValue())

slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=SliderChanged, variable=currentValue)
slider.place(x=30, y=530)

valueLabel = ttk.Label(root, text=GetCurrentValue())
valueLabel.place(x=27, y=550)

root.mainloop()