from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboard.client_cb import cancel_markup


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    price = State()
    desc = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.photo.set()
        await message.answer(f" welcome to restaurant {message.from_user.first_name} "
                             f"send your photo of food...",
                             reply_markup=cancel_markup)
    else:
        await message.answer("baeaeach write in dm !")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("give me name of food ", reply_markup=cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("how much?", reply_markup=cancel_markup)


async def load_price(message: types.Message, state: FSMContext):
    try:
        if not 0 < int(message.text) < 100000:
            await message.answer("BITCH GIVE ME NORMAL PRICE!")
        else:
            async with state.proxy() as data:
                data['price'] = int(message.text)
            await FSMAdmin.next()
            await message.answer("describe your wonderful food?", reply_markup=cancel_markup)
    except:
        await message.answer("BITCH GIVE ME NORMAL PRICE!!!!!!!!!!!")


async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"{data['name']}, {data['price']}, {data['desc']}")
    await state.finish()
    await message.answer("done!")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("FUCK YOU!")


def register_handlers_fsm_menu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(load_desc, state=FSMAdmin.desc)


