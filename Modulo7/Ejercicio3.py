# Ejercicio 3
# Taller: introducción a python
# Día 10

# Consigna:
#   Crea una clase "CuentaBancaria" con atributos privados como "saldo" y
#   "propietario". Implementa métodos para depositar y retirar dinero de
#   la cuenta, teniendo en cuenta las validaciones necesarias.

class CuentaBancaria:

    maximo_deposito = 100_000.0
    
    def __init__(self, propietario: str, saldo: float = 0):
        self.__propietario = propietario
        self.__saldo = saldo

    def depositar(self, monto: float):
        valido = monto > 0 and monto <= self.maximo_deposito
        if valido:
            self.__saldo += monto
        return valido

    def retirar(self, monto: float):
        valido = monto <= self.__saldo and monto > 0
        if valido:
            self.__saldo -= monto
        return valido

    def getSaldo(self):
        return self.__saldo

cuenta = CuentaBancaria("luisPerez", 200_000)
print(cuenta.retirar(-50_000), cuenta.getSaldo())