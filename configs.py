from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "29922662"))
    API_HASH = getenv("API_HASH", "fabd9f89368de7cc31357522a0089a56")
    BOT_TOKEN = getenv("BOT_TOKEN", "5652993501:AAEasaLU_rSNl05k9Z9eEgRVtyliEVIGWio")
    FSUB = getenv("FSUB", "cv_offical")
    CHID = int(getenv("CHID", "-1001574664407"))
    SUDO = getenv("SUDO", "6874351976 6047510747").split()
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ironman:ironman@cluster0.o1yjwis.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
