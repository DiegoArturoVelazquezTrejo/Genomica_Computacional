import re
import math
# Trabajo con las expresiones regulares
'''
Buscar en las líneas, cadenas de texto que contengan n y le siga la cadena "er"

awk '/[n][er]/ {print $0}' products.txt

Buscar cadenas que empiecen con el símbolo "p" y contengan 3

awk '/^p.*3/ {print $0}' products.txt

Reemplazar la cadena "Scanner" por "Router"

awk 'gsub(/Scanner/, "Router")'  products.txt

Buscar cadenas que contengan palabras que empiecen con la cadena "Mo" y que tengan caracteres subsecuentes

awk '/Mo*/ {print $0}' products.txt

Buscar cadenas que terminen con el símbolo 5

awk '/5$/ {print $0}' products.txt

Buscar cadenas que empiecen con el caracter "p" y que contengan Scanner o Mouse

awk '/^p.* (Scanner|Mouse)/' products.txt

Para encontrar al menos una coincidencia, buscará lineas que contengan el caracter n al menos una vez

awk '/n+/{print}' products.txt

'''
p = re.compile('01[01]00')

re.compile(r'01[01]00')
re.compile(r'01[01]01', re.UNICODE)

p = re.compile('01[01]01')

path1 = re.compile('Genomica')

path2 = re.compile('Computacional')

#print('v' if re.match(path1, 'Genomica') else 'n')
#print('v' if re.match(path2, 'Genomica') else 'n')


# Definimos una función
def encuentra(path, cad):
    val = 'v' if re.match(path, cad) else 'n'
    return val

# Patrón es una expresión regular
encuentra = lambda patron, cadena: True if re.match(patron, cadena) else False

# Con search, busca la subcadena, itera sobre toda
encuentraS = lambda patron, cadena: True if re.search(patron, cadena) else False

'''
match() : determina si está al principio de la cadena
search() : Escanea a través de toda la cadena la aparición
findall() : Regresa como lista todas las subcadenas en donde está re
finditer() : Regresa como iterador todas las subcadenas donde está re

group() : Regresa la cadena encontrada por re
start() : Regresa la posición inicial de la aparición
end() : Regresa la posición final de la aparición
span() : Regresa tupla con (inicio, fin) de la aparición
'''


# Ejemplos

print(encuentra(r'Genomica', 'Genomica'))
print(encuentra(r'G[eo]nomica', 'Genomica'))
print(encuentra(r'G[eo]nomica', 'Gonomica'))
print(encuentra(r'Genomica|Computacional', 'Genomica'))
print(encuentra(r'Genomica|Computacional', 'Computacional'))

print(encuentra(r'Computacional', 'Genomica Computacional'))
print(encuentraS(r'Computacional', 'Genomica Computacional'))

# BUscaremos primero los dígitos en la cadena

cadena = "ATTCCTA TTACTGT GCTTACAA 01001 GATTACA"

patron = r'\d\d\d\d\d'

v = re.search(patron, cadena) # La tupla de (25, 30) indica las posiciones de los números
print(cadena[v.start():v.end()])

# Buscaremos ahora la posición de todos los dígitos, no necesariamente 5
pat = r'\d+'
v = re.search(pat, cadena)
print(v.start())

# BUscaremos ahora los caracteres
pat = r'\D+'
v = re.search(pat, cadena)
print(v)

# Regresa una lista con todos los elementos dígitos
print(re.findall(pat, cadena))

# Expresiones regulares con operadores . , * , [], {}
pat = r'TT..T'
v = re.finditer(pat, cadena)
print(list(v))

print("----")
cadena = "ATTCCTA TTACTGT GCTTACAA 01001 GATTACA"
# AL menos encuentre dos veces TTA
pat = r'(TTACA){1,}'
v = re.findall(pat, cadena)
print(list(v))

cad = "ATTCTTATTACTA TTGTTGTTGTTTCCTGTGCTTACAA TTCTTCTTCA"
pat = r'(TTACA){1,}'
v = re.findall(pat, cadena)
print(list(v))

# Buscar TT y lo que sea entre dos o tres veces
pat = r'(TT.){2,3}'
v = re.findall(pat, cadena)
print(list(v))
