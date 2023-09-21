capitais ={
  'Brasil':'Brasilia',
  'Argentina':'Buenos Aires',
  'Uruguai':'Montevideu',
  'Peru':'Lima',
  'Chile':'Santiago'  
}

pais_usuario = input('Digite o país desejado: ')

if pais_usuario in capitais:
  print(f' A capital do {pais_usuario} é {capitais[pais_usuario]}')
else:
  print('Desculpe, não encontramos informações do país que você deseja')