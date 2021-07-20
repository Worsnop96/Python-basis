class Coche():
    def desplazamiento(self):
        print("me desplzado utilizando 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("me desplzado utilizando 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("me desplzado utilizando 6 ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miCarro = Camion()

desplazamientoVehiculo(miCarro)
