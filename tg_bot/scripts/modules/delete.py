#import modules.extract as extract

from modules.core import extract
import time
import modules.core.database as database
import threading

del_thread_lock = threading.Lock()

class delete_cls():

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

        self.msg_string = self.msg.text

    def delete(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return

        self.tag_msg.delete()

        msg_frm = self.msg

        del_msg = msg_frm.reply_text("Deleted !")
        
        time.sleep(1)
        
        msg_frm.delete()
        del_msg.delete()


    def silent_delete(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return
        self.tag_msg.delete()
        self.msg.delete()


    def clean(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return
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

    def router(self):
        res = self.msg_string.split(None,1)
        
        if res[0] == "/del":
            self.delete()
        
        elif res[0] == "/sdel":
            self.silent_delete()
        
        elif res[0] == "/purge":
            self.clean()


def delete_router(update,context):
    threading.Thread(target=delete_cls(update,context).router, args=(), daemon=True).start()

