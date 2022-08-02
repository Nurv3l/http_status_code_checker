from fileinput import filename
from tkinter import filedialog
import requests
from tkinter.filedialog import askopenfilename

print("""
    _             _                  _   _         
 __| |_____ _____| |___ _ __  ___ __| | | |__ _  _ 
/ _` / -_) V / -_) / _ \ '_ \/ -_) _` | | '_ \ || | 
\__,_\___|\_/\___|_\___/ .__/\___\__,_| |_.__/\_, |
                        |_|                    |__/    
███╗   ██╗██╗   ██╗██████╗ ██╗   ██╗███████╗██╗     
████╗  ██║██║   ██║██╔══██╗██║   ██║██╔════╝██║     
██╔██╗ ██║██║   ██║██████╔╝██║   ██║█████╗  ██║     
██║╚██╗██║██║   ██║██╔══██╗╚██╗ ██╔╝██╔══╝  ██║     
██║ ╚████║╚██████╔╝██║  ██║ ╚████╔╝ ███████╗███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝
                                                    """)
print("Choose file!")
filename = filedialog.askopenfilename()
try: 
    with open(filename, 'r') as f:
        read = f.read().splitlines()
        answer = input("Save results to file? (Y/N)" + "\n")
        for x in read:
            try:
                response = requests.get(x, headers=header).status_code
                if answer == "Y" or answer == "y":
                    if response == 403:
                        f = open("403.txt", "a")
                        f.write(x + "\n")
                        f.close()
                    elif response == 503:
                        f = open("503.txt", "a")
                        f.write(x + "\n")
                        f.close()
                    elif response == 200:
                        f = open("200.txt", "a")
                        f.write(x + "\n")
                        f.close()
                    elif response == 400:
                        f = open("400.txt", "a")
                        f.write(x + "\n")
                        f.close()
                    elif response == 404:
                        f = open("404.txt", "a")
                        f.write(x + "\n")
                        f.close()
                    elif response == 401:
                        f = open("401.txt", "a")
                        f.write(x + "\n")
                        f.close()
                    else:
                        continue
                elif answer == "N" or answer == "n":
                    print(x, response)
                else:
                    continue
            except Exception as e:
                continue
except Exception as e:
    pass
    
