# Ejemplo con listas

lista = [] #lista vacia
lista1 = [1,"Hola",4.5,"8"] #Lista con 4 elementos
print("Lista 1 → ",lista1)
print("Lista 1, poscn 1, elmt 2 → ",lista1[1][2])

#Listas enlazadas
lista2 =  [0,1,2,3]
lista3 = ["A","B","C"]
lista4 = [lista2,lista3]
print("sacar  el dato 2 de la lista 3  → ",lista4[1][2])

# operaciones en listas
lista5 = ["A","B","C"]
lista6 = [1,2,3,4]
lista7 = lista5 +  lista6
print("Lista 6 + lista 7 → ",lista7)

#Repetir
lista8 = [1,2,3,4,5]
lista9 = lista8 * 4
print("Lista8 4 veces → ",lista9)
#comparacion
lista10 = ["Juan"]
lista11 = ["Juan "]
print(lista10 == lista11)

#Determinar si un elemento se encuentra dentro de la lista
lista12 = ["cien","años","de","soledad"]
if "de" in lista12:
    print("'de', Si está en la lista12")
else:
    print("'de', No está en la lista12")

#Iterando una lista
lista13 = ["Hola","Estudiantes","Programación"]
for palabra in lista13:
    print(palabra, end=", ")