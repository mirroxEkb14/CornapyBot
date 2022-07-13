
"""
Handle events when clicking on buttons
Buttons themselves are stored in 'personal_actions', only their callbacks are processed here
"""

from aiogram import types
from dispatcher import dp
from config import UserMood, Show, Genre
from .keyboards import KeyboardHandler
import config

@dp.callback_query_handler(text=UserMood.list())
async def process_mood(call: types.CallbackQuery):
	"""
	Processing user's mood selection
	'call.data' represents a value of selected mood by user from UserMood
	"""
	if config.PROCESS_FLAGS['mood_selected'] == False:
		config.USER_MOOD = UserMood(call.data)
		config.PROCESS_FLAGS['mood_selected'] = True
		await call.message.answer("Understood, now you'd want to watch...", reply_markup=KeyboardHandler.get_show_inlinekeyboard())

@dp.callback_query_handler(text=Show.list())
async def process_show(call: types.CallbackQuery):
	"""Processing user's show selection"""
	if config.PROCESS_FLAGS['show_selected'] == False:
		config.USER_SHOW = Show(call.data)
		config.PROCESS_FLAGS['show_selected'] = True
		await call.message.answer('Ok then, here is maybe the most difficult part... choose a genre:', reply_markup=KeyboardHandler.get_genre_inlinekeyboard())

@dp.callback_query_handler(text=Genre.list())
async def process_genre(call: types.CallbackQuery):
	"""Processing user's genre selection"""
	if config.PROCESS_FLAGS['genre_selected'] == False:
		config.USER_GENRE = Genre(call.data)
		config.PROCESS_FLAGS['genre_selected'] = True
		await call.message.answer(f"{config.USER_MOOD}\n{config.USER_SHOW}\n{config.USER_GENRE}")