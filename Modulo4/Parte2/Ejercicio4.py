# Ejercicio 4
# Taller: introducción a python
# Día 5

# Consigna:
#   Haga varios diccionarios, donde el nombre de cada diccionario sea el
#   nombre de una mascota. En cada diccionario, incluya el tipo de animal y el
#   nombre del propietario. Guarde estos diccionarios en una lista llamada
#   mascotas. A continuación, recorra su lista y, mientras lo hace, imprima todo
#   lo que sabe sobre cada mascota.

babieca = {"tipo": "caballo", "propietario": "Mio Cid"}
timoteo = {"tipo": "gato", "propietario": "Luis Perez"}

mascotas = [babieca, timoteo]

for m in mascotas:
    print("Mascota:",m.get("tipo"), m.get("propietario"), sep="\n\t")