
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from typing import Optional, List

import telegram 
from telegram.error import BadRequest
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import mention_html
import time

updater = Updater("1262215479:AAEDrQUR-wY1XIvzHiL6_6Vu_PHyW8g4UHI", use_context=True)
dp = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def unmute(update, context):
    msg = update.message.reply_to_message

    user_id = msg.from_user.id 
    chat_id = update.effective_chat.id
    user_name = msg.from_user.username
    first_name = msg.from_user.first_name
    
    current = eval(str(context.bot.getChat(chat_id).permissions))
    new = {'can_send_messages': True, 
           'can_send_media_messages': True,
           'can_send_polls': True,
           'can_send_other_messages': True, 
           'can_add_web_page_previews': True,}

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
    
    context.bot.restrict_chat_member(chat_id, user_id,permissions=new_permissions)
    update.message.reply_text("Unmuted "+ str(first_name) + " !")


def mute(update, context):
    msg = update.message.reply_to_message
    res = update.message.text.split(None, 1)
    
    user_id = msg.from_user.id 
    chat_id = update.effective_chat.id
    user_name = msg.from_user.username
    first_name = msg.from_user.first_name
    
    current = eval(str(context.bot.getChat(chat_id).permissions))
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
    
    context.bot.restrict_chat_member(chat_id, user_id,permissions=new_permissions)
    update.message.reply_text("Muted "+ str(first_name) + " !")


def main():
    
    dp.add_handler(CommandHandler("mute", mute))
    dp.add_handler(CommandHandler("unmute", unmute))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()