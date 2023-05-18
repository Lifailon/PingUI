import os
import re
import threading
from datetime import datetime

def ping_run(ip,net,arr):
    addr = net + str(ip)                            # join ip-address (1.2.3. + 4 octet)
    ping_command = "ping -n 1 "                     # ping key
    ping = ping_command + addr                      # creat full command ping
    ping_out = os.popen(ping)                       # run ping
    out = ping_out.readlines()                      # creat array
    time = re.split("\s",out[-1])[-3]               # regex time ping
    if (time == "0"):
        output = addr + " | CURRENT"
        arr += [output]
        return
    if "TTL" in out[2]:                             # search TTL match
        output = addr + " | Available (" + str(time) + " ms)"
        arr += [output]
    else:
        output = addr + " | Not available"
        arr += [output]

def sort_key(e):
    e1 = (re.split(r"\s", e))[0]                    # pick up ip
    e2 = re.split(r"\.", e1)                        # creat array
    x2 = [int(x) for x in e2]                       # convert string to int
    return x2[-1]                                   # sort on 4 octet

def ping_list(subnet):
    arr = []                                        # creat global array
    split = subnet.split('.')                       # split ip
    net = split[0]+"."+split[1]+"."+split[2]+"."    # join three octet
    t1 = datetime.now()                             # start time

    for ip in range(1, 255):                        # range 1..254 to foreach
        thread = threading.Thread(target=ping_run, args=[ip,net,arr])
        thread.start()

    while len(threading.enumerate()) != 1:          # work to no active threads
        continue

    arr = sorted(arr, key=sort_key)                 # sort the array
    
    ok = 0                                          # start position for cout avaliable hosts
    no = 0                                          # start position for cout not avaliable hosts

    for a in arr:
        if "Not" in a:
            print("\033[31m{}".format(a))
            no += 1
        else:
            print("\033[32m{}".format(a))
            ok += 1

    t2 = datetime.now()                             # end time
    total = (t2 - t1)                               # get run time
    print("\033[0m{}".format(" "))                  # default color
    print("Total ping hosts:   ", len(arr))         # count all hosts
    print("Avaliable hosts:    ", ok)               # count avaliable hosts
    print("Not avaliable hosts:", no)               # count not avaliable hosts
    print("Run time:", total)

subnet = "192.168.3.0"
ping_list(subnet)