
"""
Contains functions for creating keyboards
"""
from config import (
	UserMood, 
	Genre, 
	Show, 
	Novelty, 
	CustomReplyKeyboardButton,
	CustomInlineKeyboardButton
)
from aiogram.types import (
	ReplyKeyboardMarkup, 
	KeyboardButton, 
	InlineKeyboardMarkup, 
	InlineKeyboardButton
)

class KeyboardHandler():

	def get_main_replykeyboard():
		"""Sets up the main basic replykeyboard"""
		return ReplyKeyboardMarkup(
			keyboard=[
				[
					KeyboardButton(CustomReplyKeyboardButton.SMART_SELECTION_BTN.value),
					KeyboardButton(CustomReplyKeyboardButton.WE_RECOMMEND_BTN.value),
					KeyboardButton(CustomReplyKeyboardButton.NO_PREFERENCES_BTN.value)
				],
				[
					KeyboardButton(CustomReplyKeyboardButton.SEND_FEEDBACK_BTN.value)
				]
			],
			resize_keyboard=True,
			one_time_keyboard=True
		)

	def get_mood_inlinekeyboard():
		"""Sets up inlinekeyboard for user's mood selection"""
		return InlineKeyboardMarkup(
			inline_keyboard=[
				[
					InlineKeyboardButton(text=CustomInlineKeyboardButton.DEPRESSION_BTN.value, callback_data=UserMood.DEPRESSION.value),
					InlineKeyboardButton(text=CustomInlineKeyboardButton.CHEERFUL_BTN.value, callback_data=UserMood.CHEERFUL.value),
					InlineKeyboardButton(text=CustomInlineKeyboardButton.DONT_KNOW_BTN.value, callback_data=UserMood.DONT_KNOW.value),
				],
				[
					InlineKeyboardButton(text=CustomInlineKeyboardButton.LOT_ON_MY_MIND_BTN.value, callback_data=UserMood.LOT_ON_MY_MIND.value),
					InlineKeyboardButton(text=CustomInlineKeyboardButton.STRESSED_OUT_BTN.value, callback_data=UserMood.STRESSED_OUT.value),
					InlineKeyboardButton(text=CustomInlineKeyboardButton.NO_STRENGTH_AT_ALL_BTN.value, callback_data=UserMood.NO_STRENGTH_AT_ALL.value),
				],
				[
					InlineKeyboardButton(text=CustomInlineKeyboardButton.FIGHTING_SPIRIT_BTN.value, callback_data=UserMood.FIGHTING_SPIRIT.value),
					InlineKeyboardButton(text=CustomInlineKeyboardButton.FAMILY_WEEKEND_BTN.value, callback_data=UserMood.FAMILY_WEEKEND.value),
					InlineKeyboardButton(text=CustomInlineKeyboardButton.GROUP_OF_FRIENDS_BTN.value, callback_data=UserMood.GROUP_OF_FRIENDS.value),
				],
				[
					InlineKeyboardButton(text=CustomInlineKeyboardButton.LOVE_BTN.value, callback_data=UserMood.LOVE.value)
				]
			]	
		)