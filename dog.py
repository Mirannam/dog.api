import requests
from pprint import pprint
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot_token = "1975598509:AAEhBnGKJDAV6RxFBX1ztMXVuR5e6g7J9yM"

bot = Bot(token=bot_token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start_comand(message: types.Message):
    await message.reply("Hello! введите породу собаки и получите фото")

@dp.message_handler()
async def get_dog(message: types.Message):
    try:

        r = requests.get(f"https://dog.ceo/api/breed/{message.text}/images/random")
        data = r.json()
        pprint(data)
    except:
        await message.reply("проверьте название")
if __name__ == "__main__":
    executor.start_polling(dp)
'''def get_dog(message):
    
def main():

    get_dog('message')


if __name__ == "__main__":
    main()'''