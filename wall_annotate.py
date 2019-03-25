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
        # self.draw.move(CURRENT, event.x - self.lastx, event.y - self.lasty)

        print(event.x, event.y, self.lastx, self.lasty)
        if self._enable == 1:
            # self.lastx = event.x
            # self.lasty = event.y
            self.draw.delete(self.item)
            self.item = self.draw.create_rectangle(self.lastx, self.lasty, event.x, event.y,
                    dash=(3, 5))

    def mouseRelease(self, event):

        ##Code here
        if self._enable == 1:

            self.draw.delete(self.item)
            self.rect = self.draw.create_rectangle(self.lastx, self.lasty, event.x, event.y,
                                               outline="green", fill="green")

            listbox_text = str(self._count) + " " + str(self.lastx) + " " + str(self.lasty) + " "
            listbox_text += str(event.x) + " " + str(event.y)

            self.rect_list.insert(self._count+1, listbox_text)

            self._count += 1



        #text.insert(INSERT, count)
        ##Add to list

    ###################################################################
    ###### Event callbacks for canvas ITEMS (stuff drawn on the canvas)
    ###################################################################
    # def mouseEnter(self, event):
    # the CURRENT tag is applied to the object the cursor is over.
    # this happens automatically.
    #    self.draw.itemconfig(CURRENT, fill="red")

    # def mouseLeave(self, event):
    # the CURRENT tag is applied to the object the cursor is over.
    # this happens automatically.
    #     self.draw.itemconfig(CURRENT, fill="blue") '''

    def createWidgets(self):
        self.map = PhotoImage(file=sys.argv[1])
        imwid = self.map.width()
        imhig = self.map.height()

        # self.QUIT = Button(self, text='QUIT', foreground='red',
        #                   command=self.quit)
        # self.QUIT.pack(side=LEFT, fill=BOTH)

        self.draw = Canvas(self, width=imwid, height=imhig)
        self.draw.config(width=imwid, height=imhig)
        self.draw.grid(column=0, columnspan=10, rowspan=8)

        self.draw.create_image(0, 0, anchor=NW, image=self.map)

        #        fred = self.draw.create_oval(0, 0, 20, 20,
        #                                     fill="green", tags="selected")

        #        self.draw.tag_bind(fred, "<Any-Enter>", self.mouseEnter)
        #        self.draw.tag_bind(fred, "<Any-Leave>", self.mouseLeave) """

        B = Button(self, text="Mouse cursor", command=lambda: [self.normalCursor(), self.setEnable(0)])
        if self._enable == 0:
            self.normalCursor()
        if self._enable == 1:
            self.changeCursorSprayCan()
        B.grid(column = 11, row = 0)

        C = Button(self, text="Drawing cursor", command=lambda:[self.changeCursorSprayCan(), self.setEnable(1)])
        C.grid(column = 11, row = 1)

        test_list = StringVar()
        self.rect_list = Listbox(self, listvariable = test_list)

        self.rect_list.grid(column = 11, row = 3)

        self.rect_list.insert(0, '#  x1  y1  x2  y2')

        Widget.bind(self.draw, "<1>", self.mouseDown)
        Widget.bind(self.draw, "<B1-Motion>", self.mouseMove)
        Widget.bind(self.draw, "<ButtonRelease-1>", self.mouseRelease)

        # getter method

    # def get_age(self):
    # return self._counter

    # setter method

    # def set_age(self, x):
    #    self._counter = x

    def setEnable(self, x):
        self._enable = x

    def changeCursorSprayCan(self):
        self.config(cursor = "crosshair")
        #self.setEnable(1)

    def normalCursor(self):
        self.config(cursor = "arrow")
        #self._setEnable(0)

    def __init__(self, master=None):
        count = 0
        self._count = count
        enable = 0
        self._enable = enable
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()

wanno = WallAnnotate()

wanno.mainloop()
