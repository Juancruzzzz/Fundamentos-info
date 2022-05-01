import re

#Ejercicio 1
#Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

def Caracter_permitido(string):
    print(len(re.findall(r"\w", string))> 0)

Caracter_permitido("Hola")

# Ejercicio 2
# Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

def Caracter_permitido(string):
    print(not len(re.findall(r"\W", string)))

Caracter_permitido("Hola")

#Ejercicio 3
#Creá un programa que verifique las siguientes condiciones:
#a si un string dado tiene una h seguida de ninguna o más e.
#b si un string dado tiene una h seguida de una o más e.
#c si un string dado tiene una h seguida de dos o tres e.

#A
def tiene_h(string_con_h):
    print(bool(re.search("he*", string_con_h)))

tiene_h("heeeola")

#B
def tiene_h(string_con_h):
    print(bool(re.search("he+", string_con_h)))

tiene_h("heeeola")

#C
def tiene_h(string_con_h):
    print(bool(re.search("he{2,3}", string_con_h) and not re.search("heeee+", string_con_h)))

tiene_h("hel")

#Ejercicio 4 
#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios)

def palabras_unidasguion(string):
    print(re.findall(r"([a-z]+)_([a-z]+)", string))

palabras_unidasguion("hola_chau")   

#Ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.

def arranca_con_numero(string, n):
    numero = "^" + n
    print(bool(re.search(numero, string)))

arranca_con_numero("7hola", "7")

#Ejercicio 6
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

def string_frase(listadestrings, frase):
    for element in listadestrings:
        print(bool(re.search(element, frase)))

string_frase(["jeje", "123"], "jeje")

#Ejercicio 7 
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

def string_con_todo(string):
    string_sin_espacios = string.replace(" ","")
    a = bool(re.search(r'[a-z]', string) and re.search(r'[A-Z]', string) and re.search(r"\s", string) and string_sin_espacios.isalnum())
    print(a)

string_con_todo("Aa1 ")

#Ejercicio 8
#Escribí un programa que separe y devuelva los caracteres númericos de un string.
def caracter_num(string):
    c = (re.findall(r"\d", string))
    print(c)

caracter_num("hola 3 hola 4")

#Ejercicio 9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")


def a(string):
    return (re.findall("-.*-",string))
print (a("-afafs-sadfafsfsf"))

#Ejercicio 10
#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.

def obtener_substring(substring):
    a = print(re.split("@|&", substring))
    print (a)

obtener_substring("Sant&iago@ssss")

#Ejercicio 11
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima.
#(Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).

lista_string = ["Práctica Python", "Práctica C++", "Práctica Fortran"]

def dos_con_p(variable):

    for lenguaje in lista_string:
        resultado = re.match("(P\w+)\W(P\w+)", lenguaje)

        if resultado:
            print(resultado.groups())

dos_con_p(lista_string)

#Ejercicio 12
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

def reemplazar(string):
    ya_reemplazado = string.replace(" ", "|").replace(":", "|").replace("_", "|")
    print(ya_reemplazado)

reemplazar("Hola como:estas_lucho")

#Ejercicio 13
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
def reemplazar2(string):
    a = (re.findall(r'\W', string))
    if a[0] == a[1]:
        ya_reemplazado_2 = string.replace(a[0], "_", 2)
        print(ya_reemplazado_2)
    else:
         ya_reemplazado_3 = string.replace(a[0], "", 1).replace(a[1], "", 1)
         print(ya_reemplazado_3)

#Dierente perspectiva
reemplazar2("Hola:Chau?Lucho!")


def reemplazar(string):
    return re.sub("\W","_", string,2)

print(reemplazar("hola*comoestas??as"))
print(reemplazar("hola como esta??ass"))

#Ejercicio 14
#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

def reemplazar3(string):
    a = re.sub(r"\s",";", string)
    print(a)
reemplazar3("Hola como estas    ")

#Ejercicio 15
#Realizá un programa que validar si una cuenta de mail está escrita correctamente.

def validar_mail(mail):
    valido = bool(re.match(r"(\S+)@(\w+)\.(\w)", mail))
    print (valido)

validar_mail("juancruzmelga@gmail.com" )