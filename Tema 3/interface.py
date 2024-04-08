import subprocess
import sys
import tkinter as tk
from tkinter import messagebox


def run_script (script_name, n):
    try:
        result = subprocess.run([sys.executable, script_name, str(n)], capture_output=True, text=True, input=str(n))
        return result.stdout
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Execution Error", e.output)
        return ""


def open_ex1 ():
    def execute ():
        n = n_entry.get()
        if not n.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid integer.")
            return
        output = run_script("ex1.py", n)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)

    ex1_window = tk.Toplevel(root)
    ex1_window.title("Execute ex1.py")

    tk.Label(ex1_window, text="Introduceti n:").pack()
    n_entry = tk.Entry(ex1_window)
    n_entry.pack()

    execute_button = tk.Button(ex1_window, text="Run", command=execute)
    execute_button.pack()

    output_text = tk.Text(ex1_window, height=25, width=70)
    output_text.pack()


def open_ex2 ():
    def execute ():
        n = n_entry.get()
        if not n.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid integer.")
            return
        output = run_script("ex2.py", n)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)

    ex1_window = tk.Toplevel(root)
    ex1_window.title("Execute ex2.py")

    tk.Label(ex1_window, text="Introduceti n:").pack()
    n_entry = tk.Entry(ex1_window)
    n_entry.pack()

    execute_button = tk.Button(ex1_window, text="Run", command=execute)
    execute_button.pack()

    output_text = tk.Text(ex1_window, height=25, width=70)
    output_text.pack()


def open_ex3 ():
    def execute ():
        n = n_entry.get()
        if not n.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid integer.")
            return
        output = run_script("ex3.py", n)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)

    ex1_window = tk.Toplevel(root)
    ex1_window.title("Execute ex3.py")

    tk.Label(ex1_window, text="Introduceti n:").pack()
    n_entry = tk.Entry(ex1_window)
    n_entry.pack()

    execute_button = tk.Button(ex1_window, text="Run", command=execute)
    execute_button.pack()

    output_text = tk.Text(ex1_window, height=25, width=70)
    output_text.pack()


def open_ex4 ():
    def execute ():
        n = n_entry.get()
        if not n.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid integer.")
            return
        output = run_script("ex4.py", n)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)

    ex1_window = tk.Toplevel(root)
    ex1_window.title("Execute ex4.py")

    tk.Label(ex1_window, text="Introduceti n:").pack()
    n_entry = tk.Entry(ex1_window)
    n_entry.pack()

    execute_button = tk.Button(ex1_window, text="Run", command=execute)
    execute_button.pack()

    output_text = tk.Text(ex1_window, height=25, width=70)
    output_text.pack()


def open_ex5 ():
    def execute ():
        n = n_entry.get()
        if not n.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid integer.")
            return
        output = run_script("ex5.py", n)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)

    ex1_window = tk.Toplevel(root)
    ex1_window.title("Execute ex5.py")

    tk.Label(ex1_window, text="Introduceti n:").pack()
    n_entry = tk.Entry(ex1_window)
    n_entry.pack()

    execute_button = tk.Button(ex1_window, text="Run", command=execute)
    execute_button.pack()

    output_text = tk.Text(ex1_window, height=25, width=70)
    output_text.pack()


def open_bonus ():
    def execute ():
        n = n_entry.get()
        if not n.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid integer.")
            return
        output = run_script("bonus.py", n)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)

    ex1_window = tk.Toplevel(root)
    ex1_window.title("Execute bonus.py")

    tk.Label(ex1_window, text="Introduceti n:").pack()
    n_entry = tk.Entry(ex1_window)
    n_entry.pack()

    execute_button = tk.Button(ex1_window, text="Run", command=execute)
    execute_button.pack()

    output_text = tk.Text(ex1_window, height=35, width=71)
    output_text.pack()


root = tk.Tk()
root.title("Interface")

ex1_button = tk.Button(root, text="Open ex1", command=open_ex1)
ex1_button.grid(row=0, column=0, padx=30, pady=30)

ex2_button = tk.Button(root, text="Open ex2", command=open_ex2)
ex2_button.grid(row=0, column=1, padx=30, pady=30)

ex3_button = tk.Button(root, text="Open ex3", command=open_ex3)
ex3_button.grid(row=0, column=2, padx=30, pady=30)

ex4_button = tk.Button(root, text="Open ex4", command=open_ex4)
ex4_button.grid(row=0, column=3, padx=30, pady=30)

ex5_button = tk.Button(root, text="Open ex5", command=open_ex5)
ex5_button.grid(row=0, column=4, padx=30, pady=30)

ex6_button = tk.Button(root, text="Open bonus", command=open_bonus)
ex6_button.grid(row=0, column=5, padx=30, pady=30)

root.mainloop()
