#import modules.extract as extract

from modules.core import extract
import time
import modules.core.database as database
import threading

del_thread_lock = threading.Lock()

class delete():

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

        bot_db = database.bot_db()

        try:
            self.tag_msg = tag_msg = update.message.reply_to_message

            self.tag_user = tag_user = tag_msg['from_user']

            bot_db.add_user(user=tag_user)
        except:
            pass

        bot_db.parse(chat=chat, user=user)


    def delete(self):
        self.tag_msg.delete()

        msg_frm = self.msg

        del_msg = msg_frm.reply_text("Deleted !")
        
        time.sleep(1)
        
        msg_frm.delete()
        del_msg.delete()


    def silent_delete(self):
        self.tag_msg.delete()
        self.msg.delete()


    def clean(self):
        del_msg = self.msg.reply_text("Purging started...")
        
        #del_thread_lock.acquire()
        
        context = self.context
        
        del_msg_id = int(del_msg.message_id)
        msg_id = int(self.tag_msg.message_id)
        chat_id = self.update.effective_chat.id # try wit self.chat

        t = 1

        while t == 1:
            if msg_id == del_msg_id:
                t = 0
    
            try:
                context.bot.deleteMessage(chat_id, del_msg_id)
            except:
                pass
            
            del_msg_id = del_msg_id-1

        #del_thread_lock.release()

        cln = context.bot.send_message(chat_id, "Purge Complete !")

        time.sleep(2)
        
        cln.delete()


def tag_del_cls(update,context):
    threading.Thread(target=delete(update,context).delete, args=(), daemon=True).start()

def s_del_cls(update,context):
    threading.Thread(target=delete(update,context).silent_delete, args=(), daemon=True).start()

def mul_del_cls(update,context):
    threading.Thread(target=delete(update,context).clean, args=(), daemon=True).start()




"""
def admin_load(update):
    global lock
    
    chat = update.effective_chat
    chat_id = str(chat.id)
    administrators = chat.get_administrators()

    l = {}
    u_dic = []

    for admin in administrators:
        user = admin.user
        u_dic.append(user.id)
        
    l[chat_id] = u_dic
"""

chat_lock = []

def lock(update, context):
    global chat_lock
    
    extract.admin_sync(update,context)
    #admin_load(update)
    
    chat = update.effective_chat
    chat_id = str(chat.id)
    
    chat_lock.append(chat_id)

    update.message.reply_text("Chat Locked !")


def ldel(update,context):
    global chat_lock
    
    chat = update.effective_chat
    chat_id = str(chat.id)

    if chat_id in chat_lock:
        pass
    else:
        return
    
    user_id = update.message.from_user.id

    link = database.get_link(chat_id,user_id)[3]

    if link == "administrator" or link == "creator":
        pass
    else:
        update.message.delete()