def sudocheck(update,context):
    msg_frm = update.message
    msg1 = msg_frm.from_user.id
    chat_id = update.effective_chat.id
    status = context.bot.get_chat_member(chat_id, msg1)
    
    if status['status'] == "creator":
           return 0
    elif status['status'] == "administrator":
           return 1
    else:
        msg_frm.delete()
        return 2