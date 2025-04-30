import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Todo List')

list_text = ttk.Label(text = 'Todo List')
list_text.grid(row = 0, column = 0, columnspan = 2)

checkbox_a = tk.Checkbutton(text = '')
checkbox_a.grid(row = 1, column = 0)

checkbox_b = tk.Checkbutton(text = '')
checkbox_b.grid(row = 2, column = 0)

checkbox_c = tk.Checkbutton(text = '')
checkbox_c.grid(row = 3, column = 0)

taskbox_a = ttk.Entry()
taskbox_a.grid(row = 1, column = 1, padx = 5, pady = 5)

taskbox_b = ttk.Entry()
taskbox_b.grid(row = 2, column = 1, padx = 5, pady = 5)

taskbox_c = ttk.Entry()
taskbox_c.grid(row = 3, column = 1, padx = 5, pady = 5)

root.mainloop()