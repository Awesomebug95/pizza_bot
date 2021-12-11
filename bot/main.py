import logging

from aiogram import executor, types

from config import dp
from states import lump


PIZZA_SIZE = ['большую', 'маленькую']
TYPE_OF_PAYMENT = ['наличкой', 'картой']
CONFIRM_ORDER = ['да']

SIZE_QUESTION = 'Какую вы хотите пиццу? Большую или маленькую?'
PAYMENT_QUESTION = 'Как вы будете платить?'

CONFIRMATION_MESSAGE = 'Спасибо за заказ'


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(SIZE_QUESTION)


@dp.message_handler(content_types=["text"])
async def order_pizza(message: types.Message):
    client_answer = message.text.lower()
    if client_answer in PIZZA_SIZE:
        lump.pizza_size(size=client_answer)
        await message.answer(PAYMENT_QUESTION)

    if client_answer in TYPE_OF_PAYMENT:
        lump.payment_method(payment=client_answer)
        await message.answer(text=lump)

    if client_answer in CONFIRM_ORDER:
        lump.confirm_order()
        await message.answer(CONFIRMATION_MESSAGE)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(__file__ + '.log')
        ],
        format='%(asctime)s, %(levelname)s, %(name)s, %(lineno)s, %(message)s,'
    )
    executor.start_polling(dp, skip_updates=True)

