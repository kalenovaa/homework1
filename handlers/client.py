from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import random



#@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f"приветствую вас госпожа {message.from_user.first_name}")

#@dp.message_handler(commands=['mem'])
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


#@dp.message_handler(commands=["quiz"])
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


async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply('команда должна быть ответов на сообщение')
    else:
        await bot.pin_chat_message(message.chat.id, message.message_id)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')

