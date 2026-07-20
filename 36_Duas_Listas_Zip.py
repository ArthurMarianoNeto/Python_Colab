cores = ['amarela', 'azul', 'verde', 'vermelho', 'rosa']
valores = [234, 543 , 123, 654, 987, 321, 456, 789]

duas_listas = list(zip(cores, valores)) #zip() irá unir as duas listas em uma só, criando uma lista de tuplas. Se não colcoar o zip irá imprimir um valor doidão. O list() irá transformar o zip em uma lista.
print(duas_listas)  