# Sección 1
rango = range(20)
print(tuple(rango))
rango_limite = range(10, 20)
print(list(rango_limite))
rango_secuencial = range(0, 10, 2)
print(tuple(rango_secuencial))

# Sección 2
mi_tuplita = ("a", "b", "c", "d", "e",
              "f", "g", "h", "i", "j",
              "f", "k"
              )
busqueda_f = mi_tuplita.index("f", 6, 11)
print(busqueda_f)

mi_lista = (1, 2 , 3, 4, 5,
            1, 2 , 3, 1, 8,
            4, 2 , 9, 0, 3,
            3, 2 , 7, 8, 6,)
print(mi_lista.count(2))

print(max("Granada"))

numeros = range(30, 40)
print(min(numeros), "-", max(numeros))

tupla_siguiente = (10,11,12,13,14)
num = len(tupla_siguiente)
print(num)

# Sección 3
print("hola" * 5)
print("hola" + "mundo")
print(("b", "o") + ("b", "o"))
print([1,2,3] + [4,5,6])
print((7,8,9)* 2)
print([2,0,2,5]* 4)

# Sección 4
print("m" in "hola mundo")
print(4 in [1,2,3,4])
print("b" in ("a", "b", "c"))
print(10 in range(20))
print("r" not in "roto")
print(5 not in (1, 2, 3, 4, 5))
print("l" not in ["a", "k", "t"])
print("tortuga" in "tengo una tortuga")
print(b"lolito" in b"yepa, soy lolito")
print(bytearray(b"iphone") in bytearray(b"iphone18"))

#Slices

lista = ["primero", "segundo", "tercero",
          "cuarto", "quinto", "sexto",]
print(lista[-1])
print(lista[-2])

alfa = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "ñ", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", 
]
print(alfa[0:4]) #se podría dejar [:4] básicamente es igual.
print(alfa[3:6]) # o si queremos que empiece desde un elemento hasta el final de la lista sería [3:]

# para copiar una lista también podríamos dejarlo en blanco [:]

copia = alfa[-2:] # Podemos hacerlo a la inversa y obtener los últimos caracteres
print(copia)

copiaSegunda = alfa[:-2] #muestra toda la fila hasta el penultimo número

print(alfa[1:7:2]) #al agregarle un tercer número indicamos que nos muestre los elementos de ese rango en una determinada secuencia. 

print(alfa[::3]) # con esto muestra toda la lista con una determinada secuencia.

textazo = "Hola Mundo"

print(textazo[5:]) # Retorna "Mundo"

print(textazo[::2]) # Retorna "Hl ud"

rango = range(10, 100, 2)
seccion = rango[3: 30]
print(type(seccion))

alpha = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "ñ", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

alpha[5:10] = 1 ,2, 3, 4, 5     # Si la secuencia es mutable podemos módificarla! 

print(alpha)

borrandoAlfa = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "ñ", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

del borrandoAlfa[:20:2] # con del podemos borrar valores de la cadena, incluso dándole una secuencia 

print(borrandoAlfa)

# VISTAS DE MEMORIA

mis_bytes = b"abcdefghijklmnopqrstuvwzyz"
vista = memoryview(mis_bytes)
print("Como lista:")
print(vista.tolist()) # retorna datos del buffer en forma de lista
print("Como bytes:") 
print(vista.tobytes())  # retorna datos del buffer en forma de cadena de bytes

sin_escritura = b"12345"
con_escritura = bytearray(b"12345")

vista_con_escritura = memoryview(con_escritura) 
vista_sin_escritura = memoryview(sin_escritura) # se accede al código

print('"vista_sin_escritura":')
print("\tTamaño de objeto:", vista_sin_escritura.itemsize) #tamaño de bytes de cada elemento.
print("\tEs Read Only:", vista_sin_escritura.readonly) #condicional

print('"vista_con_escritura":')
print("\tTamaño de objeto:", vista_con_escritura.itemsize)
print("\tEs Read Only:", vista_con_escritura.readonly)






 
