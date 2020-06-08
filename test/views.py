from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from datetime import *
from credyty.settings import BASE_DIR
from math import sqrt
from test.Euler import is_pandigital
import functools
import sys 
import os
import codecs 
import numpy as np
from operator import mul 

# Create your views here.

def index(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'test/index.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )


def ejercicio1(request):
    assert isinstance(request, HttpRequest)

    result = 0
    mesagge = ""

    for c in range(2, 1000):
        if result > 0:
            break

        for a in range(1, c):
            # Asegurando que la suma de las variables sea a + b + c == 1000.  haciendo iteraciones de cero a 1000
            # se valida que la respuesta que se encuentra es a <= b.
            b = 1000 - c - a

            # Se valida que que se cumpla el teorema de pitagoras
            if a**2 + b**2 == c**2:
                mesagge ="a = %d, b = %d, c = %d.  a*b*c = %d" % (a, b, c, a * b * c)
                result = a*b*c
                break

    return render(
        request,
        'test/ejercicio1.html',
        {
            'title':'Ejercio Uno',
            'message':'Tripleta de pitagoras a + b + c = 1000',
            'year':datetime.now().year,
            'resume': mesagge,
            'result': "a * b * c = " + str(result),
        }
    )    

def ejercicio2(request):
    assert isinstance(request, HttpRequest)

    count = 0
    year = 1901
    month = 1
    mesagge = ""

    #se toma el primer dia del siglo
    curr_day = date(year,month,1)

    #mietras el año evaluado este dentro del siglo
    while(curr_day.year < 2001):
        #si el primer dia evaluado es domingo sumo al contador.
        if(curr_day.weekday() == 6):
            count += 1
        #si el mes es diciembre reinicio el contador de meses y sumo un año
        if(month+1 == 13):
            month = 1
            year += 1
        #si no es el ultimo mes salto a evaluar el siguiente mes
        else:
            month += 1
        
        #asigno como fecha a evaluar el mes y el año correspondiente con el dia 1
        curr_day = date(year,month,1)
    
    mesagge = "Counter: " + str(count)

    return render(
        request,
        'test/ejercicio2.html',
        {
            'title':'Ejercio Dos',
            'message':'Conteo de domingos inciales en mes para siglo 20',
            'year':datetime.now().year,
            'resume': mesagge,
            'result': "Cantidad = " + str(count),
        }
    )

def ejercicio3(request):
    assert isinstance(request, HttpRequest)

    #calculo del path relativo donde se encuentra el archivo
    file_path =  os.path.join(os.path.dirname(__file__), '', 'keylog.txt') 

    #lectura del archivo keylog para procesamiento de datos
    file = open(file_path) 
    #creacion de un arreglo  vacio para procesamiento de los datos
    s = [set() for i in range(10)] 
    error= ""

    for line in file: 
        n = list(map(int, line.rstrip())) 
        s[n[0]] |= set(n[1:]) 
        s[n[1]] |= set(n[2:]) 

    line = list(map(len, s)) 
    result = "" 
    
    for i in range(max(line) + 1): 
        #se verifica si coincide la entra con la siguiente y se agrega al resultado
        result = str(line.index(i)) + result 
    print (result)
    
    for n, i in enumerate(s): 
        for j in i: 
            if n in s[j]:
                error = ("Error: "), n, j

    if error == "":
        error = "No se presento error calculando el numero"
        
    return render(
        request,
        'test/ejercicio3.html',
        {
            'title':'Ejercio Tres',
            'message':'Derivar contraseña',
            'year':datetime.now().year,
            'error': error,
            'result': result,
        }
    )

#para la elaboracion de este ejercicio se usan las funciones del proyecto euler 
#http://nayuki.eigenstate.org/page/fast-fibonacci-algorithms
def ejercicio4(request):
    assert isinstance(request, HttpRequest)
    mesagge = ""

    fk, f0, f1 = 2, 1, 1
    while not is_pandigital(f1) or not is_pandigital(top_digits(fk)):
        f0, f1 = f1, (f1+f0) % 10**9
        fk += 1
    
    mesagge = "el numero k es: " + str(fk)

    return render(
        request,
        'test/ejercicio4.html',
        {
            'title':'Ejercio Cuatro',
            'message':'Numeros de Fibonacci Pan_digitales Secuencia de 9 digitos',
            'year':datetime.now().year,
            'result': mesagge,
        }
    )

#aqui se implementa la formula matematica que resume de manera optima
#el calculo de la serie fibonacci : t = n * log10(phi) + log10(1/sqrt(5)).
def top_digits(n):
     t = n * 0.20898764024997873 + (-0.3494850021680094)
     t = int((pow(10, t - int(t) + 8)))
     return t

def ejercicio5(request):
    assert isinstance(request, HttpRequest)

    tot = 0
    mxrow = 1000000000

    for i in range(0,mxrow):
        if(i%1000000==0):
            print (i/1000000)

        vl = baseN(i,7)
        vlstr = np.array([int(i)+1 for i in str(vl)])
        tot += functools.reduce(mul,vlstr,1)

    print (tot)


    return render(
        request,
        'test/ejercicio5.html',
        {
            'title':'Ejercio Cinco',
            'message':'Numeros no divisibles por 7 Triangulo de pascal',
            'year':datetime.now().year,
            'result': tot,
        }
    )



def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

