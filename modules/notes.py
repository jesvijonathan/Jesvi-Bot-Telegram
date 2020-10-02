import telegram 
from database import push_note, get_note
import modules.extract as extract

lock = 0
msg_filter = 0
filter_text = {}
notes_data = {}


def note_check(update, context):
    global notes_data
    
    res = update.message.text

    if res.startswith("#") == True:    
        
        chat_id = update.effective_chat.id
        text = ""

        shrt = res[1:]

        chat_idd = str(chat_id)
        chat_idd = chat_idd[1:] 
        n = get_note(chat_id=chat_idd,note_name=shrt)
        if n != -1:
            text = str(n[0])
            update.message.reply_text(text,parse_mode="HTML",disable_web_page_preview=True)
        return
    else:
        return


def notes(update, context):
    global notes_data
    
    msg = update.message
    
    res = update.message.text.split(None, 3)
    chat_id = update.effective_chat.id

    text_3 = text = ""

    try:
        text_1 = res[1]
    except: 
        try:
            xt = notes_data[str(chat_id)]
            text = "Available notes -\n"
            for key in xt:
                text = text + "\n#" + key
#            text = text + "\n\nUse #NoteName to view the note"
        except:
            text = "Notes not available"
        update.message.reply_text(text)
        return

    try:
        text_2 = res[2]
    except:
        text_2 = ""
    
    m = extract.sudocheck(update,context)
    if m == 2:
        return
        
    if text_1 == 'remove':
        if text_2 != "":
            try:
                del notes_data[str(chat_id)][str(text_2)]
                text = 'Removed #' + str(text_2) + ' from notes !'
            except:
                text = "No such note availble !"

    elif text_1 == 'set':
        try:
            text_2 = res[2]
        except:
            update.message.reply_text("Note Name & Content not provided !")
            return
        try:
            text_3 = res[3]
        except:
            update.message.reply_text("Note content not provided !")
            return
        
        chat_idd = str(chat_id)
        chat_idd = chat_idd[1:]
        user_id = str(msg.from_user.id)

        push_note(chat_id=chat_idd,note_name=text_2,note=text_3,set_by=user_id)
        text = 'Note #' + str(text_2) + ' - \n"' + str(text_3) + '"'
    
    else:
        text = "Wrong format !"

    update.message.reply_text(text)