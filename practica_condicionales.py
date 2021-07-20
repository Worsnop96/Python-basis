salario_presidente = int(input("introduce salario presidente: "))
salario_director = int(input("introduce salario director: "))
salario_jefe_area = int(input("introduce salario jefe de area: "))
salario_obrero = int(input("introduce salario obrero: "))


if salario_presidente > salario_director > salario_jefe_area > salario_obrero:
    print('todo bien')

else:
    print('hay algo extraño')
