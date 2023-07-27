def reverse_string(texto):
    txt = ""
    for caracter in list(reversed(texto)):
        txt += caracter
    return txt

if __name__ == "__main__":
    print(reverse_string("hola"))