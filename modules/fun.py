import random
import modules.cricscore as cric
import config as config

def fbi_joke(update,context):
    user_id = msg = ""
    
    try:
        msg = update.message.reply_to_message.from_user
        user_id = msg.from_user.id
    except:
        msg = update.effective_message.from_user
        user_id = msg.id

    chat_id = update.effective_chat.id
    user = msg.first_name

    #d = "User link test : " + telegram.utils.helpers.mention_html(user_id, str(user))
    d = ("Why is the FBI here ?!  \n\n\n\nHaha ! you fell for the notification :P ",
    "The FBI wants to know your location... \n\n\n\nLOLZzz, unfortunately bots can't laugh at our own jokes",
    "The FBI is watching you (0_0)\n\n\n\nYou Just Triggered A Prank Command, HA ! :}",
    "I'm too tired to tell a FBI Joke :(")
    i = random.choice(d)
    
    context.bot.send_message(chat_id=user_id, text=i, 
                  parse_mode="HTML")

def cricket(update,context):
    res = update.message.text.split(None, 0)
    text = f =""
    bot = config.bot_username
    try:
        if res[0] == "/ipltoday" or res[0] == "/ipltoday@"+bot:
            f ="ipl_tday_update"
        elif res[0] == "/iplupdate" or res[0] == "/iplupdate@"+bot:
            f ="ipl_match_update"
        else:
            return
    except:
        print("error")
        return

    text = cric.get_init(func=f)

    update.message.reply_text(text=text,parse_mode="HTML",disable_web_page_preview=True)