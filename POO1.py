#Ejercicio 1
"""
Estado: El estado de un objeto es el cojunto de atributos del objeto. En este caso, el estado es self o alimento y caricias.
Interfaz: La interfaz de un objeto es el conjunto de mensajes que cada objeto expone. En este caso seria energia, comer, acariciar, esta debil.
"""
#Ejercicio 2
from wsgiref.validate import validator


def volar(self, kms):
    if self.energia >0:
        self.energia -= 10 + kms/10
    else:
        print("No puede volar")

#Ejercicio 3
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento_precio(self, porcentaje):
        self.precio = self.precio - (self.precio * porcentaje / 100)
#Ejercicio 4
class Contador:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial
    
    def inc(self):
        self.valor_inicial += 1
    
    def dis(self):
        self.valor_inicial -= 1
    
    def reset(self):
        self.valor_inicial = 0
    
    def valorNuevo(self, valor_nuevo):
        self.valor_inicial = valor_nuevo

    def valorActual(self):
        return self.valor_inicial

#Ejercicio 5
class Contador:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial
        self.lista1 = []
    def inc(self):
        self.valor_inicial += 1
        self.lista1.append("incremento")
    
    def dis(self):
        self.valor_inicial -= 1
        self.lista1.append("disminucion")
    
    def reset(self):
        self.valor_inicial = 0
    
    def valorNuevo(self, valor_nuevo):
        self.valor_inicial = valor_nuevo
        self.lista1.append("actualizacion")

    def valorActual(self):
        return self.valor_inicial
    
    def ultimoComadando(self):
        return self.lista1[-1]

#Ejercicio 6
class Calculadora:
    def __init__(self):
        self.valor = 0
    
    def cargar(self, numero):
        self.valor = numero

    def sumar(self, numero):
        self.valor += numero
    
    def restar(self, numero):
        self.valor -= numero
    
    def multiplicar(self, numero):
        self.valor = self.valor*numero

    def valorActual(self):
        return self.valor

#Ejercicio 7
class Gorriones:
    def __init__(self):
        self.gramos = 0
        self.kilometros = 0
        self.gramoscomidos = []
        self.kilometrosvolados = []

    def comer(self, gramos):
        self.gramos += gramos
        self.gramoscomidos.append(gramos)

    def volar(self, kilometros):
        self.kilometros += kilometros
        self.kilometrosvolados.append(kilometros)
    
    def CSS(self):
        if self.gramos > 0:
            return self.kilometros/self.gramos
        else:
            return "None"

    def CSSP(self):
        if self.gramos > 0: 
            return max(self.kilometrosvolados)/max(self.gramoscomidos) 
        else:
            return "None"
    def CSSV(self):
        if self.gramos > 0: 
            return len(self.kilometrosvolados)/len(self.gramoscomidos)
        else:
            return "None"  

    def esta_en_equilibrio(self):
        return 0.5 < self.CSS() < 2
