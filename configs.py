from os import path, getenv

class Config:
    API_ID = getenv("API_ID", '29922662')
    API_HASH = getenv("API_HASH", 'fabd9f89368de7cc31357522a0089a56')
    BOT_TOKEN = getenv("BOT_TOKEN", '6752673741:AAF6lxcFRxnIj-3cLoSktkfFD1MYCSo_iGA')
    FSUB = getenv("FSUB", "cvlinkz")
    CHID = getenv("CHID", '-1001630778710')
    SUDO = getenv("SUDO", "6047510747 1745047302").split()
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
