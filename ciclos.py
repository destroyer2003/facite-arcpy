#_*_ coding: utf-8 _*_
from random import randint

lista_aleatorios= [ ]
#generar una lista con 100 numeros aleatorios
for i in range (0,100,1):
    #genera un numero aleatorio entre 0 y 1000
  aleatorio = randint(0, 100)
    #agregamos el numero a la lista
  lista_aleatorios.append(aleatorio)
#imprimir la lista de numeros aleatorios
print lista_aleatorios

#buscar si existe el numero 100 en la lista
if lista_aleatorios.count(100) > 0 :
    print "si se encontro el 100 en la lista 🍀 "
else:
    print "nel compa no esta 🤡"