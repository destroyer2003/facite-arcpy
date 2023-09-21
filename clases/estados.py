#_*_ coding: utf-8 _*_

class estados:  #clase
    # constructor
    def __init__(self,clave=0, nombre="", lat=0, lon=0, poblacion=0,):
        self.clave  = clave
        self.nombre  = nombre
        self.lon = lon
        self.lat = lat
        self.poblacion = poblacion

    #funcion que nos retorna total de la póblacion del estado
    def obtener_poblacion(self):
        print "la poblacion del estado de "+ self.nombre+" es de "+ str(self.poblacion)+ " habitantes"
        return self.poblacion
    def establecer_ubicacion(self, latitud, longitud):
        self.lat = latitud
        self.lon = longitud
        print "Se etablecio la ubicacion del estado correctamente"

    def obtener_enlace_google_maps(self):
        enlace = "https://www.google.com/maps/@"+self.lat +","+self.lon+",9z?entry=ttu"
        return enlace
