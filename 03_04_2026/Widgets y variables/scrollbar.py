
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

texto = tk.Text(
    ventana,
    width = 30,
    height = 10
)

scroll = ttk.Scrollbar(
    ventana,
    command = texto.yview
)

texto.config(
    yscrollcommand = scroll.set
)

texto.pack(side = "left")
scroll.pack(
    side = "right",
    fill = "y"
)

ventana.mainloop()