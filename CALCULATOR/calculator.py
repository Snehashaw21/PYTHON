#Calculater:

import tkinter as tk
import math

exp = ""

def press(key):
    global exp
    if key == "√":
        exp += "math.sqrt("
    elif key == "^":
        exp += "**"
    elif key == "%":
        exp += "/"
    else:
        exp += str(key)
    equation.set(exp)

def equalpress():
    global exp
    try:
        result = str(eval(exp))
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""

def clear():
    global exp
    exp = ""
    equation.set("")

root = tk.Tk()
root.title(" Calculator")
equation = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("+",4,2),("=",4,3),
    ("√",5,0),("^",5,1),("%",5,2),("C",5,3),
]

for (text,row,col) in buttons:
    if text == "=":
        b = tk.Button(root, text=text, bg="lightblue", command=equalpress, height=3, width=7)
    elif text == "C":
        b = tk.Button(root, text=text, bg="red", fg="white", command=clear, height=3, width=7)
    else:
        b = tk.Button(root, text=text, command=lambda t=text: press(t), height=3, width=7)
    b.grid(row=row, column=col, padx=2, pady=2)

root.mainloop()
