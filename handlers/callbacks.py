
"""
Handle events when clicking on buttons
Buttons themselves are stored in 'personal_actions', only their callbacks are processed here
"""

from aiogram import types
from dispatcher import dp, bot
from . import keyboards
from random import randint
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import (
	SummaryConfirmation,
	UserMood, 
	Show, 
	Genre, 
	CALLBACK_MESSAGES,
	SMART_SELECTION_BACK_MESSAGES
)
import logger
import config
import asyncio

log = logger.get_logger(logger_name=__name__, file_name = 'logger/callbacks_info.log')

@dp.callback_query_handler(text=UserMood.list())
async def process_mood(call: types.CallbackQuery):
	"""
	Processing user's mood selection
	'call.data' represents a value of selected mood by user from UserMood
	'edit_message_reply_markup()' removes the keyboard user already used
	"""

	if config.PROCESS_FLAGS['mood_selected'] == False:

		log.info("'Smart Selection': mood processing")

		config.USER_MOOD = UserMood(call.data)
		config.PROCESS_FLAGS['mood_selected'] = True

		show_processing_message = CALLBACK_MESSAGES['SHOW_PROCESSING']
		await call.message.edit_text(text=show_processing_message[randint(0, len(show_processing_message) - 1)], reply_markup=keyboards.SHOW_INLINE_KEYBOARD)

@dp.callback_query_handler(text=Show.list())
async def process_show(call: types.CallbackQuery):
	"""Processing user's show selection"""

	if config.PROCESS_FLAGS['show_selected'] == False:

		log.info("'Smart Selection': show processing")

		config.USER_SHOW = Show(call.data)
		config.PROCESS_FLAGS['show_selected'] = True

		genre_processing_message = CALLBACK_MESSAGES['GENRE_PROCESSING']
		await call.message.edit_text(text=genre_processing_message[randint(0, len(genre_processing_message) - 1)], reply_markup=keyboards.GENRE_INLINE_KEYBOARD)

@dp.callback_query_handler(text=Genre.list())
async def process_genre(call: types.CallbackQuery):
	"""Processing user's genre selection"""

	if config.PROCESS_FLAGS['genre_selected'] == False:

		log.info("'Smart Selection': genre processing")

		config.USER_GENRE = Genre(call.data)
		config.PROCESS_FLAGS['genre_selected'] = True

		await call.message.edit_text(text=f'Did I catch you right?\n\nMood: <b>{config.USER_MOOD.value}</b>\nPreference: <b>{config.USER_SHOW.value}</b>\nGenre: <b>{config.USER_GENRE.value}</b>', 
			reply_markup=keyboards.SMART_SELECTION_SUMMARY_INLINE_KEYBOARD, parse_mode='html')


@dp.callback_query_handler(text=SummaryConfirmation.list())
async def verify_smart_selection(call: types.CallbackQuery):
	"""
	Processing the conformation of all user's selections 
	from 'Smart Selection'
	"""

	if call.data == SummaryConfirmation.YES_SUMMARY.value:
		"""If user agrees that all his selections are correct"""

		log.info("'Smart Selection': 'yes_summary' processing")

		await bot.edit_message_reply_markup(chat_id=call.from_user.id, 
			message_id=call.message.message_id, reply_markup=None)

		reset_smart_selection_constants()

		smart_selection_verifying_message = CALLBACK_MESSAGES['SMART_SELECTION_VERIFYING']
		await call.message.answer(smart_selection_verifying_message[randint(0, len(smart_selection_verifying_message) - 1)])

	elif call.data == SummaryConfirmation.NO_SUMMARY.value:
		"""Get user in the beggining - mood selection"""

		log.info("'Smart Selection': 'no_summary' processing")

		config.PROCESS_FLAGS['mood_selected'] = False
		config.PROCESS_FLAGS['show_selected'] = False
		config.PROCESS_FLAGS['genre_selected'] = False

		smart_selection_summing_up_back_message = SMART_SELECTION_BACK_MESSAGES['ON_SUMMING_UP_SELECTION_BACK']
		await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, 
			text=smart_selection_summing_up_back_message[randint(0, len(smart_selection_summing_up_back_message) - 1)],
			reply_markup=None)

		await asyncio.sleep(1)
		mood_selection_message = CALLBACK_MESSAGES['MOOD_SELECTION']
		await call.message.answer(mood_selection_message[randint(0, len(mood_selection_message) - 1)], 
			reply_markup=keyboards.MOOD_INLINE_KEYBOARD)


@dp.callback_query_handler(text=config.BACK_BTN_CALLBACK_DATA)
async def process_back(call: types.CallbackQuery):
	"""
	Each step during 'Smart Selection' has an option of going back 
	to the previous step

	Basically, on each step we just change the current message text and its keyboard,
	excluding the first 'if' because it returns us to the main menu with a reply-keyboard,
	so that we have to delete the current inline-keyboard and then attach a reply-one to a
	new-written message 
	"""

	if config.PROCESS_FLAGS['mood_selected'] == False:
		"""Means user on the step of selecting mood and want to return to the main menu"""

		log.info("'Smart Selection': going back from 'mood' to the 'main_keyboard'")

		config.IS_SMART_SELECTION = False

		await bot.edit_message_reply_markup(chat_id=call.from_user.id, 
			message_id=call.message.message_id, reply_markup=None)

		smart_selection_mood_back_message = SMART_SELECTION_BACK_MESSAGES['ON_MOOD_SELECTION_BACK']
		await call.message.answer(smart_selection_mood_back_message[randint(0, len(smart_selection_mood_back_message) - 1)],
			reply_markup=keyboards.MAIN_REPLY_KEYBOARD)

	elif config.PROCESS_FLAGS['show_selected'] == False:
		"""Means user on the step of selecting show and wants to change his mood"""

		log.info("'Smart Selection': going back from 'show' to the 'mood'")

		config.PROCESS_FLAGS['mood_selected'] = False

		smart_selection_show_back_message = SMART_SELECTION_BACK_MESSAGES['ON_SHOW_SELECTION_BACK']
		await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, 
			text=smart_selection_show_back_message[randint(0, len(smart_selection_show_back_message) - 1)], 
			reply_markup=keyboards.MOOD_INLINE_KEYBOARD)

	elif config.PROCESS_FLAGS['genre_selected'] == False:
		"""Means user on the step of selecting genre and wants to change his show"""

		log.info("'Smart Selection': going back from 'genre' to the 'show'")

		config.PROCESS_FLAGS['show_selected'] = False

		smart_selection_genre_back_message = SMART_SELECTION_BACK_MESSAGES['ON_GENRE_SELECTION_BACK']
		await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, 
			text=smart_selection_genre_back_message[randint(0, len(smart_selection_genre_back_message) - 1)], 
			reply_markup=keyboards.SHOW_INLINE_KEYBOARD)

	elif config.PROCESS_FLAGS['mood_selected'] == True and \
		config.PROCESS_FLAGS['show_selected'] == True and \
		config.PROCESS_FLAGS['genre_selected'] == True:
		"""Means user on the step of summing up and wants to change his genre"""

		log.info("'Smart Selection': going back from 'summing_up' to the 'genre'")

		config.PROCESS_FLAGS['genre_selected'] = False

		smart_selection_summary_back_message = SMART_SELECTION_BACK_MESSAGES['ON_SUMMARY_SELECTION_BACK']
		await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, 
			text=smart_selection_summary_back_message[randint(0, len(smart_selection_summary_back_message) - 1)], 
			reply_markup=keyboards.GENRE_INLINE_KEYBOARD)


def reset_smart_selection_constants():
	"""After user confirms he selected all the categories right"""
	config.USER_MOOD = None
	config.USER_SHOW = None
	config.USER_GENRE = None

	config.IS_SMART_SELECTION = False

	for el in config.PROCESS_FLAGS:
		config.PROCESS_FLAGS[el] = False