from tkinter import *
import sys

class WallAnnotate(Frame):
    ###################################################################
    ###### Event callbacks for THE CANVAS (not the stuff drawn on it)
    ###################################################################
    def mouseDown(self, event):
        # remember where the mouse went down
        self.lastx = event.x
        self.lasty = event.y
        self.item = self.draw.create_line(self.lastx, self.lasty, event.x, event.y)

    def mouseMove(self, event):
        # whatever the mouse is over gets tagged as CURRENT for free by tk.
        #self.draw.move(CURRENT, event.x - self.lastx, event.y - self.lasty)
        print(event.x, event.y, self.lastx, self.lasty)
        #self.lastx = event.x
        #self.lasty = event.y
        self.draw.delete(self.item)
        self.item = self.draw.create_rectangle(self.lastx, self.lasty, event.x, event.y)
    
    def mouseRelease(self, event):
        ##Code here
        self.draw.delete(self.item)
        self.rect = self.draw.create_rectangle(self.lastx, self.lasty, event.x, event.y, 
                outline="green", fill="green")
        ##Add to list


    ###################################################################
    ###### Event callbacks for canvas ITEMS (stuff drawn on the canvas)
    ###################################################################
    #def mouseEnter(self, event):
        # the CURRENT tag is applied to the object the cursor is over.
        # this happens automatically.
    #    self.draw.itemconfig(CURRENT, fill="red")

    #def mouseLeave(self, event):
        # the CURRENT tag is applied to the object the cursor is over.
        # this happens automatically.
   #     self.draw.itemconfig(CURRENT, fill="blue") '''

    def createWidgets(self):
        self.map = PhotoImage(file = sys.argv[1])
        imwid = self.map.width()
        imhig = self.map.height()

        #self.QUIT = Button(self, text='QUIT', foreground='red',
        #                   command=self.quit)
        #self.QUIT.pack(side=LEFT, fill=BOTH)

        self.draw = Canvas(self, width=imwid, height=imhig)
        self.draw.config(width = imwid, height = imhig)
        self.draw.pack(side=LEFT)

        self.draw.create_image(0, 0, anchor=NW, image=self.map)

#        fred = self.draw.create_oval(0, 0, 20, 20,
#                                     fill="green", tags="selected")

#        self.draw.tag_bind(fred, "<Any-Enter>", self.mouseEnter)
#        self.draw.tag_bind(fred, "<Any-Leave>", self.mouseLeave) """

        Widget.bind(self.draw, "<1>", self.mouseDown)
        Widget.bind(self.draw, "<B1-Motion>", self.mouseMove)
        Widget.bind(self.draw, "<ButtonRelease-1>", self.mouseRelease)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()

test = WallAnnotate()
test.mainloop()
