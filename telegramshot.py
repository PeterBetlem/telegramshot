import requests
from io import BytesIO
import PIL.ImageGrab as ImageGrab
import time
from datetime import datetime
import argparse

# Add parser options for .exe
parser = argparse.ArgumentParser()
parser.add_argument('--apiToken', type=str, required=True)
parser.add_argument('--chatID', type=str, required=True)
parser.add_argument('--timeDelta', type=int, required=False)
args = parser.parse_args()

# Specify the send to telegram script using Telegram's API and bot/chat IDs
def send_to_telegram(apiToken, chatID, img_bytes):
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendPhoto?chat_id={chatID}'
    try:
        response = requests.post(apiURL, files={"photo": img_bytes})
        print(f"Sent screengrab at {datetime.now().now()}.")
    except Exception as e:
        print(e)

# Runs the telegramshot scripts and prints information to the console window
def telegramshot():
    timeDelta = args.timeDelta or 15 # in minutes
    apiToken = args.apiToken # see https://core.telegram.org/bots#how-do-i-create-a-bot
    chatID = args.chatID # see https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

    print("Initiated telegramshot - AKA: screenshots through telegram.")
    print(f"Sceenshot interval has been set to: {timeDelta} minutes")
    while True:
        im = ImageGrab.grab() # screengrab
        byte_io = BytesIO() # saves as bytesio object
        byte_io.name = "image.png"
        im.save(byte_io, 'PNG')
        byte_io.seek(0) 
        send_to_telegram(apiToken, chatID, byte_io) #sends file
        time.sleep(60*timeDelta) # puts bot to sleep for 60*timeDelta minutes

if __name__ == "__main__":
    telegramshot()
