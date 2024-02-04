#https://www.facebook.com/mistyxd0.2

#RANI ISE BAXCK
#OPEN SOURCE 😥
#NEED FOR PROXY

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
    f"""    ____  ___    _   ______
   / __ \/   |  / | / /  _/
  / /_/ / /| | /  |/ // /  
 / _, _/ ___ |/ /|  // /   
/_/ |_/_/  |_/_/ |_/___/   
                           """
)


import requests

# API headers
headers = {
    "Content-Type": "application/json",
    "X-API-Key": "dh6345sdsh3sdr8s98fd8",  # Replace with your actual API key
}

# Base URL of the API
base_url = 'http://128.140.99.16:5622'

# Email for Instagram registration
email = input('Enter your email: ')
 # Note Always Use least Flagged Domains for email like gmail,outlook,hotmailInstagram Is Very Strict With Email Account Registratin They Block or susspend Account Registered With Temp Mails


# Proxy details for making requests
proxy_path = f'sp99801092:e2oBKm2z9fsBl09lsh@us.smartproxy.com:10000'  # Replace with your actual proxy details. username of your paid proxy " : " password of Your proxy " @ " Host of proxy " : " Port of proxy  " example =   smartuser:ERvccvRRTgfd@gate.smartptoxy.com:7777 You Can Also Use Free Proxy Of Any Country " Only Proxy Should Be alive

# Country code for advanced features Of This Api This Will Make Country Info Spoofing To Reduce Bot Detection By Instagram
country_code = 'US'

# Data payload for the API request
data = {
    "email": email,
    "proxy": proxy_path,
    "country_code": country_code
}

#Guys If Want to pass Your Username And Password
# add two parameters data =
"""{
    "full_name":'gamer', 
    "password":'gamerrrrr',
    "email": email,
    "proxy": proxy_path,
    "country_code": country_code
}
"""

# Sending an SMS containing OTP to the provided email
sendsms = requests.post(
    url=f'{base_url}/api/insta/android/email/send',
    json=data,
    headers=headers,
    timeout=200
)

# Checking if 'user_agent' is in the response text
if 'user_agent' in sendsms.text:
    print('OTP sent successfully to your email...')
    otp = str(input("Enter OTP: "))

    # Data for the second API request, including the response from the first API
    data = {
        "otp": otp,
        "proxy": proxy_path,
        "client_data": sendsms.json()
    }

    # Verifying OTP and creating an account using email
    create = requests.post(
        url=f'{base_url}/api/insta/android/email/create',
        json=data,
        headers=headers,
        timeout=200
    ).json()

    print(create)
else:
    print(sendsms.text)
