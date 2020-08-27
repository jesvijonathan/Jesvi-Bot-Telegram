
def info(update, context):

    msg = update.message.reply_to_message

    try:
        parts = update.message.text.split(None, 1)
    except:
        pass

    admin_li = ""

    try:
        user_id = msg.from_user.id
    except:
        msg = update.message
        chat_id = update.effective_chat.id
        group_name = update.effective_chat.title
        owner = ""
        name = ""
        chat = update.effective_chat

        administrators = update.effective_chat.get_administrators()
        count = None
        for admin in administrators:
            user = admin.user
            status = admin.status
            count = chat.get_members_count()
            try:
                title = admin.custom_title
            except:
                title = ""
            try:
               name = ("@" + user.username)
            except:
                try:
                    name = "@~" + user.first_name
                except:    
                    pass
            if status == "creator":
                owner = name
            elif status == "administrator":
                if title == None:
                    title = ""
                else:
                    title = "  (<i>" + str(title) +"</i>)"
                admin_li = admin_li +"\n"+ name + title
        try:
            invitelink = context.bot.exportChatInviteLink(chat_id)
        except:
            invitelink = "Unable to fetch the links ! "

        t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 =""

        username = update.effective_chat.username

        t1 = "\nChat id : <a href=''>" + str(chat_id) + "</a>"

        try:
            usr_link = "t.me/"+ username 
            t8 = "\nUsername : @" + username
            t7 = "\nGroup link : " + usr_link
        except:
            link_name = "<a href='"+ invitelink + "'>t.me/joinchat/</a>"
            t4 = "\nInvite link : " + invitelink

        try:
            usr_link_name = "<a href='t.me/"+ username + "'>" + group_name +"</a>"
            t2 = "\n\nTitle : " + usr_link_name
        except:
            t2 = "\n\nTitle : " + group_name

        t3 = "\nOwner : " + owner

        t5 = "\n\nMembers : "+ str(count)

        t6 = ""#"\nDescription : "

        text = "<b>Group Info -</b>\n" +t1+t2+t8+t3+t6+"\n\nAdministrators : "+admin_li +t5+"\n"+t7+t4

        context.bot.send_message(chat_id=chat_id, text=text, 
                  parse_mode="HTML")
        return

    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    user_name = msg.from_user.username
    user_link = msg.from_user.link
    chat_id = update.effective_chat.id
    user_status = context.bot.get_chat_member(chat_id, user_id)
    
#    contact = update.effective_message.contact
 #   phone = contact.phone_number

    no_warns = "~"

    t1 = t2 = t3 = t4 = t5 = t6 = t7 = ""

    t1 = "\nUser Id      : " + str(user_id)

    if first_name != "":
        try:
            t2 = "\n\nFirst Name   : " + first_name
        except:
            pass  
    if last_name != "":
        try:
            t3 = "\nLast Name   : " + last_name    
        except:
            pass
    try:
        t4 = "\nUsername    : @" + user_name
    except:
        pass

    t5 = "\nChat status  : " + user_status['status'] # chat warn no.
    t6 = "" 
    try:
        t7 = "\n\nUser link   : " + user_link   
    except:
        pass

    text = "User Info -\n" + t1 + t2 + t3 + t4 + t5 + t6 + t7  
    
    msg.reply_text(text)

#no_warns
#ban
#restrictions


def admin_list(update,context):
    administrators = update.effective_chat.get_administrators()
    msg = update.effective_message
    textt = ""
    try:
        text = "'{}' Member Info -\n".format(update.effective_chat.title or "This chat's")
        for admin in administrators:
            user = admin.user
            status = admin.status
            name = "[{}](tg://user?id={})".format(user.first_name + " " + (user.last_name or ""), user.id)
            if user.username:
                name = ("@" + user.username)
            if status == "creator":
                text += "\nGroup owner   : {}\n\nAdministrators : ".format(name)
        for admin in administrators:
            user = admin.user
            status = admin.status
            chat = update.effective_chat
            count = chat.get_members_count()
            name = "[{}](tg://user?id={})".format(user.first_name + " " + (user.last_name or ""), user.id)
            if user.username:
                name = ("@" + user.username)
            if status == "administrator":
                text += "\n{}".format(name)
                members = "\n\nTotal members : {} users".format(count)
    except:
        pass
    msg.reply_text(text + members)

def msg_id(update, context):
    msg = update.message.reply_to_message
    try:
        msg_id = msg.message_id
        msgid = "\n\nMessage id : " + str(msg_id)
    except:
        info(update,context)
        return

    try:
        user_id = msg.from_user.id
        userid = " (" + str(user_id) + ")"
    except:
        userid = ""
    try:
        first_name = msg.from_user.first_name
        if first_name == None:
            first_name = ""
    except:
        first_name = ""
        pass
    try:
        last_name = msg.from_user.last_name
        if last_name == None:
            last_name = ""
    except:
        last_name = ""
        pass
    
    try:
        user_name = msg.from_user.username
    except:
        user_name = ""
        pass

    name = "\nName : <a href='t.me/"+str(user_name)+"'>" + str(first_name) +" "+ str(last_name) + "</a>" + userid

    try:
        chat_id = update.effective_chat.id
    except:
        chat_id = ""
    try: 
        group_name = update.effective_chat.title
    except:
        group_name = ""
    try:
        grpusr = update.effective_chat.username
    except:
        pass

    try:
        date = "\nDate : " + str(msg.date)
    except:
        date = ""
    try:
        edt = msg.edit_date
        if edt != None:
            edit_date = "\nEdited : " + str(edt)
        else:
            edit_date = ""
    except:
        edit_date = ""
    try:
        link = "\nMessage link : <a href='" + msg.link + "'>Link</a>"
    except:
        link = ""
    try:
        chat_name = "\nChat : " + " <a href='t.me/" + grpusr + "'>" + group_name + "</a> ("+str(chat_id)+")"
    except:
        chat_name = ""

    try:
        textt = '\nText : "' + msg.text + '"'
    except:
        textt = "Type : #FILE" 

    text = ("<b>Message Info -</b>" +
            msgid +
            name + 
            chat_name + "\n" +
            textt+ "\n" +
            date + 
            edit_date+
            link)

    update.message.reply_text(text=text, 
                  parse_mode="HTML")
