#_*_ coding: utf-8 _*_

# repasar las condicionales de toma de deciciones
#DADO UN NUMERO ESCRIBIR EL DIA DE LA SEMana

dia = input('ingrese un numero de l 1 al 7: ')
dia_seleccionado = ''
#si el dia es el numero 1 decimos que es lunes
if dia == 1:
   dia_seleccionado= 'Lunes'
elif dia == 2:
    dia_seleccionado = 'Martes'
elif dia == 3:
    dia_seleccionado = 'Miercoles'
elif dia == 4:
    dia_seleccionado = 'jueves'
elif dia == 5:
   dia_seleccionado = 'viernes'
elif dia == 6:
   dia_seleccionado = 'sabado'
elif dia == 7:
   dia_seleccionado = 'domingo'
else:
    valido = False
    print "ingresa un numero valido del 1 al 7"
if valido == True:
   print "El numero " + str(dia) + " corresponde al dia " + dia_seleccionado
