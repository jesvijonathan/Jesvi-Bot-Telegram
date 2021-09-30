import modules.core.database as database
#import modules.core.extract as extract
import modules.core.extract as extract

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
        extract.admin_sync(self.update,self.context,db=self.db)

        self.db.add_settings(self.chat_id,lock=1) 
        
        self.msg.reply_text("Chat Locked !")


    def unlock(self):
        extract.admin_sync(self.update,self.context,self.db)

        self.db.add_settings(self.chat_id,lock=0) 

        self.msg.reply_text("Chat Unlocked !")


    def filter_remove(self,word,tell=0):
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
        if res == "on":
            self.db.add_settings(self.chat_id,filter=1) 
            self.msg.reply_text("Chat filter active !")

        elif res == "off":
            self.db.add_settings(self.chat_id,filter=0) 
            self.msg.reply_text("Chat filter deactivated !")
        
        elif res == "list":
            fi_li = self.db.get_filter(self.chat_id) 
            self.msg.reply_text(fi_li)
        
        elif res == "stat":
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
            self.filter_stat(res[1])
        
        elif res[0] == "/filteradd":
            self.filter_add(res[1])
        
        elif res[0] == "/filterdel":
            self.filter_remove(res[1],1)


def filter_router(update,context):
    threading.Thread(target=filter_switch(update,context).router, args=(), daemon=True).start()


def filter(msg, chat, user, tag_user):

    db = database.bot_db()

    chat_id = chat["id"]
    user_id = user["id"]
    
    sett = db.get_settings(chat_id)
    filter_bool = sett[5]
    note_bool = sett[6]
    lock_bool = sett[7]

    #msg_string = None

    def filter_del(): #use extractor | sudo check
        link = db.get_link(chat_id,user_id)[3]
        if not (link == "administrator" or link == "creator"):
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
                    msg.delete()
                    return
                elif y[3] == 1:
                    msg.reply_text(y[4])
                    if y[5] == 1:
                        msg.delete()
                elif y[3] == 2:
                    msg.reply_text("You have been warn striked !\nreason : "+y[4])
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


    