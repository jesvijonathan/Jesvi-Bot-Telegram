from ast import parse
from os import link
from mysql.connector import connection
from telegram.parsemode import ParseMode
import modules.core.extract as extract
import time
import threading
import itertools
from multiprocessing.pool import ThreadPool

import modules.core.database as database

from modules.core.warn import warn

import json

from config import *

chat_lock = []
chat_lock_bool = 0

class unparse_cls():
    next_id = 0

    def __init__(self, update, context) -> None:
            
        #threading.Thread.__init__(self)
        #threading.Thread.start(self)
        #print(threading.Thread.getName,threading.current_thread().ident)
        
        #print(object(),self.id,threading.Thread.getName,threading.current_thread().ident)
        
        #time.sleep(3)
        
        self.update = update
        self.context = context
        
        self.msg = None
        self.user = None
        self.tag_msg = None
        self.tag_user = None
        
        self.msg = update.message

        self.user = user = self.msg['from_user']
        self.chat = chat = self.msg['chat']

        self.db = database.bot_db()

        try:
            self.tag_msg = tag_msg = update.message.reply_to_message

            self.tag_user = tag_user = tag_msg['from_user']

            self.tag_user_id = tag_user["id"]

            self.db.add_user(user=tag_user)
        except:
            pass

        self.db.parse(chat=chat, user=user)

        self.user_id = self.user["id"]
        self.chat_id = self.chat["id"]
        self.msg_string = self.msg.text
        
        #self.lock_del
        #del self
        #del(self)

    def admin_sync(self, stri=0):
        chat = self.update.effective_chat
        administrators = chat.get_administrators()
        text = ""

        for admin in administrators:
            status = admin.status
            user = admin.user

            status = admin.status
            
            self.db.add_user(user)

            self.db.add_link(chat,user,status,1)
            if stri == 1:
                if status == "creator":
                    text = "(Owner) " + user["first_name"] + text
                else:
                    text = text + "\n" + "(Admin) " + user["first_name"]
        
        return text 
    
    def sync(self, rep = 0):
        ms = None
        if rep == 1:
            ms = self.msg.reply_text("Syncing...", parse_mode="HTML",disable_web_page_preview=True)

        try:
            self.db.add_chat(self.chat)
        except: pass
        
        self.admin_sync()

        for x,y in enumerate(self.db.get_link(self.chat_id,comp=1)):
            detail = self.context.bot.get_chat_member(
                self.chat_id, y[2] )
            self.db.add_link(self.chat,detail.user,detail["status"],replace=3)

        database.create_db()
        
        if rep == 1:
            ms.edit_text("Synced !", parse_mode="HTML",disable_web_page_preview=True)


    
    def group_info(self):
        text = self.admin_sync(stri=1)

        count = self.chat.get_member_count()
        
        try:
            username = self.chat["username"]
            uname = "\nUsername : @" + username
        except:
            uname = ""

        try:
            link_name = self.context.bot.exportChatInviteLink(self.chat_id)
        except:
            try:
                link_name = "telegram.me/" + username
            except:
                link_name = "Unable to fetch the links ! "

        #link_name = "<a href='" + invitelink + "'>telegram.me/joinchat/</a>"
        
        text = "Group Info -\n\n" + \
            "ID : " + str(self.chat_id) + \
            "\nName : " + self.chat["title"] + uname + \
            "\nMembers : " + str(count) + \
            "\n\nAdministrators :\n" + text + \
            "\n\nGroup link : " + link_name
        
        #text = self.db.get_link(self.chat_id)

        self.msg.reply_text(text, parse_mode="HTML",disable_web_page_preview=True)
    
    def user_info(self):
        li = self.db.get_link(self.chat_id,self.tag_user_id)

        status = "\nStatus : " + li[3]
        
        bot = ""
        if self.tag_user['is_bot'] == True:
            bot = "\nBot : True"

        spot = "\nSpotted on : " + str(li[5]) 
        
        warns = self.db.get_warn(self.chat_id,self.tag_user_id)[0][7]
        if warns != 0:
            warns = "\nWarn Strike/s : " + str(warns)
        else:
            warns = ""

        try:
            username = self.tag_user["username"]
            uname = "\nUsername : @" + self.tag_user["username"]
        except:
            uname = ""
        
        try:
            ulink = "\nUser link : " + "<a href='https://telegram.me/" + \
            username + "'>" + "https://telegram.me/" + username + "</a>"
        except:
            ulink = ""

        try:
            plink = "\nPermanent link : " + "<a href='tg://user?id=" + \
            str(self.tag_user_id) + "'>Click Here</a>"
            pass
        except:
            pass

        try:
            lname = " " + self.tag_user["last_name"]
        except:
            lname = ""

        text = "User Info - \n\n" + \
            "Id : " + str(self.tag_user_id) +\
            "\nName : " + self.tag_user["first_name"] + lname +\
            uname + ulink + \
            "\n\nIn-Group Details :\n" + bot + status + spot + warns + plink 

        self.msg.reply_text(text, parse_mode="HTML",disable_web_page_preview=True)

    
    def msg_info(self):
        msg_id = self.tag_msg.message_id
        msgid = "\n\nMessage id : " + str(msg_id)

        userid = " (" + str(self.tag_user_id) + ")"

        try:
            first_name = self.tag_user.first_name
            if first_name == None:
                first_name = ""
        except:
            first_name = ""
        try:
            last_name = self.tag_user.last_name
            if last_name == None:
                last_name = ""
        except:
            last_name = ""

        try:
            user_name = self.tag_user.username
            if user_name == None:
                name = "\nName : <a href='tg://user?id=" + \
                    str(self.tag_user_id) + "'>" + str(first_name) + \
                    " " + str(last_name) + "</a>" + str(self.tag_user_id)
            else:
                name = "\nName : <a href='telegram.me/" + \
                str(user_name)+"'>" + str(first_name) + \
                " " + str(last_name) + "</a>" + userid
        except:
            user_name = "<a href='tg://user?id=" + \
                str(self.tag_user_id) + "'>" + str(first_name) + "</a>"
            name = "\nName : <a href='tg://user?id=" + \
                str(self.tag_user_id) + "'>" + str(first_name) + \
                " " + str(last_name) + "</a>" + userid

        try:
            grpusr = self.chat["username"]
        except: pass

        try:
            date = "\nDate : " + str(self.tag_msg.date)
        except:
            date = ""
        try:
            edt = self.tag_msg.edit_date
            if edt != None:
                edit_date = "\nEdited : " + str(edt)
            else:
                edit_date = ""
        except:
            edit_date = ""

        try:
            link = "\nMessage link : <a href='" + self.tag_msg.link + "'>Link</a>"
        except:
            link = ""
        try:
            chat_name = "\nChat : " + " <a href='t.me/" + grpusr + \
                "'>" + self.chat["title"] + "</a> ("+str(self.chat_id)+")"
        except:
            chat_name = ""

        try:
            textt = '\nText :\n<b>------------------</b>\n<i>' + \
                self.tag_msg.text + '</i>\n<b>------------------</b>'
        except:
            textt = "Type : #FILE"

            try:
                ftype = self.tag_msg.document.mime_type
                file = self.tag_msg.document.file_name
                file_id = self.tag_msg.document.file_unique_id
                file_size = self.tag_msg.document.file_size/1000000
                textt = "\nType : " + ftype + "\nFile_name : " + str(file) +"\nFile Id : " + str(file_id) + "\nfile_size : " + str(file_size) + "mb"
            except Exception as x:
                print(x)
                textt = textt + " (Use /json for more detail)"

        text = ("<b>Message Info -</b>" +
                msgid +
                name +
                chat_name + "\n" +
                textt + "\n" +
                date +
                edit_date +
                link)

        self.msg.reply_text(text=text,
                                  parse_mode="HTML")

    def json(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=0,context=self.context)
        if m==0:
            return
            
        if self.tag_msg == None:
            self.msg.reply_text(text="Tag a message or file to see its full backend details !",
                                  parse_mode="HTML")
            return

        j = "<code>" + json.dumps(self.tag_msg, indent=4, sort_keys=True, default=str) + "</code>"
        self.msg.reply_text(text=j,
                                  parse_mode="HTML")

    def router(self):
        res = self.msg_string.split(None, 1)
        if res[0] == "/info":
            if self.tag_msg == None:
                self.group_info()
            else:
                if self.tag_user == None:
                    self.tag_user = self.user
                    self.tag_user_id = self.user_id

                self.user_info()
        elif res[0] == "/json":
            self.json()
        elif res[0] == "/sync":
            self.sync(rep=1)
        elif res[0] == "/msgid":
            if self.tag_msg != None:
                self.msg_info()
            else:
                self.msg.reply_text("Tag a message !")


def thread_unparse(update, context):
    threading.Thread(target=unparse_cls(update,context).router, args=(), daemon=True).start()


def filter(update,context):
    #start = time.process_time()
    db = database.bot_db()

    msg = update.message

    user = msg['from_user']
    chat = msg['chat']

    tag_user = None

    try:
        tagmsg = update.message.reply_to_message

        tag_user = tagmsg['from_user']

        db.add_user(user=tag_user)

    except:
        pass

    db.parse(chat=chat, user=user)

    chat_id = chat["id"]
    user_id = user["id"]
    
    sett = db.get_settings(chat_id)
    filter_bool = sett[5]
    note_bool = sett[6]
    lock_bool = sett[7]

    admin = 0
    link = db.get_link(chat_id,user_id)[3]
    if (link == "administrator" or link == "creator"):
        admin = 1

    #msg_string = None

    def filter_del(): #use extractor | sudo check
        if admin == 0:
            msg.delete()

    def filter_filt():
        msg_string = msg.text
        
        if note_bool == 1:
            if msg_string.startswith("#") == True:
                note_check(msg_string[1:])
                return

        for x,y in enumerate(db.get_filter(chat_id)):
            if y[2].casefold() in msg_string.casefold():
                if y[3] == 0:
                    if admin==0:
                        msg.delete()
                    return
                elif y[3] == 1:
                    msg.reply_text(y[4])
                    if y[5] == 1:
                        msg.delete()
                elif y[3] == 2:
                    if admin == 0:
                        warn(update,context).warn_strike(y[4])
                        if y[5] == 1:
                            msg.delete()
                return
    
    def note_check(note_name):
        note = db.get_note_text(chat_id=chat_id, note_name=note_name)
        
        try:
            text = str(note[3])
            msg.reply_text(text, disable_web_page_preview=True)
            return
        except:
            #msg.reply_text("Note not found !")
            return

    if lock_bool == 1:
        filter_del()
        return
    elif filter_bool == 1:
        filter_filt()
    elif note_bool == 1 and filter_bool == 0:
        msg_string = msg.text
        if msg_string.startswith("#") == True:
            note_check(msg_string[1:])
            return

    #print("\n", time.process_time() - start, "\n")