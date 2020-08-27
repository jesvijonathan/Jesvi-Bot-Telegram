# Jesvi Bot
# v0.01
# 11 Aug 2020
# By Jesvi Jonathan

import telegram 
import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import config
import modules.welcome as welcome
import modules.info as info
import modules.edit as edit
import modules.delete as delete
import modules.mute as mute
import modules.filter as filter
import modules.promote as promote
import modules.ban as ban
import modules.spam as spams
import modules.about as about
import modules.notes as notes


updater = Updater(config.bot_token, use_context=True)
dp = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def send(Update,Context):
    delete.lock_delete(Update,Context)
    filter.filter_delete(Update,Context)
    spams.spam_call(Update,Context)
    notes.note_check(Update,Context)


def main():


    info_cmd = ("info","ginfo","group","groupinfo","aboutgroup","chatinfo","infogroup","infochat","user","userinfo")
    admin_cmd = ("ainfo","adminlist","admin","listadmin","administrators","members","memb")
    message_id = ("id","minfo","msgid","msg","messageid", "msginfo","message")
    mute_cmd = ("mute", "shutup", "restrict")
    spam_cmd = ("spam", "filler", "echo", "annoy")
    promote_cmd = ("promote", "upgrade", "prom")
    demote_cmd = ("demote", "depromote", "depromo","degrade")
    filter_cmd = ("filter", "filt", "word", "fil")
    pin_cmd = ("pin", "notify", "notice", "noti")
    set_cmd = ("set","change")
    clean_cmd = ("clean", "purge", "tdel")
    delete_cmd = ("del", "delete","rem","remove")
    silent_delete_cmd = ("sdel","silentdel","sildel","silentdelete")
    rip_cmd = ("rip", "kickme", "suicide")
    kick_cmd = ("kick")
    ban_cmd = ("ban", "gban")
    unban_cmd = ("unban","forgive","accept")
    about_cmd = ("about","start", "bot", "botinfo")
    owner_cmd = ("owner","jesvi","boss","maintainer")
    boom_cmd = ("boom","yay","dang","bang","party")
    leave_cmd = ("leave","scoot")
    note_cmd = ("note","notes")
    
    dp.add_handler(CommandHandler(note_cmd, notes.notes))

    dp.add_handler(CommandHandler(boom_cmd, spams.boom))
    
    dp.add_handler(CommandHandler("owner", about.owner))
    dp.add_handler(CommandHandler(about_cmd, about.about))

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

    
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome.greet))
    dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, welcome.farewell))

    dp.add_handler(MessageHandler(Filters.all, send))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()