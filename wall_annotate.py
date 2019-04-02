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

        #print(event.x, event.y, self.lastx, self.lasty)
        if self._mode == 1:
            # self.lastx = event.x
            # self.lasty = event.y
            self.draw.delete(self.item)
            self.item = self.draw.create_rectangle(self.lastx, self.lasty, event.x, event.y,
                    dash=(3, 5))



    def mouseRelease(self, event):
    #If in drawing mode
        if self._mode == 1:

            self.draw.delete(self.item)
            new_rect = self.draw.create_rectangle(self.lastx, self.lasty, event.x, event.y,
                                               outline="green", fill="green", tags="selected")


            drawn_rect = self.draw.find_closest(event.x, event.y)

            listbox_text = str(self._all_rect_history) + " " + str(self.lastx) + " " + str(self.lasty) + " "
            listbox_text += str(event.x) + " " + str(event.y)

            self._rect_tracker[drawn_rect] = (self._all_rect_history, listbox_text)

            self.rect_list.insert(self._all_rect_history+1, listbox_text)

            self._count += 1
            self._all_rect_history += 1

            #print(self._count)
            #print(self._all_rect_history)
            #print(self._rect_tracker)
            
        
    def clickOnRect(self, event):
        curr_rect = self.draw.find_closest(event.x, event.y)
        track_listbox = self.rect_list.get(0, END)

        if self._mode == 0:

            #Find the index of the element in the listbox that has a matching
            # ID.
            iter_index = 1
            for item in track_listbox[1:]:

                if int(item.split()[0]) == self._rect_tracker[curr_rect][0]:
                    self.rect_list.activate(iter_index)
                    break

                iter_index += 1

        #If in delete mode, do the same but delete the entry instead of
        #selecting it.
        if self._mode == 2:

            iter_index = 1
            for item in track_listbox[1:]:

                if int(item.split()[0]) == self._rect_tracker[curr_rect][0]:
                    print("Deleting from listbox...")
                    self.rect_list.delete(iter_index)
                    break

                iter_index += 1

            #print("Deleting rectangle")
            self.draw.delete(curr_rect)
            del self._rect_tracker[curr_rect]

            self._count -= 1

        #text.insert(INSERT, count)
        ##Add to list

    ###################################################################
    ###### Event callbacks for canvas ITEMS (stuff drawn on the canvas)
    ###################################################################
    def mouseEnter(self, event):
    # the CURRENT tag is applied to the object the cursor is over.
    # this happens automatically.
        if self._mode == 2:
            self.draw.itemconfig(CURRENT, fill="red", outline="red")

    def mouseLeave(self, event):
    # the CURRENT tag is applied to the object the cursor is over.
    # this happens automatically.
        if self._mode == 2:
            self.draw.itemconfig(CURRENT, fill="green", outline="green")

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

        B = Button(self, text="Normal Mode", command=lambda: [self.normalCursor(), self.setMode(0)])
        if self._mode == 0: #Normal selection mode
            self.normalCursor()
        if self._mode == 1: #Drawing mode
            self.changeCursorSprayCan()
        B.grid(column = 11, row = 0)

        C = Button(self, text="Drawing Mode", command=lambda:[self.drawCursor(), self.setMode(1)])
        C.grid(column = 11, row = 1)

        D = Button(self, text="Delete Mode", command=lambda:[self.deleteCursor(), self.setMode(2)])
        D.grid(column = 11, row = 2)

        test_list = StringVar()
        self.rect_list = Listbox(self, listvariable = test_list)

        self.rect_list.grid(column = 11, row = 3)

        self.rect_list.insert(END, 'ID  x1  y1  x2  y2')

        Widget.bind(self.draw, "<1>", self.mouseDown)
        Widget.bind(self.draw, "<B1-Motion>", self.mouseMove)
        Widget.bind(self.draw, "<ButtonRelease-1>", self.mouseRelease)
        self.draw.tag_bind("selected", "<Any-Enter>", self.mouseEnter)
        self.draw.tag_bind("selected", "<Any-Leave>", self.mouseLeave) 
        self.draw.tag_bind("selected", "<1>", self.clickOnRect)

    def setMode(self, x):
        self._mode = x

    def drawCursor(self):
        self.config(cursor = "crosshair")
        #self.setMode(1)

    def normalCursor(self):
        self.config(cursor = "arrow")
        #self._setMode(0)

    def deleteCursor(self):
        self.config(cursor = "pirate")

    def __init__(self, master=None):
        count = 0
        self._count = count
        enable = 0
        self._mode = enable

        self._rect_tracker = {}
        self._all_rect_history = 1

        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()





   # master = Tk()
   # whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
   # msg = Message(master, text=whatever_you_do)
   # msg.config(bg='lightgreen', font=('times', 24, 'italic'))
   # msg.bind('<Button-1>', motion)
   # msg.pack()
   # mainloop()

wanno = WallAnnotate()

wanno.mainloop()
