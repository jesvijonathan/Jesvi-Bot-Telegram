

import modules.extract as extract


def pin(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return
        
    msg = update.effective_message.reply_to_message
    
    chat_id = update.effective_chat.id
    notify = True
    msg_id = None
    
    try:
        msg_id = msg.message_id
    except:
        return

    context.bot.pinChatMessage(chat_id, msg_id)


def unpin(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return

    chat_id = update.effective_chat.id

    try:
        context.bot.unpinChatMessage(chat_id)
    except:
        pass


def set_(update,context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return
    elif m == 1:
           n = extract.sudocheck(update,context,0)
           if m == 0:
              update.message.reply_text("He got his own title boii !")
              return

    prev_message = update.message.reply_to_message
    
    chat_id = ""
    try:
        chat_id = update.effective_chat.id
        usr_id = update.effective_chat.username
    except:
        return
    
    res = update.message.text.split(None, 2)

    if res[1] == "chatname" or res[1] == "name" or res[1] == "groupname" or res[1] == "grouptitle" or res[1] == "chattitle" or res[1] == "gname":
        try:
            context.bot.set_chat_title(chat_id=chat_id,title=res[2])
            text = "Chat name changed to '" + res[2] +  "' !"
            update.message.reply_text(text)
        except:
            pass
    elif res[1] == "commands":
        
        context.bot.send_message(chat_id, text='Added Command !')
    elif res[1] == "des" or res[1] == "desc" or res[1] == "description":
        try:
            t = prev_message.tepxt
            context.bot.set_chat_description(chat_id, prev_message.text)
            context.bot.send_message(chat_id, text='Chat descirption updated !')
        except:
            if res[2] != None or res[2] != "":
                context.bot.set_chat_description(chat_id, res[2])
                context.bot.send_message(chat_id, text='Chat descirption updated !')
            else:
                return
    
    elif res[1] == "nick" or res[1] == "title" or res[1] == "uname" or res[1] == "aname" or  res[1] == "nickname" or res[1] == "byname" or res[1] == "admintitle" or res[1] == "status" or res[1] == "customtitle" or res[1] == "customname":
        try:
            msg = update.message.reply_to_message

            chat_id = update.effective_chat.id
            user_id = msg.from_user.id 

            update.effective_chat.set_administrator_custom_title(user_id = user_id ,custom_title = res[2])
            user_name = msg.from_user.username
            text = '"' + res[2]+'" set as the custom title for @' + user_name
            update.message.reply_text(text)
        except:
            pass