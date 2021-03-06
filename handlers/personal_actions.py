
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
import logger
import config

# define a logger for this file
log = logger.get_logger(logger_name=__name__, file_name = 'logger/personal_actions_info.log')

# register the '/start' command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	"""Send a sticker and message with replykeyboard"""

	log.info("Executing 'send_welcome' function")

	wlcm_sti = open(WELCOME_STI, 'rb')
	await bot.send_sticker(chat_id=message.chat.id, sticker=wlcm_sti)

	me = await bot.get_me()
	welcome_messages = config.WELCOME_MESSAGES
	await message.answer(welcome_messages[randint(0, len(welcome_messages) - 1)].format(user_name=message.from_user.first_name, bot_name=me.first_name), 
		parse_mode='html', reply_markup=keyboards.MAIN_REPLY_KEYBOARD)

# filter user messages
@dp.message_handler()
async def filter_messages(message: types.Message):
	"""Process ReplyKeyboard calls"""

	if message.text == CustomReplyKeyboardButton.SMART_SELECTION_BTN.value and config.IS_SMART_SELECTION == False:
		""" 'Smart Selection' case  """

		log.info("Processing 'Smart Selection'")

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


# creates a menu
async def set_default_commands(dp):
	"""Sets default commands user will have when interacting with the bot"""
	await dp.bot.set_my_commands(
		[
			types.BotCommand('start', 'Launch bot'),
			types.BotCommand('help', 'Display help')
		]
	)