
import tkinter as tk
from tkinter import ttk

from calculadora import Calculadora
from numero import Numero
from usuario import Usuario

calc = Calculadora()

num1 = None
operador = ""


def presionar(valor):
    pantalla.insert(tk.END, valor)


def operacion(op):

    global num1, operador

    num1 = float(pantalla.get())
    operador = op

    pantalla.delete(0, tk.END)


def igual():

    global num1

    num2 = float(pantalla.get())

    cedula = entrada_cedula.get()
    nombre = entrada_nombre.get()

    usuario = Usuario(cedula, nombre)

    obj1 = Numero(num1)
    obj2 = Numero(num2)

    resultado = calc.hacer_operacion(obj1, obj2, operador)

    calc.guardar(
        usuario.get_cedula(),
        usuario.get_nombre(),
        num1,
        num2
    )

    pantalla.delete(0, tk.END)
    pantalla.insert(0, resultado)

    tabla.insert(
        "",
        tk.END,
        values=(
            usuario.get_cedula(),
            usuario.get_nombre(),
            f"{num1}{operador}{num2}",
            resultado
        )
    )


def borrar():
    pantalla.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("880x300+325+225")


# -----------------------
# DATOS USUARIO
# -----------------------

tk.Label(ventana,text="Cédula").grid(row=0,column=0)
entrada_cedula = tk.Entry(ventana)
entrada_cedula.grid(row=0,column=1)

tk.Label(ventana,text="Nombre").grid(row=0,column=2)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0,column=3)


# -----------------------
# FRAME CALCULADORA
# -----------------------

frame_calc = tk.Frame(ventana)
frame_calc.grid(row=1,column=0,columnspan=4,pady=10)

pantalla = tk.Entry(frame_calc,font=("Arial",18),justify="right",width=20)
pantalla.grid(row=0,column=0,columnspan=4,pady=10)


# FILA 1

tk.Button(frame_calc,text="7",width=5,height=2,command=lambda:presionar("7")).grid(row=1,column=0)
tk.Button(frame_calc,text="8",width=5,height=2,command=lambda:presionar("8")).grid(row=1,column=1)
tk.Button(frame_calc,text="9",width=5,height=2,command=lambda:presionar("9")).grid(row=1,column=2)
tk.Button(frame_calc,text="÷",width=5,height=2,command=lambda:operacion("/")).grid(row=1,column=3)

# FILA 2

tk.Button(frame_calc,text="4",width=5,height=2,command=lambda:presionar("4")).grid(row=2,column=0)
tk.Button(frame_calc,text="5",width=5,height=2,command=lambda:presionar("5")).grid(row=2,column=1)
tk.Button(frame_calc,text="6",width=5,height=2,command=lambda:presionar("6")).grid(row=2,column=2)
tk.Button(frame_calc,text="×",width=5,height=2,command=lambda:operacion("*")).grid(row=2,column=3)

# FILA 3

tk.Button(frame_calc,text="1",width=5,height=2,command=lambda:presionar("1")).grid(row=3,column=0)
tk.Button(frame_calc,text="2",width=5,height=2,command=lambda:presionar("2")).grid(row=3,column=1)
tk.Button(frame_calc,text="3",width=5,height=2,command=lambda:presionar("3")).grid(row=3,column=2)
tk.Button(frame_calc,text="-",width=5,height=2,command=lambda:operacion("-")).grid(row=3,column=3)

# FILA 4

tk.Button(frame_calc,text="0",width=5,height=2,command=lambda:presionar("0")).grid(row=4,column=0)
tk.Button(frame_calc,text="C",width=5,height=2,command=borrar).grid(row=4,column=1)
tk.Button(frame_calc,text="=",width=5,height=2,command=igual).grid(row=4,column=2)
tk.Button(frame_calc,text="+",width=5,height=2,command=lambda:operacion("+")).grid(row=4,column=3)


# -----------------------
# HISTORIAL
# -----------------------

frame_historial = tk.Frame(ventana)
frame_historial.grid(row=1,column=4,padx=20)

tk.Label(frame_historial,text="Historial").pack()

columnas = ("Cédula","Nombre","Operación","Resultado")

tabla = ttk.Treeview(
    frame_historial,
    columns=columnas,
    show="headings",
    height=10
)

for col in columnas:
    tabla.heading(col,text=col)
    tabla.column(col,width=120)

tabla.pack()

ventana.resizable(False, False)
ventana.mainloop()