import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", ""))
	API_HASH = os.environ.get("API_HASH", "")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
	DATABASE_URL = os.environ.get("DATABASE_URL", "")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

β­β[ **π FΙͺΚα΄ Sα΄α΄Κα΄ Bα΄α΄ π ** ]ββ
β
βπΈπ€ **My Name:** [FΙͺΚα΄ Sα΄α΄Κα΄ Bα΄α΄](https://telegram.me/{BOT_USERNAME})
β
βπΈπ **Language:** [Python](https://www.python.org)
β
βπΈπ **Library:** [Pyrogram](https://docs.pyrogram.org)
β
βπΈπ‘ **Hosted On:** [Mogenious](https://mogenius.com)
β
βπΈπ¨βπ» **Owner:** [ π¨ππππππππ·π΄ γ ](https://telegram.me/AnshumanPM_2006) 
β
β°β[ π** π π¨ππππππππ·π΄ γ π **π ]ββ
"""
	ABOUT_DEV_TEXT = f"""
π§π»βπ» **Owner:** [ π¨ππππππππ·π΄ γ ](https://telegram.me/AnshumanPM_2006) 

__Owner Is Super Noob. Just Learning from Official Docs. And Seeking Help From Pro Coders.__

__If You want to Donate Our Hard Work. You Can Contact The Owner.__

__Also Remember that Owner will Delete__ **Adult Contents** __from Database. So Better don't Store Those Kinds of Things.__
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FΙͺΚα΄ Sα΄α΄Κα΄ Bα΄α΄**.

How to Use Bot & it's Benefits??

π’ Send me any File & It will be uploaded in My Database & You will Get the File Link.

β οΈ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

β **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
