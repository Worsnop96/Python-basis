from io import open
archivo_texto = open("archivo.txt", "w")
frase = "estupendo dia hoy es: \nViernes n.n/"

archivo_texto.write(frase)
archivo_texto.close()
