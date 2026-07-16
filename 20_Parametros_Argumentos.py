'''
Functions (Funções)
  # DRY - Don't repeat yourself 
  # Parâmetro --> Argumento
'''
def boas_vindas(nome, quantidade):
  print(f'Olá, seja bem-vindo, {nome}!')
  print(f'Temos {str(quantidade)} laptops em estoque!')
  print('----------------------------------')

boas_vindas('Jorgina', 4)
boas_vindas('Mirian', 3)
boas_vindas('João', 2)



'''
def boas_vindas_Jorgina():
  print('Olá, seja bem-vindo, Jorgina!')
  print('Temos 5 laptops em estoque')
  print('----------------------------------')


def boas_vindas_Mirian():
  print('Olá, seja bem-vindo, Mirian!')
  print('Temos 4 laptops em estoque')
  print('----------------------------------')


def boas_vindas_Joao():
  print('Olá, seja bem-vindo, João!')
  print('Temos 3 laptops em estoque')
  print('----------------------------------')

boas_vindas_Jorgina()
boas_vindas_Mirian()
boas_vindas_Joao()
'''