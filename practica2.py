#1
def mayuscula_o_minuscula(palabra):
    if palabra[0] == str.upper(palabra[0]):
        return "Mayuscula"
    elif palabra[0] == str.lower(palabra[0]):
        return "Minuscula"
print(mayuscula_o_minuscula("computadora"))
print(mayuscula_o_minuscula("computadora"))

#2
def positivo_negativo(numero):
    resultado = ""
    if numero < 0:
        resultado += "Negativo"
    elif numero > 0:
        resultado += "Positivo"
    else:
        resultado += "Cero"
    return resultado + " " + par_o_impar(numero)

def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
print(positivo_negativo(4))

#3
def numero_opuesto(numero):
    if 1 <= numero <= 6:
        return 7 - numero
    else:
        return "El numero ingresado es incorrecto"
print(numero_opuesto(6))
print(numero_opuesto(10))

#4
def cobro_paquete(ubicación, peso):
    if peso > 5:
        return "Entrega rechazada"
    elif ubicación == "América del sur":
        return peso * 10.00
    elif ubicación == "América central":
        return peso * 15.00
    elif ubicación == "América del norte":
        return peso * 18.00 
    elif ubicación == "Europa":
        return peso * 24.00 
    elif ubicación == "Asia":
        return peso * 30.00
print(cobro_paquete("Asia", 4))

#5
def dia_semana(numero):
    if numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miercoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sabado")
    elif numero == 7:
        print("Domingo")
    else:
        print("El numero es incorrecto")
dia_semana(3)
dia_semana(20)

#6
lista1 = "messi"
lista2 = list(reversed(lista1))
print(lista2)

#7


#8
def suma_de_listas(lista11, lista22):
    lista33 = [lista11[0] + lista22[0], lista11[1] + lista22[1], lista11[2] + lista22[2], lista11[3] + lista22[3], lista11[4] + lista22[4]]
    return lista33
print(suma_de_listas([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

#10
def letra(string):
    diccionario = {}
    for letra in string:
        if letra not in diccionario:
            diccionario[letra] = 1
        elif letra in diccionario:
            diccionario[letra] += 1
    return diccionario
print(letra("bebet benedetto"))

#11
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
diccionario = {}
for letra in alfabeto + alfabeto.upper():
    diccionario[letra] = 0 
def letra2(string):
    for letra in string:
        if letra not in diccionario:
            diccionario[letra] = 1
        elif letra in diccionario:
            diccionario[letra] += 1
    return diccionario
print(letra2("lionel andres messi"))

#12


#13
def esMultiplo(numero1, numero2):
    return numero1 % numero2 == 0 or numero2 % numero1 == 0
print(esMultiplo(2, 4))

def temperatura_media(max, min):
    return (max + min) / 2
print(temperatura_media(20, 4))


#15

def cargarSocios(socios):
    numero = int(input("Número de socio: "))
    while numero != 0:
        nombre = input("Nombre y apellido: ")
        fecha = input("Fecha de ingreso: ")
        cuota = input("¿Cuota al día? s/n: ")
        pago = cuota.lower() == "s"
        socios[numero] = [nombre, fecha, pago]
        numero = int(input("Número de socio: "))
    return socios
def modificarFecha(socios, fechaAnterior, fechaNueva):
    for datos in socios.values():
        if datos[1] == fechaAnterior:datos[1] = fechaNueva
    return socios
def numeroSocio(socios, nombre):
    for numero,datos in socios.items():
        if datos[0].lower() == nombre.lower():
            return numero
            return 0
def formatoFecha(fecha):
    return fecha[:2] + "/" + fecha[2:4] + "/" + fecha[4:]
def imprimirListado(socios):
    for numero,datos in socios.items():
        print("Número: ", numero)
        print("Nombre: ", datos[0])
        print("Fecha de ingreso ", formatoFecha(datos[1]))
        if datos[2]:
            print("Cuota al día")
        else:
            print("En deuda")
            print("---------------")
        return None
    socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}
    print("Cargar socios")
    socios_activos = cargarSocios(socios_activos)
    print("El club tiene", len(socios_activos), "socios")
    print("Registrar pago de cuotas")
    numero = int(input("Numero de socio: "))
    socios_activos[numero][2] = True 
    print("Modificando fecha de ingreso...")
    socios_activos = modificarFecha(socios_activos, "21102017", "22102017")
    print("Eliminar socio:")
    nombre = input("Nombre y apellido: ")
    numero = numeroSocio(socios_activos, nombre)
    del socios_activos[numero]
    imprimirListado(socios_activos)