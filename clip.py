# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# clip.py
# Created on: 2023-09-21 16:52:56.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Sinaloa_project_shp = "C:\\Users\\17077\\Documents\\Series_M_Alejandra\\Sinaloa_project.shp"
terreno_shp = "C:\\Users\\17077\\Documents\\Series_M_Alejandra\\terreno.shp"
Recorte_shp = "C:\\Users\\17077\\Documents\\Series_M_Alejandra\\Recorte.shp"

# Process: Clip
arcpy.Clip_analysis(Sinaloa_project_shp, terreno_shp, Recorte_shp, "")
