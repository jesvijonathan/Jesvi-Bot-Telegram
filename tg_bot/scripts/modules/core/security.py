import config as config
from . import database

if config.bot_token == "":
    print("Config Bot Token Missing..")
    print("Check config.py & restart the scirpt")
    exit(1)
if config.database_name == "":
    print("Config Database Name Required..")
    print("Check config.py & restart the scirpt")
    exit(1)
if config.database_user == "":
    print("Config Database User Required..")
    print("Check config.py & restart the scirpt")
    exit(1)
if config.database_password == "":
    print("Config Database Password Required")
    print("Check config.py & restart the scirpt")
    exit(1)
if config.owner_id == "":
    print("Config Owner Id Missing.. (Required for sudo /)")
    