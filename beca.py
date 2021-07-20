print("programa de becas Guatemala 2021")

distancia_escuela = int(
    input("introduce la distancia desde la casa a la escuela en km: "))
numero_hermanos = int(input("ingresa cuantos hermanos se tiene: "))
salario_familiar = int(
    input("ingresa el salario familiar anual en Quetzales: "))

if(distancia_escuela > 40 and numero_hermanos > 3 or salario_familiar < 40000):
    print("tienes derecho a reclamar tu beca")
else:
    print("No tienes derecho a beca")
