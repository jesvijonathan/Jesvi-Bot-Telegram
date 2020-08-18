
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater("1262215479:AAEDrQUR-wY1XIvzHiL6_6Vu_PHyW8g4UHI", use_context=True)
dp = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def pin(update, context):
    msg = update.effective_message.reply_to_message
    
    chat_id = update.effective_chat.id
    notify = True
    msg_id = None
    
    try:
        msg_id = msg.message_id
    except:
        return

    context.bot.pinChatMessage(chat_id, msg_id)


def unpin(update, context):
    chat_id = update.effective_chat.id

    try:
        context.bot.unpinChatMessage(chat_id)
    except:
        pass


def main():

    dp.add_handler(CommandHandler("pin", pin))

    dp.add_handler(CommandHandler("unpin", unpin))
    
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()