from pymongo import MongoClient

import config

SWEET_TOXICdb = MongoClient(config.MONGO_URL)
SWEET_TOXIC = SWEET_TOXICdb["SWEET_TOXICDb"]["SWEET_TOXIC"]


from .chats import *
from .users import *
