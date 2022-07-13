
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

	await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, 
		reply_markup=InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text=call.data, callback_data='test')]
			]
		)
	)

	if config.PROCESS_FLAGS['mood_selected'] == False:
		config.USER_MOOD = UserMood(call.data)
		config.PROCESS_FLAGS['mood_selected'] = True

		await call.message.answer(CALLBACK_MESSAGES['SHOW_PROCESSING'][randint(0, 1)], reply_markup=KeyboardHandler.get_show_inlinekeyboard())

@dp.callback_query_handler(text=Show.list())
async def process_show(call: types.CallbackQuery):
	"""Processing user's show selection"""

	await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, 
		reply_markup=InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text=call.data, callback_data='test')]
			]
		)
	)

	if config.PROCESS_FLAGS['show_selected'] == False:
		config.USER_SHOW = Show(call.data)
		config.PROCESS_FLAGS['show_selected'] = True

		await call.message.answer(CALLBACK_MESSAGES['GENRE_PROCESSING'][randint(0, 1)], reply_markup=KeyboardHandler.get_genre_inlinekeyboard())

@dp.callback_query_handler(text=Genre.list())
async def process_genre(call: types.CallbackQuery):
	"""Processing user's genre selection"""

	await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, 
		reply_markup=InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text=call.data, callback_data='test')]
			]
		)
	)

	if config.PROCESS_FLAGS['genre_selected'] == False:
		config.USER_GENRE = Genre(call.data)
		config.PROCESS_FLAGS['genre_selected'] = True

		await call.message.answer(f"{config.USER_MOOD}\n{config.USER_SHOW}\n{config.USER_GENRE}")