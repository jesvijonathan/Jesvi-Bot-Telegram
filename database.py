import mysql.connector
import logging
import time 
import speedtest 
import modules.extract as extract

import modules.info as info

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


mydb = None
mycursor = None


def net(update,context):
  m = extract.sudocheck(update,context)
  if m == 2:
      return
  
  msg = update.message.reply_text("Connecting...")

  st = speedtest.Speedtest(secure=True)

  msg.edit_text("Checking download speed...")
  st.download()

  megabyte = 1./1000000
  d = st.results.download
  d = megabyte * d  
  d = round(d, 2)

  ds = "Download Speed : " + str(d) + " mb/s"

  msg.edit_text(ds + "\n\nChecking upload speed...")
  st.upload()

  u = st.results.upload
  u = megabyte * u
  u = round(u, 2)

  us = "\nUpload Speed : " + str(u) + " mb/s"

  servernames =[]   
  msg.edit_text(ds + us + "\n\nMeasuring ping...")
  st.get_servers(servernames)    
  ps = "\nPing : " + str(st.results.ping) + "ms"

  msg.edit_text(ds + us + ps)


def load():
  global mydb
  global mycursor


  mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Eulah2002@sql")
  mycursor = mydb.cursor()  
  mycursor.execute("CREATE DATABASE IF NOT EXISTS jesvi_bot_database")
 
  mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Eulah2002@sql",
  database="jesvi_bot_database")
  mycursor = mydb.cursor()  
  


def initgroup(chat_id):
  load()
  global mydb
  global mycursor

  sql = ("CREATE TABLE IF NOT EXISTS {s0}({s1} VARCHAR(33) PRIMARY KEY, {s2} VARCHAR(64), {s3} VARCHAR(32), {s4} VARCHAR(64), {s5} TEXT, {s6} TEXT, {s7} TEXT)".format(
  s0= str(chat_id) + "_user_data",
  s1="user_id",
  s2="status",
  s3="ban",
  s4="restrictions",
  s5="spam",
  s6="warn",
  s7="bio"
  ))

  mycursor.execute(sql)


def initsettings():
  load()
  global mydb
  global mycursor

  sql = ("CREATE TABLE IF NOT EXISTS {s0}({s1} VARCHAR(33) PRIMARY KEY, {s2} VARCHAR(64), {s3} VARCHAR(32), {s4} VARCHAR(64), {s5} TEXT, {s6} TEXT, {s7} TEXT, {s8} TEXT, {s9} TEXT, {s10} TEXT)".format(
  s0= "chat_settings",
  s1="chat_id",
  s2="welcome",
  s3="bot_check",
  s4="filter",
  s5="notes",
  s6="news",
  s7="rules",
  s8="lock_group",
  s9="spam",
  s10="defence"
  ))

  mycursor.execute(sql)


def initgroupsettings(chat_id):
  load()
  global mydb
  global mycursor

  sql = ( "INSERT INTO {s0} ({s1}) VALUE({s11})".format(
  s0="chat_settings",
  s1="chat_id",
  s11=str(chat_id)
  ))

  mycursor.execute(sql)

  mydb.commit()

#################################


def create_chat_base():
  load()
  global mydb
  global mycursor

  sql = ("CREATE TABLE IF NOT EXISTS {s0}({s1} VARCHAR(33) PRIMARY KEY, {s2} VARCHAR(64), {s3} VARCHAR(64), {s4} VARCHAR(64), {s5} VARCHAR(33), {s6} DATE)".format(
  s0= "chat_base",
  s1="chat_id",
  s2="username",
  s3="chatname",
  s4="bot_status",
  s5="members",
  s6="add_date"
  ))

  mycursor.execute(sql)

  mydb.commit()


def add_chat_base(chat_id,username,chatname,bot_activity,members,sync):
  load()
  global mydb
  global mycursor
  
  cnam = unam = "NULL"
  
  if username != None:
        unam = '"' + username + '"'

  if chatname != None:
        cnam = '"' + chatname + '"'

  if sync == 1:
        sql = ( "REPLACE INTO {s0}({s1},{s2},{s3},{s4},{s5}) VALUE({s11},{s12},{s13},{s14},{s15})".format(
        s0= "chat_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="username",s12= unam,
        s3="chatname",s13= cnam,
        s4="bot_status",s14='"' + bot_activity + '"',
        s5="members",s15= '"' + str(members) + '"'
        ))

  elif sync == 0:
        sql = ( "REPLACE INTO {s0} ({s1},{s2},{s3},{s4},{s5},{s6}) VALUE({s11},{s12},{s13},{s14},{s15},{s16})".format(
        s0= "chat_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="username",s12= unam,
        s3="chatname",s13= '"' + chatname + '"' ,
        s4="bot_status",s14='"' + bot_activity + '"',
        s5="members",s15= '"' + str(members) + '"',
        s6="add_date",s16= '"' +time.strftime("%Y-%m-%d") + '"'
        ))

  mycursor.execute(sql)

  mydb.commit()


def create_user_base():
  load()
  global mydb
  global mycursor
  
  sql = ("CREATE TABLE IF NOT EXISTS {s0}({s1} VARCHAR(33) PRIMARY KEY, {s2} VARCHAR(128), {s3} VARCHAR(128), {s4} VARCHAR(128), {s5} VARCHAR(8))".format(
  s0= "user_base",
  s1="user_id",
  s2="username",
  s3="firstname",
  s4="lastname",
  s5="gban",
  ))

  mycursor.execute(sql)


def add_user_base(user_id,username,firstname,lastname,ban):
  load()
  global mydb
  global mycursor

  sql = ( "INSERT INTO {s0} ({s1},{s2},{s3},{s4},{s5}) VALUE({s11},{s12},{s13},{s14},{s15})".format(
  s0= "user_base",
  s1="user_id",s11=user_id,
  s2="username",s12=username,
  s3="firstname",s13=firstname,
  s4="lastname",s14=lastname,
  s5="gban",s15=ban
  ))

  mycursor.execute(sql)

  mydb.commit()
  

def create_base():
  load()
  create_chat_base()
  create_user_base()
