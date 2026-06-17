## TKINTER Module is a library in python used to create GUI applications. It provides a set of tools and widgets to build graphical user interfaces, such as buttons, labels, text boxes, and more. TKINTER is included with Python, making it a convenient choice for creating desktop applications.

import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Game Over", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()