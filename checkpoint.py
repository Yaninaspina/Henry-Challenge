# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def ListaEnteros(inicio, tamanio):
    lista = []
    for i in range(inicio, inicio + tamanio):
        lista.append(i)
    return lista

def DividirDosNumeros(dividendo, divisor):
    parte_entera = None
    resto = None
    return parte_entera, resto

def NumeroCapicua(numero):
    def invert(n):
        numero = 0
        while n != 0:
            numero = 10 * numero + n % 10
            n //= 10
        return numero

    num_inv = invert(numero)
    if type(numero) == int:
        if numero == num_inv:
            return  True
        else:
            return False
    else:
            return None

def Factorial(numero):
    fact = 1
    if type (numero)==int and numero > 0:
        for i in range(1,numero+1):
            fact*=i 
        return fact
    else:
        return None

    
def ProximoPrimo(actual_primo):
    def primo(nro):
        es_primo = True
        for i in range(2,nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo
    if primo(actual_primo) == True:
        return min([a for a in range(actual_primo +1,actual_primo*2)if primo(a)])
    else:
        return None   

def factorizar_numero(numero):
    if (type(numero)!=int):
        return None
    if (numero < 1):
        return None
    lista_primos = []
    i = 2 
    while (i < (int(numero/2) + 1)):
        primo = True 
        j=2
        while (j < i):
            if(i % j == 0):
               primo = False
               break
            j+=1
        if(primo):
           lista_primos.append(i)
        i+=1
    lista_factores = []
    lista_exponentes = []
    numero_original = numero 
    for i in lista_primos:
        j=0
        while (numero % i == 0):
            numero=numero/i
            if (j==0):
                lista_factores.append(i)
            j+=1
        if (j>0):
            lista_exponentes.apped(j)
    if(len(lista_factores)==0):
        return[[numero_original],[1]] 
    else:
        return[lista_factores,lista_exponentes]    

def ClaseAnimal(especie, color):
    class Animal:
        def __init__(self, especie, color):
            self.Especie = especie
            self.Color= color
            self.Edad = 0

        def CumplirAnios(self):
            self.Edad += 1
            return self.Edad

    a= Animal(especie,color)
    return a     

def NumeroBinario(numero):
    if type(numero) == int and numero > 0:
        return int(format(numero,"b"))
    else:
            return None