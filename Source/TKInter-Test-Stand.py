import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
from tkinter import colorchooser
import re
from tkcalendar import Calendar # pip install tkcalendar

### Functions
def clicked_radio_select():
    lbl_out.configure(text=selected.get())          # присвоить содержимое (value) выбранного Radiobutton в text объекта Lable

def clicked_2():
    res = "Вывод: {}".format(txt.get())             # форматировать текст текущей переменной, добавить информацию из Entry
    lbl_2.configure(text=res)                       # изменить конфигурацию Text в объекте Lable
    global clicks                                   # объявить глобальную переменную в функции
    clicks += 1                                     # изменить значение переменной
  # btn_2["text"] = f"Кнопка {clicks}"              # изменить текст на кнопке по значению индекса
    btn_2.configure(text=f"Кнопка {clicks}")        # изменить конфигурацию объекта

### MessageBox (wshell)
def clicked_cls():
    result_clear = messagebox.askyesno(title="Выбрать", message="Очистить?")    # да/нет
    # messagebox.askyesnocancel(title="Выбрать", message="Очистить?")           # да/нет/отмена
    # messagebox.askretrycancel(title="Выбрать", message="Очистить?")           # повторить/отмена
    if result_clear:
        txt_scroll.delete(1.0, tk.END)
        messagebox.showinfo("Выбор сделан", "Текст очищен")                     # информация
    else: 
        messagebox.showerror("Результат", "Операция отменена")                # ошибка

def SaveFile():
    file = filedialog.asksaveasfilename(initialfile="result.txt", filetypes=\
                                        (("Text file","*.txt"),\
                                        ("All file","*.*")))
    count = len(file)
    if count != 0:
        messagebox.showinfo('Result', file)

def OpenFile():
    file = filedialog.askopenfilename(initialdir = "/")     # открывает диалоговое окно для выбора файла и возвращает путь к выбранному файлу
    count = len(file)                                       # фиксируем кол-во символов
    # dir = filedialog.askdirectory()                       # выбор директории
    if count != 0:                                          # если кол-во символов в путе не равно 0
        messagebox.showinfo('Заголовок', file)

    # askopenfilenames()    открывает диалоговое окно для выбора файлов и возвращает список путей к выбранным файлам. Если файл не выбран, возвращается пустая строка ""
    # asksaveasfilename()   открывает диалоговое окно для сохранения файла и возвращает путь к сохраненному файлу. Если файл не выбран, возвращается пустая строка ""
    # asksaveasfile()       открывает диалоговое окно для сохранения файла и возвращает сохраненный файл. Если файл не выбран, возвращается None
    # askdirectory()        открывает диалоговое окно для выбора каталога и возвращает путь к выбранному каталогу. Если файл не выбран, возвращается пустая строка ""
    # askopenfile()         открывает диалоговое окно для выбора файла и возвращает выбранный файл. Если файл не выбран, возвращается None
    # askopenfiles()        открывает диалоговое окно для выбора файлов и возвращает список выбранных файлов

def Select_Color():
    result = colorchooser.askcolor(initialcolor="black")
    lbl_2["foreground"] = result[1]

def font_changed(font):
    lbl_2["font"] = font
 
def Select_Font():
    window.tk.call("tk", "fontchooser", "configure", "-font", lbl_2["font"], "-command", window.register(font_changed))
    window.tk.call("tk", "fontchooser", "show")

def clicked_bar():
    if bar['value'] >= 100:                 # если значение bar больше или равно 100
        bar['value'] = 0                    # то обнулить
    else:                                   # если нет
        bar['value'] += 10                  # прибавить 10

def change_scale(newVal):
    label_scale["text"] = scale.get()

def quit():
    window.destroy()
###

### Form
window = tk.Tk()
window.title("TKInter Test Stand")
window.geometry('320x460')
#window.attributes("-fullscreen", True)     # на весь экран (Windows)
#window.attributes('-zoomed', True)         # на весь экран (Ubuntu)
#window.attributes("-toolwindow", True)     # не классический Windows режим
#window.attributes("-alpha", 0.9)           # прозрачность
#window.resizable(False, False)             # запретить изменять размер окна
#window.iconbitmap(default="favicon.ico")   # ico (файл иконки располагается рядом с файлом приложения)
#icon = PhotoImage(file = "icon.png")
#window.iconphoto(False, icon)

### base64
#import tempfile, base64, zlib
#ICON = zlib.decompress(base64.b64decode("eJxjYGAEQgEBBiDJwZDBysAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="))
#_, ICON_PATH = tempfile.mkstemp()
#with open(ICON_PATH, "wb") as icon_file:
#icon_file.write(ICON)
#window.iconbitmap(default=ICON_PATH)

### Notebook/TabControl
tab_control = ttk.Notebook(window)
Tab_Main = ttk.Frame(tab_control)
Tab_Table = ttk.Frame(tab_control)
Tab_Calendar = ttk.Frame(tab_control)
Tab_Canvas = ttk.Frame(tab_control)
tab_control.add(Tab_Main, text='Main')
tab_control.add(Tab_Table, text='Table')
tab_control.add(Tab_Calendar, text='Calendar')
tab_control.add(Tab_Canvas, text='Canvas')
tab_control.pack(expand=1, fill='both')

img_base64 = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAACMAAAAjAQMAAAAkFyEaAAAABlBMVEX///8AAABVwtN+AAAAJ0lEQVQI12P4DwQPGCDkAQYGhgRSSDv+BjwkqabZ/2/AQ+LVi+QLAGveQwjt4H11AAAAAElFTkSuQmCC")
label_img = tk.Label(Tab_Main, image=img_base64)
label_img.place(x=222, y=248)
label_img["image"] = img_base64                     # задать переменную через индекс

### Frame (используется для группировки виджетов)
frame_black = tk.Frame(
    master=Tab_Main,
    height="40",
    bg="black"                      # используется для наложения Background
    )
frame_black.pack(fill=tk.X)

### Combobox
combo = Combobox(Tab_Main)
combo['values'] = (1, 2, 3, 4, 5)
combo.current(4)                    # установить вариант из списка по умолчанию по номеру индекса
combo.place(x=10, y=10)

### Radiobutton
selected = tk.IntVar()
rad1 = Radiobutton(Tab_Main,text='Первый', value=1, variable=selected)
rad1.place(x=0, y=50)
rad2 = Radiobutton(Tab_Main,text='Второй', value=2, variable=selected)
rad2.place(x=70, y=50)
rad3 = Radiobutton(Tab_Main,text='Третий', value=3, variable=selected)
rad3.place(x=140, y=50)

### Button 1 TK
btn = tk.Button(
    Tab_Main,                       # расположение на Window/Tab_Main/tab2
    text="Кнопка 1",                # текст
    width=8,                        # ширина
    height=1,                       # высота
    command=clicked_radio_select,   # привязать ключ/команду к функции при возкникновении события
    # state='disabled'              # отключить кнопку
    )
btn.place(x=210, y=48)              # расположение

lbl_out = tk.Label(Tab_Main)
lbl_out.place(x=285, y=50)

### Checkbutton/Checkbox
chk_state = tk.BooleanVar()
chk_state.set(True)                 # задать проверку состояния чекбокса
chk = Checkbutton(
    Tab_Main,
    text='Выбрать',
    var=chk_state
    )
chk.place(x=160, y=83)

### Entry/Outputbox
txt = tk.Entry(Tab_Main,width=10)
txt.place(x=10, y=85)

### Style
label_style = ttk.Style()
label_style.configure(
    "New.TButton",                  # имя нового стиля (по умолчанию: TButton и TLable, которые можно изменить)
    font="helvetica 8",             # шрифт
    foreground="#004D40",           # цвет текста
    background="#B2DFDB"            # фоновый цвет
    )

### Button 2 TTK
btn_2 = ttk.Button(
    Tab_Main,
    text="Кнопка 2",
    command=clicked_2,
    style="New.TButton"              # указать Style для кнопки
    )
btn_2.place(x=80, y=82)
clicks = 2

font_all = 'Arial 12 normal roman'  # создать переменную фона для всех Lable

lbl_2 = tk.Label(Tab_Main,
                 text="Вывод:",
                 font=font_all
                 )  
lbl_2.place(x=10, y=115)

### scrolledtext
txt_scroll = scrolledtext.ScrolledText(Tab_Main, width=20, height=10)  
txt_scroll.place(x=10, y=150)

btn_cls = tk.Button(Tab_Main, text="Очистить", command=clicked_cls)
btn_cls.place(x=210, y=290)

### Progressbar
bar = Progressbar(
    Tab_Main,
    length=180,
    cursor='watch'                  # курсор при наведении на виджет
    )
bar['value'] = 0
bar.place(x=10, y=330)

btn_bar = tk.Button(
    Tab_Main,
    text="Двигать бар",
    bg='#856ff8',
    fg="white",
    command=clicked_bar
    )  
btn_bar.place(x=200, y=328)

### Spinbox
var = tk.IntVar()
var.set(50)
spin = tk.Spinbox(Tab_Main, from_=0, to=100, width=5, textvariable=var)
# spin = Spinbox(window, values=(3, 8, 11), width=5) 
spin.place(x=10, y=370)

### Scale
label_scale = ttk.Label(Tab_Main)
label_scale.place(x=80, y=370)

scale = ttk.Scale(Tab_Main, orient='horizontal', length=200, from_=1.0, to=100.0, command=change_scale)
scale.place(x=80, y=390)

### Menu
menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Сохранить Файл', command=SaveFile)
new_item.add_command(label='Выбрать Файл', command=OpenFile)
new_item.add_separator()
new_item.add_command(label='Выбрать Цвет', command=Select_Color)
new_item.add_command(label='Выбрать Шрифт', command=Select_Font)
new_item.add_separator()
new_item.add_command(label='Выход', command=quit)
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)

### Treeview Color
class TreeColor(ttk.Treeview):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag_configure('green', background='green')         # элементам с тегом green назначить зеленый фон
        self.tag_configure('yellow', background='yellow')       # элементам с тегом red назначить желтый фон

    def insert(self, parent_node, index, **kwargs):             # присвоение тегов по содержимому индекса
        item = super().insert(parent_node, index, **kwargs)
        values = kwargs.get('values', None)
        if values:
          # if values[0]=='Yes':
            if re.search("Yes", values[0]):
                super().item(item, tag='green')
          # elif values[0]=="No":
            if re.search("No", values[0]):
                super().item(item, tag='yellow')
        return item

### TreeView
frame_list = tk.Frame(Tab_Table)       # Frame, используется для привязки к нему Scrollbar
frame_list.grid(column=0, row=0)

headers = ['Name', 'id1', 'id2']       # значения стоблцов
list =    [('Yes',      1,2),          # кортеж с данными
           ('Yes Test', 3,4),
           ('No',       5,6)]

table = TreeColor(frame_list, columns=headers, show="headings")    # создать таблицу на Frame

for header in headers:
    table.heading(header, text=header, anchor="center")            # заполнить заголовки столбцов и выровнить по центру
    table.column(header, anchor="center", minwidth=0, width=90)    # выровнить по центру и задать ширину

for row in list:
    table.insert('',tk.END,values=row)

### Scrollbar
ScrollTable = tk.Scrollbar(frame_list, command=table.yview)
ScrollTable.pack(side=tk.RIGHT, fill=tk.Y)
table.configure(yscrollcommand=ScrollTable.set)                    # изменить конфигурацию дочерних параметров Treeview

frame_list.pack(expand=True, fill=tk.BOTH)                         # растягивать Frame на Window
table.pack(expand=True, fill=tk.BOTH)                              # растягивать TreeView на Frame

### Calendar and Pack (положение вместо place)
cal = Calendar(Tab_Calendar, selectmode = 'day', year = 2023, month = 5)
cal.pack(expand=True)                                              # виджет заполняет все пространство контейнера
cal.pack(fill=tk.BOTH)                                             # виджет будет растягиваться, чтобы заполнить свободное пространство вокруг (исключая отступы)
cal.pack(pady = 20)                                                # отступы виджета от границ контейнера Tab_Calendar по вертикали (Y)
cal.pack(padx = 20)                                                # отступы по горизонтали (X) относительно контейнера Tab_Calendar

### Anchor
cal.pack(anchor="center")                                          # помещает виджет в положение по центру (закомментировать fill)
# cal.pack(anchor="n")                                             # положение вверху по центру
# cal.pack(anchor="e")                                             # положение в правой части контейнера по центру
# cal.pack(anchor="s")                                             # положение внизу по центру
# cal.pack(anchor="w")                                             # положение в левой части контейнера по центру
# cal.pack(anchor="nw")                                            # положение в верхнем левом углу
# cal.pack(anchor="ne")                                            # положение в верхнем правом углу
# cal.pack(anchor="se")                                            # положение в нижнем правом углу
# cal.pack(anchor="sw")                                            # положение в нижнем левом углу

def grad_date():
    date.config(text = "Selected Date: " + cal.get_date())         # функция изменения Text в Lable

date = tk.Label(Tab_Calendar, text = "")                           # создать Lable
date.pack(side='left',padx=20,pady=20)                             # выравнить виджет (side) по левой стороне и добавить отступ

tk.Button(Tab_Calendar, text = "Get Date", command = grad_date     # привязать к кнопке функцию
          ).pack(side='right',padx=20,pady=20)                     

### Canvas
canvas = tk.Canvas(Tab_Canvas, bg="white", width=280, height=250)
canvas.pack()

def select():
    canvas.itemconfigure(line, fill=selected_color.get())

red = "red"
blue= "blue"

selected_color = tk.StringVar(value=red)

line = canvas.create_line(
    20,                             # отрезаем слева на право
    25,                             # угол по вертикали слева
    250,                            # увеличиваем вправо
    25,                             # угол по вертикали справа
    fill=selected_color.get()
    ) 
canvas.create_rectangle(220,50,50,200,fill="#80CBC4",outline="#004D40")

red_btn = ttk.Radiobutton(Tab_Canvas, text=red, value=red, variable=selected_color, command=select)
red_btn.pack()
blue_btn = ttk.Radiobutton(Tab_Canvas, text=blue, value=blue, variable=selected_color, command=select)
blue_btn.pack()

### bind(событие,функция)
def right_click(event): 
    btn["text"] ="Right Click"

def double_click(event): 
    btn["text"] ="Double Click"

btn = ttk.Button(Tab_Canvas, text="Click")
btn.pack()

btn.bind("<ButtonPress-3>", right_click)
btn.bind("<Double-ButtonPress-1>", double_click)

window.bind("<Control-KeyPress-F2>", right_click)                  # Ctrl+F2
window.bind("<Control-KeyPress-F3>", double_click)                 # Ctrl+F3

### Отслеживает изменения значения переменной (trace_add)
def check(*args):
    if name.get()=="admin":
        result.set("Имя занято")
    else:
        result.set("Доступно")

name = tk.StringVar()
result = tk.StringVar()

name_entry = ttk.Entry(Tab_Canvas, textvariable=name) 
name_entry.pack(padx=5, pady=5)

check_label = ttk.Label(Tab_Canvas, textvariable=result)
check_label.pack(padx=5, pady=5) 

name.trace_add("write", check)

### Listbox and Grid
Tab_ListBox = ttk.Frame(tab_control)
tab_control.add(Tab_ListBox, text='ListBox')

def delete():
    selection = languages_listbox.curselection()
    # или получить удаляемый элемент по индексу
    # selected_language = languages_listbox.get(selection[0])
    languages_listbox.delete(selection[0])

def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)
 
language_entry = ttk.Entry(Tab_ListBox)
language_entry.grid(row=0, column=0, padx=6, pady=6)
ttk.Button(Tab_ListBox, text="Add", command=add).grid(column=1, row=0, padx=6, pady=6)

languages_listbox = tk.Listbox(Tab_ListBox)
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=tk.EW, padx=5, pady=5)
languages_listbox.insert(tk.END, "Python","PowerShell","C#","JS")

ttk.Button(Tab_ListBox, text="Delete", command=delete).grid(row=2, column=1, padx=5, pady=5)

window.mainloop()