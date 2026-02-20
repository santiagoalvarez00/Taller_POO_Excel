
from calculadora import Calculadora
from numero import Numero
from usuario import Usuario

obj_calculadora = Calculadora()

# 1
obj_numero1 = Numero(50)
obj_numero2 = Numero(30)
obj_usuario = Usuario("1020345678", "Juan García López")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Suma")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-16", obj_usuario, obj_numero1, obj_numero2)

# 2
obj_numero1 = Numero(50)
obj_numero2 = Numero(30)
obj_usuario = Usuario("1020345678", "Juan García López")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Resta")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-16", obj_usuario, obj_numero1, obj_numero2)

# 3
obj_numero1 = Numero(50)
obj_numero2 = Numero(30)
obj_usuario = Usuario("1020345678", "Juan García López")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Multiplicación")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-16", obj_usuario, obj_numero1, obj_numero2)

# 4
obj_numero1 = Numero(150)
obj_numero2 = Numero(3)
obj_usuario = Usuario("1020345678", "Juan García López")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "División")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-16", obj_usuario, obj_numero1, obj_numero2)

# 5
obj_numero1 = Numero(100)
obj_numero2 = Numero(5)
obj_usuario = Usuario("1020345679", "María López Pérez")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Suma")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-16", obj_usuario, obj_numero1, obj_numero2)

# 6
obj_numero1 = Numero(100)
obj_numero2 = Numero(5)
obj_usuario = Usuario("1020345679", "María López Pérez")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Resta")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-16", obj_usuario, obj_numero1, obj_numero2)

# 7
obj_numero1 = Numero(100)
obj_numero2 = Numero(5)
obj_usuario = Usuario("1020345679", "María López Pérez")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Multiplicación")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-16", obj_usuario, obj_numero1, obj_numero2)

# 8
obj_numero1 = Numero(100)
obj_numero2 = Numero(5)
obj_usuario = Usuario("1020345679", "María López Pérez")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "División")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-16", obj_usuario, obj_numero1, obj_numero2)

# 9
obj_numero1 = Numero(200)
obj_numero2 = Numero(8)
obj_usuario = Usuario("1020345680", "Carlos Rodríguez Sánchez")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Suma")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-17", obj_usuario, obj_numero1, obj_numero2)

# 10
obj_numero1 = Numero(200)
obj_numero2 = Numero(8)
obj_usuario = Usuario("1020345680", "Carlos Rodríguez Sánchez")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Resta")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-17", obj_usuario, obj_numero1, obj_numero2)

# 11
obj_numero1 = Numero(75)
obj_numero2 = Numero(3)
obj_usuario = Usuario("1020345680", "Carlos Rodríguez Sánchez")

imp_obj_calculadora = obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "División")
imp_obj_calculadora2 = obj_calculadora.guardar_info("2026-02-17", obj_usuario, obj_numero1, obj_numero2)


# Final
obj_calculadora.mostrar_tabla()


