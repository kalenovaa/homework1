from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "лучшая дорама?"
    answers = [
        "алые сердца коре",
        "деловое предложение",
        "я не знаю",
        "псих но все в порядке",
        "потомки солнца",
        "пентхаус",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):

    question = "сколько хромосом у взрослого человека?"
    answers = [
        "46",
        "47",
        "45",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,


    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
