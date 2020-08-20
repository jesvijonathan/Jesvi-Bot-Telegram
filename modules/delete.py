
import time


lock = 0


def clean(update, context):
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

    cln = context.bot.send_message(chat_id, "Cleaned !")
    time.sleep(3)
    cln.delete()


def delete(update, context):
    msg = update.message.reply_to_message
    msg_frm = update.message
    
    msg_id = msg.message_id
    chat_id = update.effective_chat.id
    
    context.bot.deleteMessage(chat_id, msg_id)

    del_msg = update.message.reply_text("Deleted !")
    time.sleep(1)

    msg_frm.delete()
    del_msg.delete()


def silent_delete(update, context):
    msg = update.message.reply_to_message
    msg_frm = update.message
    
    msg_id = msg.message_id
    chat_id = update.effective_chat.id

    msg_frm.delete()    
    context.bot.deleteMessage(chat_id, msg_id)


def lock(update, context):
    global lock
    lock = 1
    update.message.reply_text("Locked !")


def lock_delete(update, context):
    global lock
    if lock == 1:
        msg = update.message

        msg_id = msg.message_id
        chat_id = update.effective_chat.id

        context.bot.deleteMessage(chat_id, msg_id)


def unlock(update, context):
    global lock
    lock = 0
    update.message.reply_text("Unlocked !")