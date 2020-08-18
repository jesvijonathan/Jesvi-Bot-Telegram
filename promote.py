
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater("1262215479:AAEDrQUR-wY1XIvzHiL6_6Vu_PHyW8g4UHI", use_context=True)
dp = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def promote(update, context):
    msg = update.message.reply_to_message

    chat_id = update.effective_chat.id
    user_id = msg.from_user.id 
    first_name = msg.from_user.first_name

    context.bot.promoteChatMember(int(chat_id), int(user_id),
                              can_change_info=True,
                              can_delete_messages=True,
                              can_invite_users=True,
                              can_restrict_members=True,
                              can_pin_messages=True,
                              can_promote_members=True)
        
    update.message.reply_text("Promoted " + str(first_name) +" !")


def depromote(update, context):
    msg = update.message.reply_to_message

    chat_id = update.effective_chat.id
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name

    context.bot.promoteChatMember(int(chat_id), int(user_id),
                              can_change_info=False,
                              can_delete_messages=False,
                              can_invite_users=False,
                              can_restrict_members=False,
                              can_pin_messages=False,
                              can_promote_members=False)
        
    update.message.reply_text("Depromoted " + str(first_name) +" !")


def main():

    dp.add_handler(CommandHandler("promote", promote))

    dp.add_handler(CommandHandler("demote", depromote))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()