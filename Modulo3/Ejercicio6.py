# Ejercicio 6
# Taller: introducción a python
# Día 3

# Consigna:
#   Conversor de temperatura: Escribe un programa que convierta una temperatura en
#   grados Celsius a grados Fahrenheit. Crea una función que tome como parámetro la
#   temperatura en grados Celsius y devuelva la temperatura equivalente en grados
#   Fahrenheit. Luego, solicita al usuario ingresar una temperatura en grados 
#   Celsius y muestra la temperatura equivalente en grados Fahrenheit.
#
#   ```
#   ºF = ºC x 1.8 + 32
#   ºC = (ºF-32) ÷ 1.8
#   ```

def celsius_fahrenheit(Gcelsius=0):
    """Convierte grados Celsius a Fahrenheit"""
    return ((9*Gcelsius)/5)+32

grados = float(input("Ingrese los grados C°: "))
print(celsius_fahrenheit(grados))