import code
from ctypes.wintypes import tagRECT
from distutils.command.install_egg_info import to_filename
from distutils.core import run_setup
from re import S
from time import sleep
from sys import argv
import requests
from os import system  as term , path  , stat
import sys


def os_detect():
    if "win"in sys.platform:
        term("pip install pyuseragents")
        term("cls")
    else:
        term("pip3 install pyuseragents")
        term("clear")

try:
    from platform import system
    import pyuseragents
except:
    os_detect()
blu = "\033[96m"
red = "\033[91m"
grn = "\033[32m"
ylw = "\033[93m"
res = "\033[0;m"
HEADER = '\033[95m'
lred = "\033[2;31;5m"

user_agent = pyuseragents.random()

ascii_art = f"""
{red}          _.._       '         {ylw}Ay Ulduz
{red}        .' .-'`   __/ \__         {red}Coded By {blu}➜ {grn}B4rC0d & Maxumum Radikali           
{red}       /  /       \     /         
{red}       |  |       /_   _\\      
{red}       \  '.___.;   \ /        
{red}        '._  _.'     '
{red}           ``

"""

def clear():
    sleep(0.2)
    if system() == "Windows":
        term('cls')
    elif system() == "Linux" or system() == "Darwin":
        term('clear')

#https://www.tiktok.com/@officialmartinfamsadjfjasdfjasjdfjasdfjj1j2j
def Instagram(target):
    sesnumid = requests.session()
    sesnumid.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"}
    data = sesnumid.get("https://commentpicker.com/instagram-user-id.php")
    sesnumid.headers.update({"Referer": "https://commentpicker.com/instagram-user-id.php"})
    data = sesnumid.get('https://commentpicker.com/actions/token.php?id=secret')
    data = sesnumid.get(f"https://commentpicker.com/actions/instagram-id-action.php?username={target}&token={data.text}")
    id = data.json()['username']
    if id == '':
        print(f" {ylw}[ {red}✖{ylw} ] {red}Instagram")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Instagram")
                
def Basecamp(target):
    data = requests.get(f"https://launchpad.37signals.com/session/profile?username={target}").text
    if 'password' in data:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Basecamp")
        
    else:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Basecamp")

def facebook(target):
    data = requests.get(f"https://www.facebook.com/{target}").text
    if "The link you followed may be broken" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Facebook")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Facebook")

def tiktok(target):
    data = requests.get(f"https://www.tiktok.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Tiktok")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Tiktok")

def mix(target):
    data = requests.get(f"https://mix.com/{target}").status_code
    if data == 301:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Mix")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Mix")



def twitter(target):
    payload = {"input":target}
    header = {"content-type":"application/x-www-form-urlencoded; charset=UTF-8","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36","x-requested-with":"XMLHttpRequest"}
    data = requests.post(f"https://tweeterid.com/ajax.php" , data=payload , headers=header).text
    if "error" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Twitter")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Twitter")

def blogger(target):
    data = requests.get(f"https://{target}.blogspot.com").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}blogspot")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}blogspot")

def youtube(target):
    data = requests.get(f"https://www.youtube.com/{target}").text
    if "Not Found" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Youtube")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Youtube")


def reddit(target):
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    data = requests.get(f"https://en.reddit.com/user/{target}/about.json?jsonp=_jqjsp&_1661423588377=" , headers=header).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Reddit")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Reddit")

def wordpress(target):
    data = requests.get(f"https://{target}.wordpress.com").text
    if "Do you want to register" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}wordpress")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}wordpress")

def pinterest(target):
    data = requests.get(f"https://www.pinterest.com/{target}" , allow_redirects=False).status_code
    if data == 301:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Pinterest")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Pinterest")

def github(target):
    data = requests.get(f"https://www.github.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Github")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Github")

def tumbler(target):
    data = requests.get(f"https://{target}.tumblr.com").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Tumbler")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Tumbler")

def flicker(target):
    data = requests.get(f"https://www.flickr.com/people/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Flicker")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Flicker")

def steam(target):
    data = requests.get(f"https://steamcommunity.com/id/{target}").text
    if "The specified profile could not be found" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Steam")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Steam")

def vimeo(target):
    data = requests.get(f"https://vimeo.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Vimeo")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Vimeo")

def soundcloud(target):
    data = requests.get(f"https://soundcloud.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}SoundCloud")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}SoundCloud")

def medium(target):
    data = requests.get(f"https://medium.com/@{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Medium")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Medium")

def deviantart(target):
    data = requests.get(f"https://{target}.deviantart.com").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Deviant Art")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Deviant Art")

def vk(target):
    data = requests.get(f"https://vk.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}VK")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}VK")

def about_me(target):
    data = requests.get(f"https://about.me/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}About Me")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}About Me")
        
def flipboard(target):
    data = requests.get(f"https://flipboard.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Fipboard")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Flipboard")

def fotolog(target):
    data = requests.get(f"https://fotolog.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Fotolog")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Fotolog")

def slidshare(target):
    data = requests.get(f"https://slideshare.net/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Slidshare")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Slidshare")

def spotify(target):
    data = requests.get(f"https://open.spotify.com/user/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Spotify")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Spotify")


def scrbid(target):
    data = requests.get(f"https://www.scribd.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Scrbid")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Scrbid")

def badoo(target):
    data = requests.get(f"https://www.badoo.com/en/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Badoo")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Badoo")

def patreon(target):
    data = requests.get(f"https://www.patreon.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Patreon")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Patreon")

def bitbucket(target):
    data = requests.get(f"https://bitbucket.org/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}BitBucket")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}BitBucket")

def dailymotion(target):
    data = requests.get(f"https://www.dailymotion.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Daily Motion")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Daily Motion")

def etsy(target):
    data = requests.get(f"https://www.etsy.com/shop/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Etsy")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Etsy")

def cashme(target):
    data = requests.get(f"https://cash.me/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Cash Me")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Cash Me")

def behance(target):
    data = requests.get(f"https://www.behance.net/{target}").text
    if "Oops! We" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Behance")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Behance")

def goodreads(target):
    data = requests.get(f"https://www.goodreads.com/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Good Reads")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Good Reads")

def Instructables(target):
    data = requests.get(f"https://www.instructables.com/member/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Instructables")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Instructables")

def keybase(target):
    data = requests.get(f"https://keybase.io/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}keybase")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}keybase")

def kongregate(target):
    data = requests.get(f"https://www.kongregate.com/accounts/{target}").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}kongregate")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}kongregate")

def livejournal(target):
    data = requests.get(f"https://{target}.livejournal.com").status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}livejournal")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}livejournal")

def angel(target):
    data = requests.get(f"https://angel.co/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 403:
        print(f" {ylw}[ {red}✖{ylw} ] {red}angel")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}angel")

def lastfm(target):
    data = requests.get(f"https://www.last.fm/user/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Last FM")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Last FM")

def dribbble(target):
    data = requests.get(f"https://dribbble.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Dribbble")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Dribble")

def codeacademy(target):
    data = requests.get(f"https://www.codecademy.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Code Academy")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Code Academy")

def gravater(target):
    data = requests.get(f"https://en.gravatar.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Gravater")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Gravater")

def pastebin(target):
    data = requests.get(f"https://pastebin.com/u/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Pastebin")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Pastebin")

def foursquare(target):
    data = requests.get(f"https://foursquare.com/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}foursquare")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}foursquare")

def wattpad(target):
    data = requests.get(f"https://www.wattpad.com/user/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}wattpad")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}wattpad")

def creativemarket(target):
    data = requests.get(f"https://creativemarket.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}creativemarket")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}creativemarket")

def TraktTV(target):
    data = requests.get(f"https://www.trakt.tv/users/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}TraktTV")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}TraktTV")


def buzzfeed(target):
    data = requests.get(f"https://buzzfeed.com/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}buzzfeed")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}buzzfeed")
def hubpages(target):
    data = requests.get(f"https://{target}.hubpages.com" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}hubpages")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}hubpages")

def gumroad(target):
    data = requests.get(f"https://www.gumroad.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}gumroad")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}gumroad")

def contently(target):
    data = requests.get(f"https://{target}.contently.com" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}contently")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}contently")

def houzz(target):
    data = requests.get(f"https://houzz.com/user/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}houzz")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}houzz")

def blipfm(target):
    data = requests.get(f"https://blip.fm/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}blipfm")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}blipfm")

def wikipedia(target):
    data = requests.get(f"https://www.wikipedia.org/wiki/User:{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Wikipedia")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Wikipedia")

def codementor(target):
    data = requests.get(f"https://www.codementor.io/@{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}codementor")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}codementor")

def reverbnation(target):
    data = requests.get(f"https://www.reverbnation.com/ {target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}reverbnation")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}reverbnation")

def designspiration(target):
    data = requests.get(f"https://www.designspiration.net/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}designspiration")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}designspiration")

def bandcamp(target):
    data = requests.get(f"https://www.bandcamp.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}bandcamp")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}bandcamp")

def colourlovers(target):
    data = requests.get(f"https://www.colourlovers.com/love/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 403:
        print(f" {ylw}[ {red}✖{ylw} ] {red}colourlovers")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}colourlovers")

def ifttt(target):
    data = requests.get(f"https://www.ifttt.com/p/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}ifttt")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}ifttt")

def ebay(target):
    data = requests.get(f"https://www.ebay.com/usr/{target}" , headers={"user-agent":user_agent}).text
    if "The User ID you entered was not found. Please check the User ID and try again." in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Ebay")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Ebay")

def slack(target):
    data = requests.get(f"https://{target}.slack.com" , headers={"user-agent":user_agent}).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Slack")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Slack")




def ello(target):
    data = requests.get(f"https://ello.co/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}ello")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}ello")


def newgrounds(target):
    data = requests.get(f"https://{target}.newgrounds.com" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}newgrounds")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}newgrounds")

def yandaxmusic(target):
    data = requests.get(f"https://music.yandex.ru/users/{target}/playlists" , headers={"user-agent":user_agent}).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Yandax Music")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Yandax Music")

def nitter(target):
    data = requests.get(f"https://nitter.net/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}nitter")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}nitter")

def zhihu(target):
    data = requests.get(f"https://www.zhihu.com/people/{target}" , headers={"user-agent":user_agent}).text
    if "404" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}zhihu")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}zhihu")

def codeforces(target):
    data = requests.get(f"http://codeforces.com/profile/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data !=200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}codeforces")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}codeforces")

def picuki(target):
    data = requests.get(f"https://www.picuki.com/profile/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}picuki")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}picuki")

def dumpor(target):
    data = requests.get(f"https://dumpor.com/v/{target}" , headers={"user-agent":user_agent}).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}dumpor")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}dumpor")

def hr(target):
    data = requests.get(f"https://www.hr.com/en/app/profile/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}hr")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}hr")

def aboutcar(target):
    data = requests.get(f"http://aboutcar.ru/members/{target}.html" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}aboutcar")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}aboutcar")

def statistika(target):
    data = requests.get(f"http://statistika.ru/forum/member.php?username={target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}statistika")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}statistika")

def giters(target):
    data = requests.get(f"https://giters.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}giters")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}giters")

def roblox(target):
    data = requests.get(f"https://www.roblox.com/user.aspx?username={target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Roblox")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Roblox")

def Xvideos(target):
    data = requests.get(f"https://xvideos.com/profiles/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Xvideos")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Xvideos")

def pornhub(target):
    data = requests.get(f"https://pornhub.com/users/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}pornhub")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}pornhub")

def cnet(target):
    data = requests.get(f"https://www.cnet.com/profiles/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}cnet")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}cnet")

def myspace(target):
    data = requests.get(f"https://myspace.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}myspace")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}myspace")

def bodyspace(target):
    data = requests.get(f"https://bodyspace.bodybuilding.com/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}bodyspace")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}bodyspace")

def picsart(target):
    data = requests.get(f"https://picsart.com/u/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}picsart")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}picsart")

def diigo(target):
    data = requests.get(f"https://www.diigo.com/interact_api/load_profile_info?name={target}" , headers={"user-agent":user_agent}).text
    if "{}" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}diigo")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}diigo")

def fortnitetracker(target):
    data = requests.get(f"https://fortnitetracker.com/profile/all/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Fortnite")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Fortnite")

def letterboxd(target):
    data = requests.get(f"https://letterboxd.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}letterboxd")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}letterboxd")

def bitly(target):
    data = requests.get(f"https://bit.ly/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}bitly")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}bitly")

def mouthshut(target):
    data = requests.get(f"https://www.mouthshut.com/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}mouthshut")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}mouthshut")

def smule(target):
    data = requests.get(f"https://www.smule.com/{target}" , headers={"user-agent":user_agent}).text
    if "Page Not Found" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}smule")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}smule")

def geocaching(target):
    data = requests.get(f"https://www.geocaching.com/profile/?u={target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}geocaching")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}geocaching")

def proton(target):
    data = requests.get(f"https://account.protonmail.com/api/users/available?Name={target}" , headers={"user-agent":user_agent}).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}ProtonVPN")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}ProtonVPN")

def gramhir(target):
    data = requests.get(f"https://gramhir.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}gramhir")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}gramhir")

def meetme(target):
    data = requests.get(f"https://www.meetme.com/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}meetme")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}meetme")

def spacesim(target):
    data = requests.get(f"https://spaces.im/mysite/index/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}spacesim")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}spacesim")

def libraries(target):
    data = requests.get(f"https://libraries.io/github/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}libraries")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}libraries")

def periscope(target):
    data = requests.get(f"https://www.periscope.tv/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}periscope")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}periscope")

def monitoringminecraft(target):
    data = requests.get(f"https://monitoringminecraft.ru/player/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Minecraft Player")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Minecraft Player")

def rblx(target):
    data = requests.get(f"https://rblx.trade/p/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}rblx Trade")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}rblx Trade")

def coder(target):
    data = requests.get(f"https://coder.social/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}coder social")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}coder social")

def letsbeef(target):
    data = requests.get(f"https://www.letsbeef.com/forums/member.php?&username={target}" , headers={"user-agent":user_agent}).text
    if "This user has not registered" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Lets Beef")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Lets Beef")

def xbox(target):
    data = requests.get(f"https://playerdb.co/api/player/xbox/{target}" , headers={"user-agent":user_agent}).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Xbox")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Xbox")

def ninjakiwi(target):
    data = requests.get(f"https://ninjakiwi.com/profile/{target}" , headers={"user-agent":user_agent} , allow_redirects=False).status_code
    if data != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}ninjakiwi")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}ninjakiwi")

def rumble(target):
    data = requests.get(f"https://rumble.com/user/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}rumble")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}rumble")

def quizlet(target):
    data = requests.get(f"https://quizlet.com/{target}" , headers={"user-agent":user_agent}).status_code
    if data == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}quizlet")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}quizlet")

def runescape(target):
    data = requests.get(f"https://apps.runescape.com/runemetrics/profile/profile?user={target}" , headers={"user-agent":user_agent}).text
    if "NO_PROFILE" in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}runescape")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}runescape")



def hackernews(target):
    data = requests.get(f"https://news.ycombinator.com/user?id={target}" , headers={"user-agent":user_agent}).text
    if "No such user." in data:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Hacker News")
        
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Hacker News")


def heroku(target):
    try:
        data = requests.get(f"https://{target}.herokuapp.com/").status_code
        if data != 200:
            print(f" {ylw}[ {red}✖{ylw} ] {red}Heroku")
            
        else:
            print(f" {ylw}[ {grn}✔{ylw} ] {grn}Heroku")
    except:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Heroku")



#
clear()
print(ascii_art)
print (f"{grn} Channel : {blu} @BlackFoxSecurityTeam")
target = input(f"\n[~] Enter Your UserName {red}❯❯{blu} ")
print (ylw + "[$] Please Wait Patiently .....\n\n")
Instagram(target)
Basecamp(target)
facebook(target)
codementor(target)
houzz(target)
twitter(target)
colourlovers(target)
bandcamp(target)
blogger(target)
designspiration(target)
gumroad(target)
hubpages(target)
runescape(target)
quizlet(target)
ninjakiwi(target)
xbox(target)
buzzfeed(target)
fortnitetracker(target)
diigo(target)
Xvideos(target)
monitoringminecraft(target)
periscope(target)
coder(target)
libraries(target)
meetme(target)
spacesim(target)
gramhir(target)
proton(target)
geocaching(target)
smule(target)
mouthshut(target)
bitly(target)
letterboxd(target)
letsbeef(target)
pornhub(target)
cnet(target)
picsart(target)
myspace(target)
bodyspace(target)
roblox(target)
reverbnation(target)
reddit(target)
youtube(target)
goodreads(target)
behance(target)
slack(target)
wattpad(target)
creativemarket(target)
ifttt(target)
wikipedia(target)
ello(target)
cashme(target)
heroku(target)
angel(target)
gumroad(target)
foursquare(target)
blipfm(target)
contently(target)
hackernews(target)
gravater(target)
newgrounds(target)
Instructables(target)
livejournal(target)
keybase(target)
pastebin(target)
codeacademy(target)
dribbble(target)
lastfm(target)
kongregate(target)
giters(target)
statistika(target)
yandaxmusic(target)
nitter(target)
zhihu(target)
picuki(target)
codeforces(target)
dumpor(target)
hr(target)
aboutcar(target)
etsy(target)
dailymotion(target)
bitbucket(target)
patreon(target)
badoo(target)
scrbid(target)
spotify(target)
soundcloud(target)
wordpress(target)
slidshare(target)
flipboard(target)
flicker(target)
fotolog(target)
about_me(target)
vk(target)
deviantart(target)
medium(target)
steam(target)
vimeo(target)
tumbler(target)
github(target)
pinterest(target)
print (f"{res}")
