import telegram
import os
import time
import random


bot = telegram.Bot(token='7615217105:AAHvvO7l7f5OzZ4EdP5SW-b_kFN4Z2eYWX0')
images = os.listdir("images")
while True:
    random.shuffle(images)
    for image in images:
        with open(os.path.join("images", image), 'rb') as file:
            bot.send_document(chat_id="@ljgiklgjklgyufujkyfjkm7uy657", document=file)
            time.sleep(5)
    time.sleep(14400)
