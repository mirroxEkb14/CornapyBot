
"""
Contains all the keyboards as constants
"""

from config import (
	SummaryConfirmation,
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
import config

"""Btn that every inline-keyboard contains"""
BACK_INLINE_BTN = InlineKeyboardButton(text=config.BACK_BTN, callback_data=config.BACK_BTN_CALLBACK_DATA)

"""Sets up the main basic reply-keyboard"""
MAIN_REPLY_KEYBOARD = \
	ReplyKeyboardMarkup(
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

"""Sets up inline-keyboard for user's mood selection"""
MOOD_INLINE_KEYBOARD = \
	InlineKeyboardMarkup(
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
			],
			[
				BACK_INLINE_BTN
			]
		]	
	)

"""Sets up inline-keyboard for user's show selection"""
SHOW_INLINE_KEYBOARD = \
	InlineKeyboardMarkup(
		inline_keyboard=[
			[
				InlineKeyboardButton(text=CustomInlineKeyboardButton.MOVIE_BTN.value, callback_data=Show.MOVIE.value),
				InlineKeyboardButton(text=CustomInlineKeyboardButton.SERIES_BTN.value, callback_data=Show.SERIES.value)
			],
			[
				BACK_INLINE_BTN
			]
		]
	)

"""Sets up inline-keyboard for user's genre selection"""
GENRE_INLINE_KEYBOARD = \
	InlineKeyboardMarkup(
		inline_keyboard=[
			[
				InlineKeyboardButton(text=CustomInlineKeyboardButton.COMEDY_BTN.value, callback_data=Genre.COMEDY.value),
				InlineKeyboardButton(text=CustomInlineKeyboardButton.THRILLER_BTN.value, callback_data=Genre.THRILLER.value),
				InlineKeyboardButton(text=CustomInlineKeyboardButton.ACTION_BTN.value, callback_data=Genre.ACTION.value)
			],
			[
				InlineKeyboardButton(text=CustomInlineKeyboardButton.DOCUMENTARY_BTN.value, callback_data=Genre.DOCUMENTARY.value),
				InlineKeyboardButton(text=CustomInlineKeyboardButton.FAMILY_BTN.value, callback_data=Genre.FAMILY.value),
				InlineKeyboardButton(text=CustomInlineKeyboardButton.SPORT_BTN.value, callback_data=Genre.SPORT.value)
			],
			[
				InlineKeyboardButton(text=CustomInlineKeyboardButton.FANTASY_BTN.value, callback_data=Genre.FANTASY.value),
				InlineKeyboardButton(text=CustomInlineKeyboardButton.ANIMATION_BTN.value, callback_data=Genre.ANIMATION.value)
			],
			[
				BACK_INLINE_BTN
			]
		]
	)

"""
Sets up inline-keyboard for verification user's selections 
from 'Smart Selection'
"""
SMART_SELECTION_SUMMARY_INLINE_KEYBOARD = \
	InlineKeyboardMarkup(
		inline_keyboard=[
			[
				InlineKeyboardButton(text=CustomInlineKeyboardButton.SMART_SELECTION_YES_BTN.value, callback_data=SummaryConfirmation.YES_SUMMARY.value), 
				InlineKeyboardButton(text=CustomInlineKeyboardButton.SMART_SELECTION_NO_BTN.value, callback_data=SummaryConfirmation.NO_SUMMARY.value)
			],
			[
				BACK_INLINE_BTN
			]
		]
	)
