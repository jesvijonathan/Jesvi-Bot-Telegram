
def chat_base(mycursor, mydb):

    sql = (
        "CREATE TABLE IF NOT EXISTS chat_base ( id VARCHAR(14) PRIMARY KEY, type VARCHAR(14), title VARCHAR(48), username VARCHAR(48), date TIMESTAMP)"
    )  # chat_base : id | type | title | username

    mycursor.execute(sql)
    mydb.commit()


def user_base(mycursor, mydb):

    sql = (
        "CREATE TABLE IF NOT EXISTS user_base ( id VARCHAR(14) PRIMARY KEY, first_name VARCHAR(48), last_name VARCHAR(48), username VARCHAR(48), is_bot BOOLEAN, date TIMESTAMP)"
    )  # user_base : id | first_name | lastname | username | is_bot | date

    mycursor.execute(sql)
    mydb.commit()
