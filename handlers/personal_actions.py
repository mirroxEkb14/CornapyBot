
"""
Bot activity via personal messages
"""

from aiogram import types
from dispatcher import dp, bot
from . import keyboards
from random import randint
import asyncio
from config import (
	CustomReplyKeyboardButton,
	WELCOME_STI,
	SMART_SELECTION_STI,
	REPLY_KEYBOARD_MESSAGES,
	CALLBACK_MESSAGES
)
import config

# register the '/start' command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	"""Send a sticker and message with replykeyboard"""

	wlcm_sti = open(WELCOME_STI, 'rb')
	await bot.send_sticker(chat_id=message.chat.id, sticker=wlcm_sti)

	me = await bot.get_me()
	await message.answer(f"Welcome {message.from_user.first_name}!\nI'm - <b>{me.first_name}</b>, created to be your own movie-guide\nLet's pick some movie", 
		parse_mode='html', reply_markup=keyboards.MAIN_REPLY_KEYBOARD)

# filter user messages
@dp.message_handler()
async def filter_messages(message: types.Message):
	"""Process ReplyKeyboard calls"""

	if message.text == CustomReplyKeyboardButton.SMART_SELECTION_BTN.value and config.IS_SMART_SELECTION == False:
		""" 'Smart Selection' case  """

		config.IS_SMART_SELECTION = True

		smart_selection_messages = REPLY_KEYBOARD_MESSAGES['SMART_SELECTION']
		smrt_slctn_sti = open(SMART_SELECTION_STI, 'rb')
		await bot.send_sticker(chat_id=message.chat.id, sticker=smrt_slctn_sti)
		await message.answer(smart_selection_messages[randint(0, len(smart_selection_messages) - 1)])
		
		await asyncio.sleep(1)
		mood_selection_messages = CALLBACK_MESSAGES['MOOD_SELECTION']
		await message.answer(mood_selection_messages[randint(0, len(mood_selection_messages) - 1)], reply_markup=keyboards.MOOD_INLINE_KEYBOARD)

	elif config.IS_SMART_SELECTION:
		"""If user tries to type something during 'Smart Selection' """
		await message.reply("How about finishing Smart Selection?")

	else:
		"""Process user's messages that don't contain commands or btn texts"""
		await message.reply("Don't know how to process something like this...")