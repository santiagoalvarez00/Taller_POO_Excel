
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Formulario.")
ventana.geometry("500x650")

nombre_var = tk.StringVar()
genero_var = tk.StringVar()
lenguaje_var = tk.StringVar()
lenguaje_var.set("Seleccione.")
python = tk.IntVar()
java = tk.IntVar()

label_n = tk.Label(ventana, text="Nombre")
label_n.pack()

entry_n = (tk.Entry(ventana, textvariable = nombre_var))
entry_n.pack()

label_g = tk.Label(ventana, text ="Genero:")
label_g.pack()

radio_m = tk.Radiobutton(ventana, text = "Maculino", variable = genero_var, value = "Masculino")
radio_m.pack()

radio_f = tk.Radiobutton(ventana, text = "Femenino", variable = genero_var, value = "Femenino")
radio_f.pack()

label_i = tk.Label(ventana, text = "Intereses")
label_i.pack()

check_p = tk.Checkbutton(ventana, text = "Python", variable = "Python").pack()

check_j = tk.Checkbutton(ventana, text = "Java", variable = "Java").pack()

label_l = tk.Label(ventana, text = "Lenguaje Favorito").pack()

opcion_m = tk.OptionMenu(ventana, lenguaje_var, "Python", "Java", "C++").pack()

label_pais = tk.Label(ventana, text = "Seleccione país: ").pack()

lista = tk.Listbox(ventana, height = 3)
lista.insert(1, "Colombia")
lista.insert(2, "Venezuela")
lista.insert(3, "Perú")
lista.pack()

separador = ttk.Separator(ventana, orient = "horizontal").pack(fill = "x", pady = 10)

label_r = tk.Label(ventana, text = "Resultados").pack()

frame_resultado = tk.Frame(ventana).pack()

texto = tk.Text(frame_resultado, width = 50, height = 10)
#¿Así es el text.xview?
scroll = ttk.Scrollbar(frame_resultado, command = texto.xview)
texto.config(yscrollcommand = scroll.set)
texto.pack(side = "left")
scroll.pack(side = "right", fill = "y")

def mostrar_resultado():
    texto.insert("End", "Nombre: " + nombre_var.get() + "\n")
    texto.insert("End", "Genero: " + genero_var.get() + "\n")
    texto.insert("End", "Intereses: ")
    if python.get() == 1:
        texto.insert("End", "Python")
    if java.get() == 1:
        texto.insert("End", "Java")
    texto.insert("End", "Lenguaje favorito: " + lenguaje_var.get() + "\n")
    
    seleccion = lista.curselection()
    if seleccion:
        texto.insert("End", "País" + lista.get(seleccion) + "\n")
        texto.see("End")
        
    btn__mostrar = tk.Button(ventana, text = "Mostrar resultados", command = mostrar_resultado).pack()
    

ventana.mainloop()
            
