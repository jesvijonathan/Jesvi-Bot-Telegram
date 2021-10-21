bot_token = ""  # Get It From @botfather in telegram
bot_name = ""  # Example : "Jesvi Bot"
bot_username = ""  # Example : "jesvi_bot"
bot_id = ""

# Your database name, Example : "bot_database"
database_name = ""
database_user = ""  # The sudo user, Example : "root"
database_password = ""  # your database password
database_host = ""  # Example : "127.0.0.1"
database_port = ""  # Example : "3306"

owner_id = ""  # Get your/owner telegram id via @jesvi_bot, and after starting a conversation using /start, use /info to get your details
owner_username = ""  # Your/Owner user name

suppport_group_username = "bot_garage"
sudo_users = []  # Id's of sudo users you permit



##### Misc #####

bot_dict = { "id":bot_id, 
            "first_name":bot_name, 
            "last_name":None, 
            "user_name":bot_username, 
            "is_bot":True}