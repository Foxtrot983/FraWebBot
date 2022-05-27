import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.answer("Привет!\nЯ бот компании FraWeb, через меня ты можешь оставить заявку на разработку веб-сайта. 😊")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["О нас", "Контакты", "Оставить заявку"]
    keyboard.add(*buttons)
    await message.answer("Далее вы можете узнать о нас, посмотреть контактную информацию, оставить заявку", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'О нас')
async def about(message: types.Message):
    await message.reply('Тут будет информация о нас!!')

@dp.message_handler(lambda message: message.text == 'Контакты')
async def about(message: types.Message):
    await message.reply('Тут будут контакты!!')

@dp.message_handler(lambda message: message.text == 'Оставить заявку')
async def about(message: types.Message):
    await message.reply('Тут будет последовательность заборов данных пользователя для его заявки')

@dp.message_handler()
async def echo(message: types.Message):

    await message.reply("Моя версия 0.1, фунционал еще не допилен 😠😠😠")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
