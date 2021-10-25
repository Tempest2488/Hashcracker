import csv
import hashlib
from colorama import Fore
from colorama import Back
from datetime import datetime

print(Fore.BLUE + """dP     dP                    dP           a88888b.                            dP                         
88     88                    88          d8'   `88                            88                         
88aaaaa88a .d8888b. .d8888b. 88d888b.    88        88d888b. .d8888b. .d8888b. 88  .dP  .d8888b. 88d888b. 
88     88  88'  `88 Y8ooooo. 88'  `88    88        88'  `88 88'  `88 88'  `"" 88888"   88ooood8 88'  `88 
88     88  88.  .88       88 88    88    Y8.   .88 88       88.  .88 88.  ... 88  `8b. 88.  ... 88       
dP     dP  `88888P8 `88888P' dP    dP     Y88888P' dP       `88888P8 `88888P' dP   `YP `88888P' dP       
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
                                                                                                         """)
current_time = datetime.now().strftime("%H:%M:%S")
print(
    Fore.LIGHTWHITE_EX + "[i] " + Fore.LIGHTMAGENTA_EX + "Cracking started: " + Fore.LIGHTWHITE_EX + current_time + '\n' + Fore.RESET)

wordlist = bytes(open("10-million-password-list-top-1000000.txt").read(), 'utf-8')

with open('hashlist.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        for passw in wordlist.split():
            hashed = hashlib.sha256(passw).hexdigest()

            if hashed == row[0]:
                print(Fore.LIGHTGREEN_EX + "the hash you have given is cracked")
                print(Fore.LIGHTBLUE_EX + "the password is", passw.decode('utf-8'))
                print(Fore.YELLOW + "Your hash is", row)
                print(Fore.LIGHTMAGENTA_EX + "\nCracking ended: ", current_time + '\n' + Fore.RESET)
                quit()
            elif hashed != row[0]:
                pass
                #print(Fore.LIGHTMAGENTA_EX + passw.decode('utf-8') + Back.RESET, Fore.RED + "❌" + Fore.RESET)

    print(Fore.MAGENTA + "the hash you have provided is not there in the list.Try again next time" + Fore.RESET)