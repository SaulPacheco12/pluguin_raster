import os 
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .raster import interfaz
class mainMenu:
    def __init__(self,iface):
        self.iface = iface

    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle("Raster")
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.IMenu)
        self.IMenuBar = self.iface.addToolBar("Raster")

        self.ejemploRaster = QAction(QIcon(""),"Datos", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemploRaster)
        self.ejemploRaster.triggered.connect(self.startInterfaz)

    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
        layers = QgsProject.instance().mapLayers().values() 
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType()== QgsWkbTypes.PolygonGeometry:
                vLayer = layer
            if layer.type()==QgsRasterLayer.RasterLayer:
                rLayer = layer
                self.dialogo.ui.comboBox.addItem(rLayer.name())
                epsg = rLayer.crs()
                self.dialogo.ui.label_3.setText(str(epsg.authid()))
                Alto = rLayer.height()
                ext = rLayer.extent()
                pixelsixeX = rLayer.rasterUnitsPerPixelX()
                pixelsixeY = rLayer.rasterUnitsPerPixelY()
                xmin = ext.xMinimum()
                xmax = ext.xMaximum()
                ymin = ext.yMinimum()
                ymax = ext.yMaximum()
                
                self.dialogo.ui.TXedit.setText('Alto' ' ' + str(Alto) 
                + 'Coordenadas' ' ' + str(ext) +
                'Tamaño Pixel X' ' ' + str(pixelsixeX) 
                + 'Tamaño Pixel Y' ' ' + str(pixelsixeY) 
                + 'Xmin' ' ' + str(xmin)+
                'Ymin' ' ' + str(ymin) 
                + 'Xmax' ' ' + str(xmax) 
                + 'Ymax' ' ' + str(ymax))
                
                
    def unload(self):
            QgsApplication.processingRegistry().removeProvider(self.provider)    
    