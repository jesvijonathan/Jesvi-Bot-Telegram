

import modules.extract as extract
from database import push_link, get_link, push_chat, get_chat
from config import *


def pin(update, context):
    m = extract.sudocheck(update, context)
    if m == 2:
        return

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
    m = extract.sudocheck(update, context)
    if m == 2:
        return

    chat_id = update.effective_chat.id

    try:
        context.bot.unpinChatMessage(chat_id)
    except:
        pass


def set_(update, context):
    res = update.message.text.split(None, 2)
    if res[0] == "/bio":
        pass
    else:
        m = extract.sudocheck(update, context)
        if m == 2:
            return
        elif m == 1:
            n = extract.sudocheck(update, context, 0)
            if n == 0:
                update.message.reply_text("He got his own title boii !")
                return

    chat_id = chat_idd = ""
    try:
        chat_id = str(update.effective_chat.id)
        chat_idd = chat_id[1:]
        #user_id = update.effective_chat.username
        msg = update.message.reply_to_message
        user_id = msg.from_user.id
    except:
        return

    if res[0] == "/bio" or res[0] == "/about":
        k = get_link(chat_id=chat_idd, user_id=user_id, bio=1)
        name = msg.from_user.first_name
        d = ""

        try:
            txt = ("<b>Bio</b> - " + "<a href='tg://user?id=" + str(user_id) + "'>" + str(name) + "</a>" +
                   "\n\n<i>" + str(k[0][1]) + "</i>")

        except:
            txt = "<b>No Bio set</b> for " + "<a href='tg://user?id=" + \
                str(user_id) + "'>" + str(name) + "</a> !"

        update.message.reply_text(text=txt, parse_mode="HTML")
        return

    elif res[0] == "/setbio":
        cus_bio(update, context)
        return

    prev_message = update.message.reply_to_message

    if res[1] == "chatname" or res[1] == "name" or res[1] == "groupname" or res[1] == "grouptitle" or res[1] == "chattitle" or res[1] == "gname":
        try:
            context.bot.set_chat_title(chat_id=chat_id, title=res[2])
            text = "Chat name changed to '" + res[2] + "' !"
            update.message.reply_text(text)
        except:
            pass
    elif res[1] == "commands":

        context.bot.send_message(chat_id, text='Added Command !')
    elif res[1] == "des" or res[1] == "desc" or res[1] == "description":
        try:
            t = prev_message.tepxt
            context.bot.set_chat_description(chat_id, prev_message.text)
            context.bot.send_message(
                chat_id, text='Chat descirption updated !')
        except:
            if res[2] != None or res[2] != "":
                context.bot.set_chat_description(chat_id, res[2])
                context.bot.send_message(
                    chat_id, text='Chat descirption updated !')
            else:
                return

    elif res[1] == "nick" or res[1] == "title" or res[1] == "uname" or res[1] == "nickname" or res[1] == "admintitle" or res[1] == "status":
        try:
            msg = update.message.reply_to_message

            chat_id = update.effective_chat.id
            user_id = msg.from_user.id

            update.effective_chat.set_administrator_custom_title(
                user_id=user_id, custom_title=res[2])
            user_name = msg.from_user.username
            text = '"' + res[2]+'" set as the custom title for @' + user_name
            update.message.reply_text(text)
        except:
            pass


def cus_bio(update, context):
    m = extract.sudocheck(update, context)
    if m == 2:
        return

    msg = update.message.reply_to_message

    chat_id = str(update.effective_chat.id)
    chat_id = chat_id[1:]
    user_id = msg.from_user.id

    res = update.message.text.split(None, 1)
    r = ""

    try:
        r = res[1]
        if res == None:
            return
    except:
        return

    # udat(update,context)
    k = push_link(chat_id=chat_id, user_id=user_id, bio=r)

    if k == 1:
        name = msg.from_user.first_name
        txt = ("Set " + "(<a href='tg://user?id=" + str(user_id) + "'>" + str(name) + "</a>) group <b>bio</b> as -\n\n<i>" +
               r + "</i>")
        update.message.reply_text(text=txt, parse_mode="HTML")


def rules(update, context):
    res = update.message.text.split(None, 1)
    r = ""

    chat_id = str(update.effective_chat.id)
    chat_idd = chat_id[1:]

    if res[0] == "/start":
        chat_idd = res[1]
        chat_idd = chat_idd[1:]
        k = ""
        k = get_chat(chat_id=chat_idd, rules=r)

        try:
            k = k[0][0]
        except:
            k = "Error"

        update.message.reply_text(
            text=k, parse_mode="HTML", disable_web_page_preview=True)
        return

    if res[0] == "/rules" or res[0] == ("/rules@"+bot_username):
        k = get_chat(chat_id=chat_idd, rules=r)

        try:
            k = k[0][0]
        except:
            k = "Error"

        #k = "<a href='t.me/jesvi_bot?start=" + chat_id + "'>Click Here</a>" + " to view the group's rules"

        k = get_chat(chat_id=chat_idd, rules=r)
        try:
            k = k[0][0]
        except:
            k = "No rules set in this group !"

        update.message.reply_text(
            text=k, parse_mode="HTML", disable_web_page_preview=True)
        return

    else:
        m = extract.sudocheck(update, context)
        if m == 2:
            return

    try:
        r = res[1]
        if res == None:
            return
    except:
        return

    k = push_chat(chat_id=chat_idd, rules=r)

    if k == 1:
        txt = ("Set group rules as - \n\n" +
               "<i>" + r + "</i>")
        update.message.reply_text(text=txt, parse_mode="HTML")
