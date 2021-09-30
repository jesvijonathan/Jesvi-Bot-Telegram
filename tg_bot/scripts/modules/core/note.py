import modules.core.database as database

import threading

import json


class notes_switch():

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


    def note_remove(self,note_name,tell=0):
        self.db.remove_note(self.chat_id,note_name)

        if tell==1:
            if note_name == '*':
                self.msg.reply_text("Cleared chat notes !")

            else:    
                self.msg.reply_text("\'" + note_name + "\' note removed !")


    def note_add(self,res):
        note_name=None
        note_text=None
        type=0
        
        try:
            ress = res.split(None, 2)
            
            if ress[1] == "text":
                type=0
            elif ress[1] == "button":
                type=1
            elif ress[1] == "link":
                type=2
            elif ress[1] == "poll":
                type=3
            elif ress[1] == "tag":
                type=4
            elif ress[1] == "pay":
                type=5
            else:
                return
            
            note_name=ress[0]
            note_text=ress[2]

        except:
            if type==0:
                self.msg.reply_text("Give a text to add..")
                return

        chat_id = self.chat_id

        note_list = self.db.get_note(chat_id)

        for i in note_list:
            if note_name == i[2]:
                self.note_remove(note_name)
                break
        
        user_id = self.user["id"]

        self.db.add_note(chat_id=chat_id,note_name=note_name,note_text=note_text,set_by=user_id)
        self.msg.reply_text("\'" + note_name + "\' added to chat notes !")


    def note_stat(self,res):
        if res == "on":
            self.db.add_settings(self.chat_id,notes=1)  #add notes field to settings table
            self.msg.reply_text("Chat note active !")

        elif res == "off":
            self.db.add_settings(self.chat_id,notes=0) 
            self.msg.reply_text("Chat note deactivated !")
        
        elif res == "list":
            no_li = self.db.get_note(self.chat_id)
            self.msg.reply_text(json.dumps(no_li, indent=4, sort_keys=True, default=str))
        
        elif res == "stat":
            x = 0
            
            dn = self.db.get_note(self.chat_id)

            for i in dn:
                x=x+1
            
            z = self.db.get_settings(self.chat_id)[6]
            
            if z == 0:
                z="in-active"
            else:
                z="active"

            self.msg.reply_text("Notes currently " + z + " with " + str(x) + " active notes in this chat..")
            

    def note_disply(self):
        no_li = self.db.get_note(self.chat_id)

        text = None

        if not no_li:
            text = "Notes not available in this chat.."

        else:
            text="Available notes -\n"
            for i in no_li:
                text += "\n• <code>" +  i[2] + "</code>"
            text += "\n\nUse #notename to view the note"
        
        self.msg.reply_text(text=text, parse_mode="HTML", disable_web_page_preview=True)


    def router(self):
        res = self.msg_string.split(None,1)
        
        if res[0][:6] == "/notes":
            try:                  #find a better method/algorith to do this
                r = res[1]
                self.note_stat(r)
                return
            
            except:
                self.note_disply()

        elif res[0] == "/noteadd":
            self.note_add(res[1])
        
        elif res[0] == "/notedel":
            self.note_remove(res[1],1)


def note_router(update,context):
    threading.Thread(target=notes_switch(update,context).router, args=(), daemon=True).start()