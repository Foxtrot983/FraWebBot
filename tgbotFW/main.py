import logging
from aiogram import Bot, Dispatcher, executor, types
from .config import API_TOKEN


<<<<<<< HEAD
=======
API_TOKEN = ''

>>>>>>> 3c653dbcabda33aca666e02d35949279bfc12a49
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет!\nЯ бот компании FraWeb, через меня ты можешь оставить заявку на разработку веб-сайта.😊")



@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
