#_*_ coding: utf-8 _*_

#como declarar una funcion( que de un saludo)
def saludar(): #funcion que no recibe parmetros
    print "hola saludos!!!"

def pendiente(): #funcion que no hace nada
    pass #es para que la funcion no mande error
#crear funciones que adivine edad en base a fecha de nacimiento
def adivinar_edad( mes, anio,dia="5"):
    #empezar a calcular la edad
    actual = 2023
    mes_actual= 9

    edad = actual-anio
    #si el mes es mayor al actual restamos 1 a la edad
    if mes > mes_actual:
        edad = edad-1
    print "la edad es :"+ str(edad)

#crear una funcion que reciba parametros opcinonales
def definir_sexualidad(genero="No binario"):
    print "Elejiste ser " + genero
saludar()
pendiente()
#mandar llamar la funcion llamar edad
adivinar_edad(1,2,2003)
#mandar llamar la funcion sexualidad 3 veces
definir_sexualidad("Heterosexual")
definir_sexualidad("LGBTQ+")
definir_sexualidad()