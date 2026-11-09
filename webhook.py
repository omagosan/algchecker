import time
import requests
import main
import secret
import os

url = secret.url

while True:
    try:
        res = main.main()
        if not res:
            requests.post(url, json={"content":
                    "⣿⣿⣿⣿⣿⣿⡟⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠙⠛⠛⠻⠿⠿⠿⢿⣿⣿⣿⣿\n"
                    "⣿⣿⣿⡟⠉⠀⠀⢀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⢹⣿⣿\n"
                    "⣿⣿⣿⡇⠀⣠⣶⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⡇⠀⠸⣿⣿\n"
                    "⣿⣿⡟⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠙⣿⣿⣿⣿⠏⢠⣿⣿⣿⣿⡇⠀⠀⠿⣿\n"
                    "⣿⣿⡇⠀⢀⣿⡏⠉⠛⠛⠻⠿⢿⣦⠼⣿⣿⢿⣤⣿⠿⠟⠛⠛⠓⠆⢠⡖⢀\n"
                    "⡇⠠⡄⠀⡈⠛⠋⢠⠀⠀⠀⠀⠀⠉⠴⠿⠿⠄⠀⠀⠀⠀⠀⠀⠀⡀⠘⢠⣾\n"
                    "⣿⣦⡈⠀⢿⣿⡆⠻⢦⣤⣤⣤⠀⡆⢰⣶⣦⠀⣿⣤⣄⣀⣀⡀⢸⡇⢰⣿⣿\n"
                    "⣿⣿⣿⣦⢘⣿⣿⣶⣶⣤⣤⣤⣴⡇⢸⣿⣿⠀⣤⣤⣤⣤⣤⣤⣼⡇⢸⣿⣿\n"
                    "⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⣿⣿⡄⣿⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿\n"
                    "⣿⣿⣿⣿⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠛⠿⠟⠁⢸⣿⣿⣿⣿⣿⣿⢠⣿⣿⣿\n"
                    "⣿⣿⣿⣿⣧⠸⣿⣿⣿⣿⠟⣿⣤⣿⣿⣶⣾⣷⣤⣏⠙⣿⣿⣿⡏⢸⣿⣿⣿\n"
                    "⣿⣿⣿⣿⣿⡀⢿⣿⣿⠁⡴⠛⢋⣡⣤⣌⣡⣤⣌⠙⠳⡈⢻⡿⢁⣾⣿⣿⣿\n"
                    "⣿⣿⣿⣿⣿⣇⠘⣿⡿⠋⠀⢤⣤⣤⣤⣤⣤⣤⣤⠤⠀⡈⠻⠃⣸⣿⣿⣿⣿\n"
                    "⣿⣿⣿⣿⣿⣿⣦⠈⢠⣾⣷⣄⡙⠛⠛⠛⢛⣉⣠⣴⣾⠟⢀⣼⣿⣿⣿⣿⣿\n"
                    "⣿⣿⣿⣿⣿⣿⣿⣷⣄⠉⠻⣿⣿⣁⣠⣤⣌⣹⣿⠟⠁⣴⣿⣿⣿⣿⣿⣿⣿\n"
                    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡈⠻⠿⠿⠿⠟⢉⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"}, timeout=15)
        else:
            for i in range(5):
                requests.post(url, json={"content": f"ALG ALERT 🚨🚨🚨 <{secret.role}> & <{secret.role2}> 🚨🚨🚨"})
                time.sleep(1)
            os.system("loginctl poweroff")
            break
    except requests.exceptions.RequestException as e:
        print("kys")
    except Exception as e:
        print("kys too")

    time.sleep(60 * 5)