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




        ## FUNCIONES ##




        ## MÓDULOS ##




        ## PROGRAMACIÓN ORIENTADA A OBJETOS ##




        ## AMBIENTES VIRTUALES ##




        ## ERROR Y EXCEPCIONES ##

