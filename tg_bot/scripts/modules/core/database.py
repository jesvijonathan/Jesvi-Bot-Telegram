cursor = db = None
user = chat = None


class database_create:

    # Variable Initialisation

    def __init__(self, cursorr, dbr):
        global cursor
        global db

        cursor = cursorr
        db = dbr

    # Table Creation

    def chat_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS chat_base ( chat_id VARCHAR(14) PRIMARY KEY, type VARCHAR(14), title VARCHAR(48), username VARCHAR(48), join_date TIMESTAMP)"
        )  # chat_base : chat_id | type | title | username | join_date

        cursor.execute(sql)
        db.commit()

    def user_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS user_base ( user_id VARCHAR(14) PRIMARY KEY, first_name VARCHAR(48), last_name VARCHAR(48), username VARCHAR(48), is_bot BOOLEAN, date TIMESTAMP)"
        )  # user_base : user_id | first_name | lastname | username | is_bot | date

        cursor.execute(sql)
        db.commit()

    def settings_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS settings_base ( chat_id VARCHAR(14) PRIMARY KEY, members TINYINT, warn_limit TINYINT DEFAULT 3, strike_action TINYINT DEFAULT 0, disabled_commands TINYINT DEFAULT 0, filter TINYINT DEFAULT 0, recent_pin TINYINT DEFAULT 5)"
        )  # settings_base : chat_id | members | warn_limit | strike_action | disabled_commands | filter | recent_pin

        cursor.execute(sql)
        db.commit()

    def notes_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS notes_base ( id VARCHAR(14) PRIMARY KEY, chat_id VARCHAR(14), note_name VARCHAR(32), note_text TEXT, set_by VARCHAR(32), date TIMESTAMP)"
        )  # notes_base : id | chat_id | note_name | note_text | set_by | date

        cursor.execute(sql)
        db.commit()

    def warn_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS warn_base ( id VARCHAR(14) PRIMARY KEY, chat_id VARCHAR(14), note_name VARCHAR(32), note_text TEXT, set_by VARCHAR(32), date TIMESTAMP)"
        )  # warn_base : id | chat_id | user_id | by_user_id | message_id | reason | date

        cursor.execute(sql)
        db.commit()

    def link_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS link_base ( id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, chat_id VARCHAR(14), user_id VARCHAR(14), status VARCHAR(14) DEFAULT 'member', bio TEXT, join_date TIMESTAMP, last_active TIMESTAMP)"
        )  # link_base : id | chat_id | user_id | status | bio | join_date | last_active

        cursor.execute(sql)
        db.commit()

    def filter_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS filter_base ( id VARCHAR(14) PRIMARY KEY, chat_id VARCHAR(14), user_id VARCHAR(14), word VARCHAR(32), reply_text TEXT, action VARCHAR(14))"
        )  # filter_base : id | chat_id | user_id | word | reply_text | action

        cursor.execute(sql)
        db.commit()

    def disabled_commands_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS disabled_commands_base ( id VARCHAR(14) PRIMARY KEY, chat_id VARCHAR(14), user_id VARCHAR(14), command VARCHAR(32), set_by VARCHAR(14))"
        )  # disabled_commands_base : id | chat_id | user_id | command | set_by

        cursor.execute(sql)
        db.commit()

    def recent_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS recent_base ( id VARCHAR(14) PRIMARY KEY, chat_id VARCHAR(14), pin_text TEXT, message_id VARCHAR(14), pin_by VARCHAR(32), date TIMESTAMP)"
        )  # recent_base : id | chat_id | pin_text | message_id | pin_by | date

        cursor.execute(sql)
        db.commit()

    def rules_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS rules_base ( chat_id VARCHAR(14) PRIMARY KEY, rule_text TEXT, rule_type VARCHAR(14), message_id VARCHAR(14), set_by VARCHAR(32), date TIMESTAMP)"
        )  # rules_base : chat_id | rule_text | rule_type | message_id | set_by | date

        cursor.execute(sql)
        db.commit()

    def welcome_base(self):

        sql = (
            "CREATE TABLE IF NOT EXISTS welcome_base ( chat_id VARCHAR(14) PRIMARY KEY, welcome_text TEXT, verification BOOLEAN DEFAULT 0, fail_action TINYINT DEFAULT 1)"
        )  # welcome_base : chat_id | welcome_text | verification | fail_action

        cursor.execute(sql)
        db.commit()

    def create_base(self):
        self.chat_base()
        self.user_base()
        self.link_base()
        self.settings_base()
        self.welcome_base()


def add_user(user):
    username = user['username']
    first_name = user['first_name']
    last_name = user['last_name']

    sql = (
        "INSERT INTO user_base (user_id, username, first_name, last_name, is_bot, date) VALUE(%s, %s, %s, %s, %s, CURRENT_TIMESTAMP()) ON DUPLICATE KEY UPDATE username=%s, first_name=%s, last_name=%s")
    data = (
        user['id'],
        username, first_name, last_name,
        user['is_bot'],

        username, first_name, last_name,
    )
    # print(data)

    cursor.execute(sql, data)
    db.commit()


def get_user(user_id):
    sql = (
        "SELECT * FROM user_base WHERE user_id=%s"
    )

    data = (
        user_id,
    )

    cursor.execute(sql, data)

    return cursor.fetchone()



def add_chat(chat):
    title = chat['title']
    username = chat['username']

    sql = (
        "INSERT INTO chat_base (chat_id, type, title, username, join_date) VALUE(%s, %s, %s, %s, CURRENT_TIMESTAMP()) ON DUPLICATE KEY UPDATE title=%s, username=%s")
    data = (
        chat['id'], chat['type'],
        title, username,

        title, username
    )
    # print(data)

    cursor.execute(sql, data)
    db.commit()


def get_chat(chat_id):
    sql = (
        "SELECT * FROM chat_base WHERE chat_id=%s"
    )

    data = (
        chat_id,
    )

    cursor.execute(sql, data)

    return cursor.fetchone()



def add_link(chat, user, status="member", replace=0):
    chat_id = chat['id']
    user_id = user['id']

    sql = (
        "SELECT (1) FROM link_base WHERE chat_id=%s AND user_id=%s LIMIT 1"
    )
    data = (
        chat_id,

        user_id
    )
    # print(data)

    cursor.execute(sql, data)

    if cursor.fetchone():
        if replace == 1:
            sql1 = (
                "UPDATE link_base SET status=%s, last_active=CURRENT_TIMESTAMP() WHERE chat_id=%s AND user_id= %s LIMIT 1"
            )
            data1 = (
                status, chat_id, user_id
            )
        else:
            sql1 = (
                "UPDATE link_base SET last_active=CURRENT_TIMESTAMP() WHERE chat_id=%s AND user_id= %s LIMIT 1"
            )
            data1 = (
                chat_id, user_id
            )
    else:
        sql1 = (
            "INSERT INTO link_base (chat_id, user_id, status, join_date, last_active) VALUE(%s, %s, %s, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP())"
        )
        data1 = (
            chat_id, user_id, status
        )

    cursor.execute(sql1, data1)
    db.commit()


def get_link(chat_id, user_id):
    sql = (
        "SELECT * FROM link_base WHERE chat_id=%s AND user_id=%s"
    )

    data = (
        chat_id, user_id,
    )

    cursor.execute(sql, data)

    return cursor.fetchone()


def add_settings(chat_id, members):

    sql = (
        "INSERT INTO settings_base (chat_id, members) VALUE(%s, %s) ON DUPLICATE KEY UPDATE members=%s"
    )
    data = (
        chat_id, members,
        members
    )

    # print(data)

    cursor.execute(sql, data)
    db.commit()


def get_settings(chat_id):
    sql = (
        "SELECT * FROM settings_base WHERE chat_id=%s"
    )

    data = (
        chat_id,
    )

    cursor.execute(sql, data)

    return cursor.fetchone()


def add_welcome(chat_id, welcome_text="Hello {first_name}, \nWelcome to {group_name} !"):

    sql = (
        "REPLACE INTO welcome_base (chat_id, welcome_text) VALUE(%s, %s)"
    )
    data = (
        chat_id, welcome_text
    )

    # print(data)

    cursor.execute(sql, data)
    db.commit()


def get_welcome(chat_id):
    sql = (
        "SELECT * FROM welcome_base WHERE chat_id=%s"
    )

    data = (
        chat_id,
    )

    cursor.execute(sql, data)

    return cursor.fetchone()
