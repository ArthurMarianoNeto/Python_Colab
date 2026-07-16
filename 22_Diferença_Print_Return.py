'''
# Functions (funções)
  # DRY - Don't repeat yourself
  # Parâmetro --> Argumento
  # Realizam uma tarefa, isto armazena nada, "Procedimento"
  # Calcula e retrona um valor
'''

def cliente1(nome):
  print(f'Olá {nome}!')

def cliente2(nome):
  return f'Olá {nome}'


x = cliente1('Maria')
y = cliente2('José')

print(x)
print(y)

