class Usuario:
    
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        
    def get_cedula(self):
        return self.cedula
    
    def get_nombre(self):
        return self.nombre