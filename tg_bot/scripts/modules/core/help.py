
from config import *
def help(update, context):
    text = None
    if update.effective_chat.type != 'private':
        text = ("<a href='t.me/" + bot_username + "?start=help'>Click Here</a> for more info")
        update.message.reply_text(
            text=text, parse_mode="HTML", disable_web_page_preview=True)
    else:
        text = ("Commands (unsorted)-\n\n" +
                "/start - To start the bot\n" +
                "/help - View more about the bot\n" +
                
                "/info - View the telegram info about a group/user/tagged-user in a chat\n" +
                "/msgid - Provides the full link/content/id/details of the tagged-message\n" +
                
                "/del - Deleted the tagged-message\n" +
                "/sdel - Silent deletes a tagges-message without crumb\n" +

                "/scoot - Bot leaves the group\n" +
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
                "/rule - View the rules set in a group as a direct reply in the group\n" +
                "\n\n" +
                "/nickset <short_text> - To change the Admin title\n" +
                "/descset <short_text> - To change the group description\n" +
                "/titleset <short_text> - To change the Group title\n" +
                "/bioset <text> - To change the Admin role role/info\n" +
                "/ruleset <text> - To set the groups rules\n" +
                "/filter <word> <delete/reply/replydel/warn/warndel> <response-text> - it is used to filter words/texts sent from users and respond to it by deleteing/replying/warning them\n" +
                #"/spam <reply/echo/@_username> <text> - used to spam the chat... prolly disabled from sudos :(\n" +
                "/warn <reason_for_warn_text> - Warn strikes the tagged-user\n" +
                "/warninfo - View the warn record history/detail of the tagged-user\n" +
                "/warnremove - Clears the last warn strike of the tagged-user\n" +
                "warnclear - Resets the all warn records of the tagged-user\n" +
                "/warnlist - Lists all the warns striked in the group\n" +
                #"/warnset limit <number> - Set the number of warns a user can take before taking warn action on the user\n" +
                #"/warnset action <mute/ban/kick> - Set the warn action to kick/ban/mute the user when the warn limit is reached\n" +
                "/note - View notes in a group\n"
                "/noteadd <note_name> <text> - To set a note that can be accessible in a group to all members via #<note_name>\n" +
                "/noteremove <note_name> - To remove a note from notes\n" +
                "\n\n" +
                #"/cricscore - To view cricket info\n" +
                #"/iplupdate - View todays details of ongoing match\n" +
                #"/ipltoday - LIst the ipl events/chart/details"
                "/system - Display current server stat\n" +
                "/system log - get inchat log\n" +
                "/search <search_text> - To search from the internet... just like google but alot dumber\n" +
                #"/trans - Translates the tagged-message to english from any language\n" +
                "/sync - Syncs the bot with the group, useful if bot can't recognise memebers (not likely to happen :)\n" +
                #"/create_base - Creates database\n" +
                # "/sqlon or /sqloff - Swicth sql logging from bot script\n"+
                "/oof - A fun spam command\n" +
                "/boom - A fun spam command\n"
                "\n")
        update.message.reply_text(
            text=text)