
class Usuario:
    
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        
    def get_cedula(self):
        return self.cedula
    
    def get_nombre(self):
        return self.nombre
    
    def set_cedula(self, nuevo_cedula):
        self.cedula = nuevo_cedula
        
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def mostrar_info(self):
        print(f"Cédula: {self.cedula} - Nombre: {self.nombre}")