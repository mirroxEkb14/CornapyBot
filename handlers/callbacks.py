
"""
Handle events when clicking on buttons
Buttons themselves are stored in 'personal_actions', only their callbacks are processed here
"""

from aiogram import types
from dispatcher import dp, bot
from .keyboards import KeyboardHandler
from random import randint
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import (
	SummaryConfirmation,
	UserMood, 
	Show, 
	Genre, 
	CALLBACK_MESSAGES
)
import config

@dp.callback_query_handler(text=UserMood.list())
async def process_mood(call: types.CallbackQuery):
	"""
	Processing user's mood selection
	'call.data' represents a value of selected mood by user from UserMood
	'edit_message_reply_markup()' removes the keyboard user already used
	"""

	if config.PROCESS_FLAGS['mood_selected'] == False:
		config.USER_MOOD = UserMood(call.data)
		config.PROCESS_FLAGS['mood_selected'] = True

		await call.message.edit_text(text=CALLBACK_MESSAGES['SHOW_PROCESSING'][randint(0, 1)], reply_markup=KeyboardHandler.get_show_inlinekeyboard())

@dp.callback_query_handler(text=Show.list())
async def process_show(call: types.CallbackQuery):
	"""Processing user's show selection"""

	if config.PROCESS_FLAGS['show_selected'] == False:
		config.USER_SHOW = Show(call.data)
		config.PROCESS_FLAGS['show_selected'] = True

		await call.message.edit_text(text=CALLBACK_MESSAGES['GENRE_PROCESSING'][randint(0, 1)], reply_markup=KeyboardHandler.get_genre_inlinekeyboard())

@dp.callback_query_handler(text=Genre.list())
async def process_genre(call: types.CallbackQuery):
	"""Processing user's genre selection"""

	if config.PROCESS_FLAGS['genre_selected'] == False:
		config.USER_GENRE = Genre(call.data)
		config.PROCESS_FLAGS['genre_selected'] = True

		await call.message.edit_text(text=f'Did I catch you right?\n\nMood: <b>{config.USER_MOOD.value}</b>\nPreference: <b>{config.USER_SHOW.value}</b>\nGenre: <b>{config.USER_GENRE.value}</b>', 
			reply_markup=KeyboardHandler.get_smart_selection_summary_inlinekeyboard(), parse_mode='html')


@dp.callback_query_handler(text=SummaryConfirmation.list())
async def verify_smart_selection(call: types.CallbackQuery):
	"""
	Processing the conformation of all user's selections 
	from 'Smart Selection'
	"""

	if call.data == SummaryConfirmation.YES_SUMMARY.value:
		"""If user agrees that all his selections are correct"""
		await bot.edit_message_reply_markup(chat_id=call.from_user.id, 
			message_id=call.message.message_id, reply_markup=None)

		await call.message.answer(CALLBACK_MESSAGES['SMART_SELECTION_VERIFYING'][randint(0, 1)])

	elif call.data == SummaryConfirmation.NO_SUMMARY:
		"""If user wants to go back and change some of his selections"""
		pass
