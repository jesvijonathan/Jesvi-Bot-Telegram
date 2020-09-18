

import telegram 
import database as database
import re
import time

import modules.extract as extract

lock = 0
msg_filter = 0
filter_text = {}


def silent_delete(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return

    msg = update.message.reply_to_message
    msg_frm = update.message
    
    msg_id = msg.message_id
    chat_id = update.effective_chat.id

    msg_frm.delete()    
    context.bot.deleteMessage(chat_id, msg_id)


def filter_delete(update, context):
    global msg_filter
    global filter_text #filter -> group -> username/no.strike | words/delete/warn/reply

    if msg_filter == 1:
        msg = update.message
        x = msg.text.split()
      
        for i in x :
            if i in filter_text:
                if filter_text.get(i) == "<filter-warn>":
                    user_name = msg.from_user.username
                    text = "Warn-striked @"+ user_name +" for the use of '<b>" + str(i) + "</b>' !\n" + "& (<b>~</b>" + " of " + "3)" + " strikes remaining, so be carefull !\n\n" + "(<b>3</b> of 3) warns results in <b>kick</b> or <b>ban</b> from the group !"
                    msg.reply_text(text=text, 
                  parse_mode="HTML")
                    return
                elif filter_text.get(i) == "<filter-delete>":
                    msg_id = msg.message_id
                    chat_id = update.effective_chat.id
                    context.bot.deleteMessage(chat_id, msg_id)
                else:
                    msg.reply_text(filter_text[i])


def message_filter(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return
    
    global msg_filter
    global filter_text
    
    try:
        chat_id = update.effective_chat.id
    except:
        return
    try:
        filter_text[chat_id]
    except:
        filter_text[chat_id] = {}

    prev_message = update.message.reply_to_message
    res = update.message.text.split(None, 3)

    text_3 = text = ""

    try:
        text_1 = res[1]
    except:
        if msg_filter == 1: 
            bo = "on"
        else:
            bo = "off"
        text = ("Currently filter is " + str(bo) + " !")
        update.message.reply_text(text)
        return

    try:
        text_2 = res[2]
    except:
        text_2 = ""

        
    if text_1 == 'remove':
        if text_2 != "":
            del filter_text[chat_id]['filter'][text_2]
            text = 'Removed "' + str(text_2) + '" from filter !'
    
    elif text_1 == 'list':
        text = "Here is a list of filters stored :\n" + str(filter_text[chat_id]['filter'])

    elif text_1 == 'reply':
        try:
            text_3 = res[3]
        except:
            update.message.reply_text("No to-reply-with text provided !")
            return
        filter_text[chat_id]['filter'][text_2] = text_3
#        filter_text[text_2] = text_3
        text = '"' + str(text_2) + '" will be replied with "' + str(text_3) + '" !'

    elif text_1 == 'warn':
        if text_2 == "":
            text= "No filter-warn word passed !"
        else: 
            filter_text[chat_id]['filter'][text_2] = "<filter-warn>"
            text = 'Use of "' + str(text_2) + '" will warn-strike the user !'

    elif text_1 == 'off':
        msg_filter = 0
        text = 'Filter turned off !'        
    
    elif text_1 == 'on':
        msg_filter = 1
        text = 'Filter turned on !'

    elif text_1 == 'clear':
        filter_text[chat_id]['filter'].clear()
        text = "Cleared filter data"
    
    else:
        try:
            filter_text[chat_id]['filter']
        except:
            filter_text[chat_id]['filter'] = {}

        filter_text[chat_id]['filter'][text_1] = "<filter-delete>"
        text = 'Added "' + str(text_1) + '" to filter !'

    update.message.reply_text(text)


def warn_strike(update,context):
    database.create_settings_base()
    m = extract.sudocheck(update,context)
    if m == 2:
        return
    else:
        n = extract.sudocheck(update,context,objective=0,udel=0)
        if n == 0:
            update.message.reply_text("Try /rip instead...")
            return
        elif n == 1:
            update.message.reply_text("Can't warn an Admin !")
            return
    
    reason = "~"

    try:
        res = update.message.text.split(None, 1)
        reason = res[1]
    except:
        pass

    msg = update.message.reply_to_message

    warn_user_id = str(msg.from_user.id)
    warn_by_user_id = str(update.message.from_user.id)
    msg_id = msg.message_id

    chat = msg['chat']
    chat_id = chat.id
    chat_id = re.sub(r'[^\w]', '', str(chat_id))

    database.create_warn_base()
    rem = database.add_warn_base_2(chat_id=chat_id,user_id=warn_user_id,striked_by=warn_by_user_id,message_id=msg_id,reason=reason,remove=0)
    w = database.add_settings_base(chat_id=chat_id)
    text = ""

    if str(rem) >= str(w):
        text = ("<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " has been warn striked by " + "<a href='tg://user?id=" + str(update.message.from_user.id) + "'>" + str(update.message.from_user.first_name) + "</a> !"
    "\n\nReason : '<i><a href='https://telegram.me/" + chat.username + "/"+ str(msg_id) + "'>" + reason + "</a></i>'" +
    "\nStrikes  : <b>" + str(rem) + "/"+ str(w) +"</b> " + 
    "\n\n<b>Limit " + str(w) + " of " + str(w) + " reached !"+
    "\nYou are screwed !</b>")
    else:
        text = ("<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " has been warn striked by " + "<a href='tg://user?id=" + str(update.message.from_user.id) + "'>" + str(update.message.from_user.first_name) + "</a> !"
    "\n\nReason : '<i><a href='https://telegram.me/" + chat.username + "/"+ str(msg_id) + "'>" + reason + "</a></i>'" +
    "\nStrikes  : <b>" + str(rem) + "/"+ str(w) +"</b> " + 
    "\n\n<b>" + str(w) + " of " + str(w) + "</b>" + " strikes result in ban or mute, So watch out !")

    update.message.reply_text(text=text,parse_mode="HTML",disable_web_page_preview=True)


def warn_info(update,context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return
    else:
        n = extract.sudocheck(update,context,objective=0,udel=0)
        if n == 0:
            update.message.reply_text("Try /rip instead...")
            return
        elif n == 1:
            update.message.reply_text("Can't warn an Admin !")
            return
    
    reason = "~"

    try:
        res = update.message.text.split(None, 1)
        reason = res[1]
    except:
        pass

    msg = update.message.reply_to_message

    warn_user_id = str(msg.from_user.id)
    warn_by_user_id = str(update.message.from_user.id)
    msg_id = msg.message_id

    chat = msg['chat']
    chat_id = chat.id
    chat_id = re.sub(r'[^\w]', '', str(chat_id))

    database.create_warn_base()
    rem = database.add_warn_base_2(chat_id=chat_id,user_id=warn_user_id,striked_by=warn_by_user_id,message_id=msg_id,reason=reason,remove=0)

    text = ("<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " has been warn striked by " + "<a href='tg://user?id=" + str(update.message.from_user.id) + "'>" + str(update.message.from_user.first_name) + "</a> !"
    "\n\nReason : '<i><a href='https://telegram.me/" + chat.username + "/"+ str(msg_id) + "'>" + reason + "</a></i>'" +
    "\nStrikes  : <b>" + rem + "/x</b> " + 
    "\n\n<b>x of x</b>" + " strikes result in ban or mute, So watch out !")
    
    update.message.reply_text(text=text,parse_mode="HTML",disable_web_page_preview=True)