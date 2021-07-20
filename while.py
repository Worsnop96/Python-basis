import math

# corrobora rangos de edad con ciclo while
"""
edad = int(input("ingresa tu edad: "))

while edad < 0 or edad > 125:
    print(f"la edad ingresada es erronea '{edad}'")
    edad = int(input("ingresa tu edad: "))

print(f"Gracias por participar!")
"""
# calculo de raiz cuadrada
print("programa de calculo de raiz cuadrada")
numero = int(input("Ingresa el numero por favor: "))

intentos = 0

while numero < 0:
    print("no es posible calcular la raiz cuadrada de un negativo")
    intentos = intentos + 1
    if intentos == 2:
        print("has alcanzado tus posibles oportunidades")
        break

    numero = int(input("Ingresa el numero por favor: "))
if intentos < 2:
    respuesta = math.sqrt(numero)
    print(f"la raiz cuadrada de {numero} es {respuesta}")
