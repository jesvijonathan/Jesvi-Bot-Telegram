
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater("1262215479:AAEDrQUR-wY1XIvzHiL6_6Vu_PHyW8g4UHI", use_context=True)
dp = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


spam = 0
spam_text = ""
spam_type = "echo"
spam_overflow_text = ""
spam_user = {}


def spam_check(update, context):
    global spam
    global spam_text
    global spam_type
    global spam_user

    msg = update.message.reply_to_message
    
    try:
        res = update.message.text.split(None, 3)
    except:
        pass

    try:
        text_1 = res[1]
    except:
        text_1 = ""
        pass
    
    try:
        text_2 = res[2]
    except:
        text_2 = ""
        pass


    try:
        user_name = msg.from_user.username
        res = update.message.text.split(None, 1)
        
        if text_1 == "":
            update.message.reply_text("No Spam Text Provided !")
            return
        
        if text_1 == "stop":
            del spam_user[shrt]
            update.message.reply_text("Halted spamming " + user_name + " !")
            return

        spam_user[user_name] = text_1
        text = "Spam stormming " + user_name + " with '" + str(spam_user[user_name]) + "' !"
        update.message.reply_text(text)
        return

    except:
        pass
    

        
    if text_1.startswith("@") == True:
        
        if text_2 == "":
            update.message.reply_text("No Spam Text Provided !")
            return

        shrt = text_1[1:] 
        
        if text_2 == "stop":
            del spam_user[shrt]
            update.message.reply_text("Halted spamming " + text_1 + " !")
            return

        spam_user[shrt] = text_2

        text = "Spam stormming " + text_1 + " with '" + str(spam_user[shrt]) + "' !"
        update.message.reply_text(text)
        return

########################################################

    text = ""
    temp = ''

    
    if text_1 == "":
        b = "off"
        temp = spam_text
        
        if spam == 1:
            b = "on"
        if spam_text == "":
            temp = "Not Set !"
        
        text = "Spam currently : " + b + "\nSpam mode : " + spam_type + "\nSpam text : " + temp
        update.message.reply_text(text)
        return


    if text_1 == "on":
        spam = 1
        temp = " !"
        if spam_text == "":
            temp = ', spam text not asigned !'
        text = "Spam mode turned on" + temp

    elif text_1 == "off":
        spam = 0
        text = "Spam mode turned off !"

    elif text_1 == "overflow":
        spam_type = "overflow"
    
    elif text_1 == "echo":
        spam_type = "echo"
        text = "Spam switched to 'echo' mode !"

    elif text_1 == "echo_overflow":
        spam_type = "echo_overflow"

    elif text_1 == "reply":
        spam_type = "reply"
        if spam_text != "":
            temp = '& "' + spam_text +'" set as spam text !'
        else:
            temp = '& spam text not asigned !'
        text = "Spam switched to 'reply' mode " + temp

    elif text_1 == "reply_overflow":
        spam_text = "reply_overflow"
        if text_2 != "":
            spam_text = text_2

    else:
        spam_text = text_1
        text = "'" + spam_text + "' set as spam text !"

    update.message.reply_text(text)

def spam(update,context):
    global spam_text
    global spam_type
    global spam

    msg = update.message
    
    try:
        user_name = msg.from_user.username
        
        for user in spam_user:
            if user_name == user:
                msg.reply_text(spam_user[user_name])
                return
    except:
        pass

    if spam == 1:

        if spam_type == "echo":
            msg.reply_text(msg.text)
        elif spam_type == "reply":
            msg.reply_text(spam_text)


def main():
    
    dp.add_handler(CommandHandler("spam", spam_check))
    dp.add_handler(MessageHandler(Filters.text, spam))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()