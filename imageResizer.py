#! Reduces the image by half it's size given its file path. 
from win32com.client import Dispatch

app = Dispatch("Photoshop.Application")
# Setting units to pixels
app.Preferences.RulerUnits = 1

def resizer(filepath):
    # Open an existing file
    doc = app.Open(filepath)
    w = int(doc.width)
    h = int(doc.height)
    # newLayer = doc.Artlayers.Add()
    # psNormalLayer = 1
    #
    # newLayer.kind = psNormalLayer
    # newLayer.rgb.hexValue = "ff0000" # ???

    print("Original size: Height %s px, width %s px" % (w, h))
    doc.ResizeImage(w*2, h*2) # Resize to 50%
    doc.Save()

x = input("Provide a file path")
resizer(x)
# When accepting input in console, don't need to include quotes since Python is already expecting a string and it will end up double-quoted
# "C:\\Users\\Jennifer\\Documents\\4. COMPSCI\\pythonScripts\\doge.jpg"

# TODO: Have this loop through all the files in a directory
