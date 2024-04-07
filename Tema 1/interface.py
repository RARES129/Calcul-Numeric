import tkinter as tk
from tkinter import scrolledtext
import subprocess


def clear_output():
    scroll.delete("1.0", tk.END)


def run_script(script):
    clear_output()
    output = subprocess.check_output(["python", script], universal_newlines=True)
    scroll.insert(tk.END, f"Output for {script}:\n{output}\n\n")
    scroll.see(tk.END)


window = tk.Tk()
window.title("Python Script Runner")

scroll = scrolledtext.ScrolledText(window, width=100, height=20, wrap=tk.WORD)
scroll.grid(row=0, column=0, columnspan=4)

button1 = tk.Button(window, text="Run ex_1.py", command=lambda: run_script("ex_1.py"))
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = tk.Button(window, text="Run ex_2.py", command=lambda: run_script("ex_2.py"))
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = tk.Button(window, text="Run ex_3.py", command=lambda: run_script("ex_3.py"))
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = tk.Button(window, text="Run bonus.py", command=lambda: run_script("bonus.py"))
button4.grid(row=1, column=3, padx=5, pady=5)

window.mainloop()
