import arcpy
import pythonaddins

class HerramientaClass(object):
    """Implementation for Herramienta.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pythonaddins.MessageBox("x: "+ str (x)+ "y: "+ str (y), "Coordenadas")
        coordenada_x= x
        coordenada_y= y
       #obtener la referencia a las capas de nuestro mapa en arcmap
        mapa_mxd = arcpy.mapping.MapDocument("CURRENT")

        #obtener referencia a la vista del mapa
        vista_mapa =mapa_mxd.activeView

        #generar una referencia espacial para la vista activa
        referencia_espacial= arcpy.mapping.ListDataFrames(mapa_mxd)[0].spatialReference
        #obtener el codigo de la referencia espacial
        codigo_referencia_espacial=referencia_espacial.factoryCode
        #generar un punto para extraer las coordenas en grados
        punto = arcpy.Point(coordenada_x,coordenada_y)
        #asignarle una referencia espacial al punto
        punto_referenciado = arcpy.PointGeometry(punto, codigo_referencia_espacial)
        #extraer las coordenadas en grados del punto referenciado
        coordenadas = punto_referenciado.projectAs(4326)
#coordenadas en grados
        pythonaddins.MessageBox("Lat: " + str(coordenadas.firstpoint.X)+ "Lon: " + str(coordenadas.firstpoint.Y), "Coordenadas en grados")

        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
      #  pythonaddins.MessageBox("Hola", "Herramienta")
        pass
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass

class SaludarClass(object):
    """Implementation for saludar.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
         pythonaddins.MessageBox("Hola", "saludo")