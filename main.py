# Jesvi Bot
# v0.5
# 14 Oct 2020
# By Jesvi Jonathan

import telegram
import time
import datetime
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
import modules.cit as cit
import modules.welcome as welcome
from config import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys
import os
import logging


path = path = str(os.path.dirname(sys.argv[0]))

stdoutOrigin = sys.stdout
# sys.stdout = open(path+"\\textfile.txt", "w")

# sys.stderr = open(path+"\\logs\\log_bot_runtime.log", 'w')
sys.stderr = open(path+"/logs/log_bot_runtime.log", 'w')


class writer(object):
    log = []

    def write(self, data):
        self.log.append(data)


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

print("\n-logging")

# import traceback

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

    qinfo_cmd = ("info", "ginfo", "group", "groupinfo", "aboutgroup",
                 q            "chatinfo", "infogroup", "infochat", "user", "userinfo")
    qadmin_cmd = ("ainfo", "adminlist", "admin", "listadmin",
                  q             "administrators", "members", "memb")
    qmessage_id = ("id", "minfo", "msgid", "msg",
                   q              "messageid", "msginfo", "message")
    qmute_cmd = ("mute", "shutup", "restrict")
    qspam_cmd = ("spam", "filler", "echo", "annoy")
    qpromote_cmd = ("promote", "upgrade", "prom")
    qdemote_cmd = ("demote", "depromote", "depromo", "degrade")
    qfilter_cmd = ("filter", "filt", "word", "fil",
                   q              "resetfilter", "filterreset")
    qpin_cmd = ("pin", "notify", "notice", "noti")
    qset_cmd = ("set", "change", "setbio", "bio")
    qclean_cmd = ("clean", "purge", "tdel")
    qdelete_cmd = ("del", "delete", "rem", "remove")
    qsilent_delete_cmd = ("sdel", "silentdel", "sildel", "silentdelete")
    qrip_cmd = ("rip", "kickme", "suicide")
    qkick_cmd = ("kick")
    qban_cmd = ("ban", "gban")
    qunban_cmd = ("unban", "forgive", "accept")
    qabout_cmd = ("about", "bot", "botinfo")
    qowner_cmd = ("owner", "jesvi", "boss", "maintainer")
    qboom_cmd = ("boom", "yay", "dang", "bang", "party")
    qleave_cmd = ("leave", "scoot")
    qnote_cmd = ("note", "notes")
    qwarn_cmd = {"warnset", "warnclear", "warnreset", "forgive",
                 q            "withdraw", "warninfo", "warnlist", "allwarns", "warnremove"}
    qrules_cmd = {"rules", "setrules", "setrule", "rule"}
    qsearch_cmd = {"search", "google", "usearch"}
    qtranslate_cmd = {"trans", "translate"}
    qcreate_base = {"createbase"}
    qsql_cmd = {"sqlon", "sqloff"}


q
qdp.add_handler(CommandHandler(create_base, database.create_base))
qdp.add_handler(CommandHandler(sql_cmd, sqlof))
qdp.add_handler(CommandHandler("ipltoday", fun.cricket))
qdp.add_handler(CommandHandler("iplupdate", fun.cricket))
qdp.add_handler(CommandHandler(search_cmd, ai.search))
qdp.add_handler(CommandHandler(translate_cmd, ai.translate))
qdp.add_handler(CommandHandler("warn", filter.warn_strike))
qdp.add_handler(CommandHandler(warn_cmd, filter.warn_set))
qdp.add_handler(CommandHandler(rules_cmd, edit.rules))
qdp.add_handler(CommandHandler("fbi", fun.fbi_joke))
qdp.add_handler(CommandHandler("start", welcome.start_func))
qdp.add_handler(CommandHandler("cdsync", welcome.dat))
qdp.add_handler(CommandHandler("net", database.net))
qdp.add_handler(CommandHandler(note_cmd, notes.notes))
qdp.add_handler(CommandHandler(boom_cmd, spams.boom))
qdp.add_handler(CommandHandler("owner", welcome.owner))
qdp.add_handler(CommandHandler(about_cmd, welcome.about))
qdp.add_handler(CommandHandler(rip_cmd, ban.rip))
qdp.add_handler(CommandHandler(kick_cmd, ban.kick))
qdp.add_handler(CommandHandler(ban_cmd, ban.ban))
qdp.add_handler(CommandHandler(unban_cmd, ban.unban))
qdp.add_handler(CommandHandler(leave_cmd, ban.leave))
qdp.add_handler(CommandHandler(pin_cmd, edit.pin))
qdp.add_handler(CommandHandler("unpin", edit.unpin))
qdp.add_handler(CommandHandler(set_cmd, edit.set_))
qdp.add_handler(CommandHandler(promote_cmd, promote.promote))
qdp.add_handler(CommandHandler(demote_cmd, promote.depromote))
qdp.add_handler(CommandHandler(spam_cmd, spams.spam_check))
qdp.add_handler(CommandHandler(mute_cmd, mute.mute))
qdp.add_handler(CommandHandler("unmute", mute.unmute))
qdp.add_handler(CommandHandler((info_cmd), info.info))
qdp.add_handler(CommandHandler(admin_cmd, info.admin_list))
qdp.add_handler(CommandHandler(message_id, info.msg_id))
qdp.add_handler(CommandHandler(filter_cmd, filter.message_filter))
qdp.add_handler(CommandHandler(clean_cmd, delete.clean))
qdp.add_handler(CommandHandler(delete_cmd, delete.delete))
qdp.add_handler(CommandHandler(silent_delete_cmd, delete.silent_delete))
qdp.add_handler(CommandHandler("lock", delete.lock))
qdp.add_handler(CommandHandler("unlock", delete.unlock))
q
qdp.add_handler(CommandHandler("help", welcome._help))
q
qdp.add_handler(CommandHandler("cit", cit.cit))
q
qdp.add_handler(CommandHandler("oof", fun.oof))
q
qdp.add_handler(MessageHandler(
    q    Filters.status_update.new_chat_members, welcome.greet))
qdp.add_handler(MessageHandler(
    q    Filters.status_update.left_chat_member, welcome.farewell))
qdp.add_handler(MessageHandler(Filters.all, send))
qupdater.start_polling()
qupdater.idle()


if __name__ == '__main__':
    main()

##########################
