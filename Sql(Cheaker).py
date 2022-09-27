import requests,googlesearch,time
from googlesearch import *
from colorama import Fore
G = Fore.GREEN
B = Fore.BLUE
Y = Fore.YELLOW
R = Fore.RED
W= Fore.WHITE
C = Fore.CYAN
M = Fore.MAGENTA

logo = """
\033[2;33m]     █                      █                             █
   ▄▄▄█   ▄▄▄    ▄▄▄    ▄▄▄█          ▄▄▄    ▄▄▄     ▄▄▄█   ▄▄▄
  █▀ ▀█  █▀  █  ▀   █  █▀ ▀█         █▀  ▀  █▀ ▀█  █▀ ▀█  █▀  █
 \033[2;31m █   █  █▀▀▀▀  ▄▀▀▀█  █   █         █      █   █  █   █  █▀▀▀▀
  ▀█▄██  ▀█▄▄▀  ▀▄▄▀█  ▀█▄██         ▀█▄▄▀  ▀█▄█▀  ▀█▄██  ▀█▄▄▀
"""
print(logo,'\n \033[0;90m--------------------\033[2;32mhttps://t.me/black_code_22\033[0;90m--------------------')
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
serch()                                  