diccionario = {"clave1": "Valor", "clave2": "Otro Valor"}
print(diccionario)
diccionarios = {"animal": "gato", "cosa": "piedra", "planta": "lechuga"}

print(diccionarios)

print(diccionarios["animal"]) # Mostrará "gato"

print(diccionarios["planta"]) # Mostrará "lechuga"

diccionarios["planta"] = "coliflor"

print(diccionarios["planta"]) # Ahora mostrará "coliflor"

mariposa = {"nombre": "Nazarena", "especie": "Quercusia quercus", "genero": "Quercusia"}

print(mariposa)

mariposa["familia"] = "Lycaenidae" # Se le puede agregar claves nuevas aunque no estén definidas

print(mariposa)

diccionario2 = {
    "género" : "pop",
    "cantante" : "Michael Jackson",   # Se puede dividir así para hacerlo más legible 
    "canción" : "Billie jean"
    }
print(diccionario2)

# Con la función dict() también podemos crear diccionarios con los argumentos que queramos.

diccionarioTres = dict(color = "rojo", 
                       colorDos = "Amarillo",
                       colorTres = " purpura")
print(diccionarioTres)