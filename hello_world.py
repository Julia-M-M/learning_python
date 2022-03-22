print("Hello world!") #Write "python hello_world.py" on the terminal to run the script

#Comentario de una sola línea
"""Comentario de
múltiples líneas"""


        ## DEFINICIÓN DE VARIABLES ##
    
    #Variable Texto/String: Cadena de caracteres (letras y símbolos)
nombre = "Ana" #Texto STRING
    
    #Variable numérica
edad = 20 #INTEGRER number (sin decimales)
estatura = 1.60 #FLOAT number (decimales)
    
    #Variable booleana: sólo puede tener dos valores, Verdadero/Falso --> Se usa para hacer comparaciones/condiciones
positivo = True #BOOLEAN
negativo = False #BOOLEAN

#Saber de qué tipo es tu variable
print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(positivo))
print(type(negativo))


        ## OPERADORES MATEMÁTICOS ##
""" 
    >>> 2+1 #Suma
    3
    >>> 2-1 #Resta
    1
    >>> 2*2 #Multiplicación
    4
    >>> 4/2 #División
    2.0
    >>> 5%2 #Módulo: residuo de la división 5/2
    1 
    >>> 3**2 #Potencia
    9
    
    >>> "texto1"+"texto2" #Concatenar texto
    'texto1texto2'
    >>> "texto"*3 #Repetir texto
    'textotextotexto'
   
   #Comparaciones
    >>> 1>2
    False
    >>> 1<2
    True
    >>> 1>=2
    False
    >>> 1<=2
    True
    >>> 1==2
    False
    >>> 1!=2
    True

    >>> "texto" == "texto"
    True
    >>> "texto" != "Texto"
    True
"""


        ## BUITL-IN FUNCTIONS ##
"""
    Funciones ya definidas en Python: function()
    Por ejemplo:
        print()
        help() --> Retorna la documentacuón de una función
        int() --> Convierte cualquier valor a un número entero truncándolo
            >>> int(3.23)
            3
            >>> int(3.73)
            3
        float() --> Convierte un número entero a uno florante
            >>> float(3)
            3.0
        str() --> Convierte cualquier tipo de variable a un string
            >>> str(True)
            'True'
            >>> str(3.4)
            '3.4'
        type() --> Retorna el tipo de una variable u objeto
            >>> type(True)
            <class 'bool'>
            >>> type(Hello world)
            File "<stdin>", line 1
                type(Hello world)
                        ^
            SyntaxError: invalid syntax
            >>> type("Hello world")
            <class 'str'>
"""


        ## PEP8 -- Style Guide for Python Code ##
"""
    www.python.org/dev/peps/pep-0008
    Indentation: 4 spaces per indentation level (bloque de código)
    Maximum line length: 79 characters
    Blank lines:    2 blank lines   --> Para separar funciones o clases
                    1 blank line    --> Separar los métodos de una clase
                                        Al final de cada archivo
                                        Separar la líneas de código que cumplen diferentes áreas
"""


        ## ESTRUCTURAS DE DATOS ##
"""
    Tipos:
        list = [element1, element2...]              --> ordenado, mutable y permite duplicados
        tuple = (element1, element2...)              --> ordenado, no mutable y permite duplicados
        dictionary = {key:value}                    --> no ordenado, mutable y no permite duplicados
        set = {unique_element1, unique_element2...} --> no ordenado, mutable y no permite duplicados
"""
#Listas / LISTS
"""
>>> lenguajes = ["python", "java", "golang"]
>>> lenguajes
['python', 'java', 'golang']
>>> lista = [1, 2.0, True, "python", 1]
>>> lista
[1, 2.0, True, 'python', 1]

>>> len(lenguajes) #list's length (n)
3
>>> lenguajes[0] #The first position in the list is 0
'python'
>>> lenguajes[-1] #En regresivo, la última posición es -1
'golang'
>>> lenguajes[-3] #En regresivo, la primera posición es -n
'python'
>>> lenguajes[0:2] #Nos da de la primera(0) a la posición antes de la tercera(2)    --> list[a:b]   where   a = 1st position we want
                                                                                                            b = position after the las one we want
['python', 'java']

>>> programacion = [lenguajes, "dedicacion", "practica"] #Nested lists --> las listas se pueden anidar (una lista dentro de la otra)
>>> programacion
[['python', 'java', 'golang'], 'dedicacion', 'practica']
>>> programacion[0][0] #Para obtener, del primer elemento(lista "programacion"), el primer elemento("python")
'python'

>>> lenguajes[0]="dart" #Modificar un elemento de la lista
>>> lenguajes
['dart', 'java', 'golang']
>>> lenguajes.append("python") #append --> Añadir un elemento a la última posición de la lista como un solo elemento
>>> lenguajes
['dart', 'java', 'golang', 'python']
>>> otros_lenguajes = ["c", "c++"]
>>> otros_lenguajes
['c', 'c++']
>>> lenguajes.extend(otros_lenguajes) #extend --> Añadir por separado los elementos de un elemento a la última posición de la lista
>>> lenguajes
['dart', 'java', 'golang', 'python', 'c', 'c++']
"""

#Tuplas / TUPLES --> Listas inmutables
"""
>>> lenguajes = ("python", "c", "c++")
>>> lenguajes
('python', 'c', 'c++')
>>> lenguajes1 = "python", "c", "c++" #Si no ponemos () ni [], interpreta que es una tupla
>>> lenguajes1
('python', 'c', 'c++')
>>> lenguajes[1]
'c'
>>> lenguajes[-1]
'c++'
>>> lenguajes[0] = "java" #Inmutable, es decir, no se puede modificar
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
"""

#Diccionarios / DICTIONARIES --> Almacenan datos en pares de datos llamados llave y valor (cada valor es un elemento que corresponde a una llave)
"""
>>> lenguaje = {
... "nombre":"python",
... "creador":"Guido"
... }
>>> lenguaje
{'nombre': 'python', 'creador': 'Guido'}

>>> lenguaje["nombre"]
'python'
>>> lenguaje["año_lanzamiento"]=1991 #Se pueden añadir llaves
>>> lenguaje
{'nombre': 'python', 'creador': 'Guido', 'año_lanzamiento': 1991}
>>> lenguaje["año_lanzamiento"]=1999 #Y se peuden modificar los valores de la llave, pero no se pueden duplicar las llaves
>>> lenguaje
{'nombre': 'python', 'creador': 'Guido', 'año_lanzamiento': 1999}

>>> lenguaje["caracteristicas"]=["sencillo", "facil", "genial"]
>>> lenguaje
{'nombre': 'python', 'creador': 'Guido', 'año_lanzamiento': 1999, 'caracteristicas': ['sencillo', 'facil', 'genial']} #   Llave = texto      Valor = cualquier tipo (texto, lista...)

>>> lenguaje.items()
dict_items([('nombre', 'python'), ('creador', 'Guido'), ('año_lanzamiento', 1999), ('caracteristicas', ['sencillo', 'facil', 'genial'])])
>>> lenguaje.keys()
dict_keys(['nombre', 'creador', 'año_lanzamiento', 'caracteristicas'])
>>> lenguaje.values()
dict_values(['python', 'Guido', 1999, ['sencillo', 'facil', 'genial']])
"""

#SETS --> Permite guardar elementos únicos
"""
>>> set1 = {1,2,3}
>>> set1
{1, 2, 3}
>>> set1[2] #No es un elemento ordenado, así que no se puede imprimir una posición
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> set2 = {1,1,1,2,3} #No permite duplicados
>>> set2 
{1, 2, 3}
>>> set3 = {1,2.0,"texto"} #Permite texto y números flotantes
>>> set3
{1, 2.0, 'texto'}

>>> set1.add(4) #Añadir elementos al set
>>> set1
{1, 2, 3, 4}
>>> set1.update([4,5,6]) #Añadir elementos al set
>>> set1
{1, 2, 3, 4, 5, 6}
>>> len(set1) #Saber la longitud del set
6
>>> set1.discard(2) #Eliminar elementos del set
>>> set1
{1, 3, 4, 5, 6}
>>> set1.remove(3) #Eliminar elementos del set
>>> set1
{1, 4, 5, 6}
>>> set1.clear() #Eliminar todos los elementos del set
>>> set1
set()
"""


        ## CONDICIONES Y CICLOS ##

#Condiciones
"""
Instrucción que se ejecuta o no al cumplirse una condición

Dependen de una condición lógica y se usan para comparar
    Igual ==
    Diferente !=
    Menor <
    Mayor >
    Menor o igual que <=
    Mayor o igual que >=
Obtenemos en retorno una variable booleana (True/False)

Expresiones condicionales
    is --> validar si dos variables se refieren al mismo objeto (retorna True/False)
    and --> unir dos condiciones. Retorna True si ambas son True, retorna False si una condición es False
    or --> unir dos condiciones. Retorna True si una es True, retorna False si ambas son False
    not --> retorna True si el valor es False. Verificar si un elemento está o no contenido en una lista o estructura de datos

if<condición lógica>:   #Condición principal
    print("If block")
elif<condición lógica>: #"Si no", si se incumple una condición del bloque if
    print("Elif block")
else:                   #Si ninguna de las condiciones anteriores se cumple
    print("Else block")
"""

a = 2
b = 2

if a < b:
    print("A es menor que B")
elif a == b:
    print("A es igual a B")
else:
    print("A es mayor que B")


c = False

if c:
    print("C es Verdadero")
else:
    print("C es Falso")


if type(c) is bool:
    print("C es Booleano")
else:
    print("C es otro tipo de dato")


d = 10
e = 5
f = 1

if d>e and e>f:
    print("Las dos condiciones son verdaderas")


for letra in "Texto":
    print(letra)


lenguajes = ["python", "java", "golang"]
for elemento in lenguajes:
    print(elemento)
    if elemento == "java":
        break               #Si no ponemos el IF, BREAK rompe después del primer elemento

lenguajes = ["python", "java", "golang"]
for elemento in lenguajes:
    if elemento == "java":  #Si el elemento es java,
        continue            #sáltate este elemento y
    print(elemento)         #sigue con el siguiente elemento de la lista


for element in range(5):    #El rango va de 0-4
    print(element)

for element in range(1,5):  #El rango va de 1-4
    print(element)

#Ciclos
"""
Instrucciones que se repiten hasta que se cumple una condición

Tipos:
    For
    While

for <element> in <object>    #Repetir la instrucción para cada elemento del objeto sobre el que vamos a iterar
    print("Elemento:"<element>)

while <condición>:
    print("Ciclo While")
"""

i = 1
while i<=5:     #Mientras el valor de i sea menor o igual a 5,
    print(i)    #imprime el valor de i y
    i += 1      #súmale 1
                #Vuelve a empezar

i = 1
while i<=5:     
    print(i)    
    i += 1  
    if i == 3:
        break   #Romper el ciclo


lenguajes = ["python", "java", "golang"]
for elemento in lenguajes:
    print(elemento)

lenguajes = ["python", "java", "golang"]
for index in range(len(lenguajes)):         #Para cada índice del rango de longitud de la lista "lenguajes"
    print("Índice", index)                  #imprime la palabra "Índice" y el índice del rango (número)
    print("Elemento:", lenguajes[index])    #seguido imprime la palabra "Elemento:" y el índice de la lista (lenguaje)

lenguajes = ["python", "java", "golang"]
i = 0   #contador de la lista "lenguajes", que empieza en 0
while i<len(lenguajes): #Mientras el contador sea menor a la longitud de la lista,
    print(lenguajes[i]) #imprimir el lenguaje de esa posición de la lista
    i+=1                #y sumarle 1 al contador


lenguaje = {
    "Nombre": "Python",
    "Creador": "Guido van Rossum"
}
for llave in lenguaje:
    print("Llave:", llave)
    print("Valor:", lenguaje[llave])

lenguaje = {
    "Nombre": "Python",
    "Creador": "Guido van Rossum"
}
for elemento in lenguaje.keys():
    print(elemento)
for elemento in lenguaje.values():
    print(elemento)
for elemento in lenguaje.items():       #Imprime los elementos en TUPLAS
    print(elemento)
for llave, valor in lenguaje.items():   #Imprime los elementos por separado
    print(llave, valor)


        ## FUNCIONES ##
"""
Bloques de código
Contienen instrucciones relacionadas que realizan una tarea
Sirven para organizar el código en partes pequeñas que permitan su uso y evitan la repetición de instrucciones y permiten reusarlo

def <nombre_funcion>(): --> Para crear la función (no se escriben los <>)
    <instrucción>

<nombre_funcion>    --> Para llamar a la función

Tipos:
    Built-in: no necesitan instalación
    User-defined: creadas por cada desarroyador en cada proyecto
"""

APELLIDO = "Moreno-Manjón" #Variable GLOBAL
def funcion():
    print("Mi primera función")
    nombre = "Julia"    #Variable local
    print(nombre, APELLIDO)

funcion()
print(nombre)   #Da error porque "nombre" sólo está definido dentro de la función (variable local)
print(APELLIDO) #Esta sí que se imprime porque es una variable GLOBAL

"""
def <nombre_funcion>(parámetro, argumento): 
    <instrucción>

<nombre_funcion>    --> Para llamar a la función
"""
def perimetro_cuadrado(lado, unidades):
    perimetro = lado*4
    print(f"El perímetro es: {perimetro} {unidades}")   #Op.1: IMPORTANTE la "f", si no toma todo como texto y no como función
    print("El perímetro es:", perimetro, unidades)      #Op.2

perimetro_cuadrado(25,"metros") #Op.1
perimetro_cuadrado(lado=25,unidades="metros")   #Op.2
        #Parámetro: nombre que se le da al valor que entra a la función = lado
        #Argumento: valor que entra a la función = 25

#Op.1
def perimetro_cuadrado(lado):
    perimetro = lado*4
    return perimetro    #Para almacenar el valor y poderlo usar más adelante

def area_cuadrado(lado):
    area = lado*lado
    return area

perimetro = perimetro_cuadrado(lado=5)
area = area_cuadrado(lado=5)

print(f"Área: {area}, Perímetro: {perimetro}")

#Op.2
def calcular_cuadrado(lado):
    perimetro = lado*4
    area = lado*lado
    return area, perimetro

area, perimetro = calcular_cuadrado(lado=5)
print(f"Área: {area}, Perímetro: {perimetro}")

resultado = calcular_cuadrado(lado=5)   #El resultado se guarda en una TUPLA
print(resultado)


#Documentación de una función
"""
def <nombre_funcion>(parámetro, argumento): 
    """
    #<TÍTULO o Descripción corta de la función. Al pasar el cursor por al función podemos ver su descripción>

    #<Descripción larga>

    #Args: lista con el <nombre de cada uno de los parámetros de la función (tipo de dato): descripción del parámetro>

    #Returns: lista con el <nombre de cada uno de los retornos de la función (tipo de dato): descripción del retorno>
    """
    
    <instrucción>

<nombre_funcion>  
"""

def perimetro_cuadrado(lado):
    """Calcular el perímetro de un cuadrado  
    
    Esta función recibe el valor de un lado de un cuadrado y, a partir  
    de este, calcula y retorna su perímetro

    Args:
        lado (int): medida del lado del cuadrado
    
    Returns:
        perimetro (int): perímetro del cuadrado
    """
    perimetro = lado*4
    return perimetro

perimetro = perimetro_cuadrado(lado=5)  


        ## MÓDULOS y PAQUETES/LIBRERIAS##
"""
Los PAQUETES (o librerías) son carpetas que contienen MÓDULOS que, a su vez, contienen una o varias FUNCIONES
"""
import datetime #Importar librería
hora_actual = datetime.datetime.now()
hora_actual

import datetime as dt   #Importar librería con un alias
hora_actual = dt.datetime.now()
hora_actual

from datetime import datetime   #Importar un submódulo de una librería
hora_actual = datetime.now()
hora_actual

#Crear un módulo:
    #1 Crear el módulo en un archivo llamado cuadrado.py:
        def perimetro_cuadrado(lado):
            return lado*4    

        def area_cuadrado(lado):
            return lado*lado
    #2 Importar las funciones a un nuevo archivo llamado main.py:
        from cuadrado import area_cuadrado, perimetro_cuadrado

        lado = 5
        cuadrado = {
            "lado": lado,
            "area": area_cuadrado(lado),
            "perimetro": perimetro_cuadrado(lado)
        }
        
        print(cuadrado)

        perimetro = perimetro_cuadrado(lado)
        print(perimetro)


#Crear un paquete/librería
    #1 Crear una carpeta llamada "figuras"
    #2 Crear un archivo llamado __init__.py --> Se deja vacío
    #3 Se le añade o crea un archivo con el módulo cuadrado.py
        def area_cuadrado(lado):
            return lado * lado

        def perimetro_cuadrado(lado):
            return lado * 4
    #4 Crear un nuevo módulo llamado circulo.py
        def area_circulo(radio):
            return 3.14 * radio * radio

        def perimetro_circulo(radio):
            return 3.14 * 2 * radio
    #5 Crear el archivo principal main.py fuera de la carpeta figuras
        from figuras.cuadrado import area_cuadrado, perimetro_cuadrado
        from figuras.circulo import area_circulo, perimetro_circulo

        lado = 4
        cuadrado = {
            "lado": lado,
            "area": area_cuadrado(lado),
            "perimetro": perimetro_cuadrado(lado)
        }
        print("Cuadrado", cuadrado)

        radio = 5
        circulo = {
            "radio": radio,
            "area": area_circulo(radio),
            "perimetro": perimetro_circulo(radio)
        }
        print("Círculo", circulo)


        ## PROGRAMACIÓN ORIENTADA A OBJETOS ##

class Persona:  #Definir una Clase
    def __init__(self): #SIEMPRE DEBE ESTAR
        print("Estoy en el constructor")

pedro = Persona()
print(type(pedro))

paco = Persona()
print(type(paco))

print(pedro == paco)    #False porque son objetos del mismo tipo (Personas) pero no el mismo objeto


class Persona:  
    atributo = 123  #Para todos los objetos de la clase
    def __init__(self, nombre, edad): #Atributos de instancia siempre dentro de __init__
        self.nombre = nombre
        self.edad = edad

paco = Persona("Paco", 20)

print(paco.nombre)
print(paco.edad)
print(paco.atributo)


class Persona:  
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad

    def cumplir_años(self):
        self.edad += 1
        print(f"Feliz cumpleaños #{self.edad}, {self.nombre}")

paco = Persona(nombre="Paco", edad=20)

paco.cumplir_años()


#HERENCIA de clases
class Persona:  #Clase PADRE
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad

    def cumplir_años(self):
        self.edad += 1
        print(f"Feliz cumpleaños #{self.edad}, {self.nombre}")

class Empleado(Persona):    #Clase HIJO
    def trabajar(self, horas_trabajadas):
        print(f"Usted ha trabajado {horas_trabajadas} horas")

paco = Empleado(nombre="Paco", edad=20)
paco.trabajar(horas_trabajadas=8)
paco.cumplir_años()


class Persona:  #Clase PADRE
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad

    def cumplir_años(self):
        self.edad += 1
        print(f"Feliz cumpleaños #{self.edad}, {self.nombre}")

class Empleado(Persona):    #Clase HIJO
    def __init__(self, horas_totales, nombre, edad):
        super(Empleado, self).__init__(nombre,edad) #Para mantener los atributos de la clase padre y no sobreescribirlos con la línea anterior
        self.horas_totales = horas_totales
    
    def trabajar(self, horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Usted ha trabajado {horas_trabajadas} horas")
        print(f"Horas totales: {self.horas_totales} horas")

paco = Empleado(nombre="Paco", edad=20, horas_totales=30)
paco.trabajar(horas_trabajadas=8)
paco.cumplir_años()


        ## AMBIENTES VIRTUALES ##
"""
Se pueden encontrar en https://pypi.org/

Instalar/actualizar librerías --> pip
"""


        ## ERROR Y EXCEPCIONES ##

