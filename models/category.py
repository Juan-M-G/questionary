class Category:
    def __init__(self, name):
        self._name = name
    @property.getter
    def get_name(self):
        return self._name
    @property.setter
    def set_name(self, name):
       self._name = name



class TipodeCambio:
    def __init__(self, moneda, cantidad, valor_cambio=4.09):
        self.__moneda = moneda
        self.__cantidad = cantidad
        self.__valor_cambio = valor_cambio

    def monto(self):
        return (f'{self.__cantidad} dolares, equivale a {self.__cantidad * self.__valor_cambio} {self.__moneda}')

class Soles(TipodeCambio):
    def __init__(self, moneda, cantidad):
        super().__init__(moneda, cantidad)

class Pesos(TipodeCambio):
    def __init__(self, moneda, cantidad, valor_cambio=20.7):
        super().__init__(moneda, cantidad, valor_cambio=valor_cambio)

if __name__ == "__main__":
    soles = Soles(moneda = "Soles", cantidad=200)
    print(soles.monto())

    pesos_mexicanos = Pesos(moneda = "Pesos mexicanos",cantidad=100)
    print(pesos_mexicanos.monto())