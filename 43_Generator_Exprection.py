from sys import getsizeof
'''
Generator Expression
-> Uma forma mais rápida para listas, dicionários e etc 
-> Menos Memória
-> Mais Rapido
-> Menos Linhas de Código
-> Valores em Bytes
'''
numeros = [x*10 for x in range (100)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print('+++++')

numeros = (x*10 for x in range (100))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))

