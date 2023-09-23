def dobro(numero):
  return numero *2

def quadrado(numero):
  return dobro(numero)**2

num = int(input('Digite um número:'))

print(f'O dobro do quadrado de {num} é {quadrado(num)}')