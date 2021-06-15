#################
from sys import platform
import sys
import os
from pathlib import Path
import mysql.connector

#
# switch = "ON"   #   *comment one and-
# switch = "OFF" #   -leave the other open*
#

switch = "ON"


try:
    switch = sys.argv[1]
except:
    pass

print("\nTurning '" + switch + "' MySQL general_log..")

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="remote",
    password="Eulah2002@sql")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS jesvi_bot_database")

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="remote",
    password="Eulah2002@sql",
    database="jesvi_bot_database")
mycursor = mydb.cursor()

sql = ("SET global log_output = '{s0}'".format(s0="FILE"))
mycursor.execute(sql)


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


mydb.commit()

sql = ("SET global general_log_file = '{s0}'".format(s0=pa))
mycursor.execute(sql)
mydb.commit()

sql = ("SET GLOBAL general_log = '{s0}'".format(s0=switch))
mycursor.execute(sql)

mydb.commit()

print("done")
