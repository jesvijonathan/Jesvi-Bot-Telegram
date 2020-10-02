
import modules.extract as extract
import time

from database import get_link

lock = 0


def clean(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return
    

    msg = update.message.reply_to_message
    del_msg = update.message.reply_text("Cleaning started...")

    msg_id = int(msg.message_id)
    chat_id = update.effective_chat.id
    del_msg_id = int(del_msg.message_id)

    t = 1
    
    while t == 1:
        if msg_id == del_msg_id:
           t = 0
        
        try:
            context.bot.deleteMessage(chat_id, del_msg_id)
        except:
            pass

        del_msg_id=del_msg_id-1

    """
    if msg_id >= del_msg_id:
           t = 0
        
        try:
            context.bot.deleteMessage(chat_id, msg_id)
        except:
            pass

        msg_id=msg_id+1
    """

    cln = context.bot.send_message(chat_id, "Cleaned !")
    time.sleep(3)
    cln.delete()


def delete(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return

    msg = update.message.reply_to_message
    msg_frm = update.message
    
    try:
        msg_id = msg.message_id
    except:
        return

    chat_id = update.effective_chat.id
    
    context.bot.deleteMessage(chat_id, msg_id)

    del_msg = update.message.reply_text("Deleted !")
    time.sleep(1)

    msg_frm.delete()
    del_msg.delete()


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


def lock(update, context):
    m = extract.sudocheck(update,context,1,1)
    if m == 2:
        return
    if m == 1:
        return

    global lock
    lock = 1
    update.message.reply_text("Locked !")


def lock_delete(update, context):
    global lock

    if lock == 1:
        user_id = update.message.from_user.id
        chat_id = str(update.effective_chat.id)
        #status = context.bot.get_chat_member(chat_id, user_id)['status']
        
        status = get_link(chat_id=chat_id[1:],user_id=user_id,status=1)

        if status[0][1] == "member":
            msg_id = update.message.message_id
            context.bot.deleteMessage(chat_id, msg_id)
        else:
            return 1
    else:
        return 0
        

def unlock(update, context):
    m = extract.sudocheck(update,context,1,1)
    if m == 2 or m == 1:
        return

    global lock
    lock = 0
    update.message.reply_text("Unlocked !")