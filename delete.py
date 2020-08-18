
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import time

updater = Updater("1262215479:AAEDrQUR-wY1XIvzHiL6_6Vu_PHyW8g4UHI", use_context=True)
dp = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def clean(update, context):
    msg = update.message.reply_to_message
    del_msg = update.message.reply_text("Cleaning...")

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


def msg_id(update, context):
    msg = update.message.reply_to_message
    msg_id = msg.message_id
    update.message.reply_text(str(msg_id))


lock = 0


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
    
    else:
        pass


def unlock(update, context):
    global lock
    lock = 0
    update.message.reply_text("Unlocked !")


def main():

    dp.add_handler(CommandHandler("clean", clean))
    dp.add_handler(CommandHandler("del", delete))
    dp.add_handler(CommandHandler("sdel", silent_delete))
    dp.add_handler(CommandHandler("id", msg_id))
    
    dp.add_handler(CommandHandler("lock", lock))
    dp.add_handler(CommandHandler("unlock", unlock))

    dp.add_handler(MessageHandler(Filters.all, lock_delete))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()