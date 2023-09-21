#importar el archivo estados para usar la clase estado
#import clases.estados
from clases.estados import estados
import webbrowser

#creamos el primer estado (sinaloa)
sinaloa = estados()
#vamos a asignarle valores al estado de sinaloa
sinaloa.clave = 25
sinaloa.nombre = "SINALOA"
sinaloa.poblacion= 3027000


#ejecutar la funcion de poblacion para obtener total
sinaloa.obtener_poblacion()


#creamos estado usando constructor
durango = estados(34, "DURANGO", 0,0, 654876)
durango.obtener_poblacion()

#establecerle ubucacion a sinaloa y durango, enlace maps

sinaloa.establecer_ubicacion("25.69983", "-107.87211")
url = sinaloa.obtener_enlace_google_maps()
print url
#abrir el navegaro automaticamente
webbrowser.open(url)
durango.establecer_ubicacion("24.05718","-104.53320")
webbrowser.open(durango.obtener_enlace_google_maps())