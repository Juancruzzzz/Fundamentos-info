onCommand:codegenx.open_CodeGenX

#Ejercicio 1
def no_p (archivo, letra):
    suma = 0
    with open(archivo, "r") as f:
        for linea in f.read().split("\n"):
            if linea[0] != letra:
                suma += 1
print (no_p)

print (no_p("bio.txt", "m"))

#Ejercicio 2
def imprimir (archivo, lineas):
    contador = lineas - 1
    with open (archivo, "r") as f:
        listas = f.readlines()
        print (listas[:contador + 1])

print(imprimir("bio.txt",1))

#Ejercicio 3
def guardar (archivo, lineas):
    lista =[]
    with open (archivo, "r") as f:
        for i in f:
            lista.append (i)
    print(lista[-lineas:])

print (guardar ("bio.txt",3))

#Ejercicio 4
def contar (archivo):
    with open (archivo, "r") as f:
        lista_palabras = f.read().split()
        print(len(lista_palabras))

print (contar("bio.txt"))

#Ejercicio 5
def susti(archivo1, archivo2):
    with open(archivo1, "r") as f, open (archivo2, "w") as a:
        for palabra in f.read():
            for letra in palabra:
                a.write (letra.replace(letra, letra + "\n"))

#Ejercicio 7
def palabra_larga(archivo):
    caracteres = 0
    palabra =""
    with open(archivo, "r") as f:
        lista_palabras = f.read().split()
        for word in lista_palabras:
            if len(word) > caracteres:
                caracteres = len (word)
                palabra = word
    return palabra, caracteres

print (palabra_larga("bio.txt"))

#Ejercicio 9
def world_counter(archivo):
    frecuencias = {}
    with open (archivo, "r") as arc:
        word_list = arc.read().split()
        for palabra in word_list:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
        for word in frecuencias.keys():
            frecuencias [word] = round (frecuencias[word]/ len(word_list),3)

print(world_counter("messi.txt"))

#Ejercicio 10
import glob
import os 
def funcion1 (archivo, ruta):
    os.chdir(ruta)
    lista_txt = glob.glob ("*.txt")

    with open (archivo, "a") as s:
        for f in lista_txt:
            file = open (f,"r")
            s.write(file.read())
            file.close()