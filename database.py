import mysql.connector
import logging
import time 
import pyspeedtest as speedtest 
import config as config
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
  
  msg = update.message.reply_text(text="<code>" + "Connecting..." + "</code>", 
                  parse_mode="HTML")

  st = speedtest.Speedtest(secure=True)

  msg.edit_text(text="<code>" + "Checking download speed..." + "</code>", 
                  parse_mode="HTML")
  st.download()

  megabyte = 1./1000000
  d = st.results.download
  d = megabyte * d  
  d = round(d, 2)

  ds = "Download Speed : " + str(d) + " mb/s"

  msg.edit_text(text=("<code>" + ds + "\n\nChecking upload speed..." + "</code>"), 
                  parse_mode="HTML")
  st.upload()

  u = st.results.upload
  u = megabyte * u
  u = round(u, 2)

  us = "\nUpload Speed : " + str(u) + " mb/s"

  servernames =[]   
  msg.edit_text(text=("<code>" + ds + us + "\n\nMeasuring ping..." + "</code>"), 
                  parse_mode="HTML")
  st.get_servers(servernames)    
  ps = "\nPing : " + str(st.results.ping) + "ms"

  msg.edit_text(text=( "<code>" + "Test Time : " + time.strftime("%Y-%m-%d (%H:%M:%S)") + "\n\n" +  ds + us + ps + "</code>"), 
                  parse_mode="HTML")

st =0

def load():
  global mydb
  global mycursor
  global st

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

  sql = ("CREATE TABLE IF NOT EXISTS {s0}({s1} VARCHAR(33) PRIMARY KEY, {s2} VARCHAR(64), {s3} VARCHAR(64), {s4} VARCHAR(64), {s5} VARCHAR(33), {s6} TIMESTAMP, {s7} TEXT)".format(
  s0= "chat_base",
  s1="chat_id",
  s2="username",
  s3="chatname",
  s4="bot_status",
  s5="members",
  s6="add_date",
  s7="rules"
  ))

  mycursor.execute(sql)

  mydb.commit()


def add_chat_base(chat_id,username,chatname,bot_activity,members,sync,rules=None):
#no.bot,
  load()
  global mydb
  global mycursor
  
  r = cnam = unam = "NULL"
  
  if username != None:
        unam = '"' + username + '"'

  if chatname != None:
        cnam = '"' + chatname + '"'

  if rules != None:
        r = '"' + str(rules) + '"'

  try:
    sql = ( "SELECT {s2} FROM {s3}.{s0} WHERE {s1} = {s11}".format(
        s0= "chat_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="add_date",
        s3 = config.database_name
        ))
        
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
  
    for x in myresult:
      if x == None:
        sql = ( "REPLACE INTO {s0}({s1},{s2},{s3},{s4},{s5},{s6},{s7}) VALUE({s11},{s12},{s13},{s14},{s15},{s16},{s17})".format(
        s0= "chat_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="username",s12= unam,
        s3="chatname",s13= '"' + chatname + '"' ,
        s4="bot_status",s14='"' + bot_activity + '"',
        s5="members",s15= '"' + str(members) + '"',
        s6="add_date",s16= 'CURRENT_TIMESTAMP()',
        s7="rules",s17=r
        ))
  
      else:
        sql = ( "UPDATE {s0} SET {s2} = {s12},{s3} = {s13},{s4} = {s14},{s5} = {s15} WHERE {s1} = {s11}".format(
      s0= "chat_base",
      s1="chat_id",s11= '"' + chat_id + '"',
      s2="username",s12= unam,
      s3="chatname",s13= cnam,
      s4="bot_status",s14='"' + bot_activity + '"',
      s5="members",s15= '"' + str(members) + '"'
      ))

  except:
    sql = ( "REPLACE INTO {s0}({s1},{s2},{s3},{s4},{s5},{s6},{s7}) VALUE({s11},{s12},{s13},{s14},{s15},{s16},{s17})".format(
        s0= "chat_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="username",s12= unam,
        s3="chatname",s13= '"' + chatname + '"' ,
        s4="bot_status",s14='"' + bot_activity + '"',
        s5="members",s15= '"' + str(members) + '"',
        s6="add_date",s16= 'CURRENT_TIMESTAMP()',
        s7="rules",s17= r
        ))
  
  mycursor.execute(sql)
  mydb.commit()


def push_chat(chat_id,username=None,chatname=None,bot_activity=None,members=None,date=None,rules=None):
  load()
  global mydb
  global mycursor

  s2 = ""
  
  if rules != None: 
        s2 = "rules = " + '"' + rules + '"'

  sql = ( "UPDATE {s0} SET {s2} WHERE {s1} = {s11}".format(
        s0= "chat_base",
        s1="chat_id",s11= '"' + str(chat_id) + '"',
        s2=s2
      ))

  mycursor.execute(sql)
  mydb.commit()

  return 1


def get_chat(chat_id,rules=None):
  load()
  global mydb
  global mycursor

  s2=""

  if rules != None: 
        s2 = "rules"

  sql = ( "SELECT {s2} FROM {s0} WHERE {s1} = {s11}".format(
              s0= "chat_base",
              s1="chat_id",s11= '"' + str(chat_id) + '"',
              s2=s2
              ))

  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  return myresult


def create_user_base():
  load()
  global mydb
  global mycursor

  sql = ("CREATE TABLE IF NOT EXISTS {s0}({s1} VARCHAR(33) PRIMARY KEY, {s2} VARCHAR(64), {s3} VARCHAR(64), {s4} VARCHAR(64), {s5} VARCHAR(8), {s6} VARCHAR(8), {s7} BOOLEAN ,{s8} TIMESTAMP)".format(
  s0= "user_base",
  s1="user_id",
  s2="username",
  s3="firstname",
  s4="lastname",
  s5="gban",
  s6="active",
  s7="is_bot",
  s8="add_date"
  ))

  mycursor.execute(sql)


def add_user_base(user_id,username,firstname,lastname,is_bot=False,gban="no",active="yes",add_date=None):
  load()
  global mydb
  global mycursor
  
  xnam = cnam = unam = "NULL"
  
  if username != None:
        unam = '"' + username + '"'
  if firstname != None:
        cnam = '"' + firstname + '"'
  if lastname != None:
        xnam = '"' + lastname + '"'

  try:
    sql = ( "SELECT {s2} FROM {s3}.{s0} WHERE {s1} = {s11}".format(
        s0= "user_base",
        s1="user_id",s11= '"' + user_id + '"',
        s2="add_date",
        s3 = config.database_name
        ))

    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    for x in myresult:
      if x == None:
        sql = ( "REPLACE INTO {s0}({s1},{s2},{s3},{s4},{s5},{s6},{s7},{s8}) VALUE({s11},{s12},{s13},{s14},{s15},{s16},{s17},{s18})".format(
        s0= "user_base",
        s1="user_id",s11= '"' + user_id + '"',
        s2="username",s12= unam,
        s3="firstname",s13= cnam,
        s4="lastname",s14=xnam,
        s5="gban",s15= '"' + gban + '"',
        s6="active",s16='"' + active + '"',
        s7="is_bot",s17=is_bot,
        s8="add_date",s18='CURRENT_TIMESTAMP()'
        ))
  
      else:
        sql = ( "UPDATE {s0} SET {s2} = {s12},{s3} = {s13},{s4} = {s14},{s5} = {s15} WHERE {s1} = {s11}".format(
      s0= "user_base",
      s1="user_id",s11= '"' + user_id + '"',
      s2="username",s12= unam,
      s3="firstname",s13= cnam,
      s4="lastname",s14=xnam,
      s5="active",s15='"' + active + '"'
      ))

    mycursor.execute(sql)
    mydb.commit()

  except:
    sql = ( "REPLACE INTO {s0}({s1},{s2},{s3},{s4},{s5},{s6},{s7},{s8}) VALUE({s11},{s12},{s13},{s14},{s15},{s16},{s17},{s18})".format(
        s0= "user_base",
        s1="user_id",s11= '"' + user_id + '"',
        s2="username",s12= unam,
        s3="firstname",s13= cnam,
        s4="lastname",s14=xnam,
        s5="gban",s15= '"' + gban + '"',
        s6="active",s16='"' + active + '"',
        s7="is_bot",s17=is_bot,
        s8="add_date",s18='CURRENT_TIMESTAMP()'
        ))
    mycursor.execute(sql)
    mydb.commit()

def create_link_base():
  load()
  global mydb
  global mycursor

  sql = ("CREATE TABLE IF NOT EXISTS {s0}( id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, {s1} VARCHAR(33), {s2} VARCHAR(33), {s3} VARCHAR(64), {s4} TEXT, {s5} VARCHAR(8), {s6} TIMESTAMP)".format(
  s0= "link_base",
  s1="chat_id",
  s2="user_id",
  s3="status",
  s4="bio",
  s5="warns",
  s6="spot_date"
  ))

#warn_base, settings_base, filter_base, notes_base,                   news_base, 
  mycursor.execute(sql)
  mydb.commit()


def add_link_base(chat_id,user_id,status,bio=None,warns=0):
  load()
  global mydb
  global mycursor

  cnam = xnam = "NULL"

  if bio != None:
        xnam = '"' + bio + '"'

  try:
    sql = ( "SELECT {s2} FROM {s3}.{s0} WHERE {s1} = {s11} and {s4} = {s14}".format(
        s0= "link_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="spot_date",
        s3 = config.database_name,
        s4="user_id",s14= '"' + user_id + '"'
        ))

    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    for x in myresult:
      if x == None:
        sql = ( "REPLACE INTO {s0}({s1},{s2},{s3},{s4},{s5},{s6}) VALUE({s11},{s12},{s13},{s14},{s15},{s16})".format(
        s0= "link_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="user_id",s12= '"' + user_id + '"',
        s3="status",s13= '"' + status + '"',
        s4="bio",s14= xnam,
        s5="warns",s15= '"' + str(warns) + '"',
        s6="spot_date",s16='CURRENT_TIMESTAMP()'
        ))

      else:
        sql = ( "UPDATE {s0} SET {s3} = {s13} WHERE {s1} = {s11} and {s2} = {s12}".format(
        s0= "link_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="user_id",s12= '"' + user_id + '"',
        s3="status",s13= '"' + status + '"'
      ))

    mycursor.execute(sql)
    mydb.commit()

  except:
    sql = ( "REPLACE INTO {s0}({s1},{s2},{s3},{s4},{s5},{s6}) VALUE({s11},{s12},{s13},{s14},{s15},{s16})".format(
        s0= "link_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="user_id",s12= '"' + user_id + '"',
        s3="status",s13= '"' + status + '"',
        s4="bio",s14= xnam,
        s5="warns",s15= '"' + str(warns) + '"',
        s6="spot_date",s16='CURRENT_TIMESTAMP()'
        ))
    mycursor.execute(sql)
    mydb.commit()


def create_warn_base():
  load()
  global mydb
  global mycursor

  sql = ("CREATE TABLE IF NOT EXISTS {s0}( id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, {s1} VARCHAR(33), {s2} VARCHAR(33), {s3} VARCHAR(33), {s4} VARCHAR(33), {s5} TEXT, {s6} TIMESTAMP, {s7} VARCHAR(33))".format(
  s0= "warn_base",
  s1="chat_id",
  s2="user_id",
  s3="striked_by",
  s4="message_id",
  s5="reason",
  s6="date",
  s7="streak"
  ))

  mycursor.execute(sql)
  mydb.commit()


def add_warn_base_2(chat_id,user_id,striked_by,message_id,reason=None,remove=0):
  load()
  global mydb
  global mycursor

  sql = ( "UPDATE {s0} SET {s3} = {s13} WHERE {s1} = {s11} and {s2} = {s12}".format(
        s0= "link_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="user_id",s12= '"' + user_id + '"',
        s3="warns",s13= "warns + 1"
      ))
      
  mycursor.execute(sql)
  mydb.commit()

  sql = ( "SELECT {s2} FROM {s3}.{s0} WHERE {s1} = {s11} and {s4} = {s14}".format(
        s0= "link_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="warns",
        s3 = config.database_name,
        s4="user_id",s14= '"' + user_id + '"'
        ))

  mycursor.execute(sql)
  myresult = mycursor.fetchone()

  m = None

  try:
    m = myresult[0]
  except:
    if myresult == None:
      m = myresult = 1


  sql = ( "INSERT INTO {s0}({s1},{s2},{s3},{s4},{s5},{s6},{s7}) VALUE({s11},{s12},{s13},{s14},{s15},{s16},{s17})".format(
        s0= "warn_base",
        s1="chat_id",s11='"' + chat_id +'"',
        s2="user_id",s12='"' + user_id +'"',
        s3="striked_by",s13='"' + striked_by +'"',
        s4="message_id",s14='"' + str(message_id) +'"',
        s5="reason",s15='"' + reason +'"',
        s6="date",s16='CURRENT_TIMESTAMP()',
        s7="streak",s17='"' + str(m) + '"'
        ))

  mycursor.execute(sql)
  mydb.commit()

  return m


def create_settings_base():
  load()
  global mydb
  global mycursor

  sql = ("CREATE TABLE IF NOT EXISTS {s0}({s1} VARCHAR(33) PRIMARY KEY, {s2} VARCHAR(8), {s3} VARCHAR(12))".format(
  s0= "settings_base",
  s1="chat_id",
  s2="warn_limit",
  s3="warn_action"
  ))

  mycursor.execute(sql)
  mydb.commit()


def add_settings_base(chat_id,warn_limit=None,warn_action=None,res=0):
  load()
  global mydb
  global mycursor

  create_settings_base()
  
  sql = ( "SELECT EXISTS(SELECT * from {s0} WHERE {s1}={s11})".format(
          s0="settings_base",
          s1="chat_id",
          s11='"' + chat_id + '"'
        ))
  mycursor.execute(sql)

  try:
    results = mycursor.fetchone()
    if results[0] == 0:
      res=1
  except:
    pass

  if res == 1:
    sql = ( "REPLACE INTO {s0}({s1},{s2},{s3}) VALUE({s11},{s12},{s13})".format(
        s0= "settings_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="warn_limit",s12= '"3"',
        s3="warn_action",s13='"kick"'
      ))
      
    mycursor.execute(sql)
    mydb.commit()    

  else:
    s2=s3=""

    if warn_limit != None:
      s2=',warn_limit = ' + '"' + str(warn_limit) + '"'
    if warn_action != None:
      s3=',warn_action = ' + '"' + str(warn_action) + '"'

    sql = ( "UPDATE {s0} SET {s111}{s2}{s3} WHERE {s1} = {s11}".format(
        s0= "settings_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2=s2,
        s3=s3,
        s111="chat_id = " + '"' + chat_id + '"'
      ))
      
    mycursor.execute(sql)
    mydb.commit()

  sql = ( "SELECT {s2},{s4} FROM {s3}.{s0} WHERE {s1} = {s11}".format(
        s0= "settings_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="warn_limit",
        s4="warn_action",
        s3 = config.database_name
        ))
  
  mycursor.execute(sql)
  try:
    myresult = mycursor.fetchall()
    return myresult
  except:
    return -1
    pass


def warn_clear(chat_id,user_id,reset=0):
  load()
  global mydb
  global mycursor

  
  sql = ( "SELECT EXISTS(SELECT * from {s0} WHERE {s1}={s11} and {s2}={s12})".format(
          s0="warn_base",
          s1="chat_id",s11='"' + chat_id + '"',
          s2="user_id",s12='"' + user_id + '"'
        ))
  mycursor.execute(sql)

  try:
    results = mycursor.fetchone()

    if results[0] == 0:
      return
  except:
    return

  sql = ( "SELECT EXISTS(SELECT * from {s0} WHERE {s1}={s11} and {s2}={s12})".format(
          s0="link_base",
          s1="chat_id",s11='"' + chat_id + '"',
          s2="user_id",s12='"' + user_id + '"'
        ))
  mycursor.execute(sql)

  try:
    results = mycursor.fetchone()

    if results[0] == 0:
      return
  except:
    return

  if reset == 1:
    sql = ( "DELETE FROM {s0} WHERE {s1}={s11} and {s2}={s12}".format(
          s0="warn_base",
          s1="chat_id",s11='"' + chat_id + '"',
          s2="user_id",s12='"' + user_id + '"'
        ))
    mycursor.execute(sql)
    mydb.commit()
    
    sql = ( "UPDATE {s0} SET {s3}={s13} WHERE {s1} = {s11} and {s2} = {s12}".format(
        s0= "link_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="user_id",s12='"' + user_id + '"',
        s3="warns",s13='"0"',
      ))
      
    mycursor.execute(sql)
    mydb.commit()

    return 1

  elif reset == 0:
    sql = ( "UPDATE {s0} SET {s3} = {s13} WHERE {s1} = {s11} and {s2} = {s12}".format(
        s0= "link_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="user_id",s12= '"' + user_id + '"',
        s3="warns",s13= "warns - 1"
      ))
      
    mycursor.execute(sql)
    mydb.commit()
    
    sql = ( "DELETE FROM {s0} WHERE {s1}={s11} and {s2}={s12} ORDER BY id DESC LIMIT 1".format(
          s0="warn_base",
          s1="chat_id",s11='"' + chat_id + '"',
          s2="user_id",s12='"' + user_id + '"'
        ))
    mycursor.execute(sql)
    mydb.commit()

    return 1


def warninfo(chat_id,user_id=None):
  if user_id == None:
        sql = ( "SELECT {s2}, COUNT(*) AS `t` FROM {s0} WHERE {s1} = {s11} GROUP BY {s2}".format(
              s0= "warn_base",
              s1="chat_id",s11= '"' + chat_id + '"',
              s2="user_id"
              ))
  
        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        return myresult
        
  else:
        sql = ( "SELECT {s3},{s4},{s5},{s6} FROM {s0} WHERE {s1} = {s11} and {s2}={s12}".format(
              s0= "warn_base",
              s1="chat_id",s11= '"' + chat_id + '"',
              s2="user_id",s12='"' + user_id + '"',
              s3="striked_by",
              s4="message_id",
              s5="reason",
              s6="date"
              ))
        
        mycursor.execute(sql)
      
        myresult = mycursor.fetchall()
        return myresult


def push_link(chat_id,user_id=None,bio=None,status=None,warns=None,date=None):
  load()
  global mydb
  global mycursor

  """ if bio != None:
        s1 = ",bio" 
        s11='"' + bio + '"'
  if status != None:
        s1 = ",status" 
        s11='"' + status + '"'
  if warns != None:
        s1 = ",warns" 
        s11='"' + warns + '"' """

  s3 = ""
  
  if bio != None: 
        s3 = "bio = " + '"' + bio + '"'

  sql = ( "UPDATE {s0} SET {s3} WHERE {s1} = {s11} and {s2} = {s12}".format(
        s0= "link_base",
        s1="chat_id",s11= '"' + str(chat_id) + '"',
        s2="user_id",s12='"' + str(user_id) + '"',
        s3=s3
      ))

  mycursor.execute(sql)
  mydb.commit()

  return 1


def get_link(chat_id,user_id=None,bio=None,status=None,warns=None,date=None):
  load()
  global mydb
  global mycursor

  s4 = s3=""

  if bio != None: 
        s3 = ",bio"
  if status != None:
        s4 = ",status"

  sql = ( "SELECT user_id{s3}{s4} FROM {s0} WHERE {s1} = {s11} and {s2}={s12}".format(
              s0= "link_base",
              s1="chat_id",s11= '"' + str(chat_id) + '"',
              s2="user_id",s12='"' + str(user_id) + '"',
              s3=s3,
              s4=s4
              ))

  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  return myresult


def create_note_base():
  load()
  global mydb
  global mycursor

  sql = ("CREATE TABLE IF NOT EXISTS {s0}( id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, {s1} VARCHAR(33), {s2} VARCHAR(33), {s3} MEDIUMTEXT, {s4} VARCHAR(33), {s5} TIMESTAMP)".format(
  s0= "note_base",
  s1="chat_id",
  s2="note_name",
  s3="note",
  s4="set_by",
  s5="date"
  ))

  mycursor.execute(sql)
  mydb.commit()


def push_note(chat_id,note_name=None,note=None,set_by=None,date=None,res=None,pop=None):
  load()
  global mydb
  global mycursor

  s4 = s3 = ""

  if note_name == None or chat_id == None:
        return

  if pop != None:
    try:
      sql = ( "DELETE FROM {s0} WHERE {s1}={s11} and {s2}={s12}".format(
            s0="note_base",
            s1="chat_id",s11='"' + chat_id + '"',
            s2="note_name",s12='"' + note_name + '"'
          ))

      mycursor.execute(sql)
      mydb.commit()
      if mycursor.rowcount == 0:
            return -2
      return 1
    except:
      return -1

  sql = ( "SELECT EXISTS(SELECT * from {s0} WHERE {s1}={s11} and {s2}={s12})".format(
          s0="note_base",
          s1="chat_id",s11='"' + chat_id + '"',
          s2="note_name",s12='"' + note_name + '"'
        ))
  mycursor.execute(sql)
  
  
  try:
    results = mycursor.fetchone()
    if res == 0:
      pass
    else:
      if results[0] == 0:
        res=1
  except:
    pass


  if res == 1:
    sql = ( "REPLACE INTO {s0}({s1},{s2},{s3},{s4},{s5}) VALUE({s11},{s12},{s13},{s14},{s15})".format(
        s0= "note_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="note_name",s12='"' + note_name + '"',
        s3="note",s13= '"' + note + '"',
        s4="set_by",s14='"' + set_by + '"',
        s5="date",s15='CURRENT_TIMESTAMP()'
      ))
    
    mycursor.execute(sql)
    mydb.commit()
    return 1
  
  else:
        
    s5=s6=s3=s4=""

    if note_name != None or note != None:
        s3 = "note_name = " + '"' + note_name + '"'
        s4 = "note = " + '"' + note + '"'
    else:
        return
    
    if set_by != None:
        s5 = ",set_by = " + '"' + set_by + '"'
    
    s6 = ",date=CURRENT_TIMESTAMP()"

    sql = ( "UPDATE {s0} SET {s4}{s5}{s6} WHERE {s1} = {s11} and {s3}".format(
          s0= "note_base",
          s1="chat_id",s11= '"' + str(chat_id) + '"',
          s3=s3,
          s4=s4,
          s5=s5,
          s6=s6
        ))

    mycursor.execute(sql)
    mydb.commit()
    return 1


def get_note(chat_id,note_name=None,all_name=None):
  load()
  global mydb
  global mycursor

  s4 = s3 = ""
  results = None

  if all_name != None:
    sql = ( "SELECT note_name from {s0} WHERE {s1}={s11}".format(
          s0="note_base",
          s1="chat_id",s11='"' + chat_id + '"',
        ))
    mycursor.execute(sql)
    try:
      results = mycursor.fetchall()

      if results[0] == None:
        return -1 
    except:
      return -1

    return results
        

  if note_name == None or chat_id == None:
        return

  if chat_id == None or note_name == None:
    return

  sql = ( "SELECT note from {s0} WHERE {s1}={s11} and {s2}={s12}".format(
          s0="note_base",
          s1="chat_id",s11='"' + chat_id + '"',
          s2="note_name",s12='"' + note_name + '"'
        ))
  mycursor.execute(sql)

  try:
    results = mycursor.fetchone()
    if results[0] == None or results[0] == "":
      return -1 
  except:
    return -1

  return results


def create_filter_base():
  load()
  global mydb
  global mycursor

  sql = ("CREATE TABLE IF NOT EXISTS {s0}( id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, {s1} VARCHAR(33), {s2} VARCHAR(33), {s3} VARCHAR(33), {s4} VARCHAR(33), {s5} TIMESTAMP, {s6} text)".format(
  s0= "filter_base",
  s1="chat_id",
  s2="filter",
  s3="action",
  s4="set_by",
  s5="date",
  s6="reply"
  ))

  mycursor.execute(sql)
  mydb.commit()


def push_filter(chat_id,filterr=None,action="warn",set_by=None,replyt=None,pop=None,res=None):
  load()
  global mydb
  global mycursor

  d = s4 = s3 = ""

  if chat_id == None:
        return

  if pop != None:
    if pop == 1:
      d = "and filter=" + '"' + filterr + '"'
    elif pop == 2:
      d = ""
    try:
      sql = ( "DELETE FROM {s0} WHERE {s1}={s11} {s2}".format(
            s0="filter_base",
            s1="chat_id",s11='"' + chat_id + '"',
            s2=d
          ))
        
      mycursor.execute(sql)
      mydb.commit()
      if mycursor.rowcount == 0:
            return -2
      return 1
    except:
      return -1
  
  if filterr == None or chat_id == None:
        return

  sql = ( "SELECT EXISTS(SELECT * from {s0} WHERE {s1}={s11} and {s2}={s12})".format(
          s0="filter_base",
          s1="chat_id",s11='"' + chat_id + '"',
          s2="filter",s12='"' + filterr + '"'
        ))
  mycursor.execute(sql)
  try:
    results = mycursor.fetchone()
    
    if results[0] == 0:
      res=1
  
  except:
    pass

  if res == 1:
    
    if action == "reply":
        if replyt == None:
          return
        else:
          replyt = '"' + replyt + '"'
    else:
        replyt = "NULL"

    sql = ( "REPLACE INTO {s0}({s1},{s2},{s3},{s4},{s5},{s6}) VALUE({s11},{s12},{s13},{s14},{s15},{s16})".format(
        s0= "filter_base",
        s1="chat_id",s11= '"' + chat_id + '"',
        s2="filter",s12='"' + filterr + '"',
        s3="action",s13= '"' + action + '"',
        s4="set_by",s14='"' + set_by + '"',
        s5="date",s15='CURRENT_TIMESTAMP()',
        s6="reply",s16=replyt
      ))

    mycursor.execute(sql)
    mydb.commit()
    return 1
  
  else:
        
    s7=s5=s6=s3=s4=""

    if filterr != None or action:
        s3 = "filter = " + '"' + filterr + '"'
        s4 = "action = " + '"' + action + '"'
    else:
        return
    
    if set_by != None:
        s5 = ",set_by = " + '"' + set_by + '"'
    
    if action == "reply":
        if replyt == None:
          return
        else:
          s7 = ',reply="' + replyt + '"'
    else:
        s7 = ",reply=NULL"

    s6 = ",date=CURRENT_TIMESTAMP()"

    sql = ( "UPDATE {s0} SET {s4}{s5}{s6}{s7} WHERE {s1} = {s11} and {s3}".format(
          s0= "filter_base",
          s1="chat_id",s11= '"' + str(chat_id) + '"',
          s3=s3,
          s4=s4,
          s5=s5,
          s6=s6,
          s7=s7
        ))
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    return 1


def get_filter(chat_id,filterr=None,al=None):
  load()
  global mydb
  global mycursor

  s4 = s3 = ""
  results = None

  if al != None:
    sql = ( "SELECT * from {s0} WHERE {s1}={s11}".format(
          s0="filter_base",
          s1="chat_id",s11='"' + chat_id + '"',
        ))
    mycursor.execute(sql)
    try:
      results = mycursor.fetchall()

      if results[0] == None:
        return -1 
    except:
      return -1

    return results
        

  if filterr == None:
        return

  sql = ( "SELECT filter from {s0} WHERE {s1}={s11} and {s2}={s12}".format(
          s0="filter_base",
          s1="chat_id",s11='"' + chat_id + '"',
          s2="filter",s12='"' + filterr + '"'
        ))
  mycursor.execute(sql)

  try:
    results = mycursor.fetchone()
    if results[0] == None or results[0] == "":
      return -1 
  except:
    return -1

  return results

def log(turn="OFF"):
  load()
  global mydb
  global mycursor

  sql = ("SET GLOBAL general_log = '{s0}'".format(s0=turn))
  mycursor.execute(sql)


def create_base(update=None,context=None):
  load()
  create_chat_base()
  create_user_base()
  create_link_base()
  create_warn_base()
  create_settings_base()
  create_note_base()
  create_filter_base()
