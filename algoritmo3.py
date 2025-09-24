# Estructura de datos dinamicas
# Listas, Tuplas, Diccionarios, Conjuntos

# Lista = [2,1,4,5,8,7,9,6,5,8,12,4,5,8,7,9,"hola",True]
# Tupla =(1,5,6,4,59,7,45)
# Conjunto = {1,2,3,6,5,4,9}
# Diccionario ={ "nombre": "Juan Perez","edad":45,"nacionalidad":"Peruana"}

#Lista
numeros = [10,20,30,40,50]

numeros.append(95)
numeros.append(100)
numeros.append(180)

cantidadDatos = numeros.__len__()
print(cantidadDatos)
print(numeros)
#indice = 0
ultimo = numeros.pop()
print(ultimo)

numeros.sort()
print(numeros)

#while(indice <= 7):
#    print(numeros[indice])
#    indice = indice + 1