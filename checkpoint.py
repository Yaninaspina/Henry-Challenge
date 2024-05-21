# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def ListaEnteros(inicio, tamanio):
    lista = []
    for i in range(inicio, inicio + tamanio):
        lista.append(i)
    return lista
def DividirDosNumeros(dividendo, divisor):
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    
    parte_entera = dividendo // divisor
    resto = dividendo % divisor
    
    return parte_entera, resto


def NumeroCapicua(numero):
    def invertir(n):
        numero_invertido = 0
        while n != 0:
            numero_invertido = 10 * numero_invertido + n % 10
            n //= 10
        return numero_invertido
    
    numero_invertido = invertir(numero)
    
    # Verificar si el número original es igual a su inverso
    if numero == numero_invertido:
        return True
    else:
        return False



def Factorial(numero):
    if isinstance(numero, int) and numero >= 0:
        if numero == 0:
            return 1  # Caso especial: factorial de 0 es 1
        else:
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            return factorial
    else:
        return None

    
import math

def ProximoPrimo(actual_primo):
    def es_primo(nro):
        if nro < 2:
            return False
        for i in range(2, int(math.sqrt(nro)) + 1):
            if nro % i == 0:
                return False
        return True
    
    if not es_primo(actual_primo):
        return None
    
    siguiente_primo = actual_primo + 1
    while not es_primo(siguiente_primo):
        siguiente_primo += 1
    
    return siguiente_primo
def factorizar_numero(numero):
    if not isinstance(numero, int) or numero < 1:
        return None

    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    lista_primos = [i for i in range(2, int(numero**0.5) + 1) if es_primo(i)]
    lista_factores = []
    lista_exponentes = []
    numero_original = numero

    for primo in lista_primos:
        if numero % primo == 0:
            exponente = 0
            while numero % primo == 0:
                numero //= primo
                exponente += 1
            lista_factores.append(primo)
            lista_exponentes.append(exponente)
    
    if numero > 1:  # Si el número restante es mayor que 1, es un factor primo mayor que sqrt(numero_original)
        lista_factores.append(numero)
        lista_exponentes.append(1)

    return [lista_factores, lista_exponentes]

class Animal:
    def __init__(self, especie, color):
        self.especie = especie
        self.color = color
        self.edad = 0

    def cumplir_anios(self):
        self.edad += 1
        return self.edad

def crear_animal(especie, color):
    return Animal(especie, color)


def NumeroBinario(numero):
    if isinstance(numero, int) and numero > 0:
        return int(format(numero, "b"))
    else:
        return None