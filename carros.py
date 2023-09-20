nome = input('Qual é o carro que você deseja?')
carros = ['BMW X6', 'BMW i5','BMW i8']

if nome in carros:
  print('Este carro está disponível')
else:
  print('Desculpe, este carro não está disponível')