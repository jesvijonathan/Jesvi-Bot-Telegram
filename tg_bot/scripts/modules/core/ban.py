

import modules.core.extract as extract
import modules.core.database as database

import telegram
import threading
from config import *
import time


class ban_cls():
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


    def ban(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m == 0:
            return
        else:
            n = extract.sudo_check_2(msg=self.tag_msg,context=self.context)
            
            if n == 2:
                self.msg.reply_text("Nope !")
                return
            elif n == 1:
                self.msg.reply_text("Get another admin to do it !")
                return

        self.update.effective_chat.kick_member(self.tag_user_id)

        self.update.message.reply_text("Banned " + self.tag_user["first_name"] + " !")


    def unban(self):
       m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
       if m == 0:
           return

       chat = self.update.effective_chat
       chat.unban_member(self.tag_user_id)

       self.update.message.reply_text("Un-banned " + self.tag_user["first_name"] + " !")


    def kick(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m == 0:
            return
        else:
            n = extract.sudo_check_2(msg=self.tag_msg,context=self.context)
            
            if n == 2:
                self.msg.reply_text("Nope !")
                return
            elif n == 1:
                self.msg.reply_text("Get another admin to do it !")
                return

        self.update.effective_chat.unban_member(self.tag_user_id)

        self.update.message.reply_text("Kicked " + self.tag_user["first_name"] + " !")

    def leave(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,sudo=1,context=self.context)
        
        if m != 2 or m != 7:            
            if m==1:
                self.msg.reply_text("'Owner only' command !")
            return

        msgg = self.msg.reply_text("Clearing group db befre leaving...")
        time.sleep(5)
        msgg.edit_text("You can add me back any time.\n Bye !")
        
        self.update.effective_chat.unban_member(bot_id)


    def rip(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=0,context=self.context)
        if m == 2 or m == 1:
           self.msg.reply_text("Hmm")
           return

        txt = self.msg.reply_text("You asked for it, any last words ?")

        time.sleep(5)

        self.update.effective_chat.unban_member(self.user_id)

        txt.edit_text(str(self.user["first_name"]) + " got voluntarily kicked !")

    def unmute(self):
        
        if self.tag_user_id == None:
            user_id = self.user_id
        else:
            user_id = self.tag_user_id


        #current = eval(str(context.bot.getChat(chat_id).permissions))
        new = {'can_send_messages': True,
               'can_send_media_messages': True,
               'can_send_polls': True,
               'can_send_other_messages': True,
               'can_add_web_page_previews': True,
               'can_invite_users': True,
               'can_change_info': True,
               'can_pin_messages': True}

        permissions = {'can_send_messages': None,
                       'can_send_media_messages': None,
                       'can_send_polls': None,
                       'can_send_other_messages': None,
                       'can_add_web_page_previews': None,
                       'can_invite_users': None,
                       'can_change_info': None,
                       'can_pin_messages': None}

        # permissions.update(current)
        permissions.update(new)
        new_permissions = telegram.ChatPermissions(**permissions)

        self.context.bot.restrict_chat_member(
            self.chat_id, user_id, permissions=new_permissions)


    def mute(self):

        if self.tag_user_id == None:
            user_id = self.user_id
        else:
            user_id = self.tag_user_id

        #current = eval(str(context.bot.getChat(chat_id).permissions))

        new = {'can_send_messages': False,
               'can_send_media_messages': False,
               'can_send_polls': False,
               'can_send_other_messages': False,
               'can_add_web_page_previews': False,
               'can_invite_users': False,
               'can_change_info': False,
               'can_pin_messages': False}

        permissions = {'can_send_messages': None,
                       'can_send_media_messages': None,
                       'can_send_polls': None,
                       'can_send_other_messages': None,
                       'can_add_web_page_previews': None,
                       'can_invite_users': None,
                       'can_change_info': None,
                       'can_pin_messages': None}

        # permissions.update(current)
        permissions.update(new)
        new_permissions = telegram.ChatPermissions(**permissions)

        self.context.bot.restrict_chat_member(
            self.chat_id, user_id, permissions=new_permissions)


    def router(self):
        res = self.msg_string.split(None,1)
        
        if res[0] == "/ban":
            self.ban()
        elif res[0] == "/unban":
            self.unban()
        elif res[0] == "/kick":
            self.kick()
        elif res[0] == "/leave":
            self.leave()
        elif res[0] == "/rip":
            self.rip()
        elif res[0] == "/mute":
            m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
            if m==0:
                return
            self.mute()       
        elif res[0] == "/unmute":
            m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
            if m==0:
                return
            self.unmute()  

def thread_ban(update, context):
    threading.Thread(target=ban_cls(update,context).router, args=(), daemon=True).start()
