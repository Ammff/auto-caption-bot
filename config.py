# <C> MoTechYT


import os

class Config(object):
    MT_BOT_TOKEN = os.environ.get("MT_BOT_TOKEN", "")
    API_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", "@c_i_n_i_m_a_v_i_l_l_a ")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/MO_TECH_YT")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
