import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile

TOKEN = ("8290403667:AAH-gsZiw4PI17fTdv3OV-2wIFk9zD6Bf_E")

dp = Dispatcher()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍔 menu"), KeyboardButton(text="🏢 kompaniya xaqida")],
        [KeyboardButton(text="🗣 yangiliklar"), KeyboardButton(text="📞 qo'ng'iroq uchun")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def command_start_handler(message: Message):

    user_name = message.from_user.full_name
    await message.answer(
        f"Assalomu aleykum, {html.bold(user_name)}! EVOS botiga xush kelibsiz.\nNimadan boshlaymiz?",
        reply_markup=main_menu
    )

@dp.message()
async def menu_handler(message: Message):

    text = message.text

    if text == "🍔 menu":
        await message.answer("https://evos.uz/ru", caption="EVOS — доставка еды в Ташкенте" \
        "Лаваш, шаурма, бургеры и комбо от EVOS"
        ". Заказывайте онлайн с доставкой по Ташкенту.")
    elif text == "🏢 kompaniya xaqida":
        await message.answer_photo(
        photo=FSInputFile("photo_2024-11-23_12-31-53.jpg"),
        caption="Информация о компании:Сеть ресторанов быстрого обслуживания EVOS® не стоит на месте, а постоянно растет и развивается вместе с вами и для вас! Мы расширяем свою географию и открываем новые филиалы практически каждый месяц. Сейчас в нашей сети насчитывается более 80 филиалов по всему Узбекистану. Поэтому мы всегда в поиске динамичных и активных людей, которые хотят стать частью нашей команды и готовы строить свою карьеру в EVOS®. EVOS® – это надежный бренд, которому доверяют. Работа в EVOS® – гарантия стабильного заработка и перспективы карьерного роста. Начни свою карьеру в EVOS® уже сейчас!"
    )
    elif text == "🗣 yangiliklar":
        await message.answer("Kompaniya yangiliklari-AksiyaYangi, filiallarYangi tortlar va hk.")

    elif text == "📞 qo'ng'iroq uchun":
        await message.answer_photo(
            photo=FSInputFile("photo_2024-11-23_12-31-53.jpg"),
            caption=(
                "📍 Адрес: ул. Фурката 175, 1 подъезд,\n"
                "📍 Ориентир: MAKRO THE TOWER\n"
                "📲 Контакты: +998 71 203 12 12"
            )
        )
        await message.answer("Iltimos, o'zingizga kerak bo'lgan tugmani bosing")







































async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())