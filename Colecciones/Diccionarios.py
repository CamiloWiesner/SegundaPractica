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

diccionarioCuatro = dict([("raza", "golden retriever"), ["pelo", "amarillo"]])
print(diccionarioCuatro)

claves = ["1", "2", "3"]
valores = ["X", "Y", "Z"]

listas = zip(claves, valores) # Zip() es un iterador
dicci = dict(listas)
print(dicci) 

coordenadas = {(0,0): "Eje", (0,1):"universidad", (1,1):"raiz"} # las claves de un diccionario deben ser objetos hashables. 
print(coordenadas[(0,1)])


referencias = {
    "libros": ({"titulo": "Juego de Pythons", "autor": "G. R. R. Python"},
               {"titulo": "Un Mago de Python", "autor": "U. K. Python"},
               {"titulo": "Python y yo", "autor": "J. R. Python"}
              ),
    "peliculas": ["Python III", "Con Python y a lo loco", "Pulp Python"]
}

segundo_libro = referencias["libros"][1]["titulo"]

tercera_pelicula = referencias["peliculas"][2]

print('El segundo libro se titula "{}"'.format(segundo_libro))
print('La tercera película se titula "{}"'.format(tercera_pelicula))

numeritos = {
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5
}

print(numeritos)
del numeritos["tres"] # Con del podemos borrar valores de los diccionarios
print(numeritos)

direcciones = {"N": "Norte", "S":"Sur", "E":"Este", "O":"Oeste"}
print(len(direcciones)) # Con len() podemos retornar el número de elementos que contiene un diccionario

diccionario_a = {
    "animal": "gato",
    "cosa": "piedra",
    "planta": "lechuga"
}

diccionario_b = {
    "mineral": "cuarzo",
"cosa": "pelusa",
    "metal": "cobre"
}

union = diccionario_a | diccionario_b # Con (|) podemos hacer la unión de dos diccionarios
print(union) 

diccionario_c = {
    "animal": "gato",
    "cosa": "piedra",
    "planta": "lechuga"
}

diccionario_d = {
    "mineral": "cuarzo",
    "cosa": "pelusa",
    "metal": "cobre"
}

diccionario_c |= diccionario_d # Con != en vez de unificar modificamos el primero de ellos 
print(diccionario_c)

usuario = {"nombre": "Pablo", "username": "psicobyte"}
correo = usuario.get("correo","email@email.email") # Con el metodo get() retornará el valor asociado si es que esa clave existe, si no devolverá un keyError (se le puede pasar un segundo argumento)
print(correo)

usuarios = {"nombre": "Pablo", "username": "psicobyte"}
print(usuarios.setdefault("correo", "email@email.email"))
print(usuarios)

 
