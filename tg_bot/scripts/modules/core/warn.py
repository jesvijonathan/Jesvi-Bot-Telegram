from os import name

from telegram import chat, user
import modules.core.database as database

import modules.core.extract as extract
import modules.core.ban as ban

from config import *

import time

import threading

import json


class warn():
    def __init__(self,update,context) -> None:
        self.update = update
        self.context = context
        
        self.msg = None
        self.user = None
        self.tag_msg = None
        self.tag_user = None
        self.tag_user_id = None
        
        self.msg = update.message

        self.user = user = self.msg['from_user']
        self.chat = chat = self.msg['chat']

        self.db = database.bot_db()

        try:
            self.tag_msg = tag_msg = update.message.reply_to_message

            self.tag_user = tag_user = tag_msg['from_user']
            
            self.tag_user_id = self.tag_user["id"]

            self.db.add_user(user=tag_user)
        except:
            pass

        self.db.parse(chat=chat, user=user)

        self.chat_id = self.chat["id"]
        self.user_id = self.user["id"]

        self.msg_string = self.msg.text


    def warn_act(self,action):
        if action == 0:
            self.update.effective_chat.unban_member(self.tag_user_id)
            st = "kicked"
        elif action == 1:
            self.update.effective_chat.kick_member(self.tag_user_id)
            st = "banned"
        else:
            ban.ban_cls(self.update,self.context).mute()
            st = "restricted"

        self.db.add_link(self.chat,self.user,status=st,replace=1)
 

    def warn_info(self):
       """
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return
        else:
            n = extract.sudo_check_2(msg=self.tag_msg,del_lvl=0,context=self.context)
            if n == 1 or n == 2:
                self.msg.reply_text("Can't warn admins !") 
                return
       """
       
       if self.tag_user_id == None:
           user_id = self.user_id
           user = self.user
       else:
           user_id = self.tag_user_id
           user = self.tag_user

       warn = self.db.get_warn(self.chat_id,user_id,1)
       sett = self.db.get_settings(self.chat_id)
       warn_limit = sett[2]
       #warn_action = sett[3]
       
       n = None
       tex = ""
       for x,i in enumerate(warn):
           
           try:
               use = self.db.get_user(i[3])
               try:
                   last_name = use[2]
               except:
                   last_name = ""  
               
               name = "<a href='tg://user?id=" + \
                    str(use[0]) + "'>" + str(use[1]) + \
                    " " + str(last_name) + "</a>"
           except:
               name = str(i[3])
           
           try:
                link = "\nReason : '<i><a href='https://t.me/" + self.chat["username"] + "/" + i[4] + "'>" + i[5] + "</a></i>'"
           except Exception as y:
                link = "\nReason : <i>'" + i[5] + "'</i>"
           
           tex = tex + "\n\n" + str(x+1) + " | Date : " + str(i[6]) + "\nWarned by : " + name + link
           n = x

       try:
           try:
               last_name = self.tag_user.last_name
           except:
                last_name = ""  
              
           uname = "<a href='tg://user?id=" + \
                   str(self.user_id) + "'>" + self.user.first_name + \
                   " " + last_name + "</a>"
       except:
           uname = str(self.user.first_name)

        
       if n == None:
           e = "\n\n<b>No records of warn strike !</b>"
           n = 0
       else:
           e = "\n\nUse /warnclear, /warnremove"
           n = n+1

       text = "Warn Info -" + "\n\nUser : " + uname + "\nChat : " + self.chat["title"] + "\nLimit : " + str(n) + " of " + str(warn_limit) + tex + e
       
       self.msg.reply_text(text, parse_mode="HTML", disable_web_page_preview=True) 


    def warn_strike(self,reason=None):
        
        res = self.msg_string.split(None,1)

        try:
            reason = res[1]
        except:
            if reason == None:
                self.msg.reply_text("Provide a reason for the warn strike..") 
            else:
                self.tag_user = self.user
                self.tag_user_id = self.user_id
                self.tag_msg = self.msg

                self.user_id=bot_id
                self.user= bot_dict

        msg_id = self.msg.message_id

        sett = self.db.get_settings(self.chat_id)
        warn_limit = sett[2]
        warn_action = sett[3]

        
        warn = self.db.get_warn(self.chat_id,self.tag_user_id)    

        warns = warn[0][7]+1
        
        text = ( self.tag_user["first_name"] + " has been warn struck by " + self.user["first_name"] + \
            " !\n\nReason : '" + reason + "'" + \
            "\nStrikes : " + str(warns) + "/" + str(warn_limit) + "\n\n")

        if warn_action == 0:
                act = "kick"
                acted = "kicked"
        elif warn_action == 1:
                act = "ban"
                acted = "banned"
        else:
                act = "mute"
                acted = "muted"

        if warns >= warn_limit:
            text = text + "Warn limit reached !"
            strike = self.tag_msg.reply_text(text, parse_mode="HTML")

            self.warn_act(warn_action)
            
            i = (self.tag_user["first_name"] + " has been " + acted +  " by " + bot_name + " !")
            self.context.bot.send_message(chat_id=self.chat_id, text=i,
                             parse_mode="HTML") 
        else:

            text = text + str(warn_limit-warns) + " strike/s left before " + act + ", So watch out !"
            strike = self.tag_msg.reply_text(text, parse_mode="HTML") 
        
        msg_id = strike.message_id
        self.db.add_warn(self.chat_id, self.tag_user_id, self.user_id, msg_id, reason)
    
    def warn_clear(self,last=0):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return

        self.db.remove_warn(self.chat_id,self.tag_user_id,last)

        if last==0:
            text = "last warn has been removed " + self.tag_user["first_name"] + " !"
        elif last == 2:
            text = "Warn records have been cleared for " + self.tag_user["first_name"] + " !"
            ban.ban_cls(self.update,self.context).unmute()

        self.msg.reply_text(text, parse_mode="HTML") 

    def router(self):
        res = self.msg_string.split(None,1)
        
        if res[0][:6] == "/warn":
            m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
            if m==0:
                return
            else:
                n = extract.sudo_check_2(msg=self.tag_msg,del_lvl=0,context=self.context)
                if n == 1 or n == 2:
                    self.msg.reply_text("Can't warn admins !") 
                    return
            self.warn_strike()

        elif res[0] == "/warninfo":
            self.warn_info()
        
        elif res[0] == "/warnclear":
            self.warn_clear(last=2)

        elif res[0] == "/warnremove":
            self.warn_clear()
            
        elif res[0] == "/warnlist":
            self.warn_info()

def warn_router(update, context):
    threading.Thread(target=warn(update,context).router, args=(), daemon=True).start()
