# Formataçao de string utilizando o f na frente de conteudo ex:
# linha_1 = f'{nome} tem {altura:.2f} de altura,'

# Formatando as casas decimais ex: {altura:.2f}


nome = 'João da Silva'
altura = 1.80
peso = 95
imc = peso / altura ** 2

#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

