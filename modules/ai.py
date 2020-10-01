import modules.wiki as wiki

def search(update,context):

    res = update.message.text.split(None, 1)
    tra = r = ""
    try:
        r = res[1]
        if res[1] == None:
            return
    except:
        return

    if res[0] == "/search" or res[0] == "/usearch" or res[0] == "/google":

        k = wiki.search(query=r)
        k = '%.4000s' % k
        if k != None:
            update.message.reply_text(text=k,parse_mode="HTML",disable_web_page_preview=True)
        return

def translate(update,context):
    res = update.message.text.split(None, 1)

    if res[0] == "/trans" or res[0] == "/translate":
        
        des = 'en'
        tag = 0

        try:
            text = res[1]
            if text == None:
                tag=1
        except:
            tag=1

        try:
            if tag ==1:
                msg = update.message.reply_to_message
                text = msg.text
            else:
                pass
        except:
            return

        tra = wiki.trans(text=text,des=des,od=0)

        update.message.reply_text(text=tra,parse_mode="HTML",disable_web_page_preview=True)

def images(update,context):
    pass