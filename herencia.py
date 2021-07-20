class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.en_marcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn March: ",
              self.en_marcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "voy haciendo el caballito man"


class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"


miMoto = Moto("honda", "areo")
miMoto.estado()

miFurgoneta = Furgoneta("audi", "1888")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
