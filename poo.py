class Auto():
    def __init__(self) -> None:
        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4
        self.encendido = False

    def arrancar(self):
        self.encendido = True

    def estado(self):
        if self.encendido == True:
            return "el auto esta encendido perritos"
        else:
            return f"el auto esta apagadito {self.encendido}"

    def cheque_interno(self):
        print("realizando chequeo interno: ")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False


miAuto = Auto()
miAuto.__ruedas = 8
print(f"{miAuto.estado()}")
