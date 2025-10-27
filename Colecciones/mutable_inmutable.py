variable1 = "Hola"
variable2 = variable1 # Tendrán el mismo id
variable3 = "Adiós" # Tendrán diferente id

print(id(variable1))
print(id(variable2))
print(id(variable3))
 # En python un objeto puede tener muchos nombres pero sola una ID 

# Las listas, los sets y los diccionarios son mutables y los valores lógicos, las cadenas y las tuplas, inmutables. 
lista = ["Hola","mundo","palabra"]
print(id(lista))

lista[2] = "cosa"
print(id(lista)) # El id no ha cambiado

lista_dos = ["Hola","mundo","palabra"]
copia_de_lista = lista_dos
lista_dos[2] = "cosa"
print(copia_de_lista[2]) # Imprimirá "cosa" porque es mutable por lo cuál siguen refiriendose al mismo.

lista_tres = ["Hola","mundo","palabra"]
lista_cuatro = list(lista_tres)

print(id(lista_tres))
print(id(lista_cuatro))
# Los id son distintos

diccionario = {"nombre": "Pablo", "Apellido": "Hinojosa"}
diccionario2 = dict(diccionario)

print(id(diccionario))
print(id(diccionario2))
# Los id son distintos

listas = [
            [1, 2, 3, 4],
            ["a", "b", "c", "d"]
         ]
copia_de_listas = list(listas)

# listas y copia_de_listas son distintas:
print(id(listas))
print(id(copia_de_listas))

# pero sus componentes son los mismos
print(id(listas[1]))
print(id(copia_de_listas[1]))
# Esto es mejor conocido como "shallow copy"

original = [[1, 2, 3]]

copia = list(original)

print(original[0][1])
print(copia[0][1])

original[0][1] = "Hola"

print(original[0][1])
print(copia[0][1])
# El cambio se hará también en la copia al contener el mismo objeto.

