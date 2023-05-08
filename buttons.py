'''Yosh menejer 2002 bot buttons'''

from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton

til = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="🇸🇱O'zbekcha",callback_data='uz'),
			InlineKeyboardButton(text="🇬🇧English",callback_data='en'),
		],
	]
)

salom = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="📜Loyiha haqida",callback_data='loyiha_menu'),
			InlineKeyboardButton(text="📃Royxatdan otish",callback_data='royxat'),
		],
		[
			InlineKeyboardButton(text="📝Savollar yollash",callback_data='savol'),
		],
	]
)
salom_en = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="📜About the project",callback_data='abo'),
			InlineKeyboardButton(text="📃Registration",callback_data='reg'),
		],
		[
			InlineKeyboardButton(text="📝Send questions",callback_data='send'),
		],
	]
)


loyiha_haqida_menu = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Loyiha maqsadi",callback_data='maqsad'),
			InlineKeyboardButton(text="Loyiha vazifasi",callback_data='vazifa'),
		],
		[
			InlineKeyboardButton(text="O'tkazilish tartibi",callback_data='tartibi'),
			InlineKeyboardButton(text="Talablar",callback_data='talab'),
		],

		[
			InlineKeyboardButton(text="Ortka",callback_data='ortka'),
		],
	]
)
loyiha_haqida_menu_en = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Aim of the project",callback_data='aim'),
			InlineKeyboardButton(text="Project task",callback_data='pro'),
		],
		[
			InlineKeyboardButton(text="The order of process",callback_data='the'),
			InlineKeyboardButton(text="Requirements",callback_data='req'),
		],

		[
			InlineKeyboardButton(text="Back",callback_data='back'),
		],
	]
)

loyiha_maqsad = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Ortka",callback_data='loyiha_menu'),
		],
	]
)
loyiha_maqsad_en = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Back",callback_data='abo'),
		],
	]
)

loyiha_vazifasi = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Ortka",callback_data='loyiha_menu'),
		],
	]
)
loyiha_vazifasi_en = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Back",callback_data='abo'),
		],
	]
)

loyiha_tartibi = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Ortka",callback_data='loyiha_menu'),
		],
	]
)

loyiha_tartibi_en = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Back",callback_data='abo'),
		],
	]
)

loyiha_talablari = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Ortka",callback_data='loyiha_menu'),
		],
	]
)

loyiha_talablari_en = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Back",callback_data='abo'),
		],
	]
)

savollar_yollash = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Ortka",callback_data='ortka'),
		],
	]
)

savollar_yollash_en = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Back",callback_data='back'),
		],
	]
)