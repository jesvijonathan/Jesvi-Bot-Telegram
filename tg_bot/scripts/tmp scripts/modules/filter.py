

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

    res = update.message.text.split(None, 3)

    text_3 = text = ""
    
    if res[0] == '/filterreset' or res[0] == "/resetfilter":
        chat_idd = str(chat_id)[1:]
        user_id = str(update.message.from_user.id)
        k = database.push_filter(chat_id=chat_idd,pop=2)
        text = "Reset filter data"
        update.message.reply_text(text)
        return


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

    if text_1 == 'off' or text_1 == "on":
        msg_filter = 0
        text = 'Filter turned off !'

    elif text_1 == 'remove':
        if text_2 != "":
            chat_idd = str(chat_id)[1:]
            user_id = str(update.message.from_user.id)
            k = database.push_filter(chat_id=chat_idd,filterr=text_2,pop=1)
            text = 'Removed "' + str(text_2) + '" from filter !'
    
    elif text_1 == 'warn' or text_1 == "delete" or text_1 == "reply":
        if text_2 == "":
            text= "No filter-warn word passed !"
        
        else:
            if text_1 == "reply":
                try:
                    text_3 = res[3]
                except:
                    return
            
            chat_idd = str(chat_id)[1:]
            user_id = str(update.message.from_user.id)
            k = database.push_filter(chat_id=chat_idd,filterr=text_2,action=text_1,set_by=user_id,replyt=text_3)
            text = 'Use of "' + str(text_2) + '" will - the user !'

    elif text_1 == 'list':
        k = database.get_filter(chat_id=chat_idd,filterr=None,al=1)
        text = "Here is a list of filters stored :\n"

    else:
        chat_idd = str(chat_id)[1:]
        user_id = str(update.message.from_user.id)
        database.push_filter(chat_id=chat_idd,filterr=text_1,set_by=user_id,res=1)
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
    chat_idd = chat.id
    chat_id = re.sub(r'[^\w]', '', str(chat_idd))

    database.create_warn_base()
    rem = database.add_warn_base_2(chat_id=chat_id,user_id=warn_user_id,striked_by=warn_by_user_id,message_id=msg_id,reason=reason,remove=0)

    sett = database.add_settings_base(chat_id=chat_id)
    text=""
    warn_lim = sett[0][0]
    action = sett[0][1]
    a = 0
    if int(rem) >= int(warn_lim):
        text = ("<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " has been warn struck by " + "<a href='tg://user?id=" + str(update.message.from_user.id) + "'>" + str(update.message.from_user.first_name) + "</a> !"
    "\n\nReason : '<i><a href='https://telegram.me/" + chat.username + "/"+ str(msg_id) + "'>" + reason + "</a></i>'" +
    "\nStrikes  : <b>" + rem + "/" + warn_lim +"</b> " + 
    "\n\n<b>Limit Reached !</b>" + " (Action : <b>" + action + "</b>)" )
        a = 1

    else:
        text = ("<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " has been warn struck by " + "<a href='tg://user?id=" + str(update.message.from_user.id) + "'>" + str(update.message.from_user.first_name) + "</a> !"
    "\n\nReason : '<i><a href='https://telegram.me/" + chat.username + "/"+ str(msg_id) + "'>" + reason + "</a></i>'" +
    "\nStrikes  : <b>" + rem + "/" + warn_lim + "</b> " + 
    "\n\n<b>" + warn_lim +" of " + warn_lim + "</b>" + " strikes result in <b>" + sett[0][1] + "</b>, So watch out !")

    if a == 1:
        i=""
        if action == "mute":
    
            current = eval(str(context.bot.getChat(chat_idd).permissions))
            new = {'can_send_messages': False, 
                   'can_send_media_messages': False,
                   'can_send_polls': False,
                   'can_send_other_messages': False, 
                   'can_add_web_page_previews': False,}
        
            permissions = {'can_send_messages': None, 
                           'can_send_media_messages': None, 
                           'can_send_polls': None, 
                           'can_send_other_messages': None, 
                           'can_add_web_page_previews': None, 
                           'can_change_info': None, 
                           'can_invite_users': None, 
                           'can_pin_messages': None}
            
            permissions.update(current)
            permissions.update(new)
            new_permissions = telegram.ChatPermissions(**permissions)
     
            context.bot.restrict_chat_member(chat_idd, warn_user_id,permissions=new_permissions)
            i = "<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " has been <b>Muted</b> !"
            pass

        elif action == "kick":
            kick = update.effective_chat.unban_member(warn_user_id)
            #i = "<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " has been <b>Kicked</b> !"
        elif action == "ban":
            ban = update.effective_chat.kick_member(warn_user_id)
            i = "<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " has been <b>Banned</b> !"

        context.bot.send_message(chat_id=chat_idd, text=i, 
                  parse_mode="HTML")

    update.message.reply_text(text=text,parse_mode="HTML",disable_web_page_preview=True)


def warn_set(update,context,cl=0,re=0):
    database.create_settings_base()
    m = extract.sudocheck(update,context)
    if m == 2:
        return
    
    res = update.message.text.split(None, 2)

    chat_id = str(update.effective_chat.id)
    chat_idd = chat_id[1:]

    if res[0] == "/warnclear" or res[0] == "/withdraw":
        msg = update.message.reply_to_message
        warn_user_id = str(msg.from_user.id)
        k = database.warn_clear(chat_id=str(chat_idd),user_id=warn_user_id,reset=0)
        if k == 1:
            update.message.reply_text(text= "Last warn strike on " + "<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " has been <b>removed</b> !",parse_mode="HTML",disable_web_page_preview=True)      
        return
    elif res[0] == "/warnreset" or res[0] == "/forgive":
        msg = update.message.reply_to_message
        warn_user_id = str(msg.from_user.id)
        k = database.warn_clear(chat_id=str(chat_idd),user_id=warn_user_id,reset=1)
        if k == 1:
            update.message.reply_text(text= "Warn log has been <b>reset</b> for " + "<a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name +"</a>" + " !",parse_mode="HTML",disable_web_page_preview=True)
        return
    elif res[0] == "/warninfo":
        msg = update.message.reply_to_message
        warn_user_id = str(msg.from_user.id)
        inf = database.warninfo(chat_id=chat_idd,user_id=warn_user_id)
        c = 1
        tt = tx = "Warn Info - <b><a href='tg://user?id=" + str(warn_user_id) + "'>" + msg.from_user.first_name + "</a></b>\n"
        for i in inf:
            warn_no = "\nWarn streak : " + str(c)
            warn_by = "\nWarned by : <b><a href='tg://user?id=" + str(i[0]) + "'>User</a></b>"
            reason = "\nReason : <b><i><a href='https://telegram.me/" + update.effective_chat.username + "/" + i[1] + "'>" + i[2] + "</a></i></b>"
            date = "\nDate : <i>" + str(i[3])  + "</i>\n"
            tx = tx + warn_no + warn_by + reason + date
            c+=c

        if tx == None or tx == tt:
            tx = tx + "\n<i>Clean as a whistle !</i>"
        update.message.reply_text(text=tx,parse_mode="HTML",disable_web_page_preview=True)
        return
    elif res[0] == "/warnlist":
        inf = database.warninfo(chat_id=chat_idd)
        c = 1
        cha = ""
        try:
            cha =  "@" + str(update.effective_chat.username)
            if cha == "@None":
                cha = ""
        except:
            pass
        tx = "Warn list - " + cha + "\n"
        tt = tx
        for i in inf:
            no = "\n" + str(c) + " - "
            total_strike = "(Strikes : <b>" + str(i[1]) + "</b>) - "
            user = "<b><a href='tg://user?id=" + str(i[0]) + "'>" + i[0] + "</a></b>"
            tx = tx + no + total_strike + user
            c+=c
        if tt == tx:
            tx= tx + "\n<i>No records in this chat !</i>"
        context.bot.send_message(chat_id=chat_id, text=tx, parse_mode="HTML")
        return


    if res[1] == "limit":
        try:
            if res[2] == None or isinstance(int(res[2]), int) == False:
                return
        except:
            return
        sett = database.add_settings_base(chat_id=chat_idd,warn_limit=res[2])
        update.message.reply_text(text="Warn limit set to <b>" + res[2] +"</b> !",parse_mode="HTML",disable_web_page_preview=True)

    elif res[1] == "action":
        try:
            if res[2] == "kick" or res[2] == "mute" or res[2] == "ban":
                sett = database.add_settings_base(chat_id=chat_idd,warn_action=res[2])
                update.message.reply_text(text="Warn action set to <b>" + res[2] +"</b> !",parse_mode="HTML",disable_web_page_preview=True)
            else:
                return
        except:
            return
    else:
        return