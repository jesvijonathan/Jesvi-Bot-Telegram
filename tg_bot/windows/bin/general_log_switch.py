#################
import sys
import os
from pathlib import Path
import mysql.connector
#
# switch = "ON"   #   *comment one and-
# switch = "OFF" #   -leave the other open*
#
#################

switch = "OFF"


pa = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(pa)

try:
    switch = sys.argv[1]
except:
    switch = "ON"

print("\nTurning '" + switch + "' MySQL general_log..")

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="remote",
    password="Eulah2002@sql")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS jesvi_bot_database_main")

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="remote",
    password="Eulah2002@sql",
    database="jesvi_bot_database_main")
mycursor = mydb.cursor()

sql = ("SET global log_output = '{s0}'".format(s0="FILE"))
mycursor.execute(sql)

pa = pa + "/logs/log_sql_runtime.log"
# uncomment for windows
#pa = pa + "\\logs\\log_sql_runtime.log"

print(pa)
mydb.commit()

sql = ("SET global general_log_file = '{s0}'".format(s0=pa))
mycursor.execute(sql)
mydb.commit()

sql = ("SET GLOBAL general_log = '{s0}'".format(s0=switch))
mycursor.execute(sql)

mydb.commit()

print("done")
