import logging

from mysql import connector
from telegram import (Bot, Chat, InlineKeyboardButton, InlineKeyboardMarkup,
                      Message, ParseMode, Update, User)
from telegram.error import (BadRequest, ChatMigrated, NetworkError,
                            TelegramError, TimedOut, Unauthorized)
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from telegram.utils.helpers import escape_markdown

from config import *
from modules import *
from modules.core import *

# Bot Logging & Debugging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)


# Bot Authentication
updater = Updater(bot_token, use_context=True)
dp = updater.dispatcher


# Initialize Database & Cursor
db = connector.connect(
    host=database_host,
    user=database_user,
    password=database_password,
    database=database_name,
    auth_plugin='')
cursor = db.cursor(buffered=True)

database_create = database.database_create(cursor, db)
database_create.create_base()


def unparse(update, context):  # Unparse Incoming Responses
    print(0)
    msg = update.message
    # print("\n", msg)

    user = msg['from_user']
    chat = msg['chat']

    tag_user = None

    arg = {
        "update": update,
        "context": context,
        "chat": chat,
        "user": user
    }

    # print(**arg)

    try:
        tagmsg = update.message.reply_to_message

        tag_user = tagmsg['from_user']

        add.user(**arg, user=tag_user)

    except:
        pass

    print(1)


def main():  # Main Function
    print("started")
    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome.gate))
    dp.add_handler(MessageHandler(Filters.all, unparse))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
