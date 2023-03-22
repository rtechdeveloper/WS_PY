# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')
if senha != '123456':
    print("Senha incorreta")

else:
    print('Senha correta')

#not inverte a condição
print(not True)  # False
print(not False)  # True