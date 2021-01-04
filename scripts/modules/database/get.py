
def user(mycursor, mydb, user):
    sql = ("""SELECT * FROM user_base WHERE user_id = %s""")

    data = (user['id'],)

    mycursor.execute(sql, data)
    myresult = mycursor.fetchone()

    return myresult
