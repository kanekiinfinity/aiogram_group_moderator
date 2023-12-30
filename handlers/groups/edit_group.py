import io

from aiogram import types
from aiogram.dispatcher.filters import Command, ContentTypeFilter

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot
import random as r


@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    #1-usul
    await message.chat.set_photo(photo=input_file)


@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    #2-usul
    await bot.set_chat_title(message.chat.id, title=title)



@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    # 1-usul
    # await bot.set_chat_description(message.chat.id, description=description)
    # 2-usul
    await message.chat.set_description(description=description)





@dp.message_handler(IsGroup(), commands=["info"])
async def random_check(message: types.Message):
    message = message.reply_to_message
    info = message.from_user.full_name
    # info2 = message.from_user.get_user_profile_photos
    # info1 = message.
    await message.answer(f"Nick name: {info}")
    await message.answer(f"{message.from_user.username}'s id: {message.from_user.id}")
