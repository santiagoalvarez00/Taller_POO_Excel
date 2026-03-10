
class Usuario:
    
    def __init__(self, cedula, nombre, tipo_usuario):
        self.cedula = cedula
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario
        
    def get_cedula(self):
        return self.cedula
    
    def get_nombre(self):
        return self.nombre
    
    def get_tipo_usuario(self):
        return self.tipo_usuario
    
    def set_cedula(self, nuevo_cedula):
        self.cedula = nuevo_cedula
        
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def set_tipo_usuario(self, nuevo_tipo_usuario):
        self.tipo_usuario = nuevo_tipo_usuario
        
    def mostrar_info(self):
        print(f"Cédula: {self.cedula} - Nombre: {self.nombre} - Tipo Usuario: {self.tipo_usuario}")