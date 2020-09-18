import sys 
sys.path.append('./')
import config as config

def sudocheck(update,context, objective = 1, admin_del = 0,udel = 1):
    msg = user_id = None
    
    if objective == 1:
        msg = update.message
        user_id = msg.from_user.id
        if user_id == config.owner_id:
            return 777
    else:
        msg = update.message.reply_to_message
        user_id = msg.from_user.id 

    chat_id = update.effective_chat.id
    status = context.bot.get_chat_member(chat_id, user_id)
    
    if status['status'] == "creator":
           return 0
    elif status['status'] == "administrator":
           if admin_del == 1:
               msg.delete()
           return 1
    else:
        if udel == 1:
            msg.delete()
        return 2