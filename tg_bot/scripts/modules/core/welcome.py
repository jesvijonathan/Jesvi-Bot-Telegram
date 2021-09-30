import config as config
#from . import database

import modules.core.database as database
from . import mute

import time

from mysql import connector

from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ChatMember


# if update.effective_chat.type != 'private':
# left_member = update.effective_message.left_chat_member
# update.message.delete()
def cut_str_to_bytes(s, max_bytes):
    # cut it twice to avoid encoding potentially GBs of `s` just to get e.g. 10 bytes?
    b = s[:max_bytes].encode('utf-8')[:max_bytes]

    if b[-1] & 0b10000000:
        last_11xxxxxx_index = [i for i in range(-1, -5, -1)
                               if b[i] & 0b11000000 == 0b11000000][0]
        # note that last_11xxxxxx_index is negative

        last_11xxxxxx = b[last_11xxxxxx_index]
        if not last_11xxxxxx & 0b00100000:
            last_char_length = 2
        elif not last_11xxxxxx & 0b0010000:
            last_char_length = 3
        elif not last_11xxxxxx & 0b0001000:
            last_char_length = 4

        if last_char_length > -last_11xxxxxx_index:
            # remove the incomplete character
            b = b[:last_11xxxxxx_index]

    return b.decode('utf-8')


def gate(update, context):
    db = database.bot_db()

    start = time.process_time()

    text = None

    msg = update.message
    chat = msg['chat']
    chat_id = chat['id']

    new_member = msg.new_chat_members

    for user in new_member:

        user_id = user['id']

        if user_id == config.bot_id:

            administrators = update.effective_chat.get_administrators()

            for admin in administrators:
                user = admin.user
                db.add_user(user=user)
                db.add_link(chat, user=user, status=admin.status)

            bot = context.bot.get_chat_member(
                chat_id, config.bot_id)

            db.add_link(
                chat=chat, user=bot['user'], status=bot['status'])

            members = chat.get_members_count()

            db.add_settings(chat_id=chat_id, members=members)
            db.add_chat(chat=chat)

            db.add_welcome(chat_id=chat_id)

            # blacklistcheck

            text = "Hello, This Is Jesvi Bot !"

            update.message.reply_text(
                text, parse_mode="HTML")

        else:
            reply_markup = None

            db.add_user(user=user)

            user_status = context.bot.get_chat_member(chat_id, user_id).status

            members = chat.get_member_count() #previously "get_members_count"
            db.add_settings(chat_id=chat_id, members=members)

            wel = db.get_welcome(chat_id=chat_id)

            first_name = user['first_name']
            
            if len(first_name.encode('utf-8')) > 32:
                first_name = cut_str_to_bytes(first_name,32)  # for security | to fix length < 32bytes max
            
            print(wel)
            
            text = wel[1].format(first_name=first_name,
                                 last_name=user['last_name'],
                                 group_name=chat["title"])
            
            stat = context.bot.get_chat_member(chat_id, msg.from_user.id).status
            if stat == "creator":
                stat = "administrator"
            
            if wel[2] == 1 and (msg.from_user.id == user_id or stat != "administrator"):

                mute.mute(context, chat_id=chat_id, user_id=user_id)

                db.add_link(chat=chat, user=user,
                                  status="restricted", replace=1)

                # print(context.bot.getChat(chat_id))
                # print(msg.ChatMember.chatcan_send_messages)

                if str(user_status) == 'restricted':
                    text = 'veri 1 ' + text
                else:
                    text = 'veri 0 ' + text

                keyboard = [
                    [InlineKeyboardButton(
                        "Click Here", callback_data=text)]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)

                text = "<a href='tg://user?id=" + str(user_id) + "'>" + first_name + "</a>" +\
                    ", you have been muted... \n\nClick on the human verification button within the next 2min to unmute yourself !"   # else, you will be kicked !"
                
            else:
                db.add_link(chat=chat, user=user, status=user_status)

            update.message.reply_text(
                text, reply_markup=reply_markup, parse_mode="HTML")

    print("\n", time.process_time() - start, "\n")


def farewell(update, context):
    db = database.bot_db()

    msg = update.message

    chat = msg['chat']
    user = update.effective_message.left_chat_member

    db.add_user(user=user)

    user_status = context.bot.get_chat_member(chat['id'], user['id'])
    db.add_link(chat=chat, user=user,
                      status=user_status['status'])

    members = chat.get_members_count()
    db.add_settings(chat_id=chat['id'], members=members)

    text = "Bye bye 👋🏼"
    update.effective_message.reply_text(text)
