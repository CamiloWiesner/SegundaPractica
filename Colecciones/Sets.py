cubiertos = {"tenedor", "cuchara", "cuchillo", "cucharilla"} # Se parece a los diccionarios pero esta no tiene indice y se separa por comas
print(cubiertos)

servilletas = {"Servilleta", "Servilleta", "Servilleta", "Servilleta",} # Aunque hayan elementos repetidos los sets lo ignoran. 
print(servilletas)

vajilla = set(["plato", "taza", "copa"]) # Se puede crear esta función, en este caso con un iterable retornará un set con esos elementos. 

print(vajilla)

repetidas = [1, 5, 7, 8, 8, 9, 8, 3, 8, 7]

sin_repeticiones = list(set(repetidas)) # Con esto podemos eliminar elementos repetidos rápidamente de una lista. 

print(sin_repeticiones)

