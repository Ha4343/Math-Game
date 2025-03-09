import tkinter as tk
from tkinter import simpledialog, messagebox

def show_question(question):
    root = tk.Tk()
    root.withdraw()  # Hide main window
    return simpledialog.askstring("Math Challenge", f"Solve: {question} (5 sec)")

def show_result(message, score):
    messagebox.showinfo("Result", f"{message}\nCurrent Score: {score}")
