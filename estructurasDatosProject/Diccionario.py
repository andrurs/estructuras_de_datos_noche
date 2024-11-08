#ejemplos con diccionarios
diccionario = {} #diccionario vacio
puertos = {
    22:"SSH",
    23:"Telnet",
    80:"HTTP",
    3306:"MySQL",
    1526:"Oracle"
}
print(puertos[22])

puertos1 = {
    22:"SSH",
    80:"Http"
}
puertos2 = {
    53:"DNS",
    443:"Https"
}
print("• Puertos1 →",puertos1)
puertos1.update(puertos2) #actualizar el diccionario
print("• Puertos1 actualizado →",puertos1)

#eliminar un elemento del diccionario
calificaciones = {
    "alumno1" : 5,
    "alumno2" : 4,
    "alumno3" : 3,
    "alumno4" : 2,
}
print("• Dicc Calificaciones → ",calificaciones)
del calificaciones ["alumno3"] #Eliminar una pareja
print("• Dicc Calificaciones actualizado → ",calificaciones)

# Iterar en un diccionario
dicPuerto ={
    22: "SSH",
    23: "Telnet",
    80: "HTTP"
}
for x,y in dicPuerto.items():
    print(x,"→",y)