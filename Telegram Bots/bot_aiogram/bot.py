from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputMediaVideo
from aiogram.utils import executor
from aiogram.utils.markdown import bold

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("Привет\nНапиши мне что нибудь")


@dp.message_handler(commands=["help"])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне " + bold("/cat") + " и тебя ждёт кое что интересное)")

@dp.message_handler(commands=["cat"])
async def process_multimedia_command(message: types.Message):
    with open('hedgehog.mp4', 'rb') as video:
        await bot.send_video(message.from_user.id, video)

if __name__ == "__main__":
    executor.start_polling(dp)
