# Ejercicio 5
# Taller: introducción a python
# Día 2

# Consigna:
#   Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for tabla in range(1,11):
  print("Tabla del", tabla)
  for num in range(1,11):
    print("\t",num, "x", tabla, "=", num*tabla)