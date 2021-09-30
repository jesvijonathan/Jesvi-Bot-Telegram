from os import system
from re import L
from time import sleep

from config import *

from mysql import connector


def load():    
    db = connector.connect(
    host=database_host,
    user=database_user,
    password=database_password,
    database=database_name)
    cursor = db.cursor(buffered=True)

    bot_db(cursor,db)

class create_db:
        # Variable Initialisation
        def __init__(self):
            self.db = connector.connect(
            host=database_host,
            user=database_user,
            password=database_password,
            database=database_name)
            self.cursor = self.db.cursor(buffered=True)
            
            self.user = self.chat = None

        # Table Creation
        def chat_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS chat_base ( chat_id VARCHAR(14) PRIMARY KEY, type VARCHAR(14), title VARCHAR(48), username VARCHAR(48), join_date TIMESTAMP)"
            )  # chat_base : chat_id | type | title | username | join_date
            self.cursor.execute(sql)
            self.db.commit()

        def user_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS user_base ( user_id VARCHAR(14) PRIMARY KEY, first_name VARCHAR(48), last_name VARCHAR(48), username VARCHAR(48), is_bot BOOLEAN, date TIMESTAMP)"
            )  # user_base : user_id | first_name | lastname | username | is_bot | date
            self.cursor.execute(sql)
            self.db.commit()

        def settings_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS settings_base ( chat_id VARCHAR(14) PRIMARY KEY, members TINYINT, warn_limit TINYINT DEFAULT 3, strike_action TINYINT DEFAULT 0, disabled_commands TINYINT DEFAULT 0, filter TINYINT DEFAULT 0, notes TINYINT DEFAULT 0, chat_lock TINYINT DEFAULT 0, recent_pin TINYINT)"
            )  # settings_base : chat_id | members | warn_limit | strike_action | disabled_commands | filter | notes | lock | recent_pin
            self.cursor.execute(sql)
            self.db.commit()

        def filter_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS filter_base ( id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, chat_id VARCHAR(14), filter_word VARCHAR(32), filter_type TINYINT DEFAULT 0, response TEXT NULL, remove BOOLEAN DEFAULT 0)"
            )  # filter_base : id | chat_id | filter_word | filter_type | response | remove
            self.cursor.execute(sql)
            self.db.commit()

        def notes_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS notes_base ( id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, chat_id VARCHAR(14), note_name VARCHAR(32), note_text TEXT, set_by VARCHAR(32), date TIMESTAMP)"
            )  # notes_base : id | chat_id | note_name | note_text | set_by | date
            self.cursor.execute(sql)
            self.db.commit()

        def warn_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS warn_base ( id VARCHAR(14) PRIMARY KEY, chat_id VARCHAR(14), note_name VARCHAR(32), note_text TEXT, set_by VARCHAR(32), date TIMESTAMP)"
            )  # warn_base : id | chat_id | user_id | by_user_id | message_id | reason | date
            self.cursor.execute(sql)
            self.db.commit()

        def link_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS link_base ( id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, chat_id VARCHAR(14), user_id VARCHAR(14), status VARCHAR(14) DEFAULT 'member', bio TEXT, join_date TIMESTAMP, last_active TIMESTAMP)"
            )  # link_base : id | chat_id | user_id | status | bio | join_date | last_active
            self.cursor.execute(sql)
            self.db.commit()

        def disabled_commands_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS disabled_commands_base ( id VARCHAR(14) PRIMARY KEY, chat_id VARCHAR(14), user_id VARCHAR(14), command VARCHAR(32), set_by VARCHAR(14))"
            )  # disabled_commands_base : id | chat_id | user_id | command | set_by
            self.cursor.execute(sql)
            self.db.commit()

        def recent_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS recent_base ( id VARCHAR(14) PRIMARY KEY, chat_id VARCHAR(14), pin_text TEXT, message_id VARCHAR(14), pin_by VARCHAR(32), date TIMESTAMP)"
            )  # recent_base : id | chat_id | pin_text | message_id | pin_by | date
            self.cursor.execute(sql)
            self.db.commit()

        def rules_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS rules_base ( chat_id VARCHAR(14) PRIMARY KEY, rule_text TEXT, rule_type VARCHAR(14), message_id VARCHAR(14), set_by VARCHAR(32), date TIMESTAMP)"
            )  # rules_base : chat_id | rule_text | rule_type | message_id | set_by | date
            self.cursor.execute(sql)
            self.db.commit()

        def welcome_base(self):
            sql = (
                "CREATE TABLE IF NOT EXISTS welcome_base ( chat_id VARCHAR(14) PRIMARY KEY, welcome_text TEXT, verification BOOLEAN DEFAULT 0, fail_action TINYINT DEFAULT 1)"
            )  # welcome_base : chat_id | welcome_text | verification | fail_action
            self.cursor.execute(sql)
            self.db.commit()

        def create_base(self):
            self.chat_base()
            self.user_base()
            self.link_base()
            self.settings_base()
            self.filter_base()
            self.notes_base()
            self.welcome_base()

try:
    class bot_db:
        # Variable Initialisation
        def __init__(self):
            self.db = connector.connect(
            host=database_host,
            user=database_user,
            password=database_password,
            database=database_name)
            self.cursor = self.db.cursor(buffered=True)
            
            self.user = self.chat = None

        def parse(self,chat,user):
            self.add_user(user)
            self.add_chat(chat)
            self.add_link(chat, user)


        def add_user(self,user):
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

            self.cursor.execute(sql, data)
            self.db.commit()


        def get_user(self,user_id):
            sql = (
                "SELECT * FROM user_base WHERE user_id=%s"
            )

            data = (
                user_id,
            )

            self.cursor.execute(sql, data)

            return self.cursor.fetchone()



        def add_chat(self,chat):
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

            self.cursor.execute(sql, data)
            self.db.commit()


        def get_chat(self,chat_id):
            sql = (
                "SELECT * FROM chat_base WHERE chat_id=%s"
            )

            data = (
                chat_id,
            )

            self.cursor.execute(sql, data)

            return self.cursor.fetchone()



        def add_link(self,chat, user, status="member", replace=0):
            chat_id = chat['id']
            user_id = user['id']

            sql = (
                "SELECT (1) FROM link_base WHERE chat_id=%s AND user_id=%s LIMIT 1"
            )
            data = (
                chat_id,

                user_id
            )

            self.cursor.execute(sql, data)

            if self.cursor.fetchone():
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

            self.cursor.execute(sql1, data1)
            self.db.commit()


        def get_link(self,chat_id, user_id):
            sql = (
                "SELECT * FROM link_base WHERE chat_id=%s AND user_id=%s"
            )

            data = (
                chat_id, user_id,
            )

            self.cursor.execute(sql, data)

            return self.cursor.fetchone()


        def add_settings(self, chat_id, members=None,lock=None,filter=None,notes=None):
            if lock != None:
                sql = (
                    "INSERT INTO settings_base (chat_id, chat_lock) VALUE(%s, %s) ON DUPLICATE KEY UPDATE chat_lock=%s"
                )
                data = (
                    chat_id, lock,
                    lock,
                )
            elif filter != None:
                sql = (
                    "INSERT INTO settings_base (chat_id, filter) VALUE(%s, %s) ON DUPLICATE KEY UPDATE filter=%s"
                )
                data = (
                    chat_id, filter,
                    filter,
                )
            elif notes != None:
                sql = (
                    "INSERT INTO settings_base (chat_id, notes) VALUE(%s, %s) ON DUPLICATE KEY UPDATE notes=%s"
                )
                data = (
                    chat_id, notes,
                    notes,
                )
            elif members != None:
                sql = (
                    "INSERT INTO settings_base (chat_id, members) VALUE(%s, %s) ON DUPLICATE KEY UPDATE members=%s"
                )
                data = (
                    chat_id, members,
                    members,
                )

            self.cursor.execute(sql, data)
            self.db.commit()


        def get_settings(self,chat_id):
            sql = (
                "SELECT * FROM settings_base WHERE chat_id=%s"
            )

            data = (
                chat_id,
            )

            self.cursor.execute(sql, data)

            return self.cursor.fetchone()


        def add_note(self, chat_id, note_name, note_text, set_by):

            sql = (
                "REPLACE INTO notes_base (chat_id, note_name, note_text, set_by, date) VALUE(%s, %s, %s, %s, CURRENT_TIMESTAMP())"
            )
            data = (
                chat_id, note_name, note_text, set_by,
            )

            self.cursor.execute(sql, data)
            self.db.commit()


        def get_note(self,chat_id):
            sql = (
                "SELECT * FROM notes_base WHERE chat_id=%s"
            )

            data = (
                chat_id,
            )

            self.cursor.execute(sql, data)

            return self.cursor.fetchall()

        def get_note_text(self,chat_id,note_name=None):
            sql = (
                "SELECT * FROM notes_base WHERE chat_id=%s AND note_name=%s LIMIT 1"
            )

            data = (
                chat_id,note_name,
            )

            self.cursor.execute(sql, data)

            return self.cursor.fetchone()

        def remove_note(self,chat_id,note_name=None):
            if note_name == '*':
                sql = (
                "DELETE FROM notes_base WHERE chat_id=%s"
            )
                data = (
                    chat_id,
            )
            
            else:
                sql = (
                "DELETE FROM notes_base WHERE chat_id=%s AND note_name=%s ORDER BY id DESC LIMIT 1"
            )
                data = (
                    chat_id,note_name,
            )

            self.cursor.execute(sql, data)
            self.db.commit()


        def add_filter(self,chat_id, word, type=0, response=None, delete=1):
            sql = (
                "REPLACE INTO filter_base (chat_id, filter_word, filter_type, response, remove) VALUE(%s, %s, %s, %s, %s)"
            )
            data = (
                chat_id, word, type, response, delete,
            )

            self.cursor.execute(sql, data)
            self.db.commit()


        def get_filter(self,chat_id):
            sql = (
                "SELECT * FROM filter_base WHERE chat_id=%s"
            )

            data = (
                chat_id,
            )

            self.cursor.execute(sql, data)

            return self.cursor.fetchall()


        def remove_filter(self,chat_id,word):
            if word == '*':
                sql = (
                    "DELETE FROM filter_base WHERE chat_id=%s"
                )
                data = (
                    chat_id,
                )
            else:
                sql = (
                    "DELETE FROM filter_base WHERE chat_id=%s AND filter_word=%s ORDER BY id DESC LIMIT 1"
                )
                data = (
                    chat_id, word,
                )

            self.cursor.execute(sql, data)
            self.db.commit()


        def add_welcome(self,chat_id, welcome_text="Hello {first_name}, \nWelcome to {group_name} !"):

            sql = (
                "REPLACE INTO welcome_base (chat_id, welcome_text) VALUE(%s, %s)"
            )
            data = (
                chat_id, welcome_text
            )

            # print(data)

            self.cursor.execute(sql, data)
            self.db.commit()


        def get_welcome(self,chat_id):
            sql = (
                "SELECT * FROM welcome_base WHERE chat_id=%s"
            )

            data = (
                chat_id,
            )

            self.cursor.execute(sql, data)

            return self.cursor.fetchone()

            
except Exception as ex:
    print(ex)
    load()

