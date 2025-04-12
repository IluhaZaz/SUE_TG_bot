from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON

button_register = KeyboardButton(text=LEXICON["register_button"])

button_cs_choose = KeyboardButton(text=LEXICON["cs_game_button"])
button_dota_choose = KeyboardButton(text=LEXICON["dota_game_button"])
button_back = KeyboardButton(text=LEXICON["back_button"])

button_solo_choose = KeyboardButton(text=LEXICON["solo_button"])
button_team_choose = KeyboardButton(text=LEXICON["team_button"])


main_keyboard_builder = ReplyKeyboardBuilder()
main_keyboard_builder.row(button_register)

main_keyboard: ReplyKeyboardBuilder = main_keyboard_builder.as_markup(
    resize_keyboard = True
)


main_game_keyboard_builder = ReplyKeyboardBuilder()
main_game_keyboard_builder.row(button_cs_choose, button_dota_choose, button_back, width=2)

main_game_keyboard: ReplyKeyboardBuilder = main_game_keyboard_builder.as_markup(
    resize_keyboard = True
)


main_team_or_solo_keyboard_builder = ReplyKeyboardBuilder()
main_team_or_solo_keyboard_builder.row(button_solo_choose, button_team_choose, button_back, width=2)

main_team_or_solo_keyboard: ReplyKeyboardBuilder = main_team_or_solo_keyboard_builder(
    resize_keyboard = True
)