#_*_ coding: utf-8 _*_
import arcpy
import csv
arcpy.env.overwriteOutput  = True

#archivos de trabajo con los que trabajaremos
municipios = r"C:\Users\FOTO_06\Documents\MUNICIPIOS\muni_2018gw\muni_2018gw.shp"
municipios_csv = r"C:\Users\FOTO_06\Documents\MUNICIPIOS\muni_2018gw\municipios.csv"

#crear una capa del shape de municipios
arcpy.MakeFeatureLayer_management(municipios,"municipios_capa")
#contar cuantos elementos tiene la tabla de atributos de la capa atributos
total_muni = arcpy.GetCount_management("municipios_capa")[0]

print (total_muni)

#creamos un ciclo para recorrer todod los municiipios de la capa
for i in range (0,int(total_muni)):
    #consulta SQL para extraer la informacion de la fila que coincida con la i
    FID ="FID =" + str(i)
    #seleccionar el poligono quer couicida
    seleccionado = arcpy.SelectLayerByAttribute_management("municipios_capa","NEW_SELECTION", FID)
    #EXTRAER EL NOMBRE DEL MUNICIPIO SELECCIONADO
    for columna in arcpy.da.SearchCursor(seleccionado, ["NOM_MUN", "NOM_ENT"]):
        nombre_municipio = columna[0].encode("utf-8")
        nombre_estado = columna [1].encode("utf-8")
        print ("{0} - Estado: {1} ---------Municipio:{2}".format(i,nombre_estado,nombre_municipio))
