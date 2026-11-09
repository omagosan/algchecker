import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import secret

def main():
    s = requests.Session()
    s.headers.update({
        "Accept-Language": "cs-CZ,cs;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    })

    l = "https://courseware.zcu.cz/portal/studium/courseware/kiv/alg/vysledky.html"
    ses = s.get(l, timeout=15)
    p = BeautifulSoup(ses.text, "html.parser")

    formular = p.find("form")
    if not formular:
        print("kys")
        raise Exception("kys")
    post = urljoin(ses.url, formular["action"])

    data = {}
    for i in formular.find_all("input"):
        name = i.get("name")
        if name:
            data[name] = i.get("value", "")

    data["j_username"] = secret.USERNAME
    data["j_password"] = secret.PASSWORD
    data["_eventId_proceed"] = ""

    login = s.post(post, data=data, timeout=15)
    pz = BeautifulSoup(login.text, "html.parser")

    saml = pz.find("form")
    if saml and pz.find("input", {"name": "SAMLResponse"}):
        saml_url = urljoin(login.url, saml["action"])

        saml_data = {}
        for i in saml.find_all("input"):
            name = i.get("name")
            if name:
                saml_data[name] = i.get("value", "")

        login2 = s.post(saml_url, data=saml_data)
        print(login2.text)
        if "osCislo" in login2.text:
            print("ALG ALERT")
            return True
        else:
            print("""\
    ⣿⣿⣿⣿⣿⣿⡟⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠙⠛⠛⠻⠿⠿⠿⢿⣿⣿⣿⣿
    ⣿⣿⣿⡟⠉⠀⠀⢀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⢹⣿⣿
    ⣿⣿⣿⡇⠀⣠⣶⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⡇⠀⠸⣿⣿
    ⣿⣿⡟⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠙⣿⣿⣿⣿⠏⢠⣿⣿⣿⣿⡇⠀⠀⠿⣿
    ⣿⣿⡇⠀⢀⣿⡏⠉⠛⠛⠻⠿⢿⣦⠼⣿⣿⢿⣤⣿⠿⠟⠛⠛⠓⠆⢠⡖⢀
    ⡇⠠⡄⠀⡈⠛⠋⢠⠀⠀⠀⠀⠀⠉⠴⠿⠿⠄⠀⠀⠀⠀⠀⠀⠀⡀⠘⢠⣾
    ⣿⣦⡈⠀⢿⣿⡆⠻⢦⣤⣤⣤⠀⡆⢰⣶⣦⠀⣿⣤⣄⣀⣀⡀⢸⡇⢰⣿⣿
    ⣿⣿⣿⣦⢘⣿⣿⣶⣶⣤⣤⣤⣴⡇⢸⣿⣿⠀⣤⣤⣤⣤⣤⣤⣼⡇⢸⣿⣿
    ⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⣿⣿⡄⣿⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿
    ⣿⣿⣿⣿⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠛⠿⠟⠁⢸⣿⣿⣿⣿⣿⣿⢠⣿⣿⣿
    ⣿⣿⣿⣿⣧⠸⣿⣿⣿⣿⠟⣿⣤⣿⣿⣶⣾⣷⣤⣏⠙⣿⣿⣿⡏⢸⣿⣿⣿
    ⣿⣿⣿⣿⣿⡀⢿⣿⣿⠁⡴⠛⢋⣡⣤⣌⣡⣤⣌⠙⠳⡈⢻⡿⢁⣾⣿⣿⣿
    ⣿⣿⣿⣿⣿⣇⠘⣿⡿⠋⠀⢤⣤⣤⣤⣤⣤⣤⣤⠤⠀⡈⠻⠃⣸⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣦⠈⢠⣾⣷⣄⡙⠛⠛⠛⢛⣉⣠⣴⣾⠟⢀⣼⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣷⣄⠉⠻⣿⣿⣁⣠⣤⣌⣹⣿⠟⠁⣴⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡈⠻⠿⠿⠿⠟⢉⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """)
            return False
    else:
        print("kys")
        return False

