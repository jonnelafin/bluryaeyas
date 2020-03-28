#!/bin/python3
#written by Elias Eskelinen aka jonnelafin
import os, time
from random import randint
import math

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def getW():
	rows, columns = os.popen('stty size', 'r').read().split()
	return int(columns)-2
def getH():
	rows, columns = os.popen('stty size', 'r').read().split()
	return int(rows)-2
def cls():
#	print("\033[H\033[J")
    print("\033[H")
def fsl():
    print("\033[H\033[J")
import atexit

def exit_handler():
    fsl()
    print("Exit")
atexit.register(exit_handler)

c = [bcolors.OKGREEN + "█" + bcolors.ENDC, bcolors.FAIL + "█" + bcolors.ENDC]
def cycle(tick):
    global c
    cls()
    t = int(str(tick)[-2:])
    if t == 0:
        c.append(c.pop(0))
    #print(tick)
    w = getW()
    h = getH()
    for y in range(h):
        b = ""
        for x in range(w):
            #print("h",end="", flush=True)
            #print( str(str(x+tick)[0]),end="", flush=True)
            #b = b + str(str(x+tick)[0])
            #b = b + str( randint(0, 9) )
            #█
            #b = b + str(str(x + randint(0, 3))[0])
#            if x > w / 2:
#                x = w - x
#            if y > h / 2:
#                y = h - x
#            if y == 0:
#                y = 1
            #y = 1
            #n2 = str(math.sin(randint(0, t*2) + x + y))
            #n = str(n2[0])
            if int(y - h / 2) == int((math.sin(x/10 + (tick*0.3))*6) * math.cos(y/-10) + math.cos(x/1.5)):
                #n = bcolors.OKGREEN + "1" + bcolors.ENDC
                n = c[0]
            else:
                n = str((x*tick)*(y+randint(0, t)))[0]
                if n == "1":
                	n = " "
                elif n == "2":
                	n = "."
                elif n == "3":
                	n = ":"
                elif n == "4":
                	n = ";"
#                elif n == "5":
#                	n = "|"
                elif n == "5":
                	n = "+"
                elif n == "6":
                	n = "/"
                elif n == "7":
                	n = "?"
                elif n == "8":
                	n = "0"
                elif n == "9":
                	n = "@"
                #n = bcolors.FAIL + "0" + bcolors.ENDC
            b = b + n
        print(b, flush=True)
#        time.sleep(0.001 / (t + 0.075))
if __name__ == "__main__":
    print("Starting...")
    tick = 0
    fsl()
    while True:
        cycle(tick)
        tick = tick + 1
#        time.sleep(0.1)
fsl()
