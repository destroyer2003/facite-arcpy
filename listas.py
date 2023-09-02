#_*_ coding: utf-8 _*_

#definir una lista con los dias de la semana

semana = ['martes', 'miercoles', 'jueves', 'viernes', 'sabado']
print(semana)
#insertar al final
semana.append('domingo')
#insertar donde queramos
semana.insert(0,'lunes')
print semana


#agrgarle una tupla la final
semana.append((1,2,3,4,5,6,7))

print semana

#borramos latupla
semana.pop(-1)
print semana

# y borramos el elemento con valor jueves de la lista
semana.remove('jueves')
print semana

#ordenar la lista de manera acendente
semana.sort()
print semana

#ordenar la liste de foirma decendiente
semana.sort(reverse=True)
print semana
#cuantas veces hay un valor
total_lista= semana.count('sabado')
print ("el sabado se encontro " + str(total_lista) + " veces")

# cuantos elementos hay en una lista
total = len(semana)
print ("la lista tiene " + str(total) + " elementos")