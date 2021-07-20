edad = int(input('ingresa edad: '))


def entrada(edad):
    if edad < 18:
        return f'no puedes entrar perrito tienes solo {edad}'
    elif edad > 100:
        return 'estas viejo perrito'
    else:
        return "pase perrito"


print(entrada(edad))
