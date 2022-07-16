
"""
Contains the config
"""

import os
from dotenv import load_dotenv
from enum import Enum

# get the token from '.env' file
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


# user's selected mood, show type(movie/series) and genre
# the variables are set in 'callbacks.py' and never changed
USER_MOOD = None
USER_SHOW = None
USER_GENRE = None

# represent the process of each reply-keyboard btn
IS_SMART_SELECTION = False
IS_WE_RECOMMEND = False
IS_NO_PREFERENCES = False
IS_SEND_FEEDBACK = False

# 'back' inline-keyboard btn
BACK_BTN = '⬅Back'
BACK_BTN_CALLBACK_DATA = 'back'

# used in 'callbacks.py' for verification
PROCESS_FLAGS = {
	'mood_selected': False, 
	'show_selected': False, 
	'genre_selected': False
}

class SummaryConfirmation(Enum):
	"""
	Variants of confirmations when we check the information user selected

	using as 'callback_data' in 'keyboards.py', for 'text' in 'callbacks.py' 
	and as a value for 'USER_MOOD'
	"""
	YES_SUMMARY = 'yes'
	NO_SUMMARY = 'no'

	@classmethod
	def list(cls):
		"""Get a list of values"""
		return list(map(lambda c: c.value, cls))


class UserMood(Enum):
	"""
	User's mood variants
	
	using as 'callback_data' in 'keyboards.py', for 'text' in 'callbacks.py' 
	and as a value for 'USER_MOOD'
	"""
	DEPRESSION = 'depression'
	CHEERFUL = 'cheerful'
	DONT_KNOW = "don't know"
	LOT_ON_MY_MIND = 'lot on my mind'
	STRESSED_OUT = 'stressed out'
	NO_STRENGTH_AT_ALL = 'no strength at all'
	FIGHTING_SPIRIT = 'fighting spirit'
	FAMILY_WEEKEND = 'family weekend'
	GROUP_OF_FRIENDS = 'group of friends'
	LOVE = 'love'

	@classmethod
	def list(cls):
		"""Get a list of values"""
		return list(map(lambda c: c.value, cls))


class Genre(Enum):
	"""
	Available genres of movies/series which we have in DB
	
	using as 'callback_data' in 'keyboards.py', for 'text' in 'callbacks.py' 
	and as a value for 'USER_MOOD'
	"""
	COMEDY = 'comedy'
	THRILLER = 'thriller'
	ACTION = 'action'
	DOCUMENTARY = 'documentary'
	FAMILY = 'family'
	SPORT = 'sport'
	FANTASY = 'fantasy'
	ANIMATION = 'animation'

	@classmethod
	def list(cls):
		"""Get a list of values"""
		return list(map(lambda c: c.value, cls))


class Show(Enum):
	"""
	What kind of show user wants to watch

	using as 'callback_data' in 'keyboards.py', for 'text' in 'callback.py',
	and as a value for 'USER_SHOW'
	"""
	MOVIE = 'movie'
	SERIES = 'series'

	@classmethod
	def list(cls):
		"""Get a list of values"""
		return list(map(lambda c: c.value, cls))


class Novelty(Enum):
	"""
	Films before 2010 included are considered as old (upper bound)
	Films after 2010 are considered as modern (lower bound)
	"""
	OLD = 2010
	MODERN = 2011


class CustomReplyKeyboardButton(Enum):
	"""Button texts for ReplyKeyboard"""
	SMART_SELECTION_BTN = '🎬Smart Selection'
	WE_RECOMMEND_BTN = '🎯We recommend'
	NO_PREFERENCES_BTN = '👀No preferences'
	SEND_FEEDBACK_BTN = '🎭Send feedback'


class CustomInlineKeyboardButton(Enum):
	"""Button texts for InlineKeyboard to process user's mood selection"""
	DEPRESSION_BTN = '🌧Depressed'
	CHEERFUL_BTN = '💃Сheerful'
	FIGHTING_SPIRIT_BTN = '😼Fighting mood'
	FAMILY_WEEKEND_BTN = '👨‍👩‍👧‍👦Family'
	GROUP_OF_FRIENDS_BTN = '🍻Friends'
	LOVE_BTN = '💋Love'
	DONT_KNOW_BTN = "🎲Don't know"
	LOT_ON_MY_MIND_BTN = '🕳Many thoughts'
	STRESSED_OUT_BTN = '💣Stressed out'
	NO_STRENGTH_AT_ALL_BTN = '😮‍💨No energy'

	"""Button texts for InlineKeyboard to process user's show selection"""
	MOVIE_BTN = '🎬Movie'
	SERIES_BTN = '🎬🎬Series'

	"""Button texts for InlineKeyboard to process user's genre selection"""
	COMEDY_BTN = '🕺Comedy'
	THRILLER_BTN = '🔫Thriller'
	ACTION_BTN = '🎒Action'
	DOCUMENTARY_BTN = '🎥Documentary'
	FAMILY_BTN = '👨‍👩‍👦Family'
	SPORT_BTN = '🚴‍♀️Sport'
	FANTASY_BTN = '🔮Fantasy'
	ANIMATION_BTN = '🧸Animation'

	"""
	Confirmation btns when user already selected all the categories
	in 'Smart Selection' (mood, movie/series, genre)
	""" 
	SMART_SELECTION_YES_BTN = '✔️Yes'
	SMART_SELECTION_NO_BTN = '✖️No'


"""
Sticker paths
"""

WELCOME_STI = 'static/welcome.webp'
SMART_SELECTION_STI = 'static/smart_selection.webp'


"""
Dictionaries with several variants of replying messages

Hard-coded bot messages: 
- 'personal_actions.py': welcome message in 'send_welcome' due to getting bot/user names
- 'callbacks.py': verification message in 'process_genre' due to getting user's selections
from 'Smart Selection'
"""

WELCOME_MESSAGES = ["Welcome {user_name}!\nI'm - <b>{bot_name}</b>, created to be your own movie-guide\nLet's pick some movie",
"Howdy {user_name}!\nMy name's <b>{bot_name}</b>, an avid lover of movies\nLet me find you some good movie"]

REPLY_KEYBOARD_MESSAGES = {
	'SMART_SELECTION': ["It's a movie time! 3.. 2.. 1..", "Time to eat some popcorn then..."]
}

CALLBACK_MESSAGES = {
	'MOOD_SELECTION': ['Great, let me know your spirit condition', 'Share your mood with me'],
	'SHOW_PROCESSING': ["Understood, now you'd want to watch...", "Roger that, now would you rather watch a movie or start watching some cool series?"],
	'GENRE_PROCESSING': ['Ok then, here is maybe the most difficult part... choose a genre:', 'Well-well, what about a genre?'],
	'SMART_SELECTION_VERIFYING': ["Great, let's find something for you!", 'Brilliant, give me a minute to find something...']
}

SMART_SELECTION_BACK_MESSAGES = {
	'ON_MOOD_SELECTION_BACK': ['Want to try some other category?', 'Hey, I got three more options!'],
	'ON_SHOW_SELECTION_BACK': ['Your mood changes so quickly...', 'Want to change the mood?'],
	'ON_GENRE_SELECTION_BACK': ['Changed your mind?', 'Getting back...'],
	'ON_SUMMARY_SELECTION_BACK': ['Changed your mind about the genre?', "I wouldn't watch that genre now too, actually..."],
	'ON_SUMMING_UP_SELECTION_BACK': ["Okay, let's try that again", "Go ahead and try again"]
}