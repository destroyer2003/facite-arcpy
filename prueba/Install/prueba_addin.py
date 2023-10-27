import threading
import functools

import arcpy
import pythonaddins
import webbrowser

class HerramientaClass(object):
    """Implementation for Herramienta.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        #pythonaddins.MessageBox("x: "+ str (x)+ "y: "+ str (y), "Coordenadas")
        try:
            coordenada_x= x
            coordenada_y= y
           #obtener la referencia a las capas de nuestro mapa en arcmap
            mapa_mxd = arcpy.mapping.MapDocument("CURRENT")

            #obtener referencia a la vista del mapa
            vista_mapa =mapa_mxd.activeView

            #generar una referencia espacial para la vista activa
            referencia_espacial= arcpy.mapping.ListDataFrames(mapa_mxd)[0].spatialReference

            #generar un punto para extraer las coordenas en grados
            punto = arcpy.Point(coordenada_x,coordenada_y)
            #asignarle una referencia espacial al punto
            punto_referenciado = arcpy.PointGeometry(punto, referencia_espacial)
            referencia_espacial_grados = arcpy.SpatialReference(4326)
            #extraer las coordenadas en grados del punto referenciado
            coordenadas = punto_referenciado.projectAs(referencia_espacial_grados)
            x_coord = float(coordenadas.firstPoint.X)
            y_coord = float(coordenadas.firstPoint.Y)
            url = "http://maps.google.com/?cbll={0},{1}&cbp=12,90,0,0,5&layer=c".format(y_coord,x_coord)
           #ejecutar el navegador en segudo plano para que no cuierre arcmap
            def ejecutar_proceso(function):
                @functools.wraps(function)
                def fn (*args, **kwargs):
                    tarea = threading.Thread(target=function, args=args, kwargs=kwargs)
                    tarea.start()
                    tarea.join()
                return fn
            Navegador = ejecutar_proceso(webbrowser.open)
            Navegador(url,new=2)


            print (url)
            arcpy.AddMessage(url)
        except Exception as e:
            pythonaddins.MessageBox(e.message, "Error")

#coordenadas en grados



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
        pass