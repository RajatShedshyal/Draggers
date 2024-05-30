from Draggers import *
from tkinter import *
import threading
import shutil
from PIL import ImageTk, Image
import time
import random
from tkinter import ttk
from tkinter import colorchooser as cc
from tkinter import messagebox as mb
from tkinter import filedialog
from utils import *

# Main work is to do selector

move_with_taskbar = False
task = 'no'
font_available = ['Arial', 'Times New Roman', 'MV Boli']
de_x = 0
de_y =0

quad_func_list = []
shapeless_func_list = []
imageobj_func_list = []
circle_func_list = []
row_filled = 0
column_filled = 0
bgmain = 'lightblue'  # bg = bgmain
end = '\nwindow.mainloop()'
temp = """\n
"""


def remove_enter(text):
    r_text = ''
    for i in text:
        if i != '\n':
            r_text += i
        else:
            pass
    return r_text


def quad_adder(setname, bgname, fontname, taskmain, name):
    global temp
    ticktof = False
    if name.completecheck == True:
        ticktof = True
    else:
        ticktof = False

    try:
        temp += f"""
def create():
        global column_filled, row_filled
        text_var = '''{quadt_list[name.name.quad_curindex]}'''
        name = Quad(window, text=str("{setname}"), bg=str("{bgname}"), font=str("{fontname}"), task="{taskmain}",
         placex={quadf_list[name.name.quad_curindex][0]}, placey={quadf_list[name.name.quad_curindex][1]}, 
         def_text=text_var)
        name.completecheck = {ticktof}
        name.create()
        name.work()
        name.infostation()
        window.bind('<Control-z>', lambda x: delete(name, delbut))
        delbut = Button(deleter, text=f"Delete: {name.text[0:10]}", command=lambda: delete(name, delbut))
        delbut.grid(row=row_filled, column=column_filled)
        row_filled += 1
        if row_filled >= 23:
                row_filled = 0
                column_filled += 1

create()
"""
    except IndexError:
        temp += f"""
def create():
        global column_filled, row_filled
        text_var = ''''''
        name = Quad(window, text=str("{setname}"), bg=str("{bgname}"), font=str("{fontname}"), task="{taskmain}",
            placex={quadf_list[name.name.quad_curindex][0]}, placey={quadf_list[name.name.quad_curindex][1]}, 
            def_text=text_var)
        name.completecheck = {ticktof}
        name.create()
        name.work()
        name.infostation()
        window.bind('<Control-z>', lambda x: delete(name, delbut))
        delbut = Button(deleter, text=f"Delete: {name.text[0:10]}", command=lambda: delete(name, delbut))
        delbut.grid(row=row_filled, column=column_filled)
        row_filled += 1
        if row_filled >= 23:
                row_filled = 0
                column_filled += 1

create()
"""

def imageobj_adder(setname, bgname, fontname, taskmain, name, pathname, resize, w, h, tg):
    global temp
    ticktof = False
    if name.completecheck == True:
        ticktof = True
    else:
        ticktof = False
    temp += f"""
def create():
        global column_filled, row_filled
        name = Imageobj(window, path=str("{pathname}"), text=str("{setname}"), bg=str("{bgname}"), font=str("{fontname}"), task="{taskmain}",
        resizea = {resize}, w = {w}, h = {h}, tg='{tg}',
         placex={imageobj_list[name.name.imageobj_curindex][0]}, placey={imageobj_list[name.name.imageobj_curindex][1]},)
        name.completecheck = {ticktof}
        name.create()
        name.work()
        window.bind('<Control-z>', lambda x: delete(name, delbut))
        delbut = Button(deleter, text=f"Delete: {name.text[0:10]}", command=lambda: delete(name, delbut))
        delbut.grid(row=row_filled, column=column_filled)
        row_filled += 1
        if row_filled >= 23:
                row_filled = 0
                column_filled += 1

create()
"""


def shapeless_adder(setname, bgname, fontname, taskmain, name):
    global temp
    ticktof = False
    if name.completecheck == True:
        ticktof = True
    else:
        ticktof = False

    temp += f"""
def create():
        global column_filled, row_filled
        name = Shapeless(window, text=str("{setname}"), bg=str("{bgname}"), font=str("{fontname}"), task="{taskmain}",
         placex={shapeless_list[name.name.shapeless_curindex][0]}, placey={shapeless_list[name.name.shapeless_curindex][1]})
        name.completecheck = {ticktof}
        name.create()
        name.work()
        window.bind('<Control-z>', lambda x: delete(name, delbut))
        delbut = Button(deleter, text=f"Delete: {name.text[0:10]}", command=lambda: delete(name, delbut))
        delbut.grid(row=row_filled, column=column_filled)
        row_filled += 1
        if row_filled >= 23:
                row_filled = 0
                column_filled += 1

create()             
"""


def update_default_color():
    global default_color
    with open('Accessibilty.txt', 'r') as ab:
        default_color = str(remove_enter(ab.readlines()[0]))


def update_default_font():
    global default_font
    with open('Accessibilty.txt', 'r') as ab:
        default_font = remove_enter(ab.readlines()[1])


update_default_font()
print(f'font: {default_font}')


def cleartemp():
    global temp
    temp = """ """  # to clear temp
    # print('Cleared Temp')


def delete(selected, widget):
    selected.dele()
    widget.destroy()


# Creates a Quad
def quad_creater(defaultname):
    global task
    task = 'no'
    setname = defaultname
    bgname = 'pink'
    fontname = default_font
    taskmain = 'no'  # bcoz Draggers module vars match so 'main' is used

    def set_color(e):
        global var_bg
        color_var = cc.askcolor()
        askwindow.lift()
        bgname_e.delete(0, END)
        bgname_e.insert(0, color_var[1])

    def enter_submit(event):

        if name_e.get() != '':
            setname = name_e.get()
        else:
            setname = "Rajat's Studio"
        if bgname_e.get() != '':
            bgname = bgname_e.get()
        else:
            bgname = "pink"
        if fontname_s.get() != '':
            fontname = fontname_s.get()
        else:
            fontname = default_font
        if task == 'no':
            taskmain = 'no'
        else:
            taskmain = 'yes'

        def create(setname):
            global column_filled, row_filled
            update_default_color()
            name = Quad(window, text=str(setname), bg=str(bgname), font=str(fontname), task=taskmain, tg=default_color)
            quadf_list.append([0, 0])  # To Create a initial value for the list
            name.create()
            name.work()
            name.infostation()  # Should also add same line in saving temp quad_adder for saving
            window.bind('<Control-z>', lambda x: delete(name, delbut))

            # Supa is inspired by Super Function (idk y)
            def supa(name, delbut):
                global deleter
                cleartemp()
                delete(name, delbut)
                quad_func_list.remove([setname, bgname, fontname, taskmain, name])

            delbut = Button(deleter, text=f'Delete: {name.text[0:10]}', command=lambda: supa(name, delbut))
            delbut.grid(row=row_filled, column=column_filled)
            row_filled += 1
            if row_filled >= 23:
                row_filled = 0
                column_filled += 1

            quad_func_list.append([setname, bgname, fontname, taskmain, name])

        askwindow.destroy()
        create(setname)

    def submit():
        if name_e.get() != '':
            setname = name_e.get()
        else:
            setname = "Rajat's Studio"
        if bgname_e.get() != '':
            bgname = bgname_e.get()
        else:
            bgname = "pink"
        if fontname_s.get() != '':
            fontname = fontname_s.get()
        else:
            fontname = default_font
        if task == 'no':
            taskmain = 'no'
        else:
            taskmain = 'yes'

        def create(setname):
            global column_filled, row_filled
            update_default_color()
            name = Quad(window, text=str(setname), bg=str(bgname), font=str(fontname), task=taskmain, tg=default_color)
            name.create()
            name.work()
            name.infostation()
            quadf_list.append([0, 0])  # To Create a initial value for the list
            window.bind('<Control-z>', lambda x: delete(name, delbut))

            def supa(name, delbut):
                global deleter
                cleartemp()
                delete(name, delbut)
                quad_func_list.remove([setname, bgname, fontname, taskmain, name])

            delbut = Button(deleter, text=f'Delete: {name.text[0:10]}',
                            command=lambda: supa(name, delbut))
            delbut.grid(row=row_filled, column=column_filled)
            row_filled += 1
            if row_filled >= 23:
                row_filled = 0
                column_filled += 1
            quad_func_list.append([setname, bgname, fontname, taskmain, name])

        create(setname)
        askwindow.destroy()

    askwindow = Toplevel()
    askwindow.geometry(f'260x225+{int(window.winfo_screenwidth() / 240)}+{int(window.winfo_screenheight() / 1.85)}')
    askwindow.overrideredirect(True)
    com_bg_1 = 'lightgreen'
    askwindow.config(bg=com_bg_1)

    com_bg = '#900C3F'
    bef_frame = Frame(askwindow, bg=com_bg, width=260, height=24, borderwidth=2, relief='ridge')
    bef_frame.place(x=0, y=0)

    # Task bar

    def new_placing(e):
        askwindow.geometry(f'+{e.x_root - 10}+{e.y_root - 10}')

    move_button_taskbar = Label(bef_frame, image=move_button, bg=com_bg, cursor='fleur')
    move_button_taskbar.place(x=5, y=0)

    if move_with_taskbar != True:
        move_button_taskbar.bind("<B1-Motion>", new_placing)
    else:
        bef_frame.bind("<B1-Motion>", new_placing)

    exit_button = Label(bef_frame, image=close_button, bg=com_bg)
    exit_button.place(x=235, y=0)
    exit_button.bind("<Button-1>", lambda x: askwindow.destroy())

    com_font = ('MV Boli', 10)

    frame = Frame(askwindow, bg=com_bg_1)
    frame.place(x=0, y=24)

    title = Label(frame, text='Quad Info: ', font=('MV Boli', 25), bg=com_bg_1)
    title.grid(row=1, column=0, columnspan=2)

    bgname_t = Label(frame, text='Colour: ', font=com_font, bg=com_bg_1)
    bgname_t.grid(row=3, column=0)

    bgname_e = Entry(frame, width=15)
    bgname_e.insert(0, 'Pink')
    bgname_e.grid(row=3, column=1)

    bgname_or = Label(frame, text='Or ', font=com_font, bg=com_bg_1)
    bgname_or.grid(row=3, column=2)

    bgname_color = Label(frame, image=color_choose_main, bg=com_bg_1)
    bgname_color.grid(row=3, column=3, columnspan=4)
    bgname_color.bind("<Button-1>", set_color)

    name_t = Label(frame, text='Title: ', font=com_font, bg=com_bg_1)
    name_t.grid(row=2, column=0)

    name_e = Entry(frame, width=15)
    name_e.grid(row=2, column=1)

    fontname_t = Label(frame, text='Font: ', font=com_font, bg=com_bg_1)
    fontname_t.grid(row=4, column=0)

    fontname_s = ttk.Combobox(frame, value=font_available, width=12)
    fontname_s.set('MV Boli')
    fontname_s.grid(row=4, column=1)

    task_t = Label(frame, text='Task to\n be Tracked: ', font=com_font, bg=com_bg_1)
    task_t.grid(row=5, column=0)

    def change_task_y(e):
        global task
        if task == 'no':
            task = 'yes'
            task_y.config(relief='sunken')
            task_n.config(relief='flat')
            task_show.config(text='            [Yes]')

    def change_task_n(e):
        global task
        if task == 'yes':
            task = 'no'
            task_y.config(relief='flat')
            task_n.config(relief='sunken')
            task_show.config(text='            [No]')

    task_show = Label(frame, text='            [No]', bg=com_bg_1)
    task_show.grid(row=5, column=1, columnspan=2)

    task_y = Label(frame, image=yes_button, relief='flat', bg=com_bg_1)
    task_y.grid(row=5, column=1)
    task_y.bind("<Button-1>", change_task_y)

    task_n = Label(frame, image=close_button, relief='sunken', bg=com_bg_1)
    task_n.grid(row=5, column=2)
    task_n.bind("<Button-1>", change_task_n)

    submit_button = Button(frame, text='Submit', command=submit, font=com_font, bg='#FF3383')
    submit_button.grid(row=6, column=0, columnspan=7)

    askwindow.bind('<Return>', enter_submit)

    def lift_obj(e):
        try:
            askwindow.lift()
            print('did')
        except:
            return None
    window.bind("<Button-1>", lift_obj)

    arrowwindow.destroy()
    askwindow.mainloop()


# Creates Shapeless
def shapeless_creater(defaultname):
    setname = defaultname
    bgname = 'pink'
    fontname = 'Arial'
    taskmain = 'no'  # bcoz Draggers module vars match so 'main' is used

    def set_color(e):
        global var_bg
        color_var = cc.askcolor()
        askwindow.lift()
        bgname_e.delete(0, END)
        bgname_e.insert(0, color_var[1])

    def enter_submit(event):

        if name_e.get() != '':
            setname = name_e.get()
        else:
            setname = "Rajat's Studio"
        if bgname_e.get() != '':
            bgname = bgname_e.get()
        else:
            bgname = "pink"
        update_default_font()
        if fontname_s.get() != '':
            fontname = fontname_s.get()
        else:
            fontname = default_font

        def create(setname):
            global column_filled, row_filled
            name = Shapeless(window, text=str(setname), bg=str(bgname), font=str(fontname), task=taskmain)
            name.create()
            name.work()
            shapeless_list.append([0, 0])
            window.bind('<Control-z>', lambda x: delete(name, delbut))

            def supa(name, delbut):
                global deleter
                cleartemp()
                delete(name, delbut)
                shapeless_func_list.remove([setname, bgname, fontname, taskmain, name])

            delbut = Button(deleter, text=f'Delete: {name.text[0:10]}',
                            command=lambda: supa(name, delbut))

            delbut.grid(row=row_filled, column=column_filled)
            row_filled += 1
            if row_filled >= 23:
                row_filled = 0
                column_filled += 1
            shapeless_func_list.append([setname, bgname, fontname, taskmain, name])

        askwindow.destroy()
        create(setname)

    def submit():
        if name_e.get() != '':
            setname = name_e.get()
        else:
            setname = "Rajat's Studio"
        if bgname_e.get() != '':
            bgname = bgname_e.get()
        else:
            bgname = "pink"
        update_default_font()
        if fontname_s.get() != '':
            fontname = fontname_s.get()
        else:
            fontname = default_font

        def create(setname):
            global column_filled, row_filled
            name = Shapeless(window, text=str(setname), bg=str(bgname), font=str(fontname), task=taskmain)
            name.create()
            name.work()
            shapeless_list.append([0, 0])
            window.bind('<Control-z>', lambda x: delete(name, delbut))

            def supa(name, delbut):
                global deleter
                cleartemp()
                delete(name, delbut)
                shapeless_func_list.remove([setname, bgname, fontname, taskmain, name])

            delbut = Button(deleter, text=f'Delete: {name.text[0:10]}',
                            command=lambda: supa(name, delbut))
            delbut.grid(row=row_filled, column=column_filled)
            row_filled += 1
            if row_filled >= 23:
                row_filled = 0
                column_filled += 1
            shapeless_func_list.append([setname, bgname, fontname, taskmain, name])

        create(setname)
        askwindow.destroy()

    askwindow = Toplevel()
    askwindow.geometry(f'260x185+{int(window.winfo_screenwidth() / 240)}+{int(window.winfo_screenheight() / 1.70)}')
    askwindow.overrideredirect(True)
    com_bg_1 = 'lightgreen'
    askwindow.config(bg=com_bg_1)

    com_bg = '#900C3F'
    bef_frame = Frame(askwindow, bg=com_bg, width=260, height=24, borderwidth=2, relief='ridge')
    bef_frame.place(x=0, y=0)

    # Task bar

    def new_placing(e):
        askwindow.geometry(f'+{e.x_root - 10}+{e.y_root - 10}')

    move_button_taskbar = Label(bef_frame, image=move_button, bg=com_bg, cursor='fleur')
    move_button_taskbar.place(x=5, y=0)

    if move_with_taskbar != True:
        move_button_taskbar.bind("<B1-Motion>", new_placing)
    else:
        bef_frame.bind("<B1-Motion>", new_placing)

    exit_button = Label(bef_frame, image=close_button, bg=com_bg)
    exit_button.place(x=235, y=0)
    exit_button.bind("<Button-1>", lambda x: askwindow.destroy())

    com_font = ('MV Boli', 10)

    frame = Frame(askwindow, bg=com_bg_1)
    frame.place(x=0, y=24)

    title = Label(frame, text='Shapeless Info: ', font=('MV Boli', 20), bg=com_bg_1)
    title.grid(row=1, column=0, columnspan=2)

    bgname_t = Label(frame, text='Colour: ', font=com_font, bg=com_bg_1)
    bgname_t.grid(row=3, column=0)

    bgname_e = Entry(frame, width=15)
    bgname_e.insert(0, 'Pink')
    bgname_e.grid(row=3, column=1)

    bgname_or = Label(frame, text='Or ', font=com_font, bg=com_bg_1)
    bgname_or.grid(row=3, column=2)

    bgname_color = Label(frame, image=color_choose_main, bg=com_bg_1)
    bgname_color.grid(row=3, column=3, columnspan=4)
    bgname_color.bind("<Button-1>", set_color)

    name_t = Label(frame, text='Title: ', font=com_font, bg=com_bg_1)
    name_t.grid(row=2, column=0)

    name_e = Entry(frame, width=15)
    name_e.grid(row=2, column=1)

    fontname_t = Label(frame, text='Font: ', font=com_font, bg=com_bg_1)
    fontname_t.grid(row=4, column=0)

    fontname_s = ttk.Combobox(frame, value=font_available, width=12)
    fontname_s.set('MV Boli')
    fontname_s.grid(row=4, column=1)

    submit_button = Button(frame, text='Submit', command=submit, font=com_font, bg='#FF3383')
    submit_button.grid(row=5, column=0, columnspan=7, pady=5)

    askwindow.bind('<Return>', enter_submit)

    def lift_obj(e):
        try:
            askwindow.lift()
            print('did')
        except:
            return None
    window.bind("<Button-1>", lift_obj)

    arrowwindow.destroy()
    askwindow.mainloop()


# Image Creater
def image_creater(defaultname):
    global resize
    resize = False
    w = 100
    h = 100
    update_default_font()
    setname = defaultname
    bgname = 'pink'
    fontname = default_font
    taskmain = 'no'  # bcoz Draggers module vars match so 'main' is used
    pathmain = 'Support/Source/logo2.png'  # bcoz Draggers module vars match so 'main' is used
    update_default_color()
    tg = default_color

    def set_path(e):
        set_path = filedialog.askopenfilename(
            initialdir=f'C:\\Users\\{os.getlogin()}\\Pictures',
            filetypes=[('.png', '.png'),
                       ('.jpeg', '.jpeg')]
        )
        image_e.insert(0, set_path)
        askwindow.lift()

    def enter_submit(event):
        global resize
        if name_e.get() != '':
            setname = name_e.get()
        else:
            setname = ""
        if fontname_s.get() != '':
            fontname = fontname_s.get()
        else:
            fontname = default_font
        if image_e.get() != '':
            pathmain = image_e.get()
        else:
            pathmain = 'Support/Source/logo2.png'
        # width and height
        try:
            if resize:
                w = int(Image.width_ask.get())
                h = int(Image.height_ask.get())
            else:
                w = 100
                h = 100

        except ValueError:
            resize = False
            w = 100
            h = 100

        def create(setname):
            global column_filled, row_filled
            update_default_color()
            name = Imageobj(window=window, path=pathmain, text=str(setname), bg=str(bgname), task=taskmain,
                            resizea=resize, w=w, h=h, tg=default_color, font=str(fontname))
            name.create()
            name.work()
            imageobj_list.append([0, 0])
            window.bind('<Control-z>', lambda x: delete(name, delbut))

            def supa(name, delbut):
                global deleter
                cleartemp()
                delete(name, delbut)
                imageobj_func_list.remove([setname, bgname, fontname, taskmain, name, pathmain, resize, w, h, tg])

            delbut = Button(deleter, text=f'Delete: {name.text[0:10]}', command=lambda: supa(name, delbut))
            delbut.grid(row=row_filled, column=column_filled)
            row_filled += 1
            if row_filled >= 23:
                row_filled = 0
                column_filled += 1
            imageobj_func_list.append([setname, bgname, fontname, taskmain, name, pathmain, resize, w, h, tg])

        askwindow.destroy()
        create(setname)

    def submit():
        global resize
        if name_e.get() != '':
            setname = name_e.get()
        else:
            setname = ""
        if fontname_s.get() != '':
            fontname = fontname_s.get()
        else:
            fontname = default_font
        try:
            if image_e.get() != '':
                pathmain = image_e.get()
            else:
                pathmain = 'Support/Source/logo2.png'
        except:
            pathmain = 'Support/Source/logo2.png'
        # width and height
        try:
            if resize:
                w = int(Image.width_ask.get())
                h = int(Image.height_ask.get())
            else:
                w = 100
                h = 100

        except ValueError:
            resize = False
            w = 100
            h = 100

        def create(setname):
            global column_filled, row_filled
            update_default_color()
            name = Imageobj(window=window, path=pathmain, text=str(setname), bg=str(bgname), task=taskmain,
                            resizea=resize, w=w, h=h, tg=default_color, font=str(fontname))
            name.create()
            name.work()
            imageobj_list.append([0, 0])
            window.bind('<Control-z>', lambda x: delete(name, delbut))

            def supa(name, delbut):
                global deleter
                cleartemp()
                delete(name, delbut)
                imageobj_func_list.remove([setname, bgname, fontname, taskmain, name, pathmain, resize, w, h, tg])

            delbut = Button(deleter, text=f'Delete: {name.text[0:10]}', command=lambda: supa(name, delbut))
            delbut.grid(row=row_filled, column=column_filled)
            row_filled += 1
            if row_filled >= 23:
                row_filled = 0
                column_filled += 1
            imageobj_func_list.append([setname, bgname, fontname, taskmain, name, pathmain, resize, w, h, tg])

        create(setname)
        askwindow.destroy()

    askwindow = Toplevel()
    askwindow.geometry(f'260x240+{int(window.winfo_screenwidth() / 20)}+{int(window.winfo_screenheight() / 1.9)}')
    askwindow.overrideredirect(True)
    com_bg_1 = 'lightgreen'
    askwindow.config(bg=com_bg_1)

    com_bg = '#900C3F'
    bef_frame = Frame(askwindow, bg=com_bg, width=260, height=24, borderwidth=2, relief='ridge')
    bef_frame.place(x=0, y=0)

    # Task bar

    def new_placing(e):
        askwindow.geometry(f'+{e.x_root - 10}+{e.y_root - 10}')

    move_button_taskbar = Label(bef_frame, image=move_button, bg=com_bg, cursor='fleur')
    move_button_taskbar.place(x=5, y=0)

    if move_with_taskbar != True:
        move_button_taskbar.bind("<B1-Motion>", new_placing)
    else:
        bef_frame.bind("<B1-Motion>", new_placing)

    exit_button = Label(bef_frame, image=close_button, bg=com_bg)
    exit_button.place(x=235, y=0)
    exit_button.bind("<Button-1>", lambda x: askwindow.destroy())

    com_font = ('MV Boli', 10)

    frame = Frame(askwindow, bg=com_bg_1)
    frame.place(x=0, y=24)

    title = Label(frame, text='Image Info: ', font=('MV Boli', 25), bg=com_bg_1)
    title.grid(row=1, column=0, columnspan=2)

    image_l = Label(frame, text='Image: ', font=com_font, bg=com_bg_1)
    image_l.grid(row=2, column=0)

    image_e = Entry(frame, width=20)
    image_e.grid(row=2, column=1)

    image_o = Label(frame, text='Or', font=com_font, bg=com_bg_1)
    image_o.grid(row=2, column=2)

    image_f = Label(frame, text=' ', compound='right', image=open_button, bg=com_bg_1)
    image_f.grid(row=2, column=3)
    image_f.bind("<Button-1>", set_path)

    name_t = Label(frame, text='Title: ', font=com_font, bg=com_bg_1)
    name_t.grid(row=3, column=0)

    name_e = Entry(frame, width=20)
    name_e.grid(row=3, column=1)

    fontname_t = Label(frame, text='Font: ', font=com_font, bg=com_bg_1)
    fontname_t.grid(row=4, column=0)

    fontname_s = ttk.Combobox(frame, value=font_available, width=17)
    fontname_s.set('MV Boli')
    fontname_s.grid(row=4, column=1)

    def resizeit(e):
        global resize
        resize = True

        size_y.config(relief='solid', borderwidth=1)
        size_n.config(relief='sunken', borderwidth=2)

        Image.width_ask = Entry(frame, width=5)
        Image.width_ask.grid(row=6, column=1, columnspan=30)

        Image.into_x = Label(frame, text='x', font=com_font, bg=com_bg_1)
        Image.into_x.grid(row=6, column=2)

        Image.height_ask = Entry(frame, width=5)
        Image.height_ask.grid(row=6, column=3)

    def origi(e):
        global resize
        resize = False
        size_y.config(relief='sunken', borderwidth=2)
        size_n.config(relief='solid', borderwidth=1)

        Image.width_ask.destroy()
        Image.into_x.destroy()
        Image.height_ask.destroy()

    size_a = Label(frame, text='Image Should be:', font=com_font, bg=com_bg_1)
    size_a.grid(row=5, column=0, columnspan=7)

    size_y = Label(frame, text=' Original ', font=com_font, bg='#33FFCA', relief='sunken', borderwidth=2)
    size_y.grid(row=6, column=0, ipady=2)
    size_y.bind("<Button-1>", origi)

    size_n = Label(frame, text=' Resize ', font=com_font, bg='#33FFCA', relief='solid', borderwidth=1)
    size_n.grid(row=6, column=0, columnspan=2, ipady=2)
    size_n.bind("<Button-1>", resizeit)

    submit_button = Button(frame, text='Submit', command=submit, font=com_font, bg='#FF3383')
    submit_button.grid(row=8, column=0, columnspan=7, pady=5)

    askwindow.bind('<Return>', enter_submit)

    def lift_obj(e):
        try:
            askwindow.lift()
            print('did')
        except:
            return None
    window.bind("<Button-1>", lift_obj)

    arrowwindow.destroy()
    askwindow.mainloop()


def save(event):
    global temp, end
    cleartemp()

    shutil.copy('Draggers.py',
                'Support')

    start = """from Draggers import *
from tkinter import *
import pyautogui
import threading
import time
from tkinter.ttk import *

row_filled = 0
column_filled = 0
bgmain = 'lightblue'  # bg = bgmain

def delete(selected, widget):
    selected.dele()
    widget.destroy()

window = Tk()
window.geometry(f'500x500+{int(window.winfo_screenwidth()/3)}+{int(window.winfo_screenheight()/5)}')
window.state("zoomed")
window.config(bg=bgmain)

bar = Main(window=window, placex=int(window.winfo_screenwidth() - 200), placey=0)
bar.create()

# For Delete Button
global deleter
deleter = Toplevel()
deleter.title("Delete Window")
deleter.iconbitmap("Support/Source/skull.ico")
deleter.config(bg='lightgreen')
deleter.geometry("700x600")  # set this where you want this
deleter.withdraw()

def on_closing():
    deleter.withdraw()

def show_delete_but():
    deleter.deiconify()

deleter.protocol("WM_DELETE_WINDOW", on_closing)

# Delete Button Ends\n
    """

    which_file = filedialog.asksaveasfile(
        initialdir='Saved_Files'
        , defaultextension='.drg',
        filetypes=[('Draggers File', '.drg')]
        )

    for i in range(0, len(quad_func_list)):
        quad_adder(quad_func_list[i][0], quad_func_list[i][1], quad_func_list[i][2],
                   quad_func_list[i][3], quad_func_list[i][4])

    for k in range(0, len(shapeless_func_list)):
        shapeless_adder(shapeless_func_list[k][0], shapeless_func_list[k][1], shapeless_func_list[k][2],
                        shapeless_func_list[k][3], shapeless_func_list[k][4])

    for p in range(0, len(imageobj_func_list)):
        imageobj_adder(imageobj_func_list[p][0], imageobj_func_list[p][1], imageobj_func_list[p][2],
                       imageobj_func_list[p][3], imageobj_func_list[p][4], imageobj_func_list[p][5],
                       imageobj_func_list[p][6], imageobj_func_list[p][7], imageobj_func_list[p][8],
                       imageobj_func_list[p][9])

    if which_file is None:
        return

    start += temp
    start += end
    enc_start = start
    which_file.write(enc_start)
    which_file.close()


def openfile(event):
    shutil.copy('Draggers.py',
                'Support')

    try:
        fileo = filedialog.askopenfilename(
            initialdir='Saved_Files',
            filetypes=[('Draggers File', '.drg')]
        )
        clearopen = open('Support\\temporary.py', 'w')
        clearopen.write('')
        clearopen.close()
        startopen = open(fileo, 'r')
        dec_text = startopen.read()
        tempfiler = open('Support\\temporary.py', 'w')
        tempfiler.write(dec_text)
        tempfiler.close()
        x = threading.Thread(target=runner,
                             args=('Support',
                                   'temporary.py'))
        x.start()

    except FileNotFoundError:
        return None


# Main Variables

load_secs = [1, 1.5, 1.7, 2]
load_time = random.choice(load_secs)
print(load_time)
splashtimer = int(load_time)  # in secs

# Splash_screen

window = Tk()
window.geometry(f'600x400+{int(window.winfo_screenwidth() / 4)}+{int(window.winfo_screenheight() / 5)}')
window.overrideredirect(True)

splash_1 = PhotoImage(file='Support/Source/splash_screen_1.png')
splash_2 = PhotoImage(file='Support/Source/splash_screen_2.png')
splash_3 = PhotoImage(file='Support/Source/splash_screen_3.png')
splash_screens = [splash_1, splash_2, splash_3]
chosen_splash = random.choice(splash_screens)

title = Label(window, image=chosen_splash, borderwidth=0)
title.place(x=0, y=0)


def main():
    global save, window, complete_button_main, color_choose_main, quad_create, shapeless_create, image_create, logo
    global close_button, move_button, font_available, yes_button, open_button, arrow_button, emoji_button
    global alert_button, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10, a_11, a_12, a_13, a_14, a_15, a_16
    global a_17, a_18, a_19, a_20, a_21, a_22, bank, paypal, logo_now

    window.destroy()
    window = Tk()
    window.title('Draggers')
    window.iconbitmap('Support/Source/Draggers_Logo.ico')
    window.geometry(f'500x500+{int(window.winfo_screenwidth() / 3)}+{int(window.winfo_screenheight() / 5)}')
    window.state("zoomed")
    update_default_color()
    window.config(bg=default_color)

    # loading images #0001
    # Arrows
    a_1 = PhotoImage(file='Support/Source/a_1.png')
    a_2 = PhotoImage(file='Support/Source/a_2.png')
    a_3 = PhotoImage(file='Support/Source/a_3.png')
    a_4 = PhotoImage(file='Support/Source/a_4.png')
    a_5 = PhotoImage(file='Support/Source/a_5.png')
    a_6 = PhotoImage(file='Support/Source/a_6.png')
    a_7 = PhotoImage(file='Support/Source/a_7.png')
    a_8 = PhotoImage(file='Support/Source/a_8.png')
    a_9 = PhotoImage(file='Support/Source/a_9.png')
    a_10 = PhotoImage(file='Support/Source/a_10.png')
    a_11 = PhotoImage(file='Support/Source/a_11.png')
    a_12 = PhotoImage(file='Support/Source/a_12.png')
    a_13 = PhotoImage(file='Support/Source/a_13.png')
    a_14 = PhotoImage(file='Support/Source/a_14.png')
    a_15 = PhotoImage(file='Support/Source/a_15.png')
    a_16 = PhotoImage(file='Support/Source/a_16.png')
    a_17 = PhotoImage(file='Support/Source/a_17.png')
    a_18 = PhotoImage(file='Support/Source/a_18.png')
    a_19 = PhotoImage(file='Support/Source/a_19.png')
    a_20 = PhotoImage(file='Support/Source/a_20.png')
    a_21 = PhotoImage(file='Support/Source/a_21.png')
    a_22 = PhotoImage(file='Support/Source/a_22.png')
    # Normal:
    arrow_button = PhotoImage(file='Support/Source/arrow_create.png')
    emoji_button = PhotoImage(file='Support/Source/emoji_create.png')
    alert_button = PhotoImage(file='Support/Source/alert_create.png')
    open_button = PhotoImage(file='Support/Source/open.png')
    move_button = PhotoImage(file='Support/Source/move.png')
    close_button = PhotoImage(file='Support/Source/close.png')
    yes_button = PhotoImage(file='Support/Source/yes.png')
    image_create = PhotoImage(file='Support/Source/image_create.png')
    shapeless_create = PhotoImage(file='Support/Source/shapeless_create.png')
    quad_create = PhotoImage(file='Support/Source/quad_create.png')
    complete_button_main = PhotoImage(file='Support/Source/complete.png')
    color_choose_main = PhotoImage(file='Support/Source/color_chooser.png')
    logo = PhotoImage(file='Support/Source/small_logo.png')
    india_flag = PhotoImage(file='Support/Source/india.png')
    bank = PhotoImage(file='Support/Source/bank.png')
    paypal = PhotoImage(file='Support/Source/paypal.png')
    logo_now = PhotoImage(file='Support/Source/logo2_180x180.png')

    # Progress Bar
    progressbar = Main(window=window, placex=int(window.winfo_screenwidth() - 200), placey=0)
    progressbar.create()

    # Menu Bar

    main_menu = Menu(window, bg='red')
    window.config(menu=main_menu)

    # Sub menus

    # 1.File  tearoff: it is divider at starting

    file_menu = Menu(main_menu, tearoff=0, font=('Times New Roman', 10))
    main_menu.add_cascade(label='File', menu=file_menu)

    def open_new(event):
        o_n = threading.Thread(target=runner,
                               args=('',
                                     'main.py'))
        o_n.start()

    # Option Window
    global options
    options = Toplevel()
    options.title("Options")
    options.iconbitmap("Support/Source/options.ico")
    options.geometry("400x400")  # set this where you want this
    options_bg = '#030931'

    tabs = ttk.Notebook(options)
    # Tabs..
    # 1. Dragger

    dragger = Frame(tabs)
    dragger.config(bg=options_bg)

    bg_ask_color = Label(dragger, text='Background Color: ', font=('MV Boli', 12), fg='white', bg=options_bg)
    bg_ask_color.grid(row=1, column=1)

    access_write = ' '
    access_write_1 = default_color
    access_write_2 = default_font

    def set_window_bg_color(event):
        global access_write, default_color
        update_default_color()
        update_default_font()
        access_write_1 = default_color
        access_write_2 = default_font
        color = bg_insert_color.get()
        # Checking Validity
        total = 0
        for i in color:
            total += 1
        if color == '':
            access_write_1 = 'lightblue'
            access_write = access_write_1 + '\n' + access_write_2
            with open('Accessibilty.txt', 'w') as ac:
                ac.writelines(access_write)
        elif color[0] == '#' and total == 7:
            access_write_1 = color
            access_write = str(access_write_1) + '\n' + str(access_write_2)
            with open('Accessibilty.txt', 'w') as ac:
                ac.writelines(access_write)
        elif color == None:
            access_write_1 = 'lightblue'
            access_write = str(access_write_1) + '\n' + str(access_write_2)
            with open('Accessibilty.txt', 'w') as ac:
                ac.writelines(access_write)
        else:
            mb.showinfo()
            access_write_1 = 'lightblue'
            access_write = str(access_write_1) + '\n' + str(access_write_2)
            with open('Accessibilty.txt', 'w') as ac:
                ac.writelines(access_write)
        print(f'acces_Write_1: {access_write_1}, acces_Write_2: {access_write_2}')

    bg_insert_color = Entry(dragger)
    bg_insert_color.insert(0, default_color)
    bg_insert_color.bind("<Return>", set_window_bg_color)
    bg_insert_color.grid(row=1, column=2)

    bg_or_color = Label(dragger, text='Or ', font=('MV Boli', 12), fg='white', bg=options_bg)
    bg_or_color.grid(row=1, column=3)

    def box_window_bg_color(event):
        global access_write
        update_default_color()
        update_default_font()
        access_write_1 = default_color
        access_write_2 = default_font
        color = cc.askcolor()
        options.lift()  # Lift will bring the window front
        access_write_1 = color[1]
        access_write = str(access_write_1) + '\n' + str(access_write_2)
        bg_insert_color.delete(0, END)
        bg_insert_color.insert(0, default_color)
        print(f'acces_Write_1: {access_write_1}, acces_Write_2: {access_write_2}')
        try:
            with open('Accessibilty.txt', 'w') as ac:
                ac.writelines(access_write)
        except TypeError:
            with open('Accessibilty.txt', 'w') as ac:
                ac.writelines('lightblue')

    bg_choose_color = Label(dragger, image=color_choose_main, bg=options_bg)
    bg_choose_color.bind("<Button-1>", box_window_bg_color)
    bg_choose_color.grid(row=1, column=4)

    def font_set(event):
        update_default_color()
        update_default_font()
        access_write_1 = default_color
        access_write_2 = default_font
        with open('Accessibilty.txt', 'w') as ab:
            access_write_2 = font_select.get()
            access_write = str(access_write_1) + '\n' + str(access_write_2)
            ab.writelines(access_write)

    font_ask = Label(dragger, text='Font           : ', font=('MV Boli', 12), fg='white', bg=options_bg)
    font_ask.grid(row=2, column=1)

    font_select = ttk.Combobox(dragger, value=font_available)
    font_select.grid(row=2, column=2)
    font_select.set(default_font)
    font_select.bind("<<ComboboxSelected>>", font_set)

    # 2. Object

    object = Frame(tabs)

    tabs.add(dragger, text='Dragger')
    tabs.add(object, text='Object')
    tabs.pack(expand=True, fill='both')

    options.withdraw()

    def opeing_options():
        options.deiconify()

    def on_closing_options():
        options.withdraw()

    options.protocol("WM_DELETE_WINDOW", on_closing_options)

    file_menu.add_command(label='New', command=lambda: open_new(1), accelerator="Ctrl+N")
    window.bind("<Control-n>", open_new)
    file_menu.add_command(label='Open', command=lambda: openfile(1), accelerator="Ctrl+O")
    window.bind("<Control-o>", openfile)
    file_menu.add_command(label='Save', command=lambda: save(1), accelerator="Ctrl+S")
    window.bind("<Control-s>", save)
    file_menu.add_separator()
    file_menu.add_command(label='Settings', command=opeing_options)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=exit, accelerator="Ctrl+Q")
    window.bind("<Control-q>", exit)

    # 2.Edit

    edit_menu = Menu(main_menu, tearoff=0, font=('Times New Roman', 10))
    main_menu.add_cascade(label='Edit', menu=edit_menu)

    # 3.Help

    help_menu = Menu(main_menu, tearoff=0, font=('Times New Roman', 10))
    main_menu.add_cascade(label='Help', menu=help_menu)
    
    def imp_note():
        imp_note = Toplevel()
        imp_note.geometry(f'462x195+{int(window.winfo_screenwidth() / 6)}+{int(window.winfo_screenheight() / 15)}')
        imp_note.overrideredirect(True)
        com_bg_1 = '#F75564'
        imp_note.config(bg=com_bg_1)

        imp_frame = Frame(imp_note, bg=com_bg_1, width=462, height=194, relief='solid', bd=2)
        imp_frame.place(x=0, y=0)

        imp_title = Label(imp_frame, text='IMPORTANT NOTE', fg='white', font=('MV Boli', 20), bg=com_bg_1)
        imp_title.place(x=0, y=0)

        note = """The Software "Draggers" is owned by "Rajat's Studio" and
owns every right.This Software "Draggers" is currently under 
development and at version 1.8, The Further Development is stopped due
to some reasons. The Current Draggers (i.e 1.8 Version) is having more 
than enough featuresto make a stunning flow chart and help you track
your progress. >_< :_: .If you appreciate our software and want further 
development on it to be continued then you can contact this email:
'rajatstudiosofficial@gmail.com". 💚 Thank you 💚. Click anywhere to exit"""

        imp_text = Label(imp_frame, text=note, fg='black', font=('MV Boli', 10), bg=com_bg_1, justify='left')
        imp_text.place(x=0, y=40)
    
    
    help_menu.add_command(label='IMPORTANT NOTE', command=imp_note)
    help_menu.add_command(label='Getting Started', command=exit, accelerator="F1", state=DISABLED)
    help_menu.add_command(label='KeyMap Refrence', command=exit, state=DISABLED)
    help_menu.add_command(label='Demo and Tutorials', command=exit, state=DISABLED)
    window.bind('<F1>', exit)

    # 4. About

    about_menu = Menu(main_menu, tearoff=0, font=('Times New Roman', 10))
    main_menu.add_cascade(label='About', menu=about_menu)

    def about_window():
        about_win = Toplevel()
        about_win.geometry(f'460x305+{int(window.winfo_screenwidth() / 6)}+{int(window.winfo_screenheight() / 15)}')
        about_win.overrideredirect(True)
        com_bg_1 = '#F75564' 
        about_win.config(bg=com_bg_1)

        com_bg = '#900C3F'
        about_task = Frame(about_win, bg=com_bg, width=460, height=24, borderwidth=2, relief='ridge')
        about_task.place(x=0, y=0)

        # Task bar

        def new_placing(e):
            about_win.geometry(f'+{e.x_root - 10}+{e.y_root - 10}')

        move_button_taskbar = Label(about_task, image=move_button, bg=com_bg, cursor='fleur')
        move_button_taskbar.place(x=5, y=0)

        if move_with_taskbar != True:
            move_button_taskbar.bind("<B1-Motion>", new_placing)
        else:
            about_task.bind("<B1-Motion>", new_placing)

        exit_button = Label(about_task, image=close_button, bg=com_bg, fg='white')
        exit_button.place(x=438, y=0)
        exit_button.bind("<Button-1>", lambda x: about_win.destroy())

        com_font = ('MV Boli', 10)

        arrow_frame = Label(about_task, text='RAJAT STUDIOS', bg=com_bg, font=com_font, fg='white',
                            borderwidth=0, justify='center')
        arrow_frame.place(x=175, y=0)

        about_frame = Frame(about_win, bg=com_bg_1, width=460, height=280, relief='solid', bd=2)
        about_frame.place(x=0, y=24)

        abt_title = Label(about_frame, text='Rajat Studios', fg='white', font=('MV Boli', 20), bg=com_bg_1)
        abt_title.place(x=5, y=5)

        about_t = """Rajat Studios is a Company based in 
Jamkhandi, India. At Rajat Studios
Company Software Development,
Video Making, Designing, Affilating,
Game Development, Website Development,
Entrepreneurship is done. Rajat Studios
is fully owned by Rajat Shedshyal and 
is also the CEO of Rajat Studios. Rajat 
Studios is meant to increase standards of living of most
of the people and also bring new idea and projects for everyone's 
betterment and by doing so earn some profit. If you want to contact 
me I m available at Instagram: rajat_studios_official, Youtube: Rajat Studios
or you can just mail me at rajatstudiosofficial@gmail.com"""

        abt_about = Label(about_frame, text=about_t, bg=com_bg_1, font=("MV Boli", 10), justify='left')
        abt_about.place(x=5, y=45)

        abt_logo = Label(about_frame, image=logo_now, bd=0)
        abt_logo.place(x=265, y=5)

    about_menu.add_command(label='Rajat Studios', image=logo, compound='left', font=('Times new roman', 15),
                           command=about_window)

    about_menu.add_command(label='VERSION 1.8', state=DISABLED, activebackground='#F0F0F0')

    # 5.Donation

    donate_menu = Menu(main_menu, tearoff=0, font=('Times New Roman', 10))
    main_menu.add_cascade(label='Donate 💚💚', menu=donate_menu)

    def bank_window():
        bank_win = Toplevel()
        bank_win.geometry(
            f'390x130+{int(window.winfo_screenwidth() / 6)}+{int(window.winfo_screenheight() / 15)}')
        bank_win.overrideredirect(True)
        com_bg_1 = '#000831'
        bank_win.config(bg=com_bg_1)

        com_bg = '#900C3F'
        bank_task = Frame(bank_win, bg=com_bg, width=390, height=24, borderwidth=2, relief='ridge')
        bank_task.place(x=0, y=0)

        # Task bar

        def new_placing(e):
            bank_win.geometry(f'+{e.x_root - 10}+{e.y_root - 10}')

        move_button_taskbar = Label(bank_task, image=move_button, bg=com_bg, cursor='fleur')
        move_button_taskbar.place(x=5, y=0)

        if move_with_taskbar != True:
            move_button_taskbar.bind("<B1-Motion>", new_placing)
        else:
            bank_task.bind("<B1-Motion>", new_placing)

        exit_button = Label(bank_task, image=close_button, bg=com_bg, fg='white')
        exit_button.place(x=368, y=0)
        exit_button.bind("<Button-1>", lambda x: bank_win.destroy())

        com_font = ('MV Boli', 10)

        arrow_frame = Label(bank_task, text='Thank you for Donating 💚💚', bg=com_bg, font=com_font, fg='white',
                            borderwidth=0, justify='center')
        arrow_frame.place(x=115, y=0)

        bank_frame = Frame(bank_win, bg=com_bg_1, width=400, height=274)
        bank_frame.place(x=0, y=24)

        my_name = Label(bank_frame, text='Full Name: RAJAT NANDKUMAR SHEDSHYAL', font=('Times new roman', 12),
                        bg=com_bg_1, justify='center', fg='white')
        my_name.place(x=25, y=0)


        my_nation = Label(bank_frame, text='Nationality: Indian  ', image=india_flag, compound='right'
                          ,font=('Times new roman', 12), bg=com_bg_1, justify='center', fg='white')
        my_nation.place(x=25, y=20)

        my_bank = Label(bank_frame, text='Bank: Canara Bank', font=('Times new roman', 12),
                        bg=com_bg_1, justify='center', fg='white')
        my_bank.place(x=25, y=40)

        my_acc = Label(bank_frame, text='Account No: 110019338066', font=('Times new roman', 12),
                        bg=com_bg_1, justify='center', fg='white')
        my_acc.place(x=25, y=60)

        my_ifsc = Label(bank_frame, text='IFSC Code: CNRB0003163', font=('Times new roman', 12),
                       bg=com_bg_1, justify='center', fg='white')
        my_ifsc.place(x=25, y=80)

    donate_menu.add_command(label='Bank', command=bank_window, image=bank, compound='left', font=('Times new roman', 10))

    def paypal_window():
        paypal_win = Toplevel()
        paypal_win.geometry(f'390x55+{int(window.winfo_screenwidth() / 6)}+{int(window.winfo_screenheight() / 15)}')
        paypal_win.overrideredirect(True)
        com_bg_1 = '#000831'
        paypal_win.config(bg=com_bg_1)

        com_bg = '#900C3F'
        paypal_task = Frame(paypal_win, bg=com_bg, width=390, height=24, borderwidth=2, relief='ridge')
        paypal_task.place(x=0, y=0)

        # Task bar

        def new_placing(e):
            paypal_win.geometry(f'+{e.x_root - 10}+{e.y_root - 10}')

        move_button_taskbar = Label(paypal_task, image=move_button, bg=com_bg, cursor='fleur')
        move_button_taskbar.place(x=5, y=0)

        if move_with_taskbar != True:
            move_button_taskbar.bind("<B1-Motion>", new_placing)
        else:
            paypal_task.bind("<B1-Motion>", new_placing)

        exit_button = Label(paypal_task, image=close_button, bg=com_bg, fg='white')
        exit_button.place(x=368, y=0)
        exit_button.bind("<Button-1>", lambda x: paypal_win.destroy())

        com_font = ('Times new roman', 10)

        arrow_frame = Label(paypal_task, text='Thank you for Donating 💚💚', bg=com_bg, font=com_font, fg='white',
                            borderwidth=0, justify='center')
        arrow_frame.place(x=115, y=0)

        paypal_frame = Frame(paypal_win, bg=com_bg_1, width=400, height=274)
        paypal_frame.place(x=0, y=24)

        my_mail = Label(paypal_frame, text='Mail: rajatnshedshyal@gmail.com', font=('Times new roman', 12),
                        bg=com_bg_1, justify='center', fg='white')
        my_mail.place(x=25, y=0)

    donate_menu.add_command(label='Paypal', command=paypal_window, image=paypal, compound='left', font=('Times new roman', 10))

    # Down
    taskbar_bg = '#FFA301'
    Label(window, text='', bg='black', width=window.winfo_width(), height=5).place(x=0, y=window.winfo_height() - 105)
    Label(window, text=' ', bg=taskbar_bg, width=window.winfo_width() - 500, height=100).place(x=0,
                                                                                               y=window.winfo_height() - 100)

    window.bind("<q>", lambda x: quad_creater('rajat'))

    but1 = Button(window, image=quad_create, command=lambda: quad_creater('rajat'), bd=0, bg=taskbar_bg)
    but1.place(x=10, y=window.winfo_height() - 90)

    but2 = Button(window, image=shapeless_create, command=lambda: shapeless_creater('rajat'), bd=0, bg=taskbar_bg)
    but2.place(x=80, y=window.winfo_height() - 90)

    but3 = Button(window, image=image_create, command=lambda: image_creater('rajat'), bd=0, bg=taskbar_bg)
    but3.place(x=150, y=window.winfo_height() - 90)

    def arrows_create():
        global a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10, a_11, a_12, a_13,\
            a_14, arrowwindow, a_15, a_16, a_17, a_18, a_19, a_20, a_21, a_22

        print('Called')
        arrowwindow = Toplevel()
        arrowwindow.geometry(f'290x345+{int(window.winfo_screenwidth() / 10)}+{int(window.winfo_screenheight() / 2.52)}')
        arrowwindow.overrideredirect(True)
        com_bg_1 = 'lightgreen'
        arrowwindow.config(bg=com_bg_1)

        com_bg = '#900C3F'
        a_bef_frame = Frame(arrowwindow, bg=com_bg, width=300, height=24, borderwidth=2, relief='ridge')
        a_bef_frame.place(x=0, y=0)

        # Task bar

        def new_placing(e):
            arrowwindow.geometry(f'+{e.x_root - 10}+{e.y_root - 10}')

        move_button_taskbar = Label(a_bef_frame, image=move_button, bg=com_bg, cursor='fleur')
        move_button_taskbar.place(x=5, y=0)

        if move_with_taskbar != True:
            move_button_taskbar.bind("<B1-Motion>", new_placing)
        else:
            a_bef_frame.bind("<B1-Motion>", new_placing)

        exit_button = Label(a_bef_frame, image=close_button, bg=com_bg)
        exit_button.place(x=268, y=0)
        exit_button.bind("<Button-1>", lambda x: arrowwindow.destroy())

        com_font = ('MV Boli', 10)

        arrow_frame = Label(a_bef_frame, text='Arrows: ', bg=com_bg, font=com_font, fg='white', borderwidth=0)
        arrow_frame.place(x=125, y=0)

        a_frame = Frame(arrowwindow, bg=com_bg_1)
        a_frame.place(x=0, y=24)

        def create_arrow(img):
            update_default_color()
            bgname='pink'
            fontname='Arial'
            taskmain='no'
            pathmain = f'Support/Source/{img}.png'
            resize= False
            tg_ = f'{default_color}'
            w = 1
            h = 1
            setname= ''
            def create(setname):
                global column_filled, row_filled
                update_default_color()
                update_default_font()
                name = Imageobj(window=window, path=pathmain, tg=tg_)
                name.create()
                name.work()
                imageobj_list.append([0, 0])
                window.bind('<Control-z>', lambda x: delete(name, delbut))

                def supa(name, delbut):
                    global deleter
                    cleartemp()
                    delete(name, delbut)
                    imageobj_func_list.remove([setname, bgname, fontname, taskmain, name, pathmain, resize, w, h, tg_])

                delbut = Button(deleter, text=f'Delete: {name.text[0:10]}', command=lambda: supa(name, delbut))
                delbut.grid(row=row_filled, column=column_filled)
                row_filled += 1
                if row_filled >= 23:
                    row_filled = 0
                    column_filled += 1
                imageobj_func_list.append([setname, bgname, fontname, taskmain, name, pathmain, resize, w, h, tg_])

            create(setname)

        shorter_img = lambda img: create_arrow(img)

        a_1_b = Button(a_frame, width=50, height=58, image=a_1, command=lambda: shorter_img('a_1'), bg='#33FFCA', relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_1_b.grid(row=0, column=0, ipadx=1, ipady=1, padx=1)

        a_2_b = Button(a_frame, width=50, height=58, image=a_2, command=lambda: shorter_img('a_2'), bg='#33FFCA', relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_2_b.grid(row=0, column=1, ipadx=1, ipady=1, padx=1)

        a_3_b = Button(a_frame, width=50, height=58, image=a_3, command=lambda: shorter_img('a_3'), bg='#33FFCA', relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_3_b.grid(row=0, column=2, ipadx=1, ipady=1, padx=1)

        a_4_b = Button(a_frame, width=50, height=58, image=a_4, command=lambda: shorter_img('a_4'), bg='#33FFCA', relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_4_b.grid(row=0, column=3, ipadx=1, ipady=1, padx=1)

        a_5_b = Button(a_frame, width=50, height=58, image=a_5, command=lambda: shorter_img('a_5'), bg='#33FFCA', relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_5_b.grid(row=0, column=4, ipadx=1, ipady=1, padx=1)

        a_6_b = Button(a_frame, width=50, height=58, image=a_6, command=lambda: shorter_img('a_6'), bg='#33FFCA', relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_6_b.grid(row=1, column=0, ipadx=1, ipady=1, padx=1)

        a_7_b = Button(a_frame, width=50, height=58, image=a_7, command=lambda: shorter_img('a_7'), bg='#33FFCA',
                       relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_7_b.grid(row=1, column=1, ipadx=1, ipady=1, padx=1)

        a_8_b = Button(a_frame, width=50, height=58, image=a_8, command=lambda: shorter_img('a_8'), bg='#33FFCA',
                       relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_8_b.grid(row=1, column=2, ipadx=1, ipady=1, padx=1)

        a_9_b = Button(a_frame, width=50, height=58, image=a_9, command=lambda: shorter_img('a_9'), bg='#33FFCA',
                       relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_9_b.grid(row=1, column=3, ipadx=1, ipady=1, padx=1)

        a_10_b = Button(a_frame, width=50, height=58, image=a_10, command=lambda: shorter_img('a_10'), bg='#33FFCA',
                       relief='solid', bd=1,
                       activebackground='#31d6ab')
        a_10_b.grid(row=1, column=4, ipadx=1, ipady=1, padx=1)

        a_11_b = Button(a_frame, width=50, height=58, image=a_11, command=lambda: shorter_img('a_11'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_11_b.grid(row=2, column=0, ipadx=1, ipady=1, padx=1)

        a_12_b = Button(a_frame, width=50, height=58, image=a_12, command=lambda: shorter_img('a_12'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_12_b.grid(row=2, column=1, ipadx=1, ipady=1, padx=1)

        a_13_b = Button(a_frame, width=50, height=58, image=a_13, command=lambda: shorter_img('a_13'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_13_b.grid(row=2, column=2, ipadx=1, ipady=1, padx=1)

        a_14_b = Button(a_frame, width=50, height=58, image=a_14, command=lambda: shorter_img('a_14'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_14_b.grid(row=2, column=3, ipadx=1, ipady=1, padx=1)

        a_15_b = Button(a_frame, width=50, height=58, image=a_15, command=lambda: shorter_img('a_15'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_15_b.grid(row=2, column=4, ipadx=1, ipady=1, padx=1)

        a_16_b = Button(a_frame, width=50, height=58, image=a_16, command=lambda: shorter_img('a_16'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_16_b.grid(row=3, column=0, ipadx=1, ipady=1, padx=1)

        a_17_b = Button(a_frame, width=50, height=58, image=a_17, command=lambda: shorter_img('a_17'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_17_b.grid(row=3, column=1, ipadx=1, ipady=1, padx=1)

        a_18_b = Button(a_frame, width=50, height=58, image=a_18, command=lambda: shorter_img('a_18'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_18_b.grid(row=3, column=2, ipadx=1, ipady=1, padx=1)

        a_19_b = Button(a_frame, width=50, height=58, image=a_19, command=lambda: shorter_img('a_19'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_19_b.grid(row=3, column=3, ipadx=1, ipady=1, padx=1)

        a_20_b = Button(a_frame, width=50, height=58, image=a_20, command=lambda: shorter_img('a_20'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_20_b.grid(row=3, column=4, ipadx=1, ipady=1, padx=1)

        a_21_b = Button(a_frame, width=50, height=58, image=a_21, command=lambda: shorter_img('a_21'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_21_b.grid(row=4, column=0, ipadx=1, ipady=1, padx=1)

        a_22_b = Button(a_frame, width=50, height=58, image=a_22, command=lambda: shorter_img('a_22'), bg='#33FFCA',
                        relief='solid', bd=1,
                        activebackground='#31d6ab')
        a_22_b.grid(row=4, column=1, ipadx=1, ipady=1, padx=1)


    but4 = Button(window, image=arrow_button, command=arrows_create, bd=0, bg=taskbar_bg)
    but4.place(x=220, y=window.winfo_height()-90)

    but5 = Button(window, image=emoji_button, bd=0, bg=taskbar_bg)
    but5.place(x=290, y=window.winfo_height() - 90)

    but6 = Button(window, image=alert_button, bd=0, bg=taskbar_bg)
    but6.place(x=360, y=window.winfo_height() - 90)

    # For Delete Button
    global deleter
    deleter = Toplevel()
    deleter.title("Delete Window")
    deleter.iconbitmap("Support/Source/skull.ico")
    deleter.config(bg='lightgreen')
    deleter.geometry("700x600")  # set this where you want this
    deleter.withdraw()

    def on_closing_deleter():
        deleter.withdraw()  # Hides window which already exists

    def show_delete_but(event):
        deleter.deiconify()  # Shows Window which already exists

    deleter.protocol("WM_DELETE_WINDOW", on_closing_deleter)

    # Edit menu exception****
    edit_menu.add_command(label='Delete Objects', command=lambda: show_delete_but(1), accelerator="Ctrl+D")
    window.bind("<Control-d>", show_delete_but)

    def lift_arrow(e):
        try:
            arrowwindow.lift()
        except:
            return None

    window.bind("<Button-1>", lift_arrow)

    print('reached')


window.after(int(splashtimer * 1000), main)

mainloop()
