# Level 083

# ---------------------
# --   TESTANDO A   ---
# --   BIBLIOTECA   ---
# -- CUSTOM TKINTER ---
# ---------------------

# Observação: Para funcionar você precisa digitar no terminal python3 082.py 

import tkinter as tk
from tkinter import ttk

def convert():
    km_input = entry_int.get()
    mile_output = km_input / 1.61
    output_string.set(mile_output)
# Window

window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

# Title

title_label = ttk.Label(master = window, text = 'Converta Km para Milhas', font = 'Calibri 24 bold') #Window as parameter
title_label.pack()

# Input Field 
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar() 
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Converta', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label( 
    master = window,
    text = 'Output', 
    font = 'Calibri 24', 
    textvariable = output_string)
output_label.pack(pady = 5)
# Run

window.mainloop()