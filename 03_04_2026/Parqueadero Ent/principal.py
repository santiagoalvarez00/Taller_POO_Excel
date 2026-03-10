
from parqueadero import Parqueadero
from carro import Carro
from usuario import Usuario

obj_parqueadero = Parqueadero()

# 1
obj_usuario = Usuario("1020345678", "Juan García", "Administrador")
obj_carro = Carro("ABC123", "Sedan", "Negro")
obj_parqueadero.guardar_info(obj_usuario, obj_carro, "A-01", "2026-02-16", "08:30", "", "Entrada")


# 2
obj_usuario = Usuario("1020345679", "María López", "Cliente")
obj_carro = Carro("XYZ789", "SUV", "Blanco")
obj_parqueadero.guardar_info(obj_usuario, obj_carro, "B-05", "2026-02-16", "09:15", "", "Entrada")

# 3
obj_usuario = Usuario("1020345680", "Carlos Rodríguez", "Cliente")
obj_carro = Carro("KLM456", "Pickup", "Azul")
obj_parqueadero.guardar_info(obj_usuario, obj_carro, "C-12", "2026-02-16", "10:00", "11:45", "Salida")

# 4
obj_usuario = Usuario("1020345681", "Ana Martínez", "Cliente")
obj_carro = Carro("DEF321", "Hatchback", "Rojo")
obj_parqueadero.guardar_info(obj_usuario, obj_carro, "A-03", "2026-02-16", "11:20", "", "Entrada")


obj_parqueadero.mostrar_tabla()



"""
a = obj_usuario = Usuario("1020345678", "Juan García", "Administrador")

print(a.mostrar_info())
a.set_cedula("13")
print(a.mostrar_info())

b = obj_usuario.get_cedula

print(a.mostrar_info())
"""



"""
# 1
obj_numero1 = Numero(50)
obj_numero2 = Numero(30)
obj_usuario = Usuario("1020345678", "Juan García López")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Suma")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-16", obj_usuario, obj_numero1, obj_numero2)

# Final
obj_calculadora.mostrar_tabla()

"""
