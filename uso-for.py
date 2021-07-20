valido = False

email = input("introduce tu email")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("correcto")
else:
    print("incorrecto")
