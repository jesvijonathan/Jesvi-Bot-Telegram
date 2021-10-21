import wikipedia
import threading
import modules.core.database as database

class extras_cls():
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

    def search(self, query="", urll=1):
        rep = self.msg.reply_text("Searching...", parse_mode="HTML") 

        page = None
        text = title = content = url = ""
        
        try:
            page = wikipedia.page(query+"_")
        except:
            text = "Search not found ! \n: try using familiar keywords.."
            rep.edit_text(text, parse_mode="HTML") 
        try:
            title = "Title : <b>" + page.title + "</b>\n\n"
        except:
            pass
        try:
            content = page.summary + "\n\n"
        except:
            pass
        try:
            if urll != 0:
                url = page.url
        except:
            pass

        text = title + content + url

        rep.edit_text(text, parse_mode="HTML") 
        
    
    def router(self):
        res = self.msg_string.split(None,1)
        
        if res[0] == "/search":
            self.search(res[1])

def extras_threading(update, context):
    threading.Thread(target=extras_cls(update,context).router, args=(), daemon=True).start()