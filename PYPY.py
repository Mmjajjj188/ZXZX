import random
import requests
import time
from colorama import *

req = requests.session()
print(f"""{Fore.BLUE}[!] Checker For Iphone

Check For Iphone Started
By @ZZSNN

==> ....

Good Luck

 ========================
 ... """)
time.sleep(6)

chrs = 'abcdefg_hijklmnopqrstuvwxyz1234567890'
a = 0
b = 0
while True:
    pass
    lst = str("".join(random.choice(chrs)for x in range(4)))
    url = f'https://www.tiktok.com/@{lst}?'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
    }
    reqsnd = req.get(url, headers=headers)
    if reqsnd.status_code == 404:
        b += 1
        print(
            f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{b}{Fore.LIGHTBLACK_EX}]{Fore.LIGHTGREEN_EX} Hunt | {Style.BRIGHT}{Fore.LIGHTWHITE_EX} {lst} {Fore.LIGHTGREEN_EX}|")
        with open("hunted by @ZZSNN.txt", "a")as ZZSNN:
            ZZSNN.write(lst + "\n")
            time.sleep(6)
    else:
        a += 1
        print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{a}{Fore.LIGHTBLACK_EX}]{Fore.LIGHTRED_EX} Not Available | {Style.BRIGHT}{Fore.LIGHTWHITE_EX} {lst} {Fore.LIGHTRED_EX}|")
        time.sleep(6)
