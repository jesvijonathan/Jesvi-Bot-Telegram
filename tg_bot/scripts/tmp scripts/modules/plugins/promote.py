

import modules.extract as extract


def promote(update, context):
    m = extract.sudocheck(update, context)
    if m == 2:
        return
    elif m == 1:
        n = extract.sudocheck(update, context, 0)
        if n == 0:
            update.message.reply_text(
                "'I can't give where I got my powers from' ~jesvi_bot")
            return
        elif n == 1:
            update.message.reply_text("Already a fellow admin !")
            return

    msg = update.message.reply_to_message

    chat_id = update.effective_chat.id
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name

    context.bot.promoteChatMember(int(chat_id), int(user_id),
                                  can_change_info=True,
                                  can_delete_messages=True,
                                  can_invite_users=True,
                                  can_restrict_members=True,
                                  can_pin_messages=True,
                                  can_promote_members=False)

    update.message.reply_text("Promoted " + str(first_name) + " !")


def depromote(update, context):
    m = extract.sudocheck(update, context)
    if m == 2:
        return
    elif m == 1:
        n = extract.sudocheck(update, context, 0)
        if n == 0:
            update.message.reply_text("Joke ugh ?")
            return

    msg = update.message.reply_to_message

    chat_id = update.effective_chat.id
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name

    context.bot.promoteChatMember(int(chat_id), int(user_id),
                                  can_change_info=False,
                                  can_delete_messages=False,
                                  can_invite_users=False,
                                  can_restrict_members=False,
                                  can_pin_messages=False,
                                  can_promote_members=False)

    update.message.reply_text("Depromoted " + str(first_name) + " !")
