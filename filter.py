
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import time

updater = Updater("1262215479:AAEDrQUR-wY1XIvzHiL6_6Vu_PHyW8g4UHI", use_context=True)
dp = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def silent_delete(update, context):
    msg = update.message.reply_to_message
    msg_frm = update.message
    
    msg_id = msg.message_id
    chat_id = update.effective_chat.id

    msg_frm.delete()    
    context.bot.deleteMessage(chat_id, msg_id)


lock = 0
msg_filter = 0
filter_text = {}


def filter_delete(update, context):
    global msg_filter
    global filter_text

    if msg_filter == 1:
        msg = update.message
        x = msg.text.split()
      
        for i in x :
            if i in filter_text:
                if filter_text.get(i) == "<filter-warn>":
                    user_name = msg.from_user.username
                    text = "Warn striked @"+ user_name +" for the use of <b>" + str(i) + "</b> !\n" + "& (<b>~</b>" + " of " + "3)" + " strikes remaining, so be carefull !\n\n" + "(<b>3</b> of 3) warns results in <b>kick</b> or <b>ban</b> from the group !"
                    msg.reply_text(text=text, 
                  parse_mode="HTML")
                    return
                elif filter_text.get(i) == "<filter-delete>":
                    msg_id = msg.message_id
                    chat_id = update.effective_chat.id
                    context.bot.deleteMessage(chat_id, msg_id)
                else:
                    msg.reply_text(filter_text[i])


def message_filter(update, context):
    global msg_filter
    global filter_text
    
    prev_message = update.message.reply_to_message
    res = update.message.text.split(None, 3)

    text = ""

    try:
        text_1 = res[1]
    except:
        if msg_filter == 1: 
            bo = "on"
        else:
            bo = "off"
        text = ("Currently filter is " + str(bo) + " !")
        update.message.reply_text(text)
        return

    try:
        text_2 = res[2]
    except:
        text_2 = ""

    try:
        text_3 = res[3]
    except:
        text_3 = ""
        
    if text_1 == 'remove':
        if text_2 != "":
            del filter_text[text_2]
            text = 'Removed "' + str(text_2) + '" from filter !'
    
    elif text_1 == 'list':
        text = "Here is a list of filters stored :\n" + str(filter_text)

    elif text_1 == 'reply':
        filter_text[text_2] = text_3
        text = '"' + str(text_2) + '" will be replied with "' + str(text_3) + '" !'

    elif text_1 == 'warn':
        if text_2 == "":
            text= "No filter-warn word passed !"
        else: 
            filter_text[text_2] = "<filter-warn>"
            text = 'Use of "' + str(text_2) + '" will warn-strike the user !'

    elif text_1 == 'off':
        msg_filter = 0
        text = 'Filter turned off !'        
    
    elif text_1 == 'on':
        msg_filter = 1
        text = 'Filter turned on !'

    elif text_1 == 'clear':
        filter_text.clear()
        text = "Cleared filter data"
    
    else:
        filter_text[text_1] = "<filter-delete>"
        text = 'Added "' + str(text_1) + '" to filter !'

    update.message.reply_text(text)


def main():
    
    dp.add_handler(CommandHandler("filter", message_filter))

    dp.add_handler(MessageHandler(Filters.text, filter_delete))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()