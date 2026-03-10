
import tkinter as tk

ventana = tk.Tk()

opcion = tk.StringVar()
opcion.set("Seleccione")

menu = tk.OptionMenu(
    ventana,
    opcion,
    "Python",
    "Java",
    "C++"
)
menu.pack()

btn = tk.Button(
    ventana,
    text = "Ver opción",
    command = lambda: print(opcion.get())
)

btn.pack()

ventana.geometry("200x100")
ventana.mainloop()
