correo = input("Ingresa direccion de correo: ")
respuesta = correo.find("@")

if respuesta == -1:
    print("correo invalido")
    correo = input("Ingresa direccion de correo: ")

else:
    print("correo valido pase adelante")
