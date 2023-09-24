import pyautogui
import pyscreenshot as ss
import webbrowser as wb
from time import sleep
import os
from invoke import task
import sys

Target = sys.argv[1]
Dir = sys.argv[2]


with open(f"{Target}","r")as f:
    c = f.readlines()
    lines = len(c)
    print(c)
    x = 0
    
    while(x<lines):
        
        f = open(f"{Target}","r")
        content = f.readlines()[x]
        print(content)
        url = f"{content}"
        wb.open(url)
        sleep(10)
        im = ss.grab()
        im.save(f"{Dir}/{x}.jpg")
        os.system("pkill -f 'firefox'")
        os.system("pkill -f 'chrome'")
            
        x = x + 1