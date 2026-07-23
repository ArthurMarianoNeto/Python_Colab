'''
  MAP FUNCTION 
  -> Muito utilizado com listas
  -> Applicar euma função a um Iterable, por item. (List, tupple, dici etc)
'''
lista1 = [1, 2, 3,  4]
 
def mult(x):
  return x * 2

print(list(map(mult, lista1)))
