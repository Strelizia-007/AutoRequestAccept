from os import path, getenv

class Config:
    API_ID = getenv("API_ID", "6620972")
    API_HASH = getenv("API_HASH", "3f6835286b03e000ab6d71b37cc35b92")
    BOT_TOKEN = getenv("BOT_TOKEN", "6752673741:AAF-SWw9dTRgEB0u3JO3LEASvujstmZwIR8")
    FSUB = getenv("FSUB", "CV_offical")
    CHID = getenv("CHID", "-1002116542152")
    SUDO = getenv("SUDO", "6047510747 1745047302").split()
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
