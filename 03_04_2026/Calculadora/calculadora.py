class Calculadora:
    
    def __init__(self):
        self.tipo_operacion = ""
        self.resultado = ""
        self.historial = []

    def hacer_operacion(self, num1, num2, tipo):

        self.tipo_operacion = tipo

        if tipo == "+":
            self.resultado = num1.get_numero() + num2.get_numero()

        elif tipo == "-":
            self.resultado = num1.get_numero() - num2.get_numero()

        elif tipo == "*":
            self.resultado = num1.get_numero() * num2.get_numero()

        elif tipo == "/":
            self.resultado = num1.get_numero() / num2.get_numero()

        return self.resultado


    def guardar(self, cedula, nombre, num1, num2):

        self.historial.append({
            "cedula": cedula,
            "nombre": nombre,
            "operacion": f"{num1} {self.tipo_operacion} {num2}",
            "resultado": self.resultado
        })