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