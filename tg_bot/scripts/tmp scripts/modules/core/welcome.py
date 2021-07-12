import config as config
from . import database
import time


# if update.effective_chat.type != 'private':
# left_member = update.effective_message.left_chat_member
# update.message.delete()


def gate(update, context):
    start = time.process_time()

    text = None

    msg = update.message
    chat = msg['chat']

    new_member = msg.new_chat_members

    for user in new_member:

        if user['id'] == config.bot_id:

            administrators = update.effective_chat.get_administrators()

            for admin in administrators:
                user = admin.user
                database.add_user(user=user)
                database.add_link(chat, user=user, status=admin.status)

            bot = context.bot.get_chat_member(
                chat['id'], config.bot_id)

            database.add_link(
                chat=chat, user=bot['user'], status=bot['status'])

            members = chat.get_members_count()

            database.add_settings(chat_id=chat['id'], members=members)
            database.add_chat(chat=chat)

            # blacklistcheck

            text = "Hello, This Is Jesvi Bot !"

        else:
            user = msg['from_user']

            database.add_user(user=user)

            user_status = context.bot.get_chat_member(chat['id'], user['id'])
            database.add_link(chat=chat, user=user,
                              status=user_status['status'])

            members = chat.get_members_count()
            database.add_settings(chat_id=chat['id'], members=members)

            # blacklistcheck

            text = "Welcome !"

    print("\n", time.process_time() - start, "\n")

    update.message.reply_text(text=text,
                              parse_mode="HTML")


def farewell(update, context, mycursor, mydb):
    user = update.effective_message.left_chat_member

    farewell_text = "Bye " + user['first_name'] + ", 👋🏼"
    update.effective_message.reply_text(farewell_text)
