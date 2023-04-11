import tkinter as tk 
import RPi.GPIO as GPIO
from time import sleep

GPIO17 = 17
GPIO27 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO17, GPIO.OUT)
GPIO.setup(GPIO27, GPIO.OUT)

master = tk.Tk()
master.title("Raspberry PI Home Automation")
master.geometry("800x400")


GPIO17_state = True
GPIO27_State = True

def GPIO17button():
	global GPIO17_state
	if GPIO17_state == True:
		GPIO.output(GPIO17, GPIO17_state)
		GPIO17_state = False
		ONlabel = tk.Label(master, text="Turned ON", fg="green")
		ONlabel.place(x=300, y=100)
	else:
		GPIO.output(GPIO17, GPIO17_state)
		GPIO17_state = True
		ONlabel = tk.Label(master, text="Turned OFF", fg="red")
		ONlabel.place(x=300, y=100)


def GPIO27button():
	global GPIO27_State
	if GPIO27_State == True:
		GPIO.output(GPIO27, GPIO27_State)
		GPIO27_State = False
		OFFlabel = tk.Label(master, text="Turned ON", fg="green")
		OFFlabel.place(x=300, y=150)
	else:
		GPIO.output(GPIO27, GPIO27_State)
		GPIO27_State = True
		OFFlabel = tk.Label(master, text="Turned OFF", fg="red")
		OFFlabel.place(x=300, y=150)

ONbutton = tk.Button(master, text="SWITCH_1", bg="blue", command=GPIO17button)
ONbutton.place(x=100, y=100)
ONbutton.config(font=("Courier", 20))

OFFbutton = tk.Button(master, text="SWITCH_2",bg="blue" , command=GPIO27button)
OFFbutton.place(x=100, y=150)
OFFbutton.config(font=("Courier", 20))

Exitbutton = tk.Button(master, text="EXIT",bg="red", command=master.destroy)
Exitbutton.place(x=100, y=200)

l1 = tk.Label(master, text = "HOME AUTOMATION")
l1.place(x=120, y=10)
l1.config(font=("Courier", 40))
master.mainloop()
