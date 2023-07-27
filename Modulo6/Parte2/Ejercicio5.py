# Ejercicio 5
# Taller: introducción a python
# Día 8

# Consigna:
#   Crear una función que serialice un diccionario en formato JSON y
#   guarde el resultado en un archivo.

import json

comida = {
    "tipo": "pan",
    "ingredientes": [
        ("harina", 1000),
        ("aceite", 75),
        ("sal", 25),
        ("levadura", 50),
        ("azucar", 25),
        ("agua", 750)]
    }

with open('pan.json', "w") as f:
    json.dump(comida, f)
