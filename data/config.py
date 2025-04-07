from environs import Env
# import json
# import os

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN") 
ADMINS = env.list("ADMINS")  