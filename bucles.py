# programa para contar numero de caracteres de una cadena de texto

frase = "Frase de Prueba"
contador = 0

for i in frase:
    if i == " ":
        continue
    contador += 1
print(f"la cantidad de caracteres en {frase} es {contador} ")
