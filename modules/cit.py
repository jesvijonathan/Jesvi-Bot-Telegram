def cit(update, context):
    text = "Error"

    res = update.message.text.split(None, 2)
    #j = updater.job_queue
    if res[1] == "status":
        text = ("CIT Module -\n" +
                "Status - Debugging\n" +
                "Available Commands - 'null'\n" +
                "CITdb - Disconnected")

    update.message.reply_text(text)


def attend(update, context):
    pass
