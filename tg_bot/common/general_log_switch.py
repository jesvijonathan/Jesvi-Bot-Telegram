#################
import mysql.connector
from sys import platform
import sys
import os
from pathlib import Path
#
# switch = "ON"   #   *comment one and-
# switch = "OFF" #   -leave the other open*
#

try:
    from tg_bot.scripts.config import *
except:
    pa = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    pa = pa + "/scripts"
    sys.path.insert(1, pa)
    from config import *

switch = "ON"


try:
    switch = sys.argv[1]
except:
    pass

print("\nTurning '" + switch + "' MySQL general_log..")


mydb = mysql.connector.connect(
host=database_host,
user=database_user,
password=database_password)
mycursor = mydb.cursor(buffered=True)

sql = "CREATE DATABASE IF NOT EXISTS {s0}".format(s0=database_name)
mycursor.execute(sql)

mydb = mysql.connector.connect(
host=database_host,
user=database_user,
password=database_password,
database=database_name)
mycursor = mydb.cursor(buffered=True)
    

sql = ("SET global log_output = '{s0}'".format(s0="FILE"))
mycursor.execute(sql)
mydb.commit()

pa = None


if platform == "linux" or platform == "linux2" or platform == "darwin":
    # linux
    print("Linux - Setting path")
    pa = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    pa = pa + "/logs/log_sql_runtime.log"
elif platform == "darwin":
    # OS X
    pass
elif platform == "win32":
    # Windows
    print("Windows - Setting path")
    pa = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    pa = pa + "\\logs\\log_sql_runtime.log"


sys.path.append(pa)

print(pa)


sql = ("SET global general_log_file = '{s0}'".format(s0=pa))
mycursor.execute(sql)
mydb.commit()

sql = ("SET GLOBAL general_log = '{s0}'".format(s0=switch))
mycursor.execute(sql)
mydb.commit()

print("done")