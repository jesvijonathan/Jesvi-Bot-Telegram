
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater("1262215479:AAHtwK5J-6lP8iw9b7uRjcOaazelRkHgq3s", use_context=True)
dp = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def greet(update, context):
    for new_member in update.message.new_chat_members:
            group = update.message["chat"]
            welcome_text = "Welcome to " + str(group['title']) + ", "+ str(new_member['first_name']) + " ! 🥳"
    update.message.reply_text(welcome_text)


def farewell(update, context):
    left_member = update.effective_message.left_chat_member
    farewell_text = "Bye " + str(left_member['first_name']) + ", 👋🏼"
    update.effective_message.reply_text(farewell_text)


def main():

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, greet))
    dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, farewell))
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()