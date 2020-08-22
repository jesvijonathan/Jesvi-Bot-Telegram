

import telegram 

import modules.extract as extract


def unmute(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return

    msg = update.message.reply_to_message

    user_id = msg.from_user.id 
    chat_id = update.effective_chat.id
    user_name = msg.from_user.username
    first_name = msg.from_user.first_name
    
    current = eval(str(context.bot.getChat(chat_id).permissions))
    new = {'can_send_messages': True, 
           'can_send_media_messages': True,
           'can_send_polls': True,
           'can_send_other_messages': True, 
           'can_add_web_page_previews': True,}

    permissions = {'can_send_messages': None,
                   'can_send_media_messages': None, 
                   'can_send_polls': None, 
                   'can_send_other_messages': None, 
                   'can_add_web_page_previews': None,
                   'can_change_info': None, 
                   'can_invite_users': None, 
                   'can_pin_messages': None}
    
    permissions.update(current)
    permissions.update(new)
    new_permissions = telegram.ChatPermissions(**permissions)
    
    context.bot.restrict_chat_member(chat_id, user_id,permissions=new_permissions)
    update.message.reply_text("Unmuted "+ str(first_name) + " !")


def mute(update, context):
    m = extract.sudocheck(update,context)
    if m == 2:
        return
    elif m == 1:
           n = extract.sudocheck(update,context,0)
           if n == 0:
              update.message.reply_text("I'm afraid I can't stop a group owner from speaking...")
              return
           elif n == 1:
              update.message.reply_text("Dang ! I can't hold back a admin from speaking !")
              return
              

    msg = update.message.reply_to_message
    res = update.message.text.split(None, 1)
    
    user_id = msg.from_user.id 
    chat_id = update.effective_chat.id
    user_name = msg.from_user.username
    first_name = msg.from_user.first_name
    
    current = eval(str(context.bot.getChat(chat_id).permissions))
    new = {'can_send_messages': False, 
           'can_send_media_messages': False,
           'can_send_polls': False,
           'can_send_other_messages': False, 
           'can_add_web_page_previews': False,}

    permissions = {'can_send_messages': None, 
                   'can_send_media_messages': None, 
                   'can_send_polls': None, 
                   'can_send_other_messages': None, 
                   'can_add_web_page_previews': None, 
                   'can_change_info': None, 
                   'can_invite_users': None, 
                   'can_pin_messages': None}
    
    permissions.update(current)
    permissions.update(new)
    new_permissions = telegram.ChatPermissions(**permissions)
    
    context.bot.restrict_chat_member(chat_id, user_id,permissions=new_permissions)
    update.message.reply_text("Muted "+ str(first_name) + " !")