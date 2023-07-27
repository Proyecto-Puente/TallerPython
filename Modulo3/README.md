# Ejercicios
1. Cálculo del área de un círculo: Crea una función llamada "area_circulo" que reciba como argumento el radio de un círculo y retorne el área correspondiente. Luego, pide al usuario que ingrese el radio y muestra el área calculada.
> Para utilizar el número pi, deberá importarlo con `from math import pi`
>
> Formula: `area = pi x radio^2`

2. Cálculo del volumen de un cilindro: Crea una función llamada “volumen_cilindro" que reciba como argumento el radio y la altura del cilindro, debe retornar el volumen. Luego, pida al usuario que ingrese los datos y muestra el volumen.
> Formula: `Volumen = area x altura`

3. Elabore una función que retorne la letra más utilizada en un texto que obtenga como parámetro, luego permita al usuario ingresar una cadena e imprima la letra más utilizada.

4. Escribir una función recursiva que reciba un número entero positivo y devuelva su factorial.
> Caso base: 1, si numero == 0
>
> Caso general: numero * factorial(numero - 1)

5. Escribir una función recursiva que reciba un número entero positivo y devuelva el valor de la sucesión de Fibonacci para ese valor.
> Caso base: num, si (num == 0) o (num == 1)
>
> Caso gral: fibonacci(n - 1) + fibonacci(n - 2)

6. Conversor de temperatura: Escribe un programa que convierta una temperatura en grados Celsius a grados Fahrenheit. Crea una función que tome como parámetro la temperatura en grados Celsius y devuelva la temperatura equivalente en grados Fahrenheit. Luego, solicita al usuario ingresar una temperatura en grados Celsius y muestra la temperatura equivalente en grados Fahrenheit
```
ºF = ºC x 1.8 + 32
ºC = (ºF-32) ÷ 1.8
```
