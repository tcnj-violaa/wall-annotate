from breezypythongui import EasyFrame
from breezypythongui import EasyCanvas
from tkinter import PhotoImage, E, W
import sys


class MapCanvas(EasyCanvas):
    def __init__(self, parent):
        EasyCanvas.__init__(self, parent)
        self._items = list()

    def mousePressed(self, event):
        self.drawText("("+str(event.x)+", "+str(event.y)+")",
                 event.x, event.y, fill = "black")
        self._x0 = event.x
        self._y0 = event.y

    def mouseReleased(self, event):
        if self._x0 != event.x and self._y0 != event.y:
            rect = self.drawRectangle(self._x0, self._y0, event.x, event.y,
                    fill = "green")
            self.drawText("("+str(event.x)+", "+str(event.y)+")",
                 event.x, event.y, fill = "black")
            self._items.append(rect)


    #def mouseMoved(self, event):
    #    self.drawLine((event.x-100), (event.y-100) , event.x, event.y,
    #            fill = "black",
    #            width = 3)

class WallAnnotate(EasyFrame):
    """Currently, displays an image on a canvas and allows you to draw
    rectangles on it with a click-and-drag motion. Where you first click defines
    the first corner, and where you release your click defines the opposite
    corner."""

    def __init__(self):
        """Sets up the window and the image."""
        EasyFrame.__init__(self, title = "Wall Annotator")

        #Supply the program with a valid image file as an argument.
        self.map = PhotoImage(file = sys.argv[1]) 
        imwid = self.map.width()
        imhig = self.map.height()

        #self.mapCanvas = self.addCanvas(canvas = MapCanvas(self))
        self.mapCanvas = self.addCanvas(canvas = MapCanvas(self))
        self.mapCanvas.config(width = imwid, height = imhig)
        self.mapCanvas.drawImage(self.map, imwid/2, imhig/2)


        #imageLabel = self.addLabel(text = "", row = 2, column = 0, sticky = W)

        #self.map = PhotoImage(file = "input/annotate_top.png")
        #imageLabel["image"] = self.map
        


WallAnnotate().mainloop()
