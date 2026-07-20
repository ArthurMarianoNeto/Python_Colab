core_cliente = input('Digite a cor desejada: ')
cores = ['amarela', 'azul', 'verde', 'vermelho', 'rosa']

if core_cliente.lower() in cores: #irá resolver a questão de letras maiúsculas e minúsculas, pois o .lower() transforma tudo em minúsculo.
    print('Cor disponível!')
else:
    print('Cor não disponível!')