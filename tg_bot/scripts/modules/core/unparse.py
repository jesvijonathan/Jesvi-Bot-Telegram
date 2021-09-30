from mysql.connector import connection
from modules.core import extract
import time
import threading
import itertools
from multiprocessing.pool import ThreadPool

import modules.core.database as database

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


        try:
            self.tag_msg = tag_msg = update.message.reply_to_message

            self.tag_user = tag_user = tag_msg['from_user']

            database.add_user(user=tag_user)
        except:
            pass

        database.parse(chat=chat, user=user)
        self.dele()
        #self.lock_del
        #del self
        #del(self)


    def dele(self):
        link = database.get_link(self.chat['id'],self.user['id'])[3]
        if not (link == "administrator" or link == "creator"):
            self.msg.delete()
        

        
    def lock_del(self):
        global chat_lock

        chat_id = self.chat.id

        if chat_id not in chat_lock:
            return

        user_id = self.user.id

        link = database.get_link(chat_id,user_id)[3]

        if link != "administrator" or link != "creator":
            self.msg.delete()
        self.msg.delete()



def thread_unparse(update, context):
    threading.Thread(target=unparse_cls(update,context).lock_del, args=(), daemon=True).start()