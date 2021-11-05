import re

# Vamos a construir una expresión regular que recupere los números telefónicos
'''
Los números telefónicos contienen los siguientes patrones
999-999-9999 o bien (99)-9999-9999
Hay que elegirlos de la siguiente lista:
'''

telefonos = ['553-191-1122', '(55)-3451-9932', '9323-123-39391', 'A22-2924-1914', '(432)3-43321']

# primera propuesta
pat1 = r'\d\d\d-\d\d\d-\d\d\d\d'

# Segunda propuesta
pat1 = r'\d{3}-\d{3}-\d{4}'

# Tercera propuesta
pat1 = r'(\d{3}-){2}\d{4}'

pat2 = r'\(\d\d\)(-\d{4}){2}'

patron = pat1 + "|" + pat2

for telefono in telefonos:
    print(re.match(patron, telefono))


# Otro ejemplo
pat = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.])' # Dirección URL

'''
Una tarea común es buscar secuencias genómicas:

Nos intersa todas aquellas secuencias que empiecen después de ATG
pero la secuencia final puede ser una de 3: TAA, TAG, TGA

Nos interesa, además, que la secuencia englobada sea múltiplo de 3

¿Cómo se hace esta regex?
'''
patron = r'ATG[ATG]{3}(TAA|TAG|TGA)$'

secuencias = ["ATATATACATACTGGTAATGGGCGCGCGTGTGTTAAGTTCTGTTGTAGGGGTGATTAGGGGCG",
              "GGCCCACACCCCACACCAATATATGTGGTGTGGGCTCCACTCTCTCGCGCTCGCGCTGGGGAT",
              "ATAAGGTGTGTGGGCGCGCCCCGCGCGCGCGTTTTTTCGCGCGCCCCCGCGCGCGCGCGCGCG",
              "GGCGCGGGACGCGGCGGCGGATCCCGATCCGTGCGTCAATACTATTATGGCCAGATAGAATAA",
              "GTGCTGCTGCGGCGCCCACACCTATTATCTCTCTCTCTCTGCCTCTCCACCTCGGGGCTTAAT",
              "GCGCTGCTGCTGGCTCGATGGGCGCGTGCGTCGTAGCTCGATGCTGGCTCGAGCTGTAATCTT",
              "GGCGCTCGCTCGGATGCGCGGCCGGGCTCTCTGCTCGCGCTCGCTTCGCGCTCGTGACCGCTG",
              "AATTGGTGCGCGCTCGCGCACACACAGAGAGAGGGTTTATATAGGATGATATATCCACATTGG",
              "ATGCTGCTGCTGGCTCTGCTTGCGCTCTGCTCGCTGGGGTGTGTGTGCCGCGCGCTGCTGCTC",
              "GCTGGGCTCGCTCGATGCGCGCGGGCGCGCGACCGCGGACGGCGTCGCTGCTAAATGGGCTTC"]
for secuencia in secuencias:
    print(re.search(patron, secuencia))
