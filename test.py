import os

# Specify the file path
file_path = 'PythonKeyAdem.txt'

# Check if the file exists
if os.path.exists(file_path):
   print("The file exists.")
else:
   print("The file does not exist.")
   
   
from pathlib import Path

# Create a Path object
file_path = Path('DumpStack.txt')

# Check if the file exists
if file_path.exists():
   print("The file exists.")
else:
   print("The file does not exist.")
   
try:
    # Attempt to open the file
    with open('my_data/my_file.txt', 'r') as file:
        print("The file exists.")
except FileNotFoundError:
    print("The file does not exist.")
    
import os
print (os.getcwd())


from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()