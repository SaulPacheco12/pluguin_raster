def name():
    return "Raster"

def author():
    return "Efren Garcia Reyes"

def authorName():
    return author()

def email():
    return "egarciar021@alumno.uaemex.mx"

def description():
    return "raster"

def about():
    return "Raster"

def version():
    return "0.0.1"

def qgisMinimunVersion():
    return "3.0"

def icon():
    return "raster.png"

def category():
    return "Raster"

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)