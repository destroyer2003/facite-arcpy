#_*_ coding: utf-8 _*_
import arcpy   #libreria de arcgis
from arcpy import da as data
import csv      #libreria para generar CSV


#permitir sobreescribir los archivos existentes
arcpy.env.overwriteOutput = True

#archivo de entrada
parada_autobuses = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Bus_Stops"
censo = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\CensusBlocks2010"
seleccion_paradas = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpyejercicios\RECURSOS\Data\SanFrancisco.gdb\seleccion"

#archivos generados
interseccion = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\InterseccionesCenso"
buffer = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Buffer"

'''
#seleccionar Bus stops que coincidan con el name 14 OB y el bus_signan Lowell st.
arcpyejercicios.Select_analysis(parada_autobuses, seleccion_paradas,  "NAME = '14 OB' AND BUS_SIGNAG = 'Lowell St.'")
print "Seleccion Finalizada (●'◡'●)"
#HACER BUFFER DE 100 MTRS
arcpyejercicios.Buffer_analysis(seleccion_paradas, buffer,  "100 Meters")
print "Buffer Finalizado ^_^"
# hacer interseccion de census block con el buffer
arcpyejercicios.Intersect_analysis([censo, buffer], interseccion )
print "Interseccion Finalizada ಥ_ಥ"
'''
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
