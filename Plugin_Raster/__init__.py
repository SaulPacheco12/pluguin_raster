def name():
    return "Raster"

def author():
    return "Saúl Pacheco Molina"

def authorName():
    return author()
def email():
    return author()
def email():
    return "psaul1325@gmail.com"
def descrption():
    return "raster"

def about():
    return "raster"

def version():
     return "0.0.1"
def qgisMinimumVersion():
    return "3.0"
def icon():
    return "Raster.png"

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)
    