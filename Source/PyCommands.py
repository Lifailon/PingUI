### Clear
import os
def clear():
    os.system(
    'cls' if os.name == 'nt'
    else 'clear')

clear()

### Methods
import pandas as pd
df = pd.DataFrame([[10, 20, 30], [100, 200, 300]],
                  columns=['foo', 'bar', 'baz'])
def get_methods(object, spacing=20):
  methodList = []
  for method_name in dir(object):
    try:
        if callable(getattr(object, method_name)):
            methodList.append(str(method_name))
    except Exception:
        methodList.append(str(method_name))
  processFunc = (lambda s: ' '.join(s.split())) or (lambda s: s)
  for method in methodList:
    try:
        print(str(method.ljust(spacing)) + ' ' +
              processFunc(str(getattr(object, method).__doc__)[0:90]))
    except Exception:
        print(method.ljust(spacing) + ' ' + ' getattr() failed')

#get_methods(df['foo'])
get_methods(sorted)

### Тип данных
test = input()                      # ввода переменной с клавиатуры
text = str(input("input number: ")) # предопределить тип данных
type(1)                             # тип данных int (Integer)
type("1")                           # тип данных str (String)
type([1,2,3])                       # тип данных list  [] (Array)
type((1,2,3))                       # тип данных tuple () (кортеж)
type(1.2)                           # тип данных float (число с плавающей точкой)

### Sleep
import time
time.sleep(0.01)

### Platform
import platform
oc = platform.system()
oc == "Windows"

### Sorted
arr = ["192.168.11.131 - NOT", "192.168.11.21 - OK", "192.168.11.11 - NOT"]
def sort_key(e):
    e1 = (re.split(r"\s", e))[0]    # разбить на массив, забрать только ip-адрес
    e2 = re.split(r"\.", e1)        # разбить на массив из цифр
    x2 = [int(x) for x in e2]       # преобразовать в массиве тип данных String на Int
    return x2[-1]                   # сортировать по последнему индексу в массиве (4-му октету)

sorted(arr)                         # сортировка по первому элементу
sorted(arr, key=len)                # сортировка по длинне
sorted(arr, key=sort_key)           # сортировка по INT

### Regex
import re
string = "test text new"
pattern = "text"
repl = "no text"
re.match(pattern, string)           # ищет pattern в начале строки string
re.search(pattern, string)          # ищет pattern по всей строке string, возвращает Match-объект с первым совпадением, остальные не находит
re.finditer(pattern, string)        # ищет pattern по всей строке string, возвращает Match-объекты для каждого найденного совпадения
re.findall(pattern, string)         # ищет pattern по всей строке string, возвращает список со всеми найденными совпадениями
re.split(pattern, string)           # разделяет строку string по подстрокам, соответствующим pattern
re.sub(pattern, repl, string)       # заменяет в строке string все pattern на repl
re.compile(pattern)                 # собирает регулярное выражение в объект для будущего использования в других re-функциях

print("s\ta\np\nbbb")                           # писать регулярные выражения
print(re.search (r"32", "system 32 32"))        # возвращает span-объект с индексом начала и конца
result = re.finditer (r"32", "system 32 32")    # возвращает span-объекты
for match in result:
    print (match)
print(re.findall (r"32", "system 32 32"))       # возвращает массив ['32', '32']
print(re.split (r"\s", "system 32 32"))         # создать массив
print(re.sub (r"32", "64", "system 32 32"))     # заменить все 32 на 64
print("1", "2", "3", sep=", ")                  # сепаратор

# \                   # экранирование
# . 	              # любой символ, кроме новой строки (\n)
# ^                   # начало строки (\A)
# $                   # конец строки (\Z)
# \b	              # начало или конец слова
# \B	              # середина слова
# [abc123]            # любой символ из указанных в скобках. Символы можно задавать как перечислением, так и указывая диапазон через дефис
# [^A-Za-z]           # любой символ, кроме указанных в скобках
# [0-9] | [IVXLCDM]   # логическое ИЛИ, будет находить совпадение, если цифра является либо арабской, либо римской
# \d                  # любая цифра
# \d{1,4}             # цифра, повторяющаяся от 1 до 4 раз подряд
# \d{4}               # цифра, повторяющаяся 4 подряд
# \d{4,}              # цифра, повторяющаяся от 4-х раз подряд
# \d{,4}              # цифра, повторяющаяся от 0 до 4 раз подряд
# \d{1,}              # цифра, повторяющаяся от одного (\d+)
# \D	              # любой символ, кроме цифры. То же самое, что [^0-9]
# \w	              # любая буква, цифра и нижнее подчёркивание
# \W	              # любой символ, кроме буквы, цифры и нижнего подчёркивания
# \s                  # пробел, новая строка, табуляция
# \S	              # любой символ, кроме пробельного
# \n                  # новая строка

### Операторы
5 == 5  # True
5 != 5  # False
5 >= 5  # True
5 > 6   # False
5 < 6   # True

'Fast' in 'FastEthernet' # True
vlan = [10, 20, 30, 40]
10 in vlan # True           # проверка на наличие
10 not in vlan # False      # проверка на отсутствие
15 in vlan and 10 in vlan   # False № И
15 in vlan or 10 in vlan    # True # ИЛИ

### IF-ELSE
password = "1234567"
#password = "123456789012345678"
if len(password) < 8:
    print("Слишком Короткий пароль")
elif len(password) > 16:
    print("Слишком длинный пароль")
else:
    print("Пароль валидный по длинне")

### File
file = open(r"C:\Users\Lifailon\Desktop\test.txt","r") # открыть файл на чтение, символ r"" вначале подавляет экранирование (регулярные выражения)
file.name
file.mode
# r – открыть файл для чтения
# w – открыть файл для записи
# a – открыть файл для добавления нового содержимого (записи в конец файла, без удаления существующих)
# x – открыть файл с целью создания, если файл существует, то вызов функции open завершится с ошибкой
file_read = file.read()         # читать файл
file_line_1 = file.readline()   # читать строку (по порядку, по одной)
out_split = file_read.split()   # создать массив из строк
file.close()                    # закрыть файл

file = open(r"C:\Users\Lifailon\Desktop\test.txt","a") # открыть файл на запись
file.write("text1\ntext2")                             # вначале открыть, записать и потом закрыть, что бы применить все изменения 

# Построчное чтение файла
import sys
file = open(r'/etc/passwd')
for line in file:
    sys.stdout.write(line)

### GREP
with open(r"C:\Users\Lifailon\Desktop\text.txt") as file:   # открыть файл
    for line in file.readlines():                           # добавить в цикл построчный вывод
        if "test" in line:                                  # если есть слово в строке
            print(line)                                     # выводить на экран

### Module OS
#os.<function>(<params>)
import os
os.system("ping ya.ru")
print(os.name)
print(os.environ)
print('Hello, %s' % os.environ['LOGNAME'])
print(os.getenv("TMP"))
print(os.getcwd()) # pwd
os.listdir(os.getcwd()) # ls
path = r'C:\Users\Lifailon\Documents\ADReplStatus-1.3'  # создать переменную пути
os.listdir(path)
os.chdir(r"C:\Users\Lifailon\Documents")                # cd
os.startfile(r'C:\Windows\System32\cmd.exe')            # запустить
os.path.basename(r'C:\Windows\System32\cmd.exe')        # забрать имя файла
os.path.dirname(r'C:\Windows\System32\cmd.exe')         # забрать путь
os.remove("test.txt")                                   # удалить файл
os.rmdir("dir")                                         # удалить директорию
os.rename("test.txt", "pytest.txt")                     # переименовать
print(os.path.join(r'C:\Windows\System32','cmd.exe'))   # join объеденить путь
dirname,filename = os.path.split(r'C:\Windows\System32\cmd.exe') # split разбить путь и передать в переменные
print(dirname)
print(filename)

path = r'C:\Users\Lifailon\Documents\dir\2023'
if not os.path.exists(path):    # если директория недоступна (!Test-Path)
    os.makedirs(path)           # создает промежуточные в пути директории

for root, dirs, files in os.walk(path):
    print(root)                 # отобразить все дочерние пути
    for dir in dirs:
        print(dir)              # отобразить все дочерние директории
    for file in files:
        print(file)             # отобразить все дочерние файлы 

### Циклы
for i in range(10): # 0..9
    print(i)

for i in range(20, 51, +5):
    print(i)

for i in range(3):
    print("Num: " + str(i))

i = 0
while i < 10:           # работает, пока True
    print(i)
    i += 1
    
### Array
arr = [22, 11, 33]
arr.sort()              # отсортировать массив
print(arr[1])           # значение 2-го индекса

len(arr)                # кол-во элементов в массиве (Count)
arr.count(33)           # кол-во одинаковых элементов по имени (wildcard) значения
arr.insert(0,"text")    # добавить в начало (по номеру индекса): ['text', 22, 11, 33]
arr.append("text")      # добавить в конец
arr.pop(1)              # удалить элемент массива по индексу
arr.remove(333)         # удалить элемент по имени
arr.clear()             # очистить массив

for i in arr:
    print(i)            # построчный вывод

arr_2 = [[1,2],[3,4]]   # двухмерный массив
print(arr_2[1][1])

### Срез
arr = [[1,2],[3,4],[5,6]]
print(arr[::-1])        # читать с конца
print(arr[1:])          # читать с второго индекса
print(arr[0:2])         # читать с первого по второй

### Class.Object
class TestClass:
    default_color = "green"             # статические атрибуты, доступ к которым можно получить не создавая объект класса 
    def __init__(self, width, height):  # динамические атрибуты, задаются через self, который является ссылкой на текущий экземпляр класса
        self.width = width
        self.height = height

TestClass.default_color
rect = Rectangle(10, 20)                # для доступа к width и height предварительно нужно создать объект класса Rectangle
rect.width
rect.height

Rectangle.default_color = "red" # изменить значение класса

class TestClass:
    @staticmethod               # Статический метод создается с декоратором @staticmethod
    def ex_static_method():
        print("static method")
    @classmethod                # классовый – с декоратором @classmethod, первым аргументом в него передается cls
    def ex_class_method(cls):
        print("class method")
    def ex_method(self):        # обычный метод создается без специального декоратора, где первым аргументом передается self
        print("method")

TestClass.ex_static_method()
TestClass.ex_class_method()
m = TestClass()
m.ex_method()

### HashTable/dict (словарь - ассоциативный массив)
# Ключевые значения являются именами индексов массива, в котором хранятся данные
dict = {
"UserName": "Alex",
"HostName": "book-14"
}
dict["UserName"]

### pip
# при установки python: Add Python to PATH
python -V                   # установленная версия Python
python -m pip install --upgrade pip
pip list # pip freeze       # список установленных пакетов
pip install -U              # обновление пакеты
pip search PackageName      # поиск пакета
pip show PackageName        # информация о пакете

# pip install tabulate
from tabulate import tabulate
table = [["T1",10,20],
        ["T2",11,21]]
print(tabulate(table))

# pip install prettytable
from prettytable import PrettyTable
t = PrettyTable(['Name', 'Age'])
t.add_row(['T1',10])
t.add_row(['T1',20])
t.add_row(['T2',11])
t.add_row(['T2',12])
print(t)

### VirtualEnv (виртуальное окружение)
pip install virtualenv
pip install virtualenvwrapper-win
mkvirtualenv env-name	    # создать новое окружение
workon                      # отобразить список окружений
workon env-name	            # сменить окружение
deactivate	                # выйти из окружения
rmvirtualenv env-name	    # удалить окружение

### GUI
pip install PySimpleGUI
pip install wxPython
pip install PyQt6
pip install pyqt-tools
pip install Kivy

### Calendar
pip install tkcalendar

### QR
pip install segno

### PyGame
pip install pygame
python3 -m pygame.examples.aliens

### Matplotlib (графики)
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 20, 25]
plt.plot(x, y)
plt.show()

### Threading (потоки)
for ip in range(1, 255):
    thread = threading.Thread(target=ping_run, args=[ip,net,arr])   # передать в поток выполнение функции
    thread.start()                                                  # запустить поток

len(threading.enumerate())                                          # вывести кол-во активных потоков
threading.enumerate()[2].is_alive()                                 # получить статус работы потока (True - работает) по индексу
threading.enumerate()[2]._is_stopped
threading.enumerate()[1]._args[0]                                   # значение первого аргумента переданного в функцию выполняемого потока
thread.join()                                                       # блокирует вызывающий поток до тех пор, пока не завершится поток, чей метод .join() вызван 
thread.join(1.5)                                                    # в скобках указывается время ожидания в секунда
# Если в потоке thread1 был вызван метод потока thread2.join(), то поток thread1 будет приостановлен до тех пор, пока выполнение thread2 не завершится.
thread.ident                                                        # идентификатор потока
thread.name                                                         # имя потока
threading.main_thread()                                             # основной поток