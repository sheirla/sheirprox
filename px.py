from requests import Session
from colorama import Fore, init
import json

class Px():
    def __init__(self):
        self.pcolor(Fore.GREEN,"initializing script..")
        self.pcolor(Fore.GREEN,"script by sheirla")
        init()
        self.ss = Session()
        self.burl = "https://www.proxyscan.io/api/proxy?format=json&limit=5"

    def pcolor(self,color,txt: str):
        return print(color + txt)

    def pline(self):
        return self.pcolor(Fore.GREEN,"----------------------")

    def get_px(self):
        self.pcolor(Fore.GREEN,"getting proxy..")
        try:
            px = self.ss.get(self.burl,headers={'content-type':'application/json'})
            js = px.json()
            self.pline()
            for pxx in js:
                proxy = pxx["Ip"]
                port = pxx["Port"]
                ping = pxx["Ping"]
                country = pxx["Location"]["country"]
                city = pxx["Location"]["city"]
                isp = pxx["Location"]["isp"]
                types = pxx["Type"]
                anonymity = pxx["Anonymity"]
                self.pcolor(Fore.CYAN,f"Proxy: {proxy}:{port}")
                self.pcolor(Fore.CYAN,f"Ping: {ping}")
                self.pcolor(Fore.CYAN,f"Country: {country}")
                self.pcolor(Fore.CYAN,f"City: {city}")
                self.pcolor(Fore.CYAN,f"Isp: {isp}")
                self.pcolor(Fore.CYAN,f"Type: {types}")
                self.pcolor(Fore.CYAN,f"Anonimity: {anonymity}")
                self.pline()
        except Exception as e:
            self.pcolor(Fore.RED,str(e))
        except KeyError as e:
            self.pcolor(Fore.RED,str(e))
        return


if __name__ == '__main__':
    px = Px()
    px.get_px()
