
def user(mycursor, mydb, user):
    sql = ("REPLACE INTO user_base (id, username, first_name, last_name, is_bot, date) VALUE(%s, %s, %s, %s, %s, CURRENT_TIMESTAMP())")

    data = (user['id'], user['first_name'],
            user['last_name'], user['username'],  user['is_bot'])  # gban #active #is_bot

    # print(data)

    mycursor.execute(sql, data)
    mydb.commit()


def chat(mycursor, mydb, chat):
    sql = ("REPLACE INTO chat_base (id, type, title, username, date) VALUE(%s, %s, %s, %s, CURRENT_TIMESTAMP())")

    data = (chat['id'], chat['type'],
            chat['title'], chat['username'])

    # print(data)

    mycursor.execute(sql, data)
    mydb.commit()
