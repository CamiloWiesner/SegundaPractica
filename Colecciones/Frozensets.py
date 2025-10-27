# Los frozensets son la versión inmutable de los sets.
frozen1 = frozenset("Elsa")
frozen2 = frozenset("Anna")

print(frozen1 | frozen2) # Une
print(frozen1 ^ frozen2) # diferencia simetrica 
print(len(frozen1)) # Cuenta