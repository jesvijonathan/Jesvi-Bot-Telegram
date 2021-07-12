

import telegram


def unmute(context, chat_id, user_id):

    #current = eval(str(context.bot.getChat(chat_id).permissions))
    new = {'can_send_messages': True,
           'can_send_media_messages': True,
           'can_send_polls': True,
           'can_send_other_messages': True,
           'can_add_web_page_previews': True,
           'can_invite_users': True,
           'can_change_info': True,
           'can_pin_messages': True}

    permissions = {'can_send_messages': None,
                   'can_send_media_messages': None,
                   'can_send_polls': None,
                   'can_send_other_messages': None,
                   'can_add_web_page_previews': None,
                   'can_invite_users': None,
                   'can_change_info': None,
                   'can_pin_messages': None}

    # permissions.update(current)
    permissions.update(new)
    new_permissions = telegram.ChatPermissions(**permissions)

    context.bot.restrict_chat_member(
        chat_id, user_id, permissions=new_permissions)


def mute(context, chat_id, user_id):

    #current = eval(str(context.bot.getChat(chat_id).permissions))

    new = {'can_send_messages': False,
           'can_send_media_messages': False,
           'can_send_polls': False,
           'can_send_other_messages': False,
           'can_add_web_page_previews': False,
           'can_invite_users': False,
           'can_change_info': False,
           'can_pin_messages': False}

    permissions = {'can_send_messages': None,
                   'can_send_media_messages': None,
                   'can_send_polls': None,
                   'can_send_other_messages': None,
                   'can_add_web_page_previews': None,
                   'can_invite_users': None,
                   'can_change_info': None,
                   'can_pin_messages': None}

    # permissions.update(current)
    permissions.update(new)
    new_permissions = telegram.ChatPermissions(**permissions)

    context.bot.restrict_chat_member(
        chat_id, user_id, permissions=new_permissions)
