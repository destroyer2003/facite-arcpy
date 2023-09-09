#_*_ coding: utf-8 _*_

#solicitar una clasificacion de un alumno del 0 al 10
# imprimior si aprobo o rreprobo
try :
    clasificacion = int(input('ingrese una calificacion entre 1 y 10: '))

    #si la calificacion esta entre 6 y 10 esta raprobado

    if clasificacion >= 6 and clasificacion <= 10:
        print "Aprobado 👌😍"
    elif clasificacion >= 0 and clasificacion <= 5:
        print "Reprovado 😖💀"
    else:
        print "ingrese una clasificacion entre 0 y 10 🙄"

except Exception as error :
    print "ups!! ingresaste una letra y no un numero 🤡"
    print "problema :" + error.message