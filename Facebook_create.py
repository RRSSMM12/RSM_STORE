# https://www.facebook.com/mistyxd0.2
#open source by RANI 
#WLCM TO FACEBOOK  AUTO CREATE
#VERSION :- 1

import requests
import os
import time
import sys
import webbrowser
from fake_useragent import UserAgent


E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(23.0 / 8000)

to(
    f"""RRRR   AA  N   N III 
R   R A  A NN  N  I  
RRRR  AAAA N N N  I  
R R   A  A N  NN  I  
R  RR A  A N   N III     """
)



import requests
from bs4 import BeautifulSoup
import random
S='\033[30m' 
F='\033[31m'   
A='\033[32m' 
T='\033[33m'
M='\033[34m'
N='\033[35m'
Z='\033[36m' 
B='\033[37m'
H='\033[91m' 
class RANI1():
    def __init__(self):
        self.done = False
        self.cookies = {
            "lsd": "","jazoest": "", "ccp": "","reg_instance": "","submission_request": "","reg_impression_id": ""
        };self.password = "".join(random.choice("1234567890qpwoeirutyalskdjfhgmznxbcv") for _ in range(10))
        self.email = "Rani" + "".join(random.choice("1234567890qpwoeirutyalskdjfhgmznxbcv") for _ in range(15));self.Name = "Rani";self.Name2 = "kumari";self.admin()
    def admin(self):
        print("FACEBOOK ID CREATE");self.get_cookies()
        print("");self.register()
    def get_cookies(self):
        url = "https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        lsd = soup.select_one('input[name=lsd]')['value']
        jazoest = soup.select_one('input[name=jazoest]')['value']
        ccp = soup.select_one('input[name=ccp]')['value']
        reg_instance = soup.select_one('input[name=reg_instance]')['value']
        submission_request = soup.select_one('input[name=submission_request]')['value']
        reg_impression_id = soup.select_one('input[name=reg_impression_id]')['value']
        self.cookies['lsd'] = lsd
        self.cookies['jazoest'] = jazoest
        self.cookies['ccp'] = ccp
        self.cookies['reg_instance'] = reg_instance
        self.cookies['submission_request'] = submission_request
        self.cookies['reg_impression_id'] = reg_impression_id

    def register(self):
        url = "https://mbasic.facebook.com/reg/submit/?cid=103";headers = {"Host": "mbasic.facebook.com","Cookie": f"datr={self.cookies['reg_instance']}","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",  "Accept-Language": "en-US,en;q=0.5","Referer": "https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr","Content-Type": "application/x-www-form-urlencoded", "Content-Length": "547","Origin": "https://mbasic.facebook.com","Dnt": "1","Upgrade-Insecure-Requests": "1","Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin","Sec-Fetch-User": "?1","Te": "trailers"};data = f"lsd={self.cookies['lsd']}&jazoest={self.cookies['jazoest']}&ccp={self.cookies['ccp']}&reg_instance={self.cookies['reg_instance']}&submission_request={self.cookies['submission_request']}&helper=&reg_impression_id={self.cookies['reg_impression_id']}&ns=0&zero_header_af_client=&app_id=&logger_id=&field_names%5B%5D=firstname&field_names%5B%5D=reg_email__&field_names%5B%5D=sex&field_names%5B%5D=birthday_wrapper&field_names%5B%5D=reg_passwd__&firstname={self.Name}&lastname={self.Name2}&reg_email__={self.email}%40gmail.com&sex=2&custom_gender=&did_use_age=false&birthday_month=9&birthday_day=5&birthday_year=1990&age_step_input=&reg_passwd__={self.password}&submit=Sign+Up";r = requests.post(url,headers=headers,data=data)
        if 'take you through a few steps to confirm your account on Facebook' in r.text:
            print(f'[•] DONE ACCOUNT ');print(f"[•] Email :" + self.email + "@gmail.com");print(f"[•] Password : " + self.password);print('===========================================')
            print('[•] RANI ISE BAXCK')
            return RANI1()
        elif 'There was an error with your registration. Please try registering again.' in r.text:
            print(' ERORR ')          
            exit()
        else:
            try:
                user_id = r.cookies['c_user']; print(f'[•]Done Create Account :  ');print(f'[•] Username : https://www.facebook.com/profile.php?id=' + r.cookies['c_user']);print(f"[•] Email :" + self.email + "@gmail.com");print(f"[•] Password : " + self.password);print(f"[•] Status : Done Create Account")
                print('[•] RANI ISE BAXCK')
                input('')
            except:
                print(r.cookies)
                print(r.text)
                input("ERROR _VPN_Job")
                exit()


RANI1
