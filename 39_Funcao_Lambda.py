''''
LAMBDA
-> É uma funão (pequena) sem nome 
-> Pode ter vários argumentos mas somente 1 expressão
-> Muito utilizada em outras funções
-> Código mais conciso
-> Códico é mais Clean
'''

def somar(x):
  func2 = lambda x: x + 10
  return func2(x) * 4

print(somar(2))
