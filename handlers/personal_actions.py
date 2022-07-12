
"""
Bot activity via personal messages
"""

from aiogram import types
from dispatcher import dp, bot
from .keyboards import KeyboardHandler
from config import CustomReplyKeyboardButton

# register the '/start' command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	"""Send a sticker and message with replykeyboard"""
	sti = open('static/welcome.webp', 'rb')
	await bot.send_sticker(chat_id=message.chat.id, sticker=sti)

	me = await bot.get_me()
	await message.answer(f"Welcome {message.from_user.first_name}!\nI'm - <b>{me.first_name}</b>, created to be your own movie-guide\nLet's pick some movie", 
		parse_mode='html', reply_markup=KeyboardHandler.get_main_replykeyboard())

# filter user messages
@dp.message_handler()
async def filter_messages(message: types.Message):
	if message.text == CustomReplyKeyboardButton.SMART_SELECTION_BTN.value:
		await message.answer("Great, let me know your spirit condition", reply_markup=KeyboardHandler.get_mood_inlinekeyboard())
