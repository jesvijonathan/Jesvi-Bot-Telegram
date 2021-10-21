from ast import unparse
import modules.core.database as database
#import modules.core.extract as extract
import modules.core.extract as extract
import modules.core.unparse as unparse

import time

import threading

import json


class filter_switch():

    def __init__(self,update,context) -> None:
        
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

            self.db.add_user(user=tag_user)
        except:
            pass

        self.db.parse(chat=chat, user=user)

        self.chat_id = self.chat["id"]
        self.msg_string = self.msg.text


    def lock(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return
            
        extract.admin_sync(self.update,self.context,db=self.db)
        
        self.db.add_settings(self.chat_id,lock=1) 
        
        self.msg.reply_text("Chat Locked !")


    def unlock(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return

        #extract.admin_sync(self.update,self.context,self.db)

        unparse.unparse_cls(self.update,self.context).sync()

        self.db.add_settings(self.chat_id,lock=0) 

        self.msg.reply_text("Chat Unlocked !")


    def filter_remove(self,word,tell=0):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return

        self.db.remove_filter(self.chat_id,word)
        if tell==1:
            if word == '*':
                self.msg.reply_text("Cleared filter !")
            else:    
                self.msg.reply_text(word + " removed from filter !")


    def filter_add(self,res):

        word=None
        response=None
        delete=0
        type=0
        


        try:
            ress = res.split(None, 2)
            if ress[1] == "reply":
                type=1
            elif ress[1] == "replydel":
                type=1
                delete=1
            elif ress[1] == "warn":
                type=2
            elif ress[1] == "warndel":
                type=2
                delete=1
            else:
                return
            
            word=ress[0]
            response=ress[2]

        except:
            if type==2:
                self.msg.reply_text("Give a response message for warn..")
                return

            word = res
            delete=1  #type=0

        chat_id = self.chat_id

        filter_list = self.db.get_filter(chat_id)

        for i in filter_list:
            if word == i[2]:
                #database.remove_filter(chat_id,word)
                self.filter_remove(word)
                break

        self.db.add_filter(chat_id=chat_id,word=word,type=type,response=response,delete=delete)
        self.msg.reply_text(word + " added to filter !")
    
    
    def filter_stat(self,res):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return

        if res == "on":
            self.db.add_settings(self.chat_id,filter=1) 
            self.msg.reply_text("Chat filter active !")

        elif res == "off":
            self.db.add_settings(self.chat_id,filter=0) 
            self.msg.reply_text("Chat filter deactivated !")
        
        elif res == "list":
            fi_li = self.db.get_filter(self.chat_id) 
            self.msg.reply_text(fi_li)
        
        #elif res == "stat":
        else:
            x = 0

            for x,y in enumerate(self.db.get_filter(self.chat_id)):
                pass
            
            z = self.db.get_settings(self.chat_id)
            
            if z[5] != 0:
                z="active"
            else:
                z="Off"

            self.msg.reply_text("Filter currently " + z + " with " + str(x) + " active filters in this chat..")



    def router(self):
        res = self.msg_string.split(None,1)

        if res[0] == "/lock":
            self.lock()

        elif res[0] == "/unlock":
            self.unlock()
        
        elif res[0] == "/filter":
            try:
                self.filter_stat(res[1])
            except:
                self.filter_stat("stat")
        elif res[0] == "/filteradd":
            m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
            if m==0:
                return
            try:
                self.filter_add(res[1])
            except:
                ex = "Please use this format : \n'/filteradd <word> <filter-type> <reason/reply-text>'\n\n<word> is the text that the bot has to react to\n<filter-type> is the type of filter, it can be any from ( 'warn', 'reply, 'delete', 'warndel', 'replydel' )\n <reason/reply-text> : is the text bot responds with during reply & warn\n\nEx : '/filteradd beep warndel for using profane words'"
                self.msg.reply_text(ex)
        elif res[0] == "/filterdel":
            self.filter_remove(res[1],1)


def filter_router(update,context):
    threading.Thread(target=filter_switch(update,context).router, args=(), daemon=True).start()

