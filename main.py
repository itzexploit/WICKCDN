from socket import gethostbyname
from colorama import Fore , init
from requests import get
from urllib.parse import urlparse
from os import system , name
from pystyle import Colors , Colorate
from sys import exit as ex
from fake_useragent import UserAgent

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

banner = '''

    __      __ ___     ___    _  __    ___     ___    _  _   
    \ \    / /|_ _|   / __|  | |/ /   / __|   |   \  | \| |  
     \ \/\/ /  | |   | (__   | ' <   | (__    | |) | | .` |  
      \_/\_/  |___|   \___|  |_|\_\   \___|   |___/  |_|\_|  
    _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
    "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
                  [ Created By John Wick ]

'''

print(Colorate.Horizontal(Colors.red_to_blue,banner,1))

subs = [
    'www', 'mail', 'webmail', 'blog', 'news', 'mx' , 'ns' , 'dns',
    'support', 'help', 'dev', 'test', 'staging', 'demo', 'beta', 'stage',
    'app', 'api', 'cdn', 'static', 'media', 'images', 'video', 'music',
    'chat', 'stats', 'wiki', 'docs', 'files', 'download', 'portal', 'crm',
    'admin', 'dashboard', 'panel', 'login', 'auth', 'register', 'signup',
    'subscribe', 'unsubscribe', 'feedback', 'contact', 'about', 'career',
    'jobs', 'partners', 'affiliate', 'investor', 'press', 'newsroom',
    'events', 'conference', 'summit', 'forum', 'community', 'network', 'marketplace',
    'store', 'shop', 'auction', 'deal', 'offer', 'sale', 'discount', 'coupon',
    'gift', 'reward', 'cashback', 'charity', 'donate', 'fund', 'sponsor', 'survey',
    'quiz', 'poll', 'contest', 'game', 'gambling', 'lottery', 'bet', 'casino', 'poker',
    'sport', 'fitness', 'health', 'nutrition', 'diet', 'recipe', 'cooking', 'restaurant',
    'food' , 'shop' , 'store' , 'forum'
]

us = UserAgent()
ua = us.random

headers = {
    'User-Agent':f'{ua}'
}

def main():
    try:
        url = input(f'\n  {red}[{yellow}+{red}]{green} Enter Your URL Addres {red}:{cyan} ')
        parsed_url = urlparse(url)
        target = parsed_url.netloc
        print('\n')
        for su in subs:
            try:
                ht = str(su) + '.' + str(target)
                byp = gethostbyname(str(ht))
                if url.split('://')[0] == 'https':
                    rr = get('https://'+ht, headers=headers)
                    rs = rr.status_code
                    response = get(f"http://ip-api.com/json/{ht}")
                    response.raise_for_status()
                    data = response.json()
                    isp = data['as']
                    print(f'   {magenta}--> {red}[{yellow}+{red}]{green} CDN Bypassed {red}:  {blue}{byp} {yellow}|{cyan} https://{str(ht)} {yellow}| {blue}Response {red}: {magenta}{rs} {yellow}| {green}ISP {red}: {blue}{isp}')
                else:
                    rr = get('http://'+ht, headers=headers)
                    rs = rr.status_code
                    response = get(f"http://ip-api.com/json/{ht}")
                    response.raise_for_status()
                    data = response.json()
                    isp = data['as']
                    print(f'   {magenta}--> {red}[{yellow}+{red}]{green} CDN Bypassed {red}:  {blue}{byp} {yellow}|{cyan} http://{str(ht)} {yellow}| {blue}Response {red}: {magenta}{rs} {yellow}| {green}ISP {red}: {blue}{isp}')
            except:
                pass
    except:
        print('\n')
        ex()

main()
