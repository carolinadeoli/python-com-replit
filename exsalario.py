salario = float(input('Qual o valor do salário?'))
aumento = float(input('Digite o valor do aumento:'))

valor_aumento = salario * aumento/100
salario_aumento = salario + valor_aumento

print("Um aumento %5.2f %% em um salário de R$ %7.2f" % (aumento, salario))
print('é igual a aumento de R$ %7.2f'%valor_aumento)
print('Resultando em um novo salário de R$ %7.2f'%salario_aumento)