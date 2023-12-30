from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import ContentType

from loader import dp


@dp.message_handler(content_types=ContentType.ANIMATION)
async def show_help(message: types.Message):
    await message.reply(f"{message.from_user.full_name} тй гей'🤣")

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))