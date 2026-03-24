# Level 084

# -----------------------
# --   TESTING THE   ----
# -- CUSTOM TKINTER  ----
# --     LIBRARY     ----
# -----------------------

# Remember: this only work in python3 so if u have any problem with the code
# just put at your terminal (when u are at the directory) python3 + name_file.py and this will show 
# a window

import tkinter as tk
from tkinter import * 
import random


def poesy():
    poems = ["Two roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference.\n\n— Robert Frost",
             "Do not go gentle into that good night,\nRage, rage against the dying of the light.\n\n— Dylan Thomas",
             "Hope is the thing with feathers\nThat perches in the soul.\n\n— Emily Dickinson",
             "I am the master of my fate,\nI am the captain of my soul.\n\n— William Ernest Henley",
             "The woods are lovely, dark and deep,\nBut I have promises to keep.\n\n— Robert Frost",
             "Shall I compare thee to a summer's day?\nThou art more lovely and more temperate.\n\n— William Shakespeare",
             "What lies behind us and what lies before us\nare tiny matters compared to what lies within us.\n\n— Ralph Waldo Emerson",
                "The only way out is through.\n\n— Robert Frost" 
    ]

    poem = random.choice(poems)

    poem_display.config(state = "normal")
    poem_display.delete("1.0", "end")
    poem_display.insert("1.0", poem)
    poem_display.config(state = "disabled")

# Window 

window = tk.Tk()
window.title('Poesy')
window.geometry("500x500")
window.configure(background="#1a1a2e")

title_label = tk.Label(
    master = window,
    text = "Click on the button and recive a poesy", 
    font = 'Georgia 16 bold',
    bg = "#1a1a2e",
    fg = "#2bff00"
    )
title_label.pack()

# Input 

poem_display = tk.Text(
    master = window, 
    height = 5,
    width = 50,
    fg = "#0f3460",
    bg = "#eaeaea",
    state = "disabled",
    font = ("Georgia", 12),
    relief = "sunken",
    bd = 2,
    padx = 15,
    pady = 15
    )

poem_display.pack(pady = 30)

# Button 

button = tk.Button(master = window, text = "Show Poetry", command = poesy, bg="black", fg = "#00ff40", font = "Georgia 12 bold")
button.pack(pady = 10)

# Run 

window.mainloop()