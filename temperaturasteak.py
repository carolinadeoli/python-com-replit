temperatura = int(input('Qual é a temperatura da carne? '))

if temperatura < 48:
  print('Cozinhar por mais alguns minutos')
elif temperatura in range(48,53):
  print('Selada')
elif temperatura in range(54,59):
  print('Ao ponto para mal passada')
elif temperatura in range(60,64):
  print('Ao ponto')
elif temperatura in range(65,70):
  print('Ao ponto para bem passada')
else:
  print('Bem passada')
