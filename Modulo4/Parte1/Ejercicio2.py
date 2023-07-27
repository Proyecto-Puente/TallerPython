# Ejercicio 2
# Taller: introducción a python
# Día 4

# Consigna:
#   Piense en su medio de transporte favorito, como una motocicleta o un
#   automóvil, y haga una lista que almacene varios ejemplos. Use su lista
#   para imprimir una serie de afirmaciones sobre estos elementos, como
#   "Me gustaría tener una motocicleta Honda".

vehiculos = ["trenes", "motos","monopatin"]

for vehiculo in vehiculos:
    match vehiculo:
        case "trenes":
            print ("¡Quiero viajar en tren!")
        case "motos":
            print ("¡Voy pasear en moto!")
        case "monopatin":
            print ("¡Deberia arreglar el monopatin!")