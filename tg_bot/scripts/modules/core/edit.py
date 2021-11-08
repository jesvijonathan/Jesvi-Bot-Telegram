import modules.core.extract as extract
import modules.core.database as database

import threading
try:
    from config1 import *
except:
    from config import *
    
import time


class edit_cls():
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

    def pin(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m == 0:
           return

        self.context.bot.pinChatMessage(self.chat_id, self.tag_msg.message_id)

    def unpin(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m == 0:
           return
   
        try:
            self.context.bot.unpinChatMessage(self.chat_id)
        except:
            pass


    def promote(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m == 0:
            return
        else:
            n = extract.sudo_check_2(msg=self.tag_msg,del_lvl=0,context=self.context)
            if n == 2:
                self.msg.reply_text(
                    "'I can't give where I got my powers from' ~@jesvi_bot")
                return
            elif n == 1:
                self.msg.reply_text("Already a fellow admin !")
                return
    
        self.context.bot.promoteChatMember(int(self.chat_id), int(self.tag_user_id),
                                      can_change_info=True,
                                      can_delete_messages=True,
                                      can_invite_users=True,
                                      can_restrict_members=True,
                                      can_pin_messages=True,
                                      can_promote_members=False)
    
        self.msg.reply_text("Promoted " + self.tag_user["first_name"] + " !")
    
    
    def depromote(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
        if m == 0:
            return
        elif m == 2:
            pass
        else:
            n = extract.sudo_check_2(msg=self.tag_msg,del_lvl=0,context=self.context)
            if n == 2:
                self.msg.reply_text(
                    "Wha- !")
                return
            elif n == 1:
                self.msg.reply_text("Admins have to demote other admins manually..")
                return
                
        self.context.bot.promoteChatMember(int(self.chat_id), int(self.tag_user_id),
                                      can_change_info=False,
                                      can_delete_messages=False,
                                      can_invite_users=False,
                                      can_restrict_members=False,
                                      can_pin_messages=False,
                                      can_promote_members=False)
    
        self.msg.reply_text("Depromoted " + str(self.tag_user["first_name"]) + " !")

    def router(self):
        res = self.msg_string.split(None,1)
        
        if res[0] == "/promote":
            self.promote()
        
        elif res[0] == "/demote":
            self.depromote()
        
        elif res[0] == "/pin":
            self.pin()

        elif res[0] == "/unpin":
            self.unpin()

        elif res[0] == "/titleset":
            m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
            if m == 0:
                return
            
            text = "Error"
            try:
                self.context.bot.set_chat_title(chat_id=self.chat_id, title=res[1])
                text = "Chat name changed to '" + res[1] + "' !"
            except Exception as x:
                text = str(x)

            self.msg.reply_text(text)
        elif res[0] == "/descset":
            m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
            if m == 0:
                return
            
            text= "Error !"
            try:
                if self.tag_msg == None:
                    try:
                        self.context.bot.set_chat_description(self.chat_id, str(res[1]))
                        text = 'Chat descirption updated !'
                    except:pass

                else:
                    try:
                        self.context.bot.set_chat_description(self.chat_id, self.tag_msg.text)
                        text = 'Chat descirption updated !'
                    except:pass

                self.context.bot.send_message(
                        self.chat_id, text=text)
            except:
                pass
        elif res[0] == "/nickset":
            m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
            if m == 0:
                return
            
            text = "Error"
            try:
                self.update.effective_chat.set_administrator_custom_title(
                    user_id=self.tag_user_id, custom_title=res[1])
                try:
                    user_name = "for @" + self.tag_user.username
                except:
                    user_name = ""
                text = '"' + res[1]+'" set as the custom title ' + user_name

            except Exception as x:
                text = str(x)    
            self.msg.reply_text(text)
            

        elif res[0] == "/bioset":
            m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
            if m==0:
                return
            else:
                n = extract.sudo_check_2(msg=self.tag_msg,del_lvl=0,context=self.context)
                if n == 2 and m == 1:
                    self.msg.reply_text("Admins can't set the group owner's bio") 
                    return
            try:
                bio = res[1]
            except:
                self.msg.reply_text("Provide details about the tagged user's role in the group")
                return
            self.db.add_link(self.chat,self.tag_user,status=None,replace=5,bio=bio)
            self.msg.reply_text(self.tag_user["first_name"] +" 's group-bio updated !")

        elif res[0] == "/biodel":
            m = extract.sudo_check_2(msg=self.msg,del_lvl=1,context=self.context)
            if m==0:
                return
            self.db.add_link(self.chat,self.tag_user,status=None,replace=5,bio=None)
            self.msg.reply_text( self.tag_user["first_name"] + " 's group-bio deleted !")

        elif res[0] == "/bio":
            try:
                bio = self.db.get_link(self.chat_id,self.tag_user_id)
                if bio[4] == None:
                    self.msg.reply_text("Bio has not been set for this user in this group !")
                    return
                self.msg.reply_text(str(bio[4]))
            except:
                self.msg.reply_text("Bio has not been set for this user !")


def edit_router(update,context):
    threading.Thread(target=edit_cls(update,context).router, args=(), daemon=True).start()