from os import path, getenv

class Config:
    API_ID = getenv("API_ID", '29922662')
    API_HASH = getenv("API_HASH", 'fabd9f89368de7cc31357522a0089a56')
    BOT_TOKEN = getenv("BOT_TOKEN", '6752673741:AAEBQf_ZescNZlF_bp6V6b8b_bpuMXXyr0s')
    FSUB = getenv("FSUB", "Cv_Offical")
    CHID = getenv("CHID", '-1001574664407')
    SUDO = getenv("SUDO", "")
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
