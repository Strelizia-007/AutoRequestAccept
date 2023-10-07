from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "6620972"))
    API_HASH = getenv("API_HASH", "3f6835286b03e000ab6d71b37cc35b92")
    BOT_TOKEN = getenv("BOT_TOKEN", "5744492052:AAHwoJ6Xn_jlnvHwVFafYcM0Pqx-TMIVIx4")
    FSUB = getenv("FSUB", "CV_link_ONly")
    CHID = int(getenv("CHID", "-1001437493581"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
