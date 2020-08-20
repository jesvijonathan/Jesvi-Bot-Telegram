
def greet(update, context):
    for new_member in update.message.new_chat_members:
            group = update.message["chat"]
            welcome_text = "Welcome to " + str(group['title']) + ", "+ str(new_member['first_name']) + " ! 🥳"
    update.message.reply_text(welcome_text)


def farewell(update, context):
    left_member = update.effective_message.left_chat_member
    farewell_text = "Bye " + str(left_member['first_name']) + ", 👋🏼"
    update.effective_message.reply_text(farewell_text)