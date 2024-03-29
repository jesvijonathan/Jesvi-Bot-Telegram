import config as config

try:
    import config1 as config
except:
    import config as config

import sys
sys.path.append('./')

import modules.core.database as database

def sudocheck(update, context, objective=1, admin_del=0, udel=1):
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


def sudo_check_2(msg,
                db=None, del_lvl=0,context=None, status=None, sudo=0):
    #1-del members
    #3-del admin
    #5-del creator
    #7-del sudo

    #4-del all
    #6-admin+creator

    user_id = msg.from_user.id
    chat_id = msg.chat.id
    
    if context == None:
        status = db.get_link(chat_id,user_id)[3]
  
    else:
        status = context.bot.get_chat_member(chat_id, user_id)
        #db.add_link(chat=msg.chat, user=msg.from_user,status=status, replace=1)

    if sudo == 1:
        if user_id == config.owner_id:
            if del_lvl == 4 or del_lvl == 7:
                msg.delete()
            return 7
        elif user_id in config.sudo_user_ids:
            if del_lvl == 4 or del_lvl == 7:
                msg.delete()
            return 8


    if status['status'] == "creator":
        if del_lvl == 5 or del_lvl == 4 or del_lvl == 6 or del_lvl == 8:
            msg.delete()
        return 2
    elif status['status'] == "administrator":
        if del_lvl == 3 or del_lvl == 2 or del_lvl == 4 or del_lvl == 6 or del_lvl == 8:
            msg.delete()
        return 1
    else:
        if del_lvl == 1 or del_lvl == 2 or del_lvl == 4 or del_lvl == 8:
            msg.delete()
        return 0


def admin_sync(update, context,db):
    chat = update.effective_chat
    administrators = chat.get_administrators()

    for admin in administrators:
        status = admin.status
        user = admin.user

        status = admin.status

        db.add_user(user)
        db.add_link(chat,user,status,1)