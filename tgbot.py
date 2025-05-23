import telegram
import os
import time
import random
from dotenv import load_dotenv


load_dotenv()
bot = telegram.Bot(token=os.getenv("TG_API"))
images = os.listdir("images")
while True:
    random.shuffle(images)
    for image in images:
        with open(os.path.join("images", image), 'rb') as file:
            bot.send_document(chat_id=os.getenv("CHAT_ID"), document=file)
            time.sleep(5)
    time.sleep(14400)
