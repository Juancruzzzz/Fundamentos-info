

 #Ejercicio 1
s = input("Ingresar Texto Largo:")
print (len(s))

#Ejercicio 2
s1 = input ("Ingresar Texto 5ta y 6ta:")
print (s1 [4] + s1 [5])

#Ejercicio 3 
s3 =input ("Como es tu nombre y apellido?:")
print ("Hola " + s3)

#Ejercicio 4
s4a = input ("Como es tu nombre:")
s4b = input ("como es tu primer apellido:")
s4c = input ("Como es tu segundo apellido:")
print (str.upper (s4a[0] + s4b [0] + s4c [0]))

#Ejercicio 5
s5 = input ("3 numeros:")
suma = (int(s5 [0]) + int (s5 [2]) + int (s5[4])) / 3
print (suma)

#Ejercicio 6
s6 = input ("Minutos:")
horas = (int(s6) // 60)
minutos = int (s6) - (int(horas) * 60)
print (("Horas: ") + str (horas) + " y minutos: "+ str (minutos))

#Ejercicio 7
s7a = input ("Sueldo base: ")
s7b = input ("Venta: ")
fin_de_mes = int (s7a) + (int(s7b) * 0.10)

#Ejercicio 8
s8 = [input("Respuesta 1: "), input("Respuesta 2: "), input("Respuesta 3: ")]
nota = 0
for respuesta in s8:
    if respuesta == 'Correcta' :
        nota += 4
    elif respuesta == 'Incorrecta' :
        nota += 1
    elif respuesta == ' ' :
        nota
print (nota)