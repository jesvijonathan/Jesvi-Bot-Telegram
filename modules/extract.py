def sudocheck(update,context, objective = 1):
    msg = user_id = None
    
    if objective == 1:
        msg = update.message
        user_id = msg.from_user.id
    else:
        msg = update.message.reply_to_message
        user_id = msg.from_user.id 
    
    chat_id = update.effective_chat.id
    status = context.bot.get_chat_member(chat_id, user_id)
    
    if status['status'] == "creator":
           return 0
    elif status['status'] == "administrator":
           return 1
    else:
        msg.delete()
        return 2