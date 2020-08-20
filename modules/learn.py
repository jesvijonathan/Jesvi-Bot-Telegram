
#To send reply text
text="Reply Text"
update.message.reply_text(text)

#To Send Reply Text With The Tagges msg but replied user's name
msg = update.message.reply_to_message
msg.reply_text("ok so he told this to you ?")


#update previous text
msg = update.message.reply_text("original")
time.sleep(5)
msg.edit_text("updated")


#to delete replied txt
msg = update.message.reply_text("Delete Text")
time.sleep(2)

context.bot.delete_message(chat_id=msg.chat_id,
message_id=msg.message_id)


#to get tagged user id & the note along in the msg
def reply(update, context):
    prev_message = update.message.reply_to_message
    user_id = prev_message.from_user.id
    res = update.message.text.split(None, 1) #to get 2nd portion of text
    print(user_id, " : ", res[1] )


#priv msg from chat, test
context.bot.send_message(chat_id, text='Howdy')