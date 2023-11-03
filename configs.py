from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "6620972"))
    API_HASH = getenv("API_HASH", "3f6835286b03e000ab6d71b37cc35b92")
    BOT_TOKEN = getenv("BOT_TOKEN", "6752673741:AAEBQf_ZescNZlF_bp6V6b8b_bpuMXXyr0s")
    FSUB = getenv("FSUB", "CV_Offical")
    CHID = int(getenv("CHID", "-1001574664407"))
    SUDO = list(map(int, getenv("SUDO", "6047510747 6874351976").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ironman:ironman@cluster0.o1yjwis.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
