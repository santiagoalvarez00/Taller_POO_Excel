
class Calculadora:
    
    def __init__(self):
        self.fecha = ""
        self.tipo_operacion = ""
        self.resultado = ""
        self.texto_tabla = []
        
    def get_fecha(self):
        return self.fecha
    
    def get_tipo_operacion(self):
        return self.tipo_operacion
    
    def get_resultado(self):
        return self.resultado
    
    def get_texto_tabla(self):
        return self.texto_tabla
        
    def set_fecha(self, nuevo_fecha):
        self.fecha = nuevo_fecha
        
    def set_tipo_operacion(self, nuevo_tipo_operacion):
        self.tipo_operacion = nuevo_tipo_operacion
        
    def set_resultado(self, nuevo_resultado):
        self.resultado = nuevo_resultado
        
    def set_texto_tabla(self, nuevo_texto_tabla):
        self.texto_tabla = nuevo_texto_tabla
        
    def mostrar_info(self):
        print(f"Fecha: {self.fecha} - Operacion: {self.tipo_operacion} - Resultado: {self.resultado}")
    
    def hacer_operacion(self, num1, num2, tipo_operacion):
        self.tipo_operacion = tipo_operacion
        if self.tipo_operacion == "Suma":
            self.resultado = self.hacer_suma(num1.get_numero(), num2.get_numero())
        elif self.tipo_operacion == "Resta":
            self.resultado = self.hacer_resta(num1.get_numero(), num2.get_numero())
        elif self.tipo_operacion == "Multiplicación":
            self.resultado = self.hacer_multiplicacion(num1.get_numero(), num2.get_numero())
        elif self.tipo_operacion == "División":
            self.resultado = self.hacer_division(num1.get_numero(), num2.get_numero())
        else: return "Error."
        return self.resultado
        
    def hacer_suma(self, num1, num2):
        return num1 + num2
    
    def hacer_resta(self, num1, num2):
        return num1 - num2
    
    def hacer_multiplicacion(self, num1, num2):
        return num1 * num2
    
    def hacer_division(self, num1, num2):
        return num1 / num2
    
    def guardar_info(self, fecha, obj_usuario, num1, num2):

        fila = {
            "cedula": obj_usuario.get_cedula(),
            "nombre": obj_usuario.get_nombre(),
            "num1": num1.get_numero(),
            "num2": num2.get_numero(),
            "operacion": self.tipo_operacion,
            "resultado": self.resultado,
            "fecha": fecha   
                }
        

        self.texto_tabla.append(fila)

    
    def mostrar_tabla(self):
        if not self.texto_tabla:
            print("No hay datos en la tabla.")
            return

        print("-" * 100)
        print(
            f"{'Cédula':<20}"
            f"{'Nombre Usuario':<40}"
            f"{'Número 1':<15}"
            f"{'Número 2':<15}"
            f"{'Tipo de Operación':<25}"
            f"{'Resultado':<15}"
            f"{'Fecha de Uso':<20}"
            )
        print("-" * 100)

        for fila in self.texto_tabla:
            print(
                f"{fila['cedula']:<20}"
                f"{fila['nombre']:<40}"
                f"{fila['num1']:<15}"
                f"{fila['num2']:<15}"
                f"{fila['operacion']:<25}"
                f"{fila['resultado']:<15}"
                f"{fila['fecha']:<20}"
                )

        print("-" * 100)
        