from typing_extensions import ValuesView
''''
Dicionários
 - Utiliza index no formato de Keys e Values
 - Aceita string, integer, float, boolean...
'''

aluno = {
          'nome': 'Ana', 
          'idade': 16, 
          'nota_final': 'A', 
          'aprovação': True,
          'Materias': ['Fisica', 'Matemática', 'Inglês']
         }

print(aluno)
print()
print(aluno.items())
print()
print(aluno.keys()) 
print()
print(aluno.get('Materias'))
print()
print(len(aluno))