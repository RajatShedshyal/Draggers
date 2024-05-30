from tkinter import *
import time
import threading
import tkinter.ttk as t
from PIL import ImageTk, Image

# save clicked rajat
# LEGEND:
#   1."  *  " indicates that it is a required argument
#   2." {!} " indicates that its Complex and differnet
#   3." []  " indicates all the arguments
#   4." ()  " indicates the use or gives info
#   5."  I  " Roman Nums indicate available functions
#   6."// or //*" shows note for the following line
#
# INDEX:
#
# 1. Main
#   [args = None]
#   (Main Class is used for dragging)
#
#
# 2. Quad
#   [args = window*, name, color, length, width, placex, placey, text, font, size]
#   (Quad stands for Quadrilateral, This Class is used to make Object Boxes with Text)
#   Functions:-
#       I.create() //Creates the Following Widget
#
# 3.QuadA{!}
#   [args = window*, name, color, placex, placey]
#   (QuadA stands for Quadrilateral Advanced, This Class is Similiar to that of Quad but
#   you should send sepreate agruments for create  and can change the class arguments,
#   for example:- [args for function create: text, font, size, change_color]
#
#   quada = QuadA(window)
#   quada.create(text='Rajat', font='Cosmic San MS', size=25, change_color='green')
#   )
#   Functions:-
#       I.create() //Creates the Following Widget
#
# 4.Image
#   [args= window*, path*, name=, placex, placey, text] //* pass the path or file directory of image
#   (Image is used to create widget with a Image and text is displayed below the Image)
#   Functions:-
#       I.create() //Creates the Following Widget
#
# 5.Circle
#   [args= window*, path*, name, fontcolor, placex, placey, text, fontname, size, bg]
#   (Creates a Circle Image with a Text)
#   Functions:-
#       I.create() //Creates the Following Widget
#       II.double_drag_start() //Function is for Dragging and is used internally in class
#       III.double_drag_motion() //Function is for Dragging and is used internally in class
#

# Task Related
total_task = 0
task_completed = 0

# Save Objects Co. Related

circle_list = []
circle_curindex = 0
circle_firsttime = True

imageobj_list = []
imageobj_curindex = 0
imageobj_firsttime = True

shapeless_list = []
shapeless_curindex = 0
shapeless_firsttime = True

quadf_list = []
quadt_list = []
quad_curindex = 0
quad_firsttime = True

class Main:

    def __init__(self, window, placex=0, placey=0):
        self.window = window
        self.placex = placex
        self.placey = placey

    def create(self):
        global bar, percenta
        bar = t.Progressbar(self.window, orient=HORIZONTAL, length=200)
        bar.place(x=self.placex, y=self.placey)
        if total_task == 0:
            percenta = Label(self.window, text=f'Progress: 0%', bg='#009BFF', fg='white')
            percenta.place(x=self.placex + 55, y=self.placey + 24)
        else:
            percenta = Label(self.window, text=f'Progress: {int(task_completed/total_task)}%')
            percenta.place(x=self.placex + 55, y=self.placey + 24)

    def add(self):
        global total_task, task_completed
        if total_task == 0:
            bar['value'] = 0
            self.window.update_idletasks()
            percenta.config(text=f'Progress: 0%')
            percenta.update()
        else:
            if bar['value'] < 0:
                bar['value'] = 0
            if bar['value'] > 100:
                bar['value'] = 100
            bar['value'] += (1 / total_task) * 100
            self.window.update_idletasks()
            percenta.config(text=f'Progress: {int((task_completed / total_task) * 100)}%')
            percenta.update()

    def remove(self):
        global total_task, task_completed
        if total_task == 0:
            bar['value'] = 0
            self.window.update_idletasks()
            percenta.config(text=f'Progress: 0%')
            percenta.update()
        else:
            if bar['value'] < 0:  # Bcoz while subtracting if it goe below 100 make it 0
                bar['value'] = 0
            if bar['value'] > 100:  # while adding if it becomes more than 100 make it 100
                bar['value'] = 100
            bar['value'] -= (1/total_task) * 100
            self.window.update_idletasks()
            percenta.config(text=f'Progress: {int((task_completed / total_task) * 100)}%')
            percenta.update()

    def drag_start(self, event):
        widget = event.widget
        widget.cur_x = event.x
        widget.cur_y = event.y

    def drag_motion(self, event):
        widget = event.widget
        new_x = widget.winfo_x() - widget.cur_x + event.x
        new_y = widget.winfo_y() - widget.cur_y + event.y
        if new_y + self.name.winfo_height() > self.window.winfo_height() - 85:
            new_y = self.window.winfo_height() - 85 - int(self.name.winfo_height())
        if new_x < 0:
            new_x = 0
        if new_y < 0:
            new_y = 0
        if self.slidebutton_avai == True:
            if new_x + self.name.winfo_width() > self.window.winfo_width():
                new_x = self.window.winfo_width() - self.name.winfo_width()-10
        else:
            if new_x + self.name.winfo_width() > self.window.winfo_width():
                new_x = self.window.winfo_width() - self.name.winfo_width()
        widget.place(x=new_x, y=new_y)
        # Saving Related:
        try:
            quadf_list[widget.quad_curindex] = [new_x, new_y]
        except:
            try:
                shapeless_list[widget.shapeless_curindex] = [new_x, new_y]
            except:
                try:
                    imageobj_list[widget.imageobj_curindex] = [new_x, new_y]
                except:
                    None

        # Canvas Related:
        try:
            if self.slideinfo_opened == True:
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width() + self.maincanvas.winfo_width(),
                                       y=self.name.winfo_y())
                self.maincanvas.destroy()
                self.slidebutton.config(image=self.slideinfoimg)
                self.slideinfo_opened = False
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width(),
                                       y=self.name.winfo_y())
            else:
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width(), y=self.name.winfo_y())
                self.window.update()

        except:
            return None

    # Ulta
    # X --> Y
    # Y --> X
    def drag_ctrlxmotion(self, event):
        widget = event.widget
        new_x = widget.winfo_x() - widget.cur_x + event.x
        new_y = widget.winfo_y() - widget.cur_y + event.y

        if new_y + self.name.winfo_height() > self.window.winfo_height() - 85:
            new_y = self.window.winfo_height() - 85 - int(self.name.winfo_height())
        if new_x < 0:
            new_x = 0
        if new_y < 0:
            new_y = 0
        if self.slidebutton_avai == True:
            if new_x + self.name.winfo_width() > self.window.winfo_width():
                new_x = self.window.winfo_width() - self.name.winfo_width()-10
        else:
            if new_x + self.name.winfo_width() > self.window.winfo_width():
                new_x = self.window.winfo_width() - self.name.winfo_width()

        widget.place(x=widget.winfo_x(), y=new_y)

        # Related to Saving
        try:
            quadf_list[widget.quad_curindex] = [self.name.winfo_x(), new_y]
        except:
            try:
                imageobj_list[widget.imageobj_curindex] = [self.name.winfo_x(), new_y]
            except:
                try:
                    shapeless_list[widget.shapeless_curindex] = [self.name.winfo_x(), new_y]
                except:
                    return None


        # Canvas Related:
        try:
            if self.slideinfo_opened == True:
                self.maincanvas.place(x=self.name.winfo_x() + self.name.winfo_width(), y=new_y)
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width() + self.maincanvas.winfo_width(), y=new_y)
            else:
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width(), y=new_y)

        except:
            None

    def drag_ctrlymotion(self, event):
        widget = event.widget
        new_x = widget.winfo_x() - widget.cur_x + event.x
        new_y = widget.winfo_y() - widget.cur_y + event.y

        if new_y + self.name.winfo_height() > self.window.winfo_height() - 85:
            new_y = self.window.winfo_height() - 85 - int(self.name.winfo_height())
        if new_x < 0:
            new_x = 0
        if new_y < 0:
            new_y = 0
        if self.slidebutton_avai == True:
            if new_x + self.name.winfo_width() > self.window.winfo_width():
                new_x = self.window.winfo_width() - self.name.winfo_width()-10
        else:
            if new_x + self.name.winfo_width() > self.window.winfo_width():
                new_x = self.window.winfo_width() - self.name.winfo_width()

        widget.place(x=new_x, y=widget.winfo_y())

        # Saving Related:
        try:
            quadf_list[widget.quad_curindex] = [new_x, self.name.winfo_y()]
        except:
            try:
                imageobj_list[widget.imageobj_curindex] = [new_x, self.name.winfo_y()]
            except:
                try:
                    shapeless_list[widget.shapeless_curindex] = [new_x, self.name.winfo_y()]
                except:
                    return None

        # Canvas Related:
        try:
            if self.slideinfo_opened == True:
                self.maincanvas.place(x=self.name.winfo_width() + new_x, y=self.maincanvas.winfo_y())
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_width() + self.maincanvas.winfo_width() + new_x, y=self.maincanvas.winfo_y())
            else:
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_width() + new_x, y=self.name.winfo_y())
        except:
            return None

class Quad(Main):

    def __init__(self, window, name='name', bg='pink', length=10, width=5, placex=0, placey=0, text='', font='Arial',
                 size=10, fg='black', task='no', tg='lightblue', def_text=''):
        self.window = window
        self.name = name
        self.color = bg
        self.tg = tg   # Transparent Background, Set this to tg=Mainbg in Main.py
        self.width = length
        self.height = width
        self.placex = placex
        self.placey = placey
        self.text = text
        self.font = font
        self.fg = fg
        self.size = size
        self.task = task
        self.complete = PhotoImage(file='Support/Source/complete.png')
        self.incomplete = PhotoImage(file='Support/Source/incomplete.png')
        self.save = PhotoImage(file='Support/Source/save.png')
        self.clear = PhotoImage(file='Support/Source/clear.png')
        self.compeletewidget = 'complete'
        self.incompeletewidget = 'incomplete'
        self.completecheck = False
        self.slidebutton_avai = True
        self.slideinfoimg = PhotoImage(file='Support/Source/slideinfo.png')
        self.slideinfoimg_opp = PhotoImage(file='Support/Source/slideinfo_opp.png')
        self.slideinfo_opened = False
        self.typo_text = def_text  # def_text = Default text

    def create(self):
        global total_task, quad_curindex, quad_firsttime
        self.name = Label(self.window, bg=self.color, width=10, height=5, text=self.text,
                          font=(self.font, 10), wraplength=81, justify="center", fg=self.fg)
        self.name.place(x=self.placex, y=self.placey)

        # For Index Adding and Excluding first time
        if quad_firsttime == True:
            print(f'quad cur index is 0 curindex: {quad_curindex}')
            quad_curindex = 0
            quad_firsttime = False
        else:
            print(f'Added 1 nd before quad index was:{quad_curindex}')
            quad_curindex += 1

        self.name.quad_curindex = quad_curindex

        if self.task == 'yes':
            global task_completed, total_task

            self.compeletewidget = Label(self.window, image=self.incomplete, bg=self.color)
            self.compeletewidget.place(x=self.placex, y=self.placey)
            total_task += 1
            self.add()
            self.remove()

            if self.completecheck == True:
                self.compeletewidget.config(image=self.complete, bg=self.color)
                task_completed += 1
                self.completecheck = True
                self.add()

    def infostation(self):

        self.maincanvas = Canvas(self.window, width=200, height=250, bg='lightgreen', bd=0, highlightthickness=0)

        def tagi_much(event):
            if self.slideinfo_opened == False:
                self.slideinfo_opened = True
                print(f'Slide Info Opened: {self.slideinfo_opened}')
                # Canvas Modfication:
                maincanvas_bg = '#428dff'
                self.maincanvas = Canvas(self.window, width=300, height=250, bg=maincanvas_bg,
                                         bd=0, highlightthickness=0)
                # self.maincanvas.lower(0)
                # Adding widgets

                #Border
                self.maincanvas.create_line(5, 5, 295, 5, fill='black', width=3)
                self.maincanvas.create_line(295, 5, 295, 245, fill='black', width=3)
                self.maincanvas.create_line(295, 245, 5, 245, fill='black', width=3)
                self.maincanvas.create_line(5, 245, 5, 5, fill='black', width=3)
                # Headline
                let_in_text = 0
                for i in self.text:
                    let_in_text += 1
                if let_in_text <= 9:
                    self.maincanvas.create_rectangle(65, 15, 240, 45, fill=maincanvas_bg)
                    self.maincanvas.create_text(160, 30, text=self.text, font=(self.font, 20, 'bold'), fill='black')
                elif let_in_text <= 12:
                    self.maincanvas.create_rectangle(35, 15, 265, 45, fill=maincanvas_bg)
                    self.maincanvas.create_text(160, 30, text=self.text, font=(self.font, 20, 'bold'), fill='black')
                else:
                    self.maincanvas.create_rectangle(15, 15, 285, 45, fill=maincanvas_bg)
                    self.maincanvas.create_text(155, 30, text=self.text[0:14], font=(self.font, 20, 'bold'), fill='black')

                # Typing area

                text_saved = False

                def typing(event):
                    self.maincanvas.create_rectangle(57, 225, 110, 240, fill=maincanvas_bg, width=0)
                    self.maincanvas.create_text(59, 225, text='Typing..', anchor='nw', font=(self.font, 10))

                def store_text(event):
                    global total_task, quad_curindex, quad_firsttime, text_saved
                    self.typo_text = str(self.typo.get("1.0", END))
                    for i in range(0, quad_curindex+1):
                        quadt_list.append(i)
                    quadt_list[self.name.quad_curindex] = self.typo_text
                    self.maincanvas.create_rectangle(57, 225, 110, 243, fill=maincanvas_bg, width=0)
                    self.maincanvas.create_text(59, 225, text='Saved', anchor='nw', font=(self.font, 10))

                def rem_text(event):
                    self.typo.delete("1.0", END)
                    global total_task, quad_curindex, quad_firsttime, text_saved
                    self.typo_text = str(self.typo.get("1.0", END))
                    for i in range(0, quad_curindex + 1):
                        quadt_list.append(i)
                    quadt_list[self.name.quad_curindex] = self.typo_text
                    self.maincanvas.create_rectangle(57, 225, 110, 243, fill=maincanvas_bg, width=0)
                    self.maincanvas.create_text(59, 225, text='Idle', anchor='nw', font=(self.font, 10))

                self.typo = Text(self.window, bg='#FFA600', font=(self.font, 10), wrap=WORD, fg='black')
                self.typo_window = self.maincanvas.create_window(15, 50, width=270, height=175, anchor='nw',
                                                                 window=self.typo)
                self.typo.insert('1.0', self.typo_text)
                self.typo.bind('<Control-s>', store_text)
                self.typo.bind('<Return>', store_text)
                self.typo.bind('<Key>', typing)

                self.save_img = Label(self.window, image=self.save, bg=maincanvas_bg)
                self.save_img_window = self.maincanvas.create_window(267, 225, anchor='nw', window=self.save_img)
                self.save_img.bind("<Button-1>", store_text)

                self.clear_img = Label(self.window, image=self.clear, bg=maincanvas_bg)
                self.clear_img_window = self.maincanvas.create_window(247, 225, anchor='nw', window=self.clear_img)
                self.clear_img.bind("<Button-1>", rem_text)

                self.maincanvas.create_text(15, 225, text='Status: ', anchor='nw', font=(self.font, 10))
                self.maincanvas.create_text(59, 225, text='Idle', anchor='nw', font=(self.font, 10))

                # Canvas Modification Ends.
                self.window.update()
                self.maincanvas.subnew_x = self.name.winfo_x() + self.name.winfo_width()
                self.maincanvas.subnew_y = self.name.winfo_y()
                self.maincanvas.place(x=self.maincanvas.subnew_x, y=self.maincanvas.subnew_y)
                self.window.update()
                self.slidebutton.config(image=self.slideinfoimg_opp)
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width() + self.maincanvas.winfo_width(), y=self.name.winfo_y())
                self.window.update()
            else:
                self.slideinfo_opened = False
                print(f'Slide Info Opened: {self.slideinfo_opened}')
                self.maincanvas.destroy()
                self.window.update()
                self.slidebutton.config(image=self.slideinfoimg)
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width(), y=self.name.winfo_y())

        # slide button related
        self.slidebutton = Label(self.window, image=self.slideinfoimg, bg=self.tg, bd=0, highlightthickness=0)
        self.window.update()
        self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width(), y=self.name.winfo_y())
        self.slidebutton.bind("<Button-1>", tagi_much)
        self.window.update()

    def work(self):

        def double_drag_start(event):
            self.window.update()
            self.name.cur_x = event.x
            self.name.cur_y = event.y
            self.compeletewidget.cur_x = event.x
            self.compeletewidget.cur_y = event.y
            self.window.update()

        def double_drag_motion(event):
            self.window.update()
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            if self.name.new_y + self.name.winfo_height() > self.window.winfo_height()-85:
                self.name.new_y = self.window.winfo_height()-85 - int(self.name.winfo_height())
                self.compeletewidget.new_y = self.window.winfo_height()-85 - 15
            if self.name.new_x < 0:
                self.name.new_x = 0
                self.compeletewidget.new_x = self.name.new_x + 65
            if self.name.new_y < 0:
                self.name.new_y = 0
                self.compeletewidget.new_y = self.name.new_y + 70
            if self.name.new_x + self.name.winfo_width() > self.window.winfo_width():
                self.name.new_x = self.window.winfo_width() - self.name.winfo_width() - 10
                self.compeletewidget.new_x = self.window.winfo_width() - 25
            self.name.place(x=self.name.new_x, y=self.name.new_y)
            self.compeletewidget.place(x=self.name.new_x, y=self.name.new_y)
            self.window.update()

            # Menu Related
            if self.slideinfo_opened == True:
                self.maincanvas.destroy()
                self.slidebutton.config(image=self.slideinfoimg)
                self.slideinfo_opened = False
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width(),
                                       y=self.name.winfo_y())
                self.window.update()
            else:
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width(), y=self.name.winfo_y())
                self.window.update()

            # Related to Saving
            quadf_list[self.name.quad_curindex] = [self.name.new_x, self.name.new_y]

        # Ulta Motions
        # Ctrl --> Y
        # Shift --> X

        def double_drag_ctrlxmotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.name.place(x=self.name.winfo_x(), y=self.name.new_y)

            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.compeletewidget.place(x=self.compeletewidget.winfo_x(), y=self.compeletewidget.new_y)

            # Related to Saving
            quadf_list[self.name.quad_curindex] = [self.name.winfo_x(), self.name.new_y]

            # Menu Related
            if self.slideinfo_opened == True:
                self.maincanvas.place(x=self.name.winfo_x() + self.name.winfo_width(), y=self.name.new_y)
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width() + self.maincanvas.winfo_width(),
                                       y=self.name.new_y)
            else:
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_x() + self.name.winfo_width(), y=self.name.new_y)

        def double_drag_shiftymotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.name.place(x=self.name.new_x, y=self.name.winfo_y())
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.compeletewidget.place(x=self.compeletewidget.new_x, y=self.compeletewidget.winfo_y())

            # Related to Saving
            quadf_list[self.name.quad_curindex] = [self.name.new_x, self.name.winfo_y()]

            # Menu Related
            if self.slideinfo_opened == True:
                self.maincanvas.place(x=self.name.winfo_width() + self.name.new_x, y=self.maincanvas.winfo_y())
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_width() + self.maincanvas.winfo_width() + self.name.new_x,
                                       y=self.maincanvas.winfo_y())
            else:
                self.window.update()
                self.slidebutton.place(x=self.name.winfo_width() + self.name.new_x, y=self.name.winfo_y())


        if self.task == 'yes':

            self.name.bind('<Button-1>', double_drag_start)
            self.name.bind('<B1-Motion>', double_drag_motion)
            self.name.bind('<Control-B1-Motion>', double_drag_ctrlxmotion)
            self.name.bind('<Shift-B1-Motion>', double_drag_shiftymotion)

            # Here sing means Sign
            def task_sing_chnager(event):
                global task_completed
                if self.completecheck == False:
                    self.compeletewidget.config(image=self.complete, bg=self.color)
                    task_completed += 1
                    self.completecheck = True
                    self.add()

                else:
                    self.compeletewidget.config(image=self.incomplete, bg=self.color)
                    task_completed -= 1
                    self.completecheck = False
                    self.remove()

            self.compeletewidget.bind('<Button-1>', task_sing_chnager)

        else:
            self.name.bind('<Button-1>', self.drag_start)
            self.name.bind('<B1-Motion>', self.drag_motion)
            self.name.bind('<Control-B1-Motion>', self.drag_ctrlxmotion)
            self.name.bind('<Shift-B1-Motion>', self.drag_ctrlymotion)

    def dele(self):
        global total_task
        global task_completed
        if self.task == 'yes':
            self.name.destroy()
            self.maincanvas.destroy()
            self.slidebutton.destroy()
            self.compeletewidget.destroy()
            total_task -= 1
            if self.completecheck == True:
                task_completed -= 1
                self.add()
                self.remove()
        else:
            self.name.destroy()
            self.maincanvas.destroy()
            self.slidebutton.destroy()


class Imageobj(Main):

    def __init__(self, window, path, name='name', placex=0, placey=0, text='', bg='white', fg='black', task='no',
                 font='MV Boli', resizea=False, w=1, h=1, tg='lightblue'):
        self.window = window
        self.name = name
        self.path = path
        self.image = PhotoImage(file=self.path)
        self.tg = tg
        self.w = w
        self.h = h
        self.resize_ask = resizea
        self.placex = placex
        self.placey = placey
        self.font = font
        self.text = text
        self.bg = bg
        self.fg = fg
        self.task = task
        self.slidebutton_avai = False
        self.complete = PhotoImage(file='Support/Source/complete.png')
        self.incomplete = PhotoImage(file='Support/Source/incomplete.png')
        self.compeletewidget = 'complete'
        self.incompeletewidget = 'incomplete'
        self.completecheck = False

    def create(self):
        global total_task, imageobj_firsttime, imageobj_curindex, imageobj_list

        if self.resize_ask == False:
            self.name = Label(self.window, image=self.image, text=self.text, compound='top', bg=self.tg, fg=self.fg,
                              font=(self.font, 10), bd=0)
        else:
            self.org_file = Image.open(self.path)
            self.resize = self.org_file.resize((self.w, self.h), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.resize)
            self.name = Label(self.window, image=self.image, text=self.text, compound='top', bg=self.tg, fg=self.fg,
                              font=(self.font, 10))
        self.name.place(x=self.placex, y=self.placey)

        # For Index Adding and Excluding first time
        if imageobj_firsttime == True:
            imageobj_curindex += 0
            imageobj_firsttime = False
        else:
            imageobj_curindex += 1

        self.name.imageobj_curindex = imageobj_curindex

        if self.task == 'yes':
            global task_completed, total_task

            self.compeletewidget = Label(self.window, image=self.incomplete, bg=self.bg)
            self.compeletewidget.place(x=self.placex + 65, y=self.placey + 70)
            total_task += 1
            self.add()
            self.remove()

            if self.completecheck == True:
                self.compeletewidget.config(image=self.complete, bg=self.bg)
                task_completed += 1
                self.completecheck = True
                self.add()

    def work(self):

        def double_drag_start(event):
            self.name.cur_x = event.x
            self.name.cur_y = event.y
            self.compeletewidget.cur_x = event.x
            self.compeletewidget.cur_y = event.y

        def double_drag_motion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.name.place(x=self.name.new_x, y=self.name.new_y)
            self.compeletewidget.place(x=self.compeletewidget.new_x, y=self.compeletewidget.new_y)
            # Related to Saving
            imageobj_list[self.name.quad_curindex] = [self.name.new_x, self.name.new_y]

        def double_drag_ctrlxmotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.name.place(x=self.name.winfo_x(), y=self.name.new_y)
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.compeletewidget.place(x=self.compeletewidget.winfo_x(), y=self.compeletewidget.new_y)

        def double_drag_shiftymotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.name.place(x=self.name.new_x, y=self.name.winfo_y())
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.compeletewidget.place(x=self.compeletewidget.new_x, y=self.compeletewidget.winfo_y())

        if self.task == 'yes':

            self.name.bind('<Button-1>', double_drag_start)
            self.name.bind('<B1-Motion>', double_drag_motion)
            self.name.bind('<Control-B1-Motion>', double_drag_ctrlxmotion)
            self.name.bind('<Shift-B1-Motion>', double_drag_shiftymotion)

            def task_sing_chnager(event):
                global task_completed
                if self.completecheck == False:
                    self.compeletewidget.config(image=self.complete, bg=self.bg)
                    task_completed += 1
                    self.completecheck = True
                    self.add()
                else:
                    self.compeletewidget.config(image=self.incomplete, bg=self.bg)
                    task_completed -= 1
                    self.completecheck = False
                    self.remove()

            self.compeletewidget.bind('<Button-1>', task_sing_chnager)

        else:
            self.name.bind('<Button-1>', self.drag_start)
            self.name.bind('<B1-Motion>', self.drag_motion)
            self.name.bind('<Control-B1-Motion>', self.drag_ctrlxmotion)
            self.name.bind('<Shift-B1-Motion>', self.drag_ctrlymotion)

    def dele(self):
        global total_task
        global task_completed
        if self.task == 'yes':
            self.name.destroy()
            self.compeletewidget.destroy()
            total_task -= 1
            if self.completecheck == True:
                task_completed -= 1
        else:
            self.name.destroy()


class Circle(Main):

    def __init__(self, window, name='name', fg='black', placex=0, placey=0, text='', font='Arial',
                 size=10, bg='white', task='no'):
        self.window = window
        self.fontcolor = fg
        self.text = text
        self.name = name
        self.placex = placex
        self.placey = placey
        self.file = 'Support/Source/white_circle.png'
        self.hesar = 'name1234'
        self.path = PhotoImage(file=self.file)
        self.fontname = font
        self.size = size
        self.bg = bg
        self.task = task
        self.complete = PhotoImage(file='Support/Source/complete.png')
        self.incomplete = PhotoImage(file='Support/Source/incomplete.png')
        self.compeletewidget = 'complete'
        self.incompeletewidget = 'incomplete'
        self.completecheck = False

    def create(self):
        global total_task, circle_firsttime, circle_curindex, circle_list

        self.name = Label(self.window, image=self.path, bg=self.bg, bd=0, highlightthickness=0)
        self.name.place(x=self.placex, y=self.placey)
        self.hesar = Label(self.window, text=self.text, font=(self.fontname, self.size), fg=self.fontcolor, bg=self.bg)
        self.hesar.place(x=20, y=16)

        # For Index Adding and Excluding first time
        if circle_firsttime == True:
            circle_curindex += 0
            circle_firsttime = False
        else:
            circle_curindex += 1

        self.name.circle_curindex = circle_curindex

        if self.task == 'yes':
            global task_completed, total_task

            self.compeletewidget = Label(self.window, image=self.incomplete, bg=self.bg)
            self.compeletewidget.place(x=self.placex + 65, y=self.placey + 70)
            total_task += 1
            self.add()
            self.remove()

            if self.completecheck == True:
                self.compeletewidget.config(image=self.complete, bg=self.bg)
                task_completed += 1
                self.completecheck = True
                self.add()

    def work(self):

        def pair_drag_start(event):
            self.name.cur_x_p = event.x
            self.name.cur_y_p = event.y
            self.hesar.cur_x_p = event.x
            self.hesar.cur_y_p = event.y

        def pair_drag_motion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x_p + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y_p + event.y
            self.hesar.new_x = self.hesar.winfo_x() - self.hesar.cur_x_p + event.x
            self.hesar.new_y = self.hesar.winfo_y() - self.hesar.cur_y_p + event.y
            self.name.place(x=self.name.new_x, y=self.name.new_y)
            self.hesar.place(x=self.hesar.new_x, y=self.hesar.new_y)
            # Related to Saving
            circle_list[self.name.circle_curindex] = [self.name.new_x, self.name.new_y]
            print('Pair Drag')

        def pair_drag_ctrlxmotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x_p + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y_p + event.y
            self.name.place(x=self.name.winfo_x(), y=self.name.new_y)
            self.hesar.new_x = self.hesar.winfo_x() - self.hesar.cur_x_p + event.x
            self.hesar.new_y = self.hesar.winfo_y() - self.hesar.cur_y_p + event.y
            self.hesar.place(x=self.hesar.winfo_x(), y=self.hesar.new_y)

        def pair_drag_shiftymotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x_p + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y_p + event.y
            self.name.place(x=self.name.new_x, y=self.name.winfo_y())
            self.hesar.new_x = self.hesar.winfo_x() - self.hesar.cur_x_p + event.x
            self.hesar.new_y = self.hesar.winfo_y() - self.hesar.cur_y_p + event.y
            self.hesar.place(x=self.hesar.new_x, y=self.hesar.winfo_y())

        def double_drag_start(event):
            self.name.cur_x = event.x
            self.name.cur_y = event.y
            self.hesar.cur_x = event.x
            self.hesar.cur_y = event.y
            self.compeletewidget.cur_x = event.x
            self.compeletewidget.cur_y = event.y

        def double_drag_motion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.hesar.new_x = self.hesar.winfo_x() - self.hesar.cur_x + event.x
            self.hesar.new_y = self.hesar.winfo_y() - self.hesar.cur_y + event.y
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.name.place(x=self.name.new_x, y=self.name.new_y)
            self.hesar.place(x=self.hesar.new_x, y=self.hesar.new_y)
            self.compeletewidget.place(x=self.compeletewidget.new_x, y=self.compeletewidget.new_y)
            # Related to Saving
            circle_list[self.name.circle_curindex] = [self.name.new_x, self.name.new_y]
            print('Double Drag')

        def double_drag_ctrlxmotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.name.place(x=self.name.winfo_x(), y=self.name.new_y)
            self.hesar.new_x = self.hesar.winfo_x() - self.hesar.cur_x + event.x
            self.hesar.new_y = self.hesar.winfo_y() - self.hesar.cur_y + event.y
            self.hesar.place(x=self.hesar.winfo_x(), y=self.hesar.new_y)
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.compeletewidget.place(x=self.compeletewidget.winfo_x(), y=self.compeletewidget.new_y)

        def double_drag_shiftymotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.name.place(x=self.name.new_x, y=self.name.winfo_y())
            self.hesar.new_x = self.hesar.winfo_x() - self.hesar.cur_x + event.x
            self.hesar.new_y = self.hesar.winfo_y() - self.hesar.cur_y + event.y
            self.hesar.place(x=self.hesar.new_x, y=self.hesar.winfo_y())
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.compeletewidget.place(x=self.compeletewidget.new_x, y=self.compeletewidget.winfo_y())

        if self.task == 'yes':

            self.name.bind('<Button-1>', double_drag_start)
            self.name.bind('<B1-Motion>', double_drag_motion)
            self.hesar.bind('<Button-1>', double_drag_start)
            self.hesar.bind('<B1-Motion>', double_drag_motion)
            self.name.bind('<Control-B1-Motion>', double_drag_shiftymotion)
            self.name.bind('<Shift-B1-Motion>', double_drag_ctrlxmotion)
            self.hesar.bind('<Control-B1-Motion>', double_drag_shiftymotion)
            self.hesar.bind('<Shift-B1-Motion>', double_drag_ctrlxmotion)

            def task_sing_chnager(event):
                global task_completed
                if self.completecheck == False:
                    self.compeletewidget.config(image=self.complete, bg=self.bg)
                    task_completed += 1
                    self.completecheck = True
                    self.add()
                else:
                    self.compeletewidget.config(image=self.incomplete, bg=self.bg)
                    task_completed -= 1
                    self.completecheck = False
                    self.remove()

            self.compeletewidget.bind('<Button-1>', task_sing_chnager)

        else:
            self.name.bind('<Button-1>', pair_drag_start)
            self.name.bind('<B1-Motion>', pair_drag_motion)
            self.hesar.bind('<Button-1>', pair_drag_start)
            self.hesar.bind('<B1-Motion>', pair_drag_motion)
            self.name.bind('<Control-B1-Motion>', pair_drag_shiftymotion)
            self.name.bind('<Shift-B1-Motion>', pair_drag_ctrlxmotion)
            self.hesar.bind('<Control-B1-Motion>', pair_drag_shiftymotion)
            self.hesar.bind('<Shift-B1-Motion>', pair_drag_ctrlxmotion)

        # self.name.bind('<Button-1>', double_drag_start)
        # self.name.bind('<B1-Motion>', double_drag_motion)
        # self.hesar.bind('<Button-1>', double_drag_start)
        # self.hesar.bind('<B1-Motion>', double_drag_motion)
        # self.name.bind('<Control-B1-Motion>', double_drag_ctrlymotion)
        # self.name.bind('<Shift-B1-Motion>', double_drag_ctrlxmotion)
        # self.hesar.bind('<Control-B1-Motion>', double_drag_ctrlymotion)
        # self.hesar.bind('<Shift-B1-Motion>', double_drag_ctrlxmotion)

    def dele(self):
        global total_task
        global task_completed
        if self.task == 'yes':
            self.name.destroy()
            self.hesar.destroy()
            self.compeletewidget.destroy()
            self.s
            total_task -= 1
            if self.completecheck == True:
                task_completed -= 1
        else:
            self.name.destroy()
            self.hesar.destroy()

class Shapeless(Main):

    def __init__(self, window, name='name', bg='pink', placex=0, placey=0, text='', font='Arial',
                 size=10, task='no'):
        self.window = window
        self.name = name
        self.color = bg
        self.placex = placex
        self.placey = placey
        self.text = text
        self.font = font
        self.size = size
        self.task = task
        self.slidebutton_avai = False
        self.complete = PhotoImage(file='Support/Source/complete.png')
        self.incomplete = PhotoImage(file='Support/Source/incomplete.png')
        self.compeletewidget = 'complete'
        self.incompeletewidget = 'incomplete'
        self.completecheck = False

    def create(self):
        global total_task, shapeless_curindex, shapeless_list, shapeless_firsttime
        self.name = Label(self.window, bg=self.color, text=self.text,
                          font=(self.font, self.size), wraplength=120)
        self.name.place(x=self.placex, y=self.placey)

        # For Index Adding and Excluding first time
        if shapeless_firsttime == True:
            shapeless_curindex += 0
            shapeless_firsttime = False
        else:
            shapeless_curindex += 1

        self.name.shapeless_curindex = shapeless_curindex

        if self.task == 'yes':
            global task_completed, total_task

            self.compeletewidget = Label(self.window, image=self.incomplete, bg=self.color)
            self.compeletewidget.place(x=self.placex, y=self.placey-15)
            total_task += 1
            self.add()
            self.remove()

            if self.completecheck == True:
                self.compeletewidget.config(image=self.complete, bg=self.color)
                task_completed += 1
                self.completecheck = True
                self.add()

    def work(self):

        def double_drag_start(event):
            self.name.cur_x = event.x
            self.name.cur_y = event.y
            self.compeletewidget.cur_x = event.x
            self.compeletewidget.cur_y = event.y

        def double_drag_motion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.name.place(x=self.name.new_x, y=self.name.new_y)
            self.compeletewidget.place(x=self.compeletewidget.new_x, y=self.compeletewidget.new_y)
            # Related to Saving
            shapeless_list[self.name.shapeless_curindex] = [self.name.new_x, self.name.new_y]

        def double_drag_ctrlxmotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.name.place(x=self.name.winfo_x(), y=self.name.new_y)
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.compeletewidget.place(x=self.compeletewidget.winfo_x(), y=self.compeletewidget.new_y)

        def double_drag_shiftymotion(event):
            self.name.new_x = self.name.winfo_x() - self.name.cur_x + event.x
            self.name.new_y = self.name.winfo_y() - self.name.cur_y + event.y
            self.name.place(x=self.name.new_x, y=self.name.winfo_y())
            self.compeletewidget.new_x = self.compeletewidget.winfo_x() - self.compeletewidget.cur_x + event.x
            self.compeletewidget.new_y = self.compeletewidget.winfo_y() - self.compeletewidget.cur_y + event.y
            self.compeletewidget.place(x=self.compeletewidget.new_x, y=self.compeletewidget.winfo_y())

        if self.task == 'yes':

            self.name.bind('<Button-1>', double_drag_start)
            self.name.bind('<B1-Motion>', double_drag_motion)
            self.name.bind('<Control-B1-Motion>', double_drag_ctrlxmotion)
            self.name.bind('<Shift-B1-Motion>', double_drag_shiftymotion)

            def task_sing_chnager(event):
                global task_completed
                if self.completecheck == False:
                    self.compeletewidget.config(image=self.complete, bg=self.color)
                    task_completed += 1
                    self.completecheck = True
                    self.add()
                else:
                    self.compeletewidget.config(image=self.incomplete, bg=self.color)
                    task_completed -= 1
                    self.completecheck = False
                    self.remove()

            self.compeletewidget.bind('<Button-1>', task_sing_chnager)

        else:
            self.name.bind('<Button-1>', self.drag_start)
            self.name.bind('<B1-Motion>', self.drag_motion)
            self.name.bind('<Control-B1-Motion>', self.drag_ctrlxmotion)
            self.name.bind('<Shift-B1-Motion>', self.drag_ctrlymotion)

    def dele(self):
        global total_task
        global task_completed
        if self.task == 'yes':
            self.name.destroy()
            self.compeletewidget.destroy()
            total_task -= 1
            if self.completecheck == True:
                task_completed -= 1
        else:
            self.name.destroy()
