
import modules.extract as extract
import time

def ban(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return

    msg = update.message.reply_to_message

    user_id = msg.from_user.id 
    first_name = msg.from_user.first_name

    ban = update.effective_chat.kick_member(user_id)

    update.message.reply_text("Banned " + str(first_name) + " !")


def unban(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return

    msg = update.message.reply_to_message

    user_id = msg.from_user.id 
    first_name = msg.from_user.first_name
    user_name = msg.from_user.username
    chat = update.effective_chat

    chat.unban_member(user_id)

    update.message.reply_text("Unbanned " + str(first_name) + " !")


def kick(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return
    elif m == 1:
           n = extract.sudocheck(update,context,0)
           if m == 0:
              update.message.reply_text("Try /rip instead...")
              return
           #elif m == 1:
            #  update.message.reply_text("Get an admin to do it !")
             # return

    msg = update.message.reply_to_message

    user_id = msg.from_user.id 
    first_name = msg.from_user.first_name

    kick = update.effective_chat.unban_member(user_id)
    
    msg.reply_text( "Kicked " + str(first_name) + " !")


def leave(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return
    if m == 1:
        update.message.reply_text("Will leave only if the group owner says to do so...")

    msg = update.message.reply_text("Okay, I'm leaving ...")
    time.sleep(5)
    msg.edit_text("Bye !")
    time.sleep(1)
    user_id = msg.from_user.id
    kick = update.effective_chat.unban_member(user_id)


def rip(update, context):
    user_id = update.effective_message.from_user.id
    first_name = update.effective_message.from_user.first_name

    txt = update.message.reply_text("Okay, You asked for it.. !")
    
    time.sleep(3)

    kick = update.effective_chat.unban_member(user_id)
    
    txt.edit_text( str(first_name) + " got voluntarily kicked !")