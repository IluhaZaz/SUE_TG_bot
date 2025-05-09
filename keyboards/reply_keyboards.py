from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON
from lexicon.commands import COMMANDS

button_register = KeyboardButton(text=LEXICON["register_button"])

button_cs_choose = KeyboardButton(text=LEXICON["cs_game_button"])
button_dota_choose = KeyboardButton(text=LEXICON["dota_game_button"])
button_back = KeyboardButton(text=LEXICON["back_button"])

button_solo_choose = KeyboardButton(text=LEXICON["solo_button"])
button_team_choose = KeyboardButton(text=LEXICON["team_button"])

button_add_teammate = KeyboardButton(text=LEXICON["add_teammate_button"])
button_team_done = KeyboardButton(text=LEXICON["team_done_button"])

button_stop_fsm = KeyboardButton(text=COMMANDS["/cancel"])

button_yes_stop = KeyboardButton(text=LEXICON["yes_stop_button"])
button_no_stop = KeyboardButton(text=LEXICON["no_stop_button"])

main_keyboard_builder = ReplyKeyboardBuilder()
main_keyboard_builder.row(button_register)

main_keyboard: ReplyKeyboardMarkup = main_keyboard_builder.as_markup(
    resize_keyboard = True
)


main_game_keyboard_builder = ReplyKeyboardBuilder()
main_game_keyboard_builder.row(button_cs_choose, button_dota_choose, button_back, width=2)

main_game_keyboard: ReplyKeyboardMarkup = main_game_keyboard_builder.as_markup(
    resize_keyboard = True
)


main_team_or_solo_keyboard_builder = ReplyKeyboardBuilder()
main_team_or_solo_keyboard_builder.row(button_solo_choose, button_team_choose, button_back, width=2)

main_team_or_solo_keyboard: ReplyKeyboardMarkup = main_team_or_solo_keyboard_builder.as_markup(
    resize_keyboard = True
)

teammates_keyboard_builder = ReplyKeyboardBuilder()
teammates_keyboard_builder.row(button_add_teammate, button_team_done, button_back, width=2)

teammates_keyboard: ReplyKeyboardMarkup = teammates_keyboard_builder.as_markup(
    resize_keyboard = True
)


button_stop_fsm_builder = ReplyKeyboardBuilder()
button_stop_fsm_builder.row(button_stop_fsm)

main_cancel_registration_keyboard: ReplyKeyboardMarkup = button_stop_fsm_builder.as_markup(
    resize_keyboard = True
)


button_agree_fsm_builder = ReplyKeyboardBuilder()
button_agree_fsm_builder.row(button_yes_stop, button_no_stop, width=2)

main_cancel_registration_choice_keyboard: ReplyKeyboardMarkup = button_agree_fsm_builder.as_markup(
    resize_keyboard = True
)