'''
# Functions (funções)
  # DRY - Don't repeat yourself
  # Parâmetro --> Argumento
  # Vários Argumentos (xargs) identificando o Parâmetro
  # Criar uma função que soma vários numeros
'''
def agencia(**carro):
  return carro

print(agencia(marca='Gol', cor='Branco', motor=1.0))
print(agencia(marca='HB20', cor='Vermelho', motor=1.8))
print(agencia(marca='Onix', cor='Cinza', motor=2.0))

