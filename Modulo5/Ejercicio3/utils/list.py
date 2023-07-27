
#def find_max(lista):
#    return max(lista)

def find_max(lista):
    if len(lista) == 0:
        return 0
    else:
        mayor = lista[0]
        for x in lista:
            mayor = x if x > mayor else mayor
        return mayor

if __name__ == "__main__":
    print(find_max([92, 92.1, 32,-123]))