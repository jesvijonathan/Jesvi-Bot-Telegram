
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import time


updater = Updater("1262215479:AAEDrQUR-wY1XIvzHiL6_6Vu_PHyW8g4UHI", use_context=True)
dp = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def rip(update, context):
    user_id = update.effective_message.from_user.id
    first_name = update.effective_message.from_user.first_name

    txt = update.message.reply_text("Okay, You asked for it.. !")
    
    time.sleep(3)

    kick = update.effective_chat.unban_member(user_id)
    
    txt.edit_text( str(first_name) + " got voluntarily kicked !")


def ban(update, context):
    msg = update.message.reply_to_message

    user_id = msg.from_user.id 
    first_name = msg.from_user.first_name

    ban = update.effective_chat.kick_member(user_id)

    update.message.reply_text("Banned " + str(first_name) + " !")


def unban(update, context):
    msg = update.message.reply_to_message

    user_id = msg.from_user.id 
    first_name = msg.from_user.first_name
    user_name = msg.from_user.username
    chat = update.effective_chat

    chat.unban_member(user_id)

    update.message.reply_text("Unbanned " + str(first_name) + " !")


def kick(update, context):
    msg = update.message.reply_to_message

    user_id = msg.from_user.id 
    first_name = msg.from_user.first_name

    kick = update.effective_chat.unban_member(user_id)
    
    msg.reply_text( "Kicked " + str(first_name) + " !")


def leave(update, context):
    msg = update.message.reply_to_message

    user_id = msg.from_user.id 
    first_name = msg.from_user.first_name

    kick = update.effective_chat.unban_member(user_id)
    
    msg.reply_text( "Kicked " + str(first_name) + " !")
    

def main():

    dp.add_handler(CommandHandler("rip", rip))

    dp.add_handler(CommandHandler("kick", kick))

    dp.add_handler(CommandHandler("ban", ban))

    dp.add_handler(CommandHandler("unban", unban))

    dp.add_handler(CommandHandler("leave", leave))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()