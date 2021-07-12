
from modules.edit import rules
import modules.info as info
import re
import database as database
import config as config
import sys
sys.path.append('./')


def dat(update, context, sync=0):
    chat = update.effective_chat
    count = update.effective_chat.get_members_count()

    chat_id = str(chat['id'])
    bot_activity = context.bot.get_chat_member(chat_id, config.bot_id)

    chat_id = chat_id[1:]

    database.create_base()

    if sync == 0:
        msg = update.message.reply_text("Syncing..")
        database.add_chat_base(
            chat_id, chat['username'], chat['title'], bot_activity['status'], count, sync=sync)
        msg.edit_text("Current Chat Base Updated !")
    else:
        database.add_chat_base(
            chat_id, chat['username'], chat['title'], bot_activity['status'], count, sync=sync)


def ldat(update, context):
    user_id = update.message.from_user.id
    chat_id = str(update.effective_chat.id)

    user = context.bot.get_chat_member(chat_id, user_id)

    chat_id = chat_id[1:]
    database.add_link_base(chat_id=chat_id, user_id=str(
        user_id), status=user['status'])


def udat(update, context, sync=0, quick=0):
    user = update.message.from_user

    database.add_user_base(user_id=str(user['id']), firstname=user['first_name'],
                           username=user['username'], lastname=user['last_name'], is_bot=user['is_bot'])

    chat = update.effective_chat

    if chat['type'] != "private":
        # ldat(update,context)
        chat_id = str(chat['id'])
        chat_idd = chat_id[1:]

        user1 = context.bot.get_chat_member(chat_id, user['id'])

        database.add_link_base(chat_id=chat_idd, user_id=str(
            user['id']), status=user1['status'])

        """if quick == 0:
            dat(update,context,1)"""


def start_func(update, context):
    t = update.message.text
    res = t

    try:
        res = t.split(None, 1)

        if res[1] == "start":
            about(update, context)

        elif res[1] == "help":
            _help(update, context)

        else:
            rules(update, context)

        udat(update, context)
        return

    except:
        pass

    try:
        if t == "/start" or t == "/start"+"@"+config.bot_username:
            if update.effective_chat.type != 'private':
                update.message.reply_text(text="<a href='http://t.me/jesvi_bot?start=start'>" + "Click Here" +
                                          "</a>" + " to get started !", parse_mode="HTML", disable_web_page_preview=True)
            else:
                about(update, context)

    except:
        pass

    udat(update, context)


def greet(update, context):

    for new_member in update.message.new_chat_members:
        if str(new_member['id']) == str(config.bot_id):
            dat(update, context, 1)
            ldat(update, context)
            about(update, context)
        else:
            group = update.message["chat"]
            user = new_member
            welcome_text = "Welcome to " + \
                str(group['title']) + ", " + \
                str(new_member['first_name']) + " ! 🥳"
            database.add_user_base(user_id=str(user['id']), firstname=user['first_name'],
                                   username=user['username'], lastname=user['last_name'], is_bot=user['is_bot'])

    update.message.reply_text(text=welcome_text,
                              parse_mode="HTML")


def farewell(update, context):
    user = left_member = update.effective_message.left_chat_member
    database.add_user_base(user_id=str(user['id']), firstname=user['first_name'],
                           username=user['username'], lastname=user['last_name'], is_bot=['is_bot'])

    farewell_text = "Bye " + str(left_member['first_name']) + ", 👋🏼"
    update.effective_message.reply_text(farewell_text)


def owner(update, context):
    text = ("I am still being built by my owner @jesvijonathan & am being tested in @bot_garage for proper functionality &" +
            "\nFYI : you CAN NOT PM without a good reason or be ready to get banned\nHave a nice day ! ;)")
    update.message.reply_text(text)


def about(update, context):
    text = "This is Jesvi Bot & I am a telegram handler bot being developed to provide users with a better UX experience... \n\nAdd me in a group and you can get started to use my features.\n\n" +\
        "You can check out for my source/feature updates at @bot_garage_channel\n\nUse /help for more info about available commands & its uses.."
    update.message.reply_text(text)


def _help(update, context):
    text = None
    if update.effective_chat.type != 'private':
        text = ("<a href='t.me/jesvi_bot?start=help'>Click Here</a> for more info")
        update.message.reply_text(
            text=text, parse_mode="HTML", disable_web_page_preview=True)
    else:
        text = ("Commands (unsorted)-\n\n" +
                "/start - To start the bot\n" +
                "/help - View more about the bot\n" +
                "/info - View the telegram info about a group/user/tagged-user in a chat\n" +
                "/group - View group info in full detail\n" +
                "/adminlist - Provides the list of admin and their roles\n" +
                "/id - Provides the full link/content/id/details of the tagged-message\n" +
                "/del - Deleted the tagged-message\n" +
                "/sdel - Silent deletes a tagges-message without crumb\n" +
                "/leave - Bot leaves the group\n" +
                "/boom - A spam text to check if bot is alive\n" +
                "/fbi - A spam text for fun ;)\n" +
                "/pin - Pins the tagged-message to the group\n" +
                "/unpin - Unpins the pinned message in the group"
                "/promote - Promotes a the tagged-user to an administrator\n" +
                "/demote - Demotes an Admin\n" +
                "/lock - locks the group from texts/media/messages from members\n" +
                "/unlock - Unlock the group from lock state\n" +
                "/bio - View a Admins role in a chat\n" +
                "/ban - Bans the tagged-user from the group\n" +
                "/kick - Kicks the tagged-user from the group\n" +
                "/rip - To kick yourself from the group, share it with an annoying user ;)\n" +
                "/mute - Mute/restrict a user from sending messages in a group\n" +
                "/unmute - UNmute a member in a group\n" +
                "/purge - Deletes all the messages between/till the tagged-message.. useful to clean unwanted spams/chats in a group\n" +
                "/net - View the network statistics\n" +
                "/notes - View the notes available in a group\n" +
                "/rules - View the rules set in a group in PM \n" +
                "/rules - View the rules set in a group as a direct reply in the group\n" +
                "\n\n" +
                "/set title <short_text> - To change the Admin title\n" +
                "/set bio <text> - To change the Admin role role/info\n" +
                "/setrules <text> - To set the groups rules\n" +
                "/filter <del/reply/warn> <text_to_filter> - it is used to filter words/texts sent from users and respond to it by deleteing/replying/warning them\n" +
                "/spam <reply/echo/@_username> <text> - used to spam the chat... prolly disabled from sudos :(\n" +
                "/warn <reason_for_warn_text> - Warn strikes the tagged-user\n" +
                "/warninfo - View the warn record history/detail of the tagged-user\n" +
                "/warnclear - Clears the last warn strike of the tagged-user\n" +
                "warnreset - Resets the all warn records of the tagged-user\n" +
                "/warnlist - Lists all the warns striked in the group\n" +
                "/warnset limit <number> - Set the number of warns a user can take before taking warn action on the user\n" +
                "/warnset action <mute/ban/kick> - Set the warn action to kick/ban/mute the user when the warn limit is reached\n" +
                "/note set <note_name> <text> - To set a note that can be accessible in a group to all members via #<note_name>\n" +
                "/note remove <note_name> - To remove a note from notes\n" +
                "\n\n" +
                "/cricscore - To view cricket info\n" +
                "/iplupdate - View todays details of ongoing match\n" +
                "/ipltoday - LIst the ipl events/chart/details"
                "/search <search_text> - To search from the internet... just like google but alot dumber\n" +
                "/trans - Translates the tagged-message to english from any language\n" +
                "/cdsync - Syncs the bot with the group, useful if bot can't recognise memebers (not likely to happen :)\n" +
                # "/create_base - Creates database\n" +
                # "/sqlon or /sqloff - Swicth sql logging from bot script\n"+
                "/oof - A fun spam command\n" +
                "\n")
        update.message.reply_text(
            text=text)
