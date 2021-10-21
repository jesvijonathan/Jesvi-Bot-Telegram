from re import L
import modules.core.database as database
import modules.core.extract as extract

from config import *

import time
import threading

class rule_cls():

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

    def rule_view(self,info=1):
        
        rule = self.db.get_rule(self.chat_id)

        if not rule:
            text = "Rules not available on this chat !"
        elif info == 1:
            text = "Group rules (" + rule[0] + ") -\n\n" + rule[1]
        else:
            text = rule[1]
        
        self.msg.reply_text(
                    text=text, parse_mode="HTML", disable_web_page_preview=True)
    
    def rule_add(self,str):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return

        try:
            res = str.split(None, 1)
            type = res[0]
        except:
            self.msg.reply_text(
                    text="Format incorrect ! #1")
            return
        
        try:
            res = str.split(None, 2)
            red = int(res[1])
        except:
            self.msg.reply_text(
                    text="Format incorrect ! #2")
            return

        try:
            res = str.split(None, 2)
            text = res[2]
        except:
            self.msg.reply_text(
                    text="Format incorrect #3")
            return

        self.db.add_rule(self.chat_id, type, red, text)

        self.msg.reply_text(
                    text="Rule set !", parse_mode="HTML", disable_web_page_preview=True)

    def rule_del(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m==0:
            return
            
        self.db.del_rule(self.chat_id)

        self.msg.reply_text(
                    text="Rule Removed !")
        

    def router(self):
        res = self.msg_string.split(None,1)
        
        if res[0] == "/ruleset":
            self.rule_add(res[1])

        elif res[0] == "/ruledel":
            self.rule_del()
        elif res[0][:6] == "/rules":

            rule = self.db.get_rule(self.chat_id)
            if not rule:
                text = "Rules not available on this chat !"
            
            elif self.update.effective_chat.type != 'private':
                text = ("<a href='t.me/" + bot_username + "?start=" + str(self.chat_id) + "'>Click Here</a> to view the group rules")
            self.msg.reply_text(
                    text=text, parse_mode="HTML", disable_web_page_preview=True)

        elif res[0] == "/rule":
            self.rule_view(0)
        
        elif res[0][:6] == "/start":
            self.chat_id = res[1]
            self.rule_view(1)


def rule_router(update, context):
    threading.Thread(target=rule_cls(update,context).router, args=(), daemon=True).start()
