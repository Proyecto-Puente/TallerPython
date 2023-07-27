# Ejercicio 1
# Taller: introducción a python
# Día 2

# Consigna:
#   Escribir un programa que pregunte al usuario su edad y muestre por pantalla
#   si es mayor de edad o no, además debe mostrar si es niño, adolescente, adulto o adulto mayor.

edad = int(input("Ingrese su edad: "))
if not (edad > 0 and edad <= 100):
  print("El valor no es correcto")
else:
  if edad < 13:
    print("Es menor de edad - niño")
  elif edad >= 13 and edad < 18:
    print("Es menor de edad - adolescente")
  elif edad >= 18 and edad < 75:
    print("Es mayor de edad - adulto")
  else:
    print("Es mayor de edad - adulto mayor")