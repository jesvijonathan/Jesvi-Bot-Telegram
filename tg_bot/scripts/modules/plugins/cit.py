
from config import *
import mysql.connector
import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

mydb = None
mycursor = None


def load():
    global mydb
    global mycursor
    global st

    mydb = mysql.connector.connect(
        host=database_host,
        user=database_user,
        password=database_password)
    mycursor = mydb.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS {s0}".format(s0=database_name)
    mycursor.execute(sql)

    mydb = mysql.connector.connect(
        host=database_host,
        user=database_user,
        password=database_password,
        database=database_name)
    mycursor = mydb.cursor()


def create_class_base():

    load()
    global mydb
    global mycursor

    sql = (
        "CREATE TABLE IF NOT EXISTS cit_class_base ( id VARCHAR(32) PRIMARY KEY, code VARCHAR(32), cls_msg VARCHAR(32), sem VARCHAR(32))"
    )  # cit_class_base : id | code | cls_msg | sem

    mycursor.execute(sql)
    mydb.commit()


def create_subjects_base():

    load()
    global mydb
    global mycursor

    sql = (
        "CREATE TABLE IF NOT EXISTS cit_subjects_base ( code VARCHAR(14) PRIMARY KEY, subject TEXT, link TEXT, teacher VARCHAR(32), contact VARCHAR(32), sem VARCHAR(12))"
    )  # cit_subjects_base : code | subject | link | teacher | contact | sem

    mycursor.execute(sql)
    mydb.commit()


def add_subject(tbl=None):
    load()
    global mydb
    global mycursor

    sql = (
        "REPLACE INTO cit_subjects_base (code, subject, link, teacher, contact, sem) VALUE(%s, %s, %s, %s, %s, %s)")
    data = (
        tbl['code'],
        tbl['subject'],
        tbl['link'],
        tbl['teacher'],
        tbl['contact'],
        tbl['sem']
    )
    mycursor.execute(sql, data)
    mydb.commit()


def get_subject(code=None, sem=None):
    load()
    global mydb
    global mycursor

    sql = ("""SELECT * FROM cit_subjects_base""")
    data = ()

    if code != None:
        sql = ("""SELECT * FROM cit_subjects_base WHERE code = %s""")
        data = (code,)
    if sem != None:
        sql = ("""SELECT * FROM cit_subjects_base WHERE sem = %s""")
        data = (sem,)

    mycursor.execute(sql, data)
    myresult = mycursor.fetchall()

    return myresult


def create_timetable_base():

    load()
    global mydb
    global mycursor

    sql = (
        "CREATE TABLE IF NOT EXISTS cit_timetable_base ( id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, day VARCHAR(32), hour VARCHAR(32), code VARCHAR(32), time VARCHAR(32))"
    )  # cit__timetable_base : key | day | hour | code | time

    mycursor.execute(sql)
    mydb.commit()


def add_timetable(tbl=None):
    load()
    global mydb
    global mycursor

    sql = (
        "SELECT (1) FROM cit_timetable_base WHERE day=%s AND hour=%s LIMIT 1"
    )
    data = (
        tbl['day'],
        tbl['hour']
    )

    mycursor.execute(sql, data)

    if mycursor.fetchone():
        sql1 = (
            "UPDATE cit_timetable_base SET code=%s, time=%s WHERE day=%s AND hour=%s LIMIT 1"
        )
        data1 = (
            tbl['code'],
            tbl['time'],
            tbl['day'],
            tbl['hour']
        )
        mycursor.execute(sql1, data1)
    else:

        sql1 = (
            "INSERT INTO cit_timetable_base (day, hour, code, time) VALUE(%s, %s, %s, %s)")
        data1 = (
            tbl['day'],
            tbl['hour'],
            tbl['code'],
            tbl['time']
        )
        mycursor.execute(sql1, data1)
    # print(data)

    mydb.commit()


def get_timetable(day=None, hour=None, code=None):
    load()
    global mydb
    global mycursor

    day1 = hour1 = code1 = ""

    if day != None:
        day1 = "WHERE day='" + str(day) + "'"
        if hour != None:
            hour1 = "AND hour='" + str(hour) + "'"
        if code != None:
            code1 = "AND code='" + str(code) + "'"
    else:
        pass
    sql = ("SELECT * FROM cit_timetable_base {day} {hour} {code} ".format(
        day=day1,
        hour=hour1,
        code=code1))

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult


def cit(update, context):
    text = "Module Error"

    res = update.message.text.split(None, 2)
    # j = updater.job_queue

    """
"""
    try:
        if res[1] == "status":
            text = ("CIT Module -\n" +
                    "Status - Debugging\n" +
                    "Available Commands - 'null'\n" +
                    "CITdb - Disconnected")

        elif res[1] == "add_timetable":
            res = update.message.text.split(None, 5)
            data = {'day': res[2],
                    'hour': res[3],
                    'code': res[4],
                    'time': res[5]}
            add_timetable(data)
            text = "added/updated period !"

        elif res[1] == "add_subject":
            res = update.message.text.split(None, 7)
            data = {'code': res[2],
                    'subject': res[3],
                    'link': res[4],
                    'teacher': res[5],
                    'contact': res[6],
                    'sem': res[7]}
            add_subject(data)
            text = "subject added/updated !"

        elif res[1] == "show_timetable":
            res = update.message.text.split(None, 4)

            day = hour = code = None

            try:
                day = res[2]
            except:
                pass
            try:
                hour = res[3]
            except:
                pass
            try:
                code = res[4]
            except:
                pass

            text = get_timetable(day, hour, code)

        elif res[1] == "show_subject":
            try:
                res = update.message.text.split(None, 2)

                sem = code = None

                temp = res[2]
                try:
                    sem = int(temp)
                    text = get_subject(sem=sem)
                except:
                    code = temp
                    text = get_subject(code=code)
            except:
                text = get_subject()

        elif res[1] == "attendance":
            attend(update, context)
            return

        elif res[1] == "create_cit_base":
            create_subjects_base()
            create_timetable_base()
            create_class_base()
            text = "CIT Data Bases Created !"
        elif res[1] == "cls":
            period(update, context)
            return
    except:
        pass

    update.message.reply_text(text)


cls_msg = None
uid = ()
hr = '1'
dei = None


def period(update, context):
    global cls_msg
    global hr
    global dei

    res = update.message.text.split(None, 3)
    now = datetime.datetime.now()
    sday = now.strftime("%A")

    day = sday
    hour = '1'

    try:
        day = res[2]
        try:
            hour = res[3]
        except:
            try:
                hour = int(day)
                day = sday
            except:
                hour = '1'
    except:
        day = sday
        hour = '1'

    try:
        if day == "nxt" or hour == "nxt":
            x = int(hr)+1
            hour = str(x)
            if hour >= '6':
                hour = '6'
            day = dei

        elif day == "prev" or hour == "prev":
            x = int(hr)-1
            hour = str(x)
            if hour <= '1':
                hour = '1'
            day = dei
    except:
        pass

    dei = day

    table = get_timetable(day=day, hour=hour)

    """text = ("Tuesday | Hour 3 (10:40/11:20)\n\n" +
            "Technical_English (HS8152)\n\n" +
            "Ms.S.Shama | 13/63")
    """

    hr = table[0][2]

    text = (table[0][1] + " | Hour " + table[0][2] +
            " (" + table[0][4] + ")\n\n")

    code = table[0][3]

    #######
    sem = '2'
    #######
    id = update.effective_chat.id
    #######
    # cls_msg=

    table1 = get_subject(code=code)

    text = (text + table1[0][1] + " (" + code + ")\n\n" +
            table1[0][3])

    try:
        url = table1[0][2]
    except:
        url = "no_link_available"

    try:
        context.bot.deleteMessage(id, cls_msg)
    except:
        pass

    keyboard = [
        [
            InlineKeyboardButton(
                text="Join", callback_data='1', url=url),
        ],
        [InlineKeyboardButton(text="Prev", callback_data='2'),
         InlineKeyboardButton("Next", callback_data='3')
         ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = update.message.reply_text(text, reply_markup=reply_markup)
    cls_msg = int(msg.message_id)


def attend(update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                text="Present", callback_data='1', url='https://meet.google.com/bqj-vjhu-rrq'),
        ],
        [InlineKeyboardButton(text="On Duty", callback_data='2'),
         InlineKeyboardButton("Absent", callback_data='3',
                              url='tg://user?id=1151196678')
         ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Attendace - Auto", reply_markup=reply_markup)
