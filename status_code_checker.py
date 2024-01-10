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
                response = requests.get(x, timeout=1).status_code
                if answer == "Y" or answer == "y":
                    f = open(f"{response}.txt", "a")
                    f.write(x + "\n")
                    f.close()
                elif answer == "N" or answer == "n":
                    print(x, response)
                else:
                    continue
            except Exception as e:
                f = open("error.txt", "a")
                f.write(x + "\n")
                f.close()
                continue
except Exception as e:
    pass