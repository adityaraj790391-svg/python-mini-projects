import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")

def time():
    string = time.strftime("%H:%M%S \n %D")
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(root, font=("ds-digital", 50), background="black", foreground="cyan")

