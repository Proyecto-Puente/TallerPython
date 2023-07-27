# Ejercicio 7
# Taller: introducción a python
# Día 2

# Consigna:
#   Crea un programa que genere un número aleatorio entre 1 y 100. Luego, permite al
#   usuario intentar adivinar ese número. Si el número ingresado es menor al generado,
#   muestra el mensaje "El número es más grande". Si es mayor, muestra 
#   "El número es más pequeño". Cuando el usuario adivine el número, 
#   muestra "¡Correcto!" y finaliza el programa.

# El método "randint" genera un numero pseudo-aleatorio en el 
# intervalo de [a,b], siendo 'a' y 'b' dos numeros enteros
from random import randint

nro = randint(1,100)

while True:
  eleccion = int(input("Ingrese un numero: "))

  if eleccion == nro:
    print("¡Ganaste! Ese es el numero.")
    if input("¿Queres seguir jugando? (Si-No): ").upper() == "SI":
        nro = randint(1,100)
        continue
    else:
        break

  elif eleccion > nro:
    print("El numero es menor...")

  else:
    print("El numero es mayor...")
print("Fin del juego.")