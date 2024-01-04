"""
Shallow Copy (Copia Superficial):

Una copia superficial crea un nuevo objeto, pero no copia recursivamente los objetos contenidos dentro del objeto original.
Los elementos internos se comparten entre el objeto original y la copia. Esto significa que, si modificas un objeto interno en la copia, ese cambio se reflejará en 
el objeto original y viceversa.
"""

"""
Deep Copy (Copia Profunda):

Una copia profunda crea un nuevo objeto y copia recursivamente todos los objetos contenidos dentro del objeto original, incluyendo todos los objetos internos.
Los elementos internos en la copia son independientes de los objetos internos en el objeto original. Las modificaciones en la copia no afectan al objeto original y viceversa.
"""
##Clonar una lista.
##Clonar una lista.
##Clonar una lista.

# Lista original
lista_original = [1, 2, 3, 4, 5]

# Copia de la lista sin utilizar funciones
copia_lista = []

for elemento in lista_original:
    copia_lista.append(elemento)

# Mostrar las listas originales y la copia
print("Lista original:", lista_original)
print("Copia de la lista:", copia_lista)

##Añado un elemento
##Añado un elemento
##Añado un elemento

copia_lista.append(6)
print("Copia de la lista con elemento añadido: ", copia_lista)


##Quito un elemento de la lista
##Quito un elemento de la lista
##Quito un elemento de la lista

del copia_lista[0]

print("Copia de la lista con elemento borrado :", copia_lista)


## Crear una lista nueva con los 4 últimos elementos de una lista
## Crear una lista nueva con los 4 últimos elementos de una lista
## Crear una lista nueva con los 4 últimos elementos de una lista

# Lista original
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crear una nueva lista con los últimos 4 elementos utilizando rebanado
nueva_lista = lista_original[-4:]

# Mostrar la nueva lista
print("Nueva lista con los últimos 4 elementos:", nueva_lista)

##Convertir las palabras de una cadena (separadas por espacio) a una lista.
##Convertir las palabras de una cadena (separadas por espacio) a una lista.
##Convertir las palabras de una cadena (separadas por espacio) a una lista.

# Cadena de palabras

cadena_palabras = "Hola cómo estás hoy"

# Convertir la cadena a una lista de palabras
lista_palabras = cadena_palabras.split()

# Mostrar la lista de palabras
print("Lista de palabras:", lista_palabras)

##Comentarios con una linea
##Comentarios con una linea

"""
comentario.
multilinea
hola mundo
"""