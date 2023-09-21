cidades =('São Paulo', 'Rio de Janeiro','Salvador')
pesquisando_cidade = input('Qual cidade você está procurando?')

if pesquisando_cidade in cidades:
  print(f'A cidade foi encontrada e é {pesquisando_cidade}')
else:
  print('A cidade que você digitou não foi encontrada')