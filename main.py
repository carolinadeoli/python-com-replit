# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))

# soma = n1 + n2
# subtracao = n1 - n2
# multiplica = n1 * n2
# divide = n1/ n2
# print(f'{n1} + {n2} = {soma} ')
# print(f'{n1} - {n2} = {subtracao}')
# print(f'{n1} * {n2}= {multiplica}')
# print(f'{n1} / {n2} = {divide}' )

nome = input('Qual é o carro que você deseja?')
carros = ['BMW X6', 'BMW i5','BMW i8']

if nome in carros:
  print('Este carro está disponível')
else:
  print('Desculpe, este carro não está disponível')