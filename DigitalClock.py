import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")

def time():
    string = time.strftime("%H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(root, font=("calibri", 50, 'bold'), background="black", foreground="cyan")
label.pack(anchor='center')

time()
root.mainloop()

