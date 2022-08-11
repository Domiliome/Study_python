from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputMediaVideo
from aiogram.utils import executor
from aiogram.utils.markdown import bold

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

cities = {
    "Калининград" : ["Аптека №12 ул. Багратиона 53а","Здоровье Дзержинского 19"],
    "Багратионовск" : ["Аптека №11 ул. Центральная 5","Здоровье Багратиона 1"]
         }
@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("Привет\nНапиши мне город")

@dp.message_handler()
async def process_multimedia_command(message: types.Message):
    data = cities[message.text]
    for item in data:
        await message.answer(item)


if __name__ == "__main__":
    executor.start_polling(dp)
