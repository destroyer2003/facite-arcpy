#_*_ coding: utf-8 _*_

import csv
ubicacion_archivo = 'csv/data_estados.csv'
datos= {}
total_localidades = 0
with open(ubicacion_archivo, mode='r') as archivo:
    datos = csv.DictReader(archivo)


#imprime los datos en diccionario
    for estado in datos:
        if estado['CVE_ENT'] == "25" and estado ['CVE_MUN'] == '018':
            print estado ['NOM_ENT'] + " _ "+ estado ['NOM_MUN']+ " _ "+ estado ['NOM_LOC'] + "🎈 Cordenadas: (" + " _ "+ estado ['LAT_DEC']+ " , "+ estado ['LON_DEC'] +")"
            total_localidades += 1
    print "total de localidades del csv ಥ_ಥ:" + str(total_localidades)


