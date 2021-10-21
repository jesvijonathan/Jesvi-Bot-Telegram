
import modules.core.extract as extract
import random

def oof(update, context):
    m = extract.sudo_check_2(msg=update.message,del_lvl=0,context=context)
    if m==0:
        return

    oof = "oof"

    msg = update.message.reply_text(text=oof)

    #if m == 2:
    #    return

    for i in range(0, 3):
        oof = "o" + oof
        msg.edit_text(text=oof)

def fbi_joke(update, context):
    user_id = msg = ""

    try:
        msg = update.message.reply_to_message.from_user
        user_id = msg.from_user.id
    except:
        msg = update.effective_message.from_user
        user_id = msg.id

    #d = "User link test : " + telegram.utils.helpers.mention_html(user_id, str(user))
    d = ("Why is the FBI here ?!  \n\n\n\nHaha ! you fell for the notification :P ",
         "The FBI wants to know your location... \n\n\n\nLOLZzz, unfortunately bots can't laugh at our own jokes",
         "The FBI is watching you (0_0)\n\n\n\nYou Just Triggered A Prank Command, HA ! :}",
         "I'm too tired to tell a FBI Joke :(")
    i = random.choice(d)

    try:
        context.bot.send_message(chat_id=user_id, text=i,
                             parse_mode="HTML")
    except:
        update.message.reply_text("I can't !")
        
def boom(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id, "Boom !\nWe have something to celebrate ! 🥳")