# Ejercicios

1. Crea un módulo llamado funciones.py que contenga las siguientes funciones
matemáticas:
* raiz(argumento, radicando): devuelve argumento**(1/radicando).
* divisible(a, b): devuelve a % b == 0.
* cuadrado(a): devuelve el cuadrado de a.
* cubo(a): devuelve el cubo de a.

  Luego, en otro archivo llamado main.py, importa el módulo funciones y utiliza las
funciones para realizar operaciones matemáticas.

2. Crea un paquete llamado geometria que contenga dos módulos:
* circulo.py: Contiene una función area(radio) que reciba el radio de un círculo y devuelva su área.
* rectangulo.py: Contiene una función area(base, altura) que reciba la base y la altura de un rectángulo y devuelva su área.

  Luego, en otro archivo llamado main.py, importa los módulos del paquete
geometria y utiliza las funciones para calcular áreas de círculos y rectángulos.

3. Crea un paquete llamado utils que contenga los siguientes módulos:
* string.py: Contiene una función reverse_string(texto) que reciba un texto y devuelva el texto invertido.
* list.py: Contiene una función find_max(lista) que reciba una lista de números y devuelva el valor máximo.

  Luego, en otro archivo llamado main.py, importa los módulos del paquete utils y utiliza las funciones para realizar operaciones con cadenas y listas.

4. Crea un subpaquete para utils, debe llamarse “validacion”, este incluye un módulo llamado numbers.py que contenga las siguientes funciones:
* is_positive_integer(num): Recibe un número y devuelve True si es un entero positivo, de lo contrario, devuelve False.
