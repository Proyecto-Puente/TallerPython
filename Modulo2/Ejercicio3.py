# Ejercicio 3
# Taller: introducción a python
# Día 2

# Consigna:
#   Mejora el programa de la calculadora básica del día 1 utilizando estructuras de control.
#   Solicita al usuario dos números y una operación (suma, resta, multiplicación o división).
#   Utiliza una estructura condicional (if-elif-else) para realizar la operación correspondiente
#   y mostrar el resultado por pantalla.

mensaje="""
Operaciones:
\t1.\tSuma
\t2.\tResta
\t3.\tMultiplicacion
\t4.\tDivision
\t5.\tResto
\t6.\tPotencia
\t0.\tSalir
"""

# Este bucle permite al usuario seguir interactuando con el programa, finaliza si la operacion es igual a '0'

while True:
  print(mensaje)
  operacion = input("Ingrese el numero de operacion: ")

  # Si la operacion es igual a 0 finaliza el bucle
  if operacion == '0':
      break
  # Si el numero de la operacion no esta en el conjunto ['1','2','3','4','5','6'] imprime un error
  elif operacion not in ['1','2','3','4','5','6']:
    print("El valor no es correcto")
  # Si todo salió bien, el usuario ingresa dos numeros
  else:
    nro1 = float(input("Ingrese un numero: "))
    nro2 = float(input("Ingrese un numero: "))

    # En base a la operacion, ejecuta una determinada expresion
    match operacion:
      case '1':
        print("Suma:", nro1 + nro2)
      case '2':
        print("Resta:", nro1 - nro2)
      case '3':
        print("Multiplicacion:", nro1 * nro2)
      case '4':
        print("Division:", nro1/nro2)
      case '5':
        print("Resto:", nro1 % nro2)
      case '6':
        print("Potencia:", nro1 ** nro2)