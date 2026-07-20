produtos = ['arroz', 'feijão', 'macarrão', 'carne', 'frango']
# Extraindo variáveis da lista
produto1, produto2, produto3, *outros = produtos #outros pode ficar em qualquer posição, mas só pode haver um *outros
print(produto1) 
print(produto2)
print(produto3)
print(outros)

# se eu esquecer de incluir algum item? 