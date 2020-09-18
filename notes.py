

import telegram 

import modules.extract as extract

lock = 0
msg_filter = 0
filter_text = {}
notes_data = {}


def note_check(update, context):
    global notes_data
    
    try:
        prev_message = update.message.reply_to_message
    except:
        return
    res = update.message.text
    chat_id = update.effective_chat.id

    text_1 = text = ""

    try:
        if res.startswith("#") == True:
            shrt = res[1:]
            text = str(notes_data[str(chat_id)][str(shrt)])
            update.message.reply_text(text)
            return
    except:
        return

def notes(update, context):
    global notes_data
    
    try:
        prev_message = update.message.reply_to_message
    except:
        return
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

    elif text_1 == 'list':
        try:
            text = notes_data[str(chat_id)]
        except:
            text = "No notes available !"
        update.message.reply_text(text)
        return

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
        try:
            notes_data[str(chat_id)][str(text_2)] = str(text_3)
            text = 'Note #' + str(text_2) + ' - \n"' + str(text_3) + '"'
        except:
            notes_data[str(chat_id)] = {}
            notes_data[str(chat_id)][str(text_2)] = str(text_3)
            text = 'Note #' + str(text_2) + ' - \n"' + str(text_3) + '"'
    
    else:
        text = "Wrong format !"

    update.message.reply_text(text)