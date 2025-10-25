cubiertos = {"tenedor", "cuchara", "cuchillo", "cucharilla"} # Se parece a los diccionarios pero esta no tiene indice y se separa por comas
print(cubiertos)

servilletas = {"Servilleta", "Servilleta", "Servilleta", "Servilleta",} # Aunque hayan elementos repetidos los sets lo ignoran. 
print(servilletas)

vajilla = set(["plato", "taza", "copa"]) # Se puede crear esta función, en este caso con un iterable retornará un set con esos elementos. 

print(vajilla)

repetidas = [1, 5, 7, 8, 8, 9, 8, 3, 8, 7]

sin_repeticiones = list(set(repetidas)) # Con esto podemos eliminar elementos repetidos rápidamente de una lista. 

print(sin_repeticiones)

pares = {(1, 3), (2, 4), (9, 2)} #Se puede hacer sets que contengan valores hashables más no l ocontrario. 

print(pares)

mi_set_ = set("1234567890")
print(len(mi_set_)) #Con esto podemos contar el números de elementos en un set
 
a = {1,2,3,4,5,6,7}
b = {1,2,8,9,10}

union = a|b # podemos hacer una unión de sets con (|)
print(union) 
c = {1, 2, 3, 4, 5, 6, 7}
d = {1, 2, 8, 9 , 10}

diferencia = c - d # Con el (-) retornamos otro set con elementos del primero de ellos o viceveras pero excluyendo los elementos que tengan en común con el otro
print(diferencia)

al_reves = d - c
print(al_reves)

e = {1, 2, 3, 4, 5, 6, 7}
f = {1, 2, 8, 9 , 10}

diferencia_simetrica = e ^ f # Con la diferencia simetrica  "unimos" los elmentos de ambos sets pero excluyendo los que se repiten en ambos. 
print(diferencia_simetrica)

g = {1, 2, 3, 4, 5, 6, 7}
h = {1, 2, 8, 9 , 10}

interseccion = g & h # Con una intersección hacemos lo contrario a una diferencia simetrica.
print(interseccion)
