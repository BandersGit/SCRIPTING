import configparser
import shutil

config = configparser.ConfigParser()

config.read("test.ini")

# value = config.getboolean("","")
#       = config.getint("","")

for k, v in config["databas"].items():
    print(k, v)

print("Utvalt värde", config.get("databas", "password", fallback=None))

config.set("databas", "password", value="New Password")

print("Ändrat värde:", config["databas"]["password"])

shutil.copy2("test.ini", "test.bak.ini")

config["New Section"] = {"debug": "true"}

with open("test.ini", "w") as cfg:
    config.write(cfg)
