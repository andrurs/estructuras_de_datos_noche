# Ejemplo con tuplas
tupla1 = () #tupla vacia
print(tupla1)
tupla2 = ("apple",2018,"Samsung",4.9,"t",True)
print(tupla2)
print("Tupla 2 dato 1 → ",tupla2[1]); print("Tupla 2 dato 3 → ",tupla2[3])

# operación con tuplas
tupla3 = ("A","B","C","D")
tupla4 = (1,2,3,4)
#concatenar
tupla5 = tupla3 + tupla4
print("Tupla 5 →",tupla5)
#Repetirlas
tupla6 = tupla3 * 3
print("Tupla 6 → ",tupla6)
#Tupla enlazada
tupla7 = (0,1,2,3)
tupla8 = ("A","B","C")
tupla9 = (tupla7,tupla8)
print("Enlazar tupla 7 y 8 → ",tupla9)
print("sacar  el dato 2 de la tupla 7  → ",tupla9[0][2])

#Comparar
tupla10 = ("Rojas")
tupla11 = (123)
tupla12 = ("Rosas")
tupla13 = ("rosas")
print(tupla10 < tupla12)