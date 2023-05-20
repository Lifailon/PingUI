### Python version 3.11.3
### PingUI version 0.1
### Source: https://github.com/Lifailon/PingUI
 
import os
import re
import time
import threading
import webbrowser
import tkinter as tk
from tkinter import ttk
from datetime import datetime

######################################################################## DEF
### run thread ping
def ping_run(ip,net,arr):
    addr = net + str(ip)
    ping_command = "ping -n 1 "
    ping = ping_command + addr  # + " -w 1"
    ping_out = os.popen(ping)
    out = ping_out.readlines()
    time = re.split("\s",out[-1])[-3]
    if (time == "0"):
        output = addr + " CURRENT "  + str(time)
        arr += [output]
        return
    if "TTL" in out[2]:
        output = addr + " Available " + str(time)
        arr += [output]
    else:
        output = addr + " Not"
        arr += [output]

### creat subnet array for thread
def ping_list(subnet):
    arr = []
    split = subnet.split('.')
    net = split[0]+"."+split[1]+"."+split[2]+"."
    t1 = datetime.now()

    for ip in range(1, 255):
        thread = threading.Thread(target=ping_run, args=[ip,net,arr])
        thread.start()

### slow mode (work to end active threads)
    if Debug_mode.get() == True:
        while len(threading.enumerate()) != 1:
            continue

### fast mode (simulate ping for output)
    if Debug_mode.get() == False:
        time.sleep(1)
        if Avaliable_mode.get() == False:
            not_ping_len = len(threading.enumerate())
            for arg in threading.enumerate()[1:not_ping_len]:
                arr += [net + str(arg._args[0]) + " Not"]

    arr = sorted(arr, key=sort_key)

    ok = 0
    no = 0

    for a in arr:
        if "Not" in a:
            no += 1

        else:
            ok += 1
    
    for item in table.get_children():
        table.delete(item)                  # clear treeview

    for row in arr:
        row = row.split(" ")
        table.insert('',tk.END,values=row)  # add treeview

    t2 = datetime.now()
    total = (t2 - t1)
    runtime = "Avalibale: " + str(ok) + "  |  Not avaliable: " + str(no) + "  |  Run time: " + str(total)
    statusbar.configure(text=runtime)
    
def button_ping():
    subnet = ip.get()
    ping_list(subnet)

### sort treeview ip and array
def sort_key(e):
    if str(type(e)) == "<class 'tuple'>":
        e1 = e[0]
    else:
        e1 = (re.split(r"\s", e))[0]
    e2 = re.split(r"\.", e1)
    x2 = [int(x) for x in e2]
    return x2[-1]

### sort time
def sort_time(e):
    if e[0] == "":
        return 999
    else:
        e1 = int(e[0])
        return e1

### sort columns in treeview
def sort_col(col, reverse):
    list = [(table.set(id, col), id) for id in table.get_children("")]
    
    if col == 0:
        list = sorted(list, key=sort_key, reverse=reverse)

    if col == 1:
        list.sort(reverse=reverse)

    if col == 2:
        list = sorted(list, key=sort_time, reverse=reverse)
        
    for line_number, (_, id) in enumerate(list):
        table.move(id, "", line_number)

    table.heading(col, command=lambda: sort_col(col, not reverse))

### treeview color
class TreeColor(ttk.Treeview):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag_configure("green", background="#BDFCC9")
        self.tag_configure("red", background="#EDEDED")

    def insert(self, parent_node, index, **kwargs):
        item = super().insert(parent_node, index, **kwargs)
        values = kwargs.get('values', None)
        if re.search("Not", values[1]):
            super().item(item, tag='red')
        else:
            super().item(item, tag='green')
        return item

### button event color
def button_enter(e):
    button_ping["bg"] = "#d7e4f2"
    label_image.configure(background="#d7e4f2")

def button_leave(e):
    button_ping["bg"] = "#DCDCDC"
    label_image.configure(background="#DCDCDC")
    
### entry event watermark
def watermark_click(event):
    global temp
    # event_now = str(window.focus_get())
    # print(event_now)
    event_now = str(event.widget)
    if event_now == ".!entry":
        if ip.get() == temp and ip.get() != entry_default:
                return
        else:
            ip.configure(fg="black")
            ip.delete(0, tk.END)
    if event_now != ".!entry":
        if ip.get() == "":
            ip.configure(fg="silver")
            ip.insert(0, entry_default)
        else:
            temp = ip.get()

def link():
    webbrowser.open("https://github.com/Lifailon", new=2)
######################################################################## end DEF

window = tk.Tk()
window.title("PingUI")
window.geometry("1280x717")
window.configure(bg="#EDEDED")

### menu
menu = tk.Menu(window)
menu_file = tk.Menu(menu, tearoff=0)
menu_file.add_command(label='Exit', command=quit)
menu.add_cascade(label='File', menu=menu_file)

Debug_mode = tk.BooleanVar()
Debug_mode.set(False)

Avaliable_mode = tk.BooleanVar()
Avaliable_mode.set(False)

menu_mode = tk.Menu(menu, tearoff=0)
menu_mode.add_checkbutton(label="Show only Avaliable", onvalue=1, offvalue=0, variable=Avaliable_mode)
menu_mode.add_checkbutton(label="Slow mode (Debug)", onvalue=1, offvalue=0, variable=Debug_mode)
menu.add_cascade(label='Mode', menu=menu_mode)

menu_help = tk.Menu(menu, tearoff=0)
menu_help.add_command(label='Source GitHub', command=link)
menu.add_cascade(label='Help', menu=menu_help)
window.config(menu=menu)

### button
button_frame = tk.Frame(window, highlightbackground="silver", highlightthickness=1)
button_ping = tk.Button(button_frame, text="Start", width=18, height=3, bg="#DCDCDC", borderwidth=0, activebackground= "#d7e4f2", command=button_ping)
button_ping.pack()
button_frame.pack(anchor="nw", pady=3, padx=3)

button_ping.bind("<Enter>", button_enter)
button_ping.bind("<Leave>", button_leave)

### from PIL import Image, ImageTk
### image = Image.open(".\Image\Start_48px.png").resize((42,42))
### image_button = ImageTk.PhotoImage(image)

image = "iVBORw0KGgoAAAANSUhEUgAAACoAAAAqCAYAAADFw8lbAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAdeSURBVFhHxVlbbFtFGp6ZY6etV9qHRQIktNrSJi3vqJCL7SS1kzTXpiUbVkKIPiDBC/CAeCj7VGmFYCXUy6phywNdIVbazabEbUraOJc6TuIkKkVQAjSJk7aCldhKXWhoLvY5M7PfP7ZDWmVL7MbpZ/3nnLmcmW/++f9/Zo45A/7wbQP/x2/P6hdnK11z3PM80/wAZ/whzfQMY7ojyVVX6PFzP1Ld3880WspKqlNbezSlNwp8/2Q1/3hn2HTaGq9/iwtx0JSsBNdfKKUP2TzZHdrWm3h2spUr123+r+3dKl0j7+Ct8TqrvbBbtszUVQjOzyLrV8gnAgJCAyChZ6a1bsf1OAhGKd06W+dKCiVDW8/nXbvCxXm6E74LD0TShhhiAAq1gFAdxThrZZyHWmbr322J1+5s39btEMn9s7WZ+nmDsdHma/UFbsWO4vFliIRYlL8KVpZdUVqfTGx2jp99LDwP7QqbKd25LT/aNUT3xRu3WFy9h2l9Acl7ESWktPtznTFkvHNqe3eIEi3xeq6EZB+vM+EU0akqjxCuNs75WohmsFwPhuGgpS7mUn889bvz31Des5N7eNJivLPw/Lo4nCH6zFTQwyx3G5LZECWQ1kjSNqrnNdfHpKOOnN4RvkE5sGUroZXqKrq/cJbWaA00KtqQypZoBhkSpj0431VkHCKT7SzqmaO8ffEaq7Owh9rOCUYTSeHA6FK+naPwtNAzmuKPI1z8DbTbm+PVtdQHkWydqnM1z1SZwWQL81Jj3O9xsS1tWI1eQF+5aDTVEID3zQ1phWdqJwH5UHN1IrQ9fIkKm6errVBROCvtmvab4hUeixXkYqO/hJVtXcecfcSEczi0beDm3ukqQZN4ekdvemz3hiHaHK/0MJaTM60FRGRFONNfwjwOny4Kn6TU/m/ruVxMsl8ibIjumQ14NkkLU5+zM60FRJb6I8FaoQdhxwdDO3vHqZDQNB0UZ4r6Vg1n6bDCzbDzLFiKzZ1sV2AprtSCDe2dqvprw1RwK4oYkWycrLIa4ruNAlfCZNRdDXpckrdhhPnU6EoQZ4LpH4kbMNc/YdvxzzOF/Sb+Nl2Bdp/4WbtGo9zBPgSGkx7xRgjthEjomcg8DMbHECs6G6cDzzR853UTyaap4LLCDFFhwwFRHXazoYILicAzMpjEtRRkO/jCpr/UTlQ+cmZHn2ycCqQ40sXhsNHM+DZQMj88o3cN7WmYHaXZS5ZbvFv3TeDXXTv6VcOVADdEsajQLfXKgxULQs5Ge9/nhNBNyGbarUXKRo1iV1R/sAIyxhDpV+obKXZ9sn1AGqJMLKZtJlP3wYuhk9DMupSmSJeMa91V90GJwkZB6CS8K6FikVdjTsPloGWIOuBLlVZ9bSOFw5m4FiqhhFqUf5c37DMoYMlbSypFFKZKFoF1zQQ1c98IWe4LM80RnhxtyXnF5II+kfxJvt5XPzpXPeQVYd8wGS7mP5nEgGhUQOa+EaC+OPHVXC4oS95WMTkvW5z/8lcGAiP/qYn6LZCk8aRslDlUN63+jRFcjJDDCDmnbqh59Zq8pff1eodPDdRG7JpouejxR2k5NzABdM/lEg9zY5uX3eEuF2SYCi1BcpHZcJoPlC3f7i+PXaMKtWOVlqOk6i2NUr1lGKLll8s8m93Y5uV+ZloLaAo5IiSHFpVa0oNK6YMDZSPL27zqYb8Ie6Nmqu+GIVo54fW4Leye8rVxJjtUzFI2jlNL7DKIHun3j5iN897rAb74b5uF79Lg3TBEd0+UeVyWWP+NMzwZNEEQ05zU1xF2PhKaH+7zxm4GL3kFs5nuKx6+J8EMDNHgxNMecce5njYI2cI0BVC/2GNAi9rWFggmVFJ/qBPyxIWKcXO4CwyVWf2+EVLImmFar/iqxOPmFojev0Zh50orbN1w9oQme2CLRyPlo+eobM+Q32ULKfvLRtakxZUw4YnOtlm/eSfodRPgJMKNuq2vIi4ekDft1gzJ4FCpdd4XdXIhSTAarfy6DMdllotGaYppURNYh5laUvPaZsfgMEcigVFzpAiOlVm2rdWgL3ZfukgTLfXgtJWdM6UdBdNMQduBnMUi+OYF37j5SFY9UcLtHxi/4BtdNdxkC0M08PmuLcztem+NAT8VbiRIkjcvsTHc34n4x8xnx8BXPq5vOWygdPQ+relOGKKlHU8WbC4qOMpd/N4fcjPhBlswltRXcD9pM/fxmG94PhArERKnn0gxfS5df/Da7/3i3KNRVfFZ8RuigP8ZZOjTuDtVvAxjiwg1FPt+gEeflEn5/tDui5NUWDFcLCLesXWZ4v8HsXgtYbQql9RFhJN5EHJjQsny6JeKh9jKqgV486Jqh0c3g9TrRNIfKXOVjxXzfJMk8KcHn+Tj5ZfMdPliT71lFfCDbJMpM6szvBiiv2COPmTPye7R+s8SNdNBvvT9T3zQN553ghkYbXoju/hwxUX9aEehq+iR3zwvuD6gOX8IFGeY4h1qYbFruOZL84dYRbTEUsxWUf+nebHF1cHY/wDAxoioe35HtAAAAABJRU5ErkJggg=="
image_button = tk.PhotoImage(data=image)

label_image = ttk.Label(button_frame, image=image_button, background="#DCDCDC")
label_image.place(x=5,y=3)

### entry
entry_default = "192.168.3.0"
ip = tk.Entry(window, width=100, fg="silver")
ip.place(x=30, y=10)
ip.configure(font="Arial 10")
ip.insert(0, entry_default)
ip.pack(anchor="sw", pady=3, padx=3, fill=tk.BOTH)

temp = ""
window.bind('<Button-1>', watermark_click)

### status bar
statusbar = tk.Label(window, bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill="both")

### frame for treeview
frame = tk.Frame(window)
frame.pack(side=tk.LEFT,anchor=tk.NW,padx=3,pady=3)

### columns treeview
columns = ["IP-Address", "Status", "Time(ms)"]
table = TreeColor(frame, columns=columns, show="headings")

table.heading("IP-Address", text="IP-Address", anchor="center", command=lambda: sort_col(0, True))
table.heading("Status", text="Status", anchor="center", command=lambda: sort_col(1, False))
table.heading("Time(ms)", text="Time(ms)", anchor="center", command=lambda: sort_col(2, False))
 
table.column("#1", anchor="center", minwidth=0, width=90)
table.column("#2", anchor="center", minwidth=0, width=90)
table.column("#3", anchor="center", minwidth=0, width=90)

### scroll bar for treeview
ScrollTable = tk.Scrollbar(frame, command=table.yview)
ScrollTable.pack(side=tk.RIGHT, fill=tk.Y)
table.configure(yscrollcommand=ScrollTable.set)

frame.pack(expand=True, fill=tk.BOTH)
table.pack(expand=True, fill=tk.BOTH)

window.mainloop()