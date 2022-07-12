
"""
Bot activity via personal messages
"""

from aiogram import types
from dispatcher import dp, bot
import config

# register the '/start' command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	"""Send a sticker and message"""
	sti = open('static/welcome.webp', 'rb')
	await bot.send_sticker(chat_id=message.chat.id, sticker=sti)

	me = await bot.get_me()
	await message.reply(f"Welcome {message.from_user.first_name}!\nI'm - <b>{me.first_name}</b>, created to be your own movie-guide", parse_mode='html')

# echo function
@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)