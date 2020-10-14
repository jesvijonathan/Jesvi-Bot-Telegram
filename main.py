# Jesvi Bot
# v0.5
# 14 Oct 2020
# By Jesvi Jonathan

import telegram
import time
import modules.cricscore as cric
import database as database
import modules.notes as notes
import modules.fun as fun
import modules.spam as spams
import modules.ban as ban
import modules.promote as promote
import modules.filter as filter
import modules.mute as mute
import modules.delete as delete
import modules.edit as edit
import modules.info as info
import modules.ai as ai
import modules.welcome as welcome
from config import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys
import os
import logging


path = path = str(os.path.dirname(sys.argv[0]))

# stdoutOrigin=sys.stdout
#sys.stdout = open(path+"\\textfile.txt", "w")

sys.stderr = open(path+"\\logs\\log_bot_runtime.log", 'w')


class writer(object):
    log = []

    def write(self, data):
        self.log.append(data)


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

print("-logging")

#import traceback

print("-loaded modules")
updater = Updater(bot_token, use_context=True)
dp = updater.dispatcher
print("-authenticating")


def send(Update, Context):
    k = delete.lock_delete(Update, Context)
    notes.note_check(Update, Context)
    welcome.udat(Update, Context, quick=k)
    # filter.filter_delete(Update,Context)
    # spams.spam_call(Update,Context)


def sqlof(update, context):
    res = update.message.text
    l = "OFF"
    if res == "/sqlon":
        l = "ON"
    else:
        l = "OFF"
    print("adas")
    database.log(turn=l)


def main():

    dp.bot.send_message(chat_id=owner_id, text="<code>Started Service !\n\nTime : " +
                        time.strftime("%Y-%m-%d (%H:%M:%S)") + "</code>", parse_mode="HTML")
    database.load()
    print("-database ready")
    # time.sleep(0.5)
    print("-active")
    print("\n--------------------------------------")

    logger = writer()
    sys.stdout = logger
    sys.stderr = logger

    info_cmd = ("info", "ginfo", "group", "groupinfo", "aboutgroup",
                "chatinfo", "infogroup", "infochat", "user", "userinfo")
    admin_cmd = ("ainfo", "adminlist", "admin", "listadmin",
                 "administrators", "members", "memb")
    message_id = ("id", "minfo", "msgid", "msg",
                  "messageid", "msginfo", "message")
    mute_cmd = ("mute", "shutup", "restrict")
    spam_cmd = ("spam", "filler", "echo", "annoy")
    promote_cmd = ("promote", "upgrade", "prom")
    demote_cmd = ("demote", "depromote", "depromo", "degrade")
    filter_cmd = ("filter", "filt", "word", "fil",
                  "resetfilter", "filterreset")
    pin_cmd = ("pin", "notify", "notice", "noti")
    set_cmd = ("set", "change", "setbio", "bio", "about")
    clean_cmd = ("clean", "purge", "tdel")
    delete_cmd = ("del", "delete", "rem", "remove")
    silent_delete_cmd = ("sdel", "silentdel", "sildel", "silentdelete")
    rip_cmd = ("rip", "kickme", "suicide")
    kick_cmd = ("kick")
    ban_cmd = ("ban", "gban")
    unban_cmd = ("unban", "forgive", "accept")
    about_cmd = ("about", "bot", "botinfo")
    owner_cmd = ("owner", "jesvi", "boss", "maintainer")
    boom_cmd = ("boom", "yay", "dang", "bang", "party")
    leave_cmd = ("leave", "scoot")
    note_cmd = ("note", "notes")
    warn_cmd = {"warnset", "warnclear", "warnreset", "forgive",
                "withdraw", "warninfo", "warnlist", "allwarns", "warnremove"}
    rules_cmd = {"rules", "setrules"}
    search_cmd = {"search", "google", "usearch"}
    translate_cmd = {"trans", "translate"}
    create_base = {"createbase"}
    sql_cmd = {"sqlon", "sqloff"}

    dp.add_handler(CommandHandler(create_base, database.create_base))
    dp.add_handler(CommandHandler(sql_cmd, sqlof))
    dp.add_handler(CommandHandler("ipltoday", fun.cricket))
    dp.add_handler(CommandHandler("iplupdate", fun.cricket))
    dp.add_handler(CommandHandler(search_cmd, ai.search))
    dp.add_handler(CommandHandler(translate_cmd, ai.translate))
    dp.add_handler(CommandHandler("warn", filter.warn_strike))
    dp.add_handler(CommandHandler(warn_cmd, filter.warn_set))
    dp.add_handler(CommandHandler(rules_cmd, edit.rules))
    dp.add_handler(CommandHandler("fbi", fun.fbi_joke))
    dp.add_handler(CommandHandler("start", welcome.start_func))
    dp.add_handler(CommandHandler("cdsync", welcome.dat))
    dp.add_handler(CommandHandler("net", database.net))
    dp.add_handler(CommandHandler(note_cmd, notes.notes))
    dp.add_handler(CommandHandler(boom_cmd, spams.boom))
    dp.add_handler(CommandHandler("owner", welcome.owner))
    dp.add_handler(CommandHandler(about_cmd, welcome.about))
    dp.add_handler(CommandHandler(rip_cmd, ban.rip))
    dp.add_handler(CommandHandler(kick_cmd, ban.kick))
    dp.add_handler(CommandHandler(ban_cmd, ban.ban))
    dp.add_handler(CommandHandler(unban_cmd, ban.unban))
    dp.add_handler(CommandHandler(leave_cmd, ban.leave))
    dp.add_handler(CommandHandler(pin_cmd, edit.pin))
    dp.add_handler(CommandHandler("unpin", edit.unpin))
    dp.add_handler(CommandHandler(set_cmd, edit.set_))
    dp.add_handler(CommandHandler(promote_cmd, promote.promote))
    dp.add_handler(CommandHandler(demote_cmd, promote.depromote))
    dp.add_handler(CommandHandler(spam_cmd, spams.spam_check))
    dp.add_handler(CommandHandler(mute_cmd, mute.mute))
    dp.add_handler(CommandHandler("unmute", mute.unmute))
    dp.add_handler(CommandHandler((info_cmd), info.info))
    dp.add_handler(CommandHandler(admin_cmd, info.admin_list))
    dp.add_handler(CommandHandler(message_id, info.msg_id))
    dp.add_handler(CommandHandler(filter_cmd, filter.message_filter))
    dp.add_handler(CommandHandler(clean_cmd, delete.clean))
    dp.add_handler(CommandHandler(delete_cmd, delete.delete))
    dp.add_handler(CommandHandler(silent_delete_cmd, delete.silent_delete))
    dp.add_handler(CommandHandler("lock", delete.lock))
    dp.add_handler(CommandHandler("unlock", delete.unlock))
    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome.greet))
    dp.add_handler(MessageHandler(
        Filters.status_update.left_chat_member, welcome.farewell))
    dp.add_handler(MessageHandler(Filters.all, send))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

##########################
