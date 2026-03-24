import configparser
import shutil
from pathlib import Path

config = configparser.ConfigParser()

while True:
    config.read("settings.ini")     # Läser in filen (kräver att filen ligger i samma mapp som scriptet)

    print("Here are the current settings:")
    for s in config.sections():     # Loopar igenom och skriver ut sections och key-value pairs i dem
        print("")
        print("[", s.swapcase(), "]")
        for k, v in config[s].items():
            print(k, ":", v)

    print("")
    print("The current IP address is: ", config.get("network", "ip_address"))
    edit = input("Do you want to edit the IP address? (y/n): ")

    if edit == "y":     # Körs endast om användaren önskar att redigera IP adressen

        current_folder = Path.cwd()

        copies_folder = current_folder / "copies"     # Sätter up en mapp där kopian av filen kommer hamna

        copies_folder.mkdir(exist_ok=True)     # Ser till att mappen inte skapas om den redan finns

        shutil.copy2("settings.ini", copies_folder / "settings.bak.ini")      # Kopierar filen in i mappen

        print("")
        print(fr"Copy of current settings saved to: {copies_folder}\settings.bak.ini") 

        print ("")
        input_adress = input("Please enter a new IP-adress: ")

        config.set("network", "ip_address", value=input_adress)     # Sätter det värde som användaren valt till "ip_address" nyckeln (Kollar inte om det är en rimlig IP adress)

        print("Your new IP address is: ", config.get("network", "ip_address"))
        save = input("Do you want to save these settings? (y/n): ")

        if save == "y":     # Kollar om det inskrivna värdet ska sparas till filen
            with open("settings.ini", "w") as cfg:     # Sparar den redigerade versionen av filen
                config.write(cfg)
            break
        else:
            break
    else:
        break
