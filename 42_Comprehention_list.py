'''
List Comprehension 
-> Mais simples de se escrever 
-> Utilizado quando se precia criar uma nova lista a partir de uma existente
-> [expressão for iten in itens]
'''

frutas1 = ["abacate", 'banana', 'caju', 'morango']
frutas2 = []
'''
for itens in frutas1:
    if 'b' in itens:
        frutas2.append(itens)
'''
frutas2 = [itens for itens in frutas1 if 'b' in itens]

print()
print('Frutas total')
print(frutas1)
print()
print('Frutas Selecionadas')
print(frutas2)