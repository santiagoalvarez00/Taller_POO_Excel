
class Parqueadero:
    
    def __init__(self):
        self.puesto = ""
        self.fecha_entrada = ""
        self.hora_entrada = ""
        self.hora_salida = ""
        self.estado = ""
        self.texto_tabla = []
        
    def get_puesto(self):
        return self.puesto
    
    def get_fecha_entrada(self):
        return self.fecha_entrada
    
    def get_hora_entrada(self):
        return self.hora_entrada
    
    def get_hora_salida(self):
        return self.hora_salida
    
    def get_estado(self):
        return self.estado
    
    def get_texto_tabla(self):
        return self.texto_tabla
    
    def set_puesto(self, nuevo_puesto):
        self.puesto = nuevo_puesto
        
    def set_fecha_entrada(self, nuevo_fecha_entrada):
        self.fecha_entrada = nuevo_fecha_entrada
        
    def set_hora_entrada(self, nuevo_hora_entrada):
        self.hora_entrada = nuevo_hora_entrada
        
    def set_hora_salida(self, nuevo_hora_salida):
        self.hora_salida = nuevo_hora_salida
        
    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def set_texto_tabla(self, nuevo_texto_tabla):
        self.texto_tabla = nuevo_texto_tabla
        
    def mostrar_info(self):
        print(f"Puesto: {self.puesto} - Fecha Entrada: {self.fecha_entrada} - Hora Entrada: {self.hora_entrada}")
        
    def guardar_info(self, obj_usuario, obj_carro, puesto, fecha_entrada, hora_entrada, hora_salida, estado):
        
        fila = {
            "cedula": obj_usuario.get_cedula(),
            "nombre": obj_usuario.get_nombre(),
            "tipo_usuario": obj_usuario.get_tipo_usuario(),
            "placa": obj_carro.get_placa_carro(),
            "tipo_carro": obj_carro.get_tipo_carro(),
            "color_carro": obj_carro.get_color_carro(),
            "puesto": puesto,
            "fecha_entrada": fecha_entrada,
            "hora_entrada": hora_entrada,
            "hora_salida": hora_salida,
            "estado": estado
            }
        
        self.texto_tabla.append(fila)
        
    def mostrar_tabla(self):
        if not self.texto_tabla:
            print("No hay datos en la tabla.")
            return
        
        print("-" * 100)
        print(
            f"{"Cédula Usuario":<20}"
            f"{"Nombre Usuario":<20}"
            f"{"Tipo Usuario":<20}"
            f"{"Placa Carro":<20}"
            f"{"Tipo Carro":<20}"
            f"{"Color Carro":<20}"
            f"{"Puesto":<15}"
            f"{"Fecha Entrada":<20}"
            f"{"Hora Entrada":<20}"
            f"{"Hora Salida":<20}"
            f"{"Estado"}"
        )
        print("-" * 100)
        
        for fila in self.texto_tabla:
            print(
                f"{fila["cedula"]:<20}"
                f"{fila["nombre"]:<20}"
                f"{fila["tipo_usuario"]:<20}"
                f"{fila["placa"]:<20}"
                f"{fila["tipo_carro"]:<20}"
                f"{fila["color_carro"]:<20}"
                f"{fila["puesto"]:<15}"
                f"{fila["fecha_entrada"]:<20}"
                f"{fila["hora_entrada"]:<20}"
                f"{fila["hora_salida"]:<20}"
                f"{fila["estado"]:<20}"
            )
        
        print("-" * 100)