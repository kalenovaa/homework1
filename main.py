from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import bot, dp
import logging
import random

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f"приветствую вас госпожа {message.from_user.first_name}")

@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = [
        'ali/1',
        'ali/img2',
        'ali/img3',
        'ali/img4',
        'ali/img5',
        'ali/img6',
        'ali/img7',
        'ali/img8',
        'ali/img9',
        'ali/img10',
        'ali/img11',
        'ali/img12',
        'ali/img13',
        'ali/img14',
        'ali/img15',
        'ali/img16',
        'ali/img17',
        'ali/img18',
        'ali/img19',
        'ali/img20',
    ]

    img=open(random.choice(photo), 'rb')
    await bot.send_photo(message.chat.id, photo=img)


@dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "в чем смысл жизни?"
    answers = [
        'ни в чем',
        'его нет',
        'я хз',
        'вроде есть',
        'да',
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="смысла жизни нет)))",
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
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

    )


@dp.message_handler(content_types=['text', 'photo'])
async def echo(message: types.Message):
    if message.text == "adel":
        await message.answer("это моя госпожа !")
    elif message.text.isdigit():
        await message.reply(int(message.text) * int(message.text))
    else:
        # print(message)
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
