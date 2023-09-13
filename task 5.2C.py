from tkinter import *  # library for gui 
from gpiozero import LED # to initialize gpio pins
import RPi.GPIO

led1 = LED(11)
led2 = LED(10)
led3 = LED(9)

box = Tk()  # box  will be used to access the functions of tkinter. 

box.geometry("200x200")

box.configure(bg="black")

label2 = Label(box, text=" (a traffic light inspire) ")  # this text on our gui. 
label2.pack(pady=10) # pack variable for displaying. 

def red():
    if led1.is_lit:
        selection = "red light is off - you can go"
        label.config(text = selection)
        led1.off()

    else:
        selection = "red light on - please stop"
        label.config(text = selection)
        led1.on()
        led2.off()
        led3.off()

def blue():
    if led2.is_lit:
        selection = "blue led is off"
        label.config(text = selection)
        led2.off()

    else:
        selection = "blue light glowing, wait"
        label.config(text = selection)
        led1.off()
        led2.on()
        led3.off()

def green():
    if led3.is_lit:
        selection = "green light is off, stop"
        label.config(text = selection)
        led3.off()

    else:
        selection = "green light on - go  "
        label.config(text = selection)
        led1.off()
        led2.off()
        led3.on()

button1 = Radiobutton(text = "Red",  background="red", command=red)
button1.pack(pady=10)

button2 = Radiobutton(text = "Blue", background="blue", command=blue)
button2.pack(pady=10)

button3 = Radiobutton(text = "Green", background="green", command=green)
button3.pack(pady=10)

label = Label(box)
label.pack(pady=10)

box.mainloop()