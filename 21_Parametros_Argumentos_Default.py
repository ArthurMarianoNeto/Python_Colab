'''
# Functions (funções)
  # DRY - Don't repeat yourself
  # Parâmetro --> Argumento
  # Default = Aquele que você define o valor no parâmetro
  # Non-Default = Aquele que você não define o valor no parâmetro

'''
def boas_vindas(nome, quantidade=6):
  print(f'Olá, seja bem-vindo, {nome}!')
  print(f'Temos {quantidade} laptops em estoque')
  print('----------------------------------')

boas_vindas('Jorgina') # Using default quantity
boas_vindas('Mirian', 3) # Overriding default quantity
boas_vindas('João', 2) # Overriding default quantity