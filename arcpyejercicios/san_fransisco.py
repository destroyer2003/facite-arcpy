#_*_ coding: utf-8 _*_
import arcpy   #libreria de arcgis
from arcpy import da as data
import csv      #libreria para generar CSV


#permitir sobreescribir los archivos existentes
arcpy.env.overwriteOutput = True

#archivo de entrada
parada_autobuses = arcpy.GetParameterAsText(0) #r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Bus_Stops"
censo =  arcpy.GetParameterAsText(1) #r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\CensusBlocks2010"
seleccion_paradas = arcpy.GetParameterAsText(2) #r"C:\Users\FOTO_06\PycharmProjects\facite-arcpyejercicios\RECURSOS\Data\SanFrancisco.gdb\seleccion"

#archivos generados
interseccion = arcpy.GetParameterAsText(4)#r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\InterseccionesCenso"
buffer =  arcpy.GetParameterAsText(3)#r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Buffer"
resultado_csv = arcpy.GetParameterAsText(5)

#seleccionar Bus stops que coincidan con el name 14 OB y el bus_signan Lowell st.
arcpy.Select_analysis(parada_autobuses, seleccion_paradas,  "NAME = '14 OB' AND BUS_SIGNAG = 'Lowell St.'")
arcpy.AddMessage("Seleccion Finalizada ")
print "Seleccion Finalizada (●'◡'●)"
#HACER BUFFER DE 100 MTRS
arcpy.Buffer_analysis(seleccion_paradas, buffer,  "100 Meters")
arcpy.AddMessage("Buffer Finalizado ^_^")
print "Buffer Finalizado ^_^"
# hacer interseccion de census block con el buffer
arcpy.Intersect_analysis([censo, buffer], interseccion )
arcpy.AddMessage("Interseccion Finalizada :-)")
print "Interseccion Finalizada "

#diccionario para extraer informacion
interseccion_datos= { }

#recorrer los registros de tabla de atributos tomando los campos llamados PO10(poblacion) y STOPID(parada de camiones)
with data.SearchCursor (interseccion,["POP10","STOPID", "NAME"]) as cursor:
    #por cada fila agragamos al diccionario
     for fila in cursor:
         stop_id= fila[1]
         pop10=fila[0]
         name = fila[2]
         #verificar si la parada ya existe en el diccionario
         if stop_id not in interseccion_datos.keys():
            #si no existe en el diccionario lo agreegamos
          interseccion_datos[stop_id] = [pop10]
         else:
         #si ya estava en el dicc entonces solo agregar el POP10
            interseccion_datos[stop_id].append(pop10)


print "informacion del diccionario: "
print interseccion_datos
#generara el archivo Csv a partir de la interseccion de datos
with open(resultado_csv, 'wb') as archivo_csv:
    csvwriter = csv.writer(archivo_csv, delimiter = ',')
    csvwriter.writerow(['STOPID','PROMEDIO','Nombre autobus'])
    #por cada llave en el diccionario interseccion
    for i in interseccion_datos.keys():
        #obtener lista de paradas y la poblacion
        pop10_list = interseccion_datos[i]
        #calacular el promedio de la lista
        promedio = sum(pop10_list) / len(pop10_list)
        #crear lista con los datos para el CSV en la lista
        #EXTRAER EL NOMBRE DEL STOPID DE LA CAPA BUSSTOPS
        nombre_parada_autobus =""
        with arcpy.da.SearchCursor(parada_autobuses,["STOPID", "BUS_SIGNAG"]) as cursor:
          for fila in cursor:
            #si la variable i es igual a la columna stop id entonce exraemos bus sinag
             if fila[0]== i:
                nombre_parada_autobus = cursor[1]
                break
        csvwriter.writerow([i, promedio, nombre_parada_autobus])
print "Archivo csv generado ☜(ﾟヮﾟ☜)"
arcpy.AddMessage("Archivo csv generado 1 ☜(ﾟヮﾟ☜)")