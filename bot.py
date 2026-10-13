import asyncio
import aiomax
from aiomax import buttons


# ⚠️ ВСТАВЬТЕ СЮДА ВАШ ТОКЕН
TOKEN = "f9LHodD0cOL-jsenNSZiXeNp0SgAvgcduRi4wpbYCY9_qq_03PkGYMM4xPtuOZdChrnEDCiWOfw7M9kLmCQn"


bot = aiomax.Bot(TOKEN)


@bot.on_bot_start()
async def on_start(payload: aiomax.BotStartPayload):
    """Отправляем приветствие и кнопки главного меню."""
    kb = buttons.KeyboardBuilder()
    kb.row(buttons.CallbackButton("📚 Библиотеки", "menu_libraries"))
    kb.row(buttons.CallbackButton("❓ Частые вопросы", "menu_faq"))
    kb.row(buttons.LinkButton("🎭 Афиша мероприятий", "https://ckd-pn.gosuslugi.ru/afisha/"))

    await payload.send(
        "Добро пожаловать! Я помогу вам с выбором библиотеки, "
        "ответами на вопросы и афишей мероприятий.",
        keyboard=kb
    )


@bot.on_button_callback()
async def handle_callback(callback: aiomax.Callback):
    """Реагируем на нажатия кнопок."""

    if callback.payload == "menu_libraries":
        kb = buttons.KeyboardBuilder()
        kb.add(buttons.CallbackButton("⬅️ Назад в меню", "menu_main"))

        await callback.reply(
            "📚 Раздел «Основная информация о библиотеки»\n\n"
            "Здесь вы можете узнать адреса библиотеки и режим работы.",
            keyboard=kb
        )

    elif callback.payload == "menu_faq":
        kb = buttons.KeyboardBuilder()
        kb.row(buttons.CallbackButton("Имеются ли в Центральной районной библиотеке клубы для людей пожилого возраста, если есть то какие?", "faq_no_ticket"))
        kb.row(buttons.CallbackButton("Можно ли в у Вас отксерокопировать, отсканировать и распечатать   документы?", "faq_get_card"))
        kb.row(buttons.CallbackButton("Можно ли расплатиться платёжной картой за билеты на мероприятия?", "faq_extend_online"))
        kb.row(buttons.CallbackButton("⬅️ Назад в меню", "menu_main"))

        await callback.reply(
            "❓ Частые вопросы\n\n"
            "Выберите интересующий вас вопрос:",
            keyboard=kb
        )

    # ============================================================
    # ОБРАБОТЧИКИ ОТВЕТОВ НА ВОПРОСЫ
    # ============================================================

    elif callback.payload == "faq_no_ticket":
        kb = buttons.KeyboardBuilder()
        kb.add(buttons.CallbackButton("⬅️ К вопросам", "menu_faq"))
        kb.add(buttons.CallbackButton("🔙 В начало", "menu_main"))

        await callback.answer(
            text="Да. В центральной районной модельной библиотеке имеются клубы для  людей пожилого возраста."

        'Клуб любителей русской песни  «Жизнелюб», клуб людей пожилого возраста «Беседа», клуб «Цветовод», клуб любителей поэзии «Лира».',
        keyboard=kb
        )

    elif callback.payload == "faq_get_card":
        kb = buttons.KeyboardBuilder()
        kb.add(buttons.CallbackButton("⬅️ К вопросам", "menu_faq"))
        kb.add(buttons.CallbackButton("🔙 В начало", "menu_main"))

        await callback.answer(

            text="Да можно, но эта услуга платная. Подробнее с положением о платных услугах можно ознакомиться по ссылке:\n"
            "https://ckd-pn.gosuslugi.ru/dokumenty/polozhenie-o-platnyh-uslugah.html",
            keyboard=kb
        )

    elif callback.payload == "faq_extend_online":
        kb = buttons.KeyboardBuilder()
        kb.add(buttons.CallbackButton("⬅️ К вопросам", "menu_faq"))
        kb.add(buttons.CallbackButton("🔙 В начало", "menu_main"))

        await callback.answer(
            text="Можно купить билет по Пушкинской карте на нашем сайте или наличный расчёт.",
            keyboard=kb
        )

    elif callback.payload == "menu_main":
        kb = buttons.KeyboardBuilder()
        kb.row(buttons.CallbackButton("📚 Библиотеки", "menu_libraries"))
        kb.row(buttons.CallbackButton("❓ Частые вопросы", "menu_faq"))
        kb.row(buttons.LinkButton("🎭 Афиша мероприятий", "https://ckd-pn.gosuslugi.ru/afisha/"))

        await callback.reply(
            "Главное меню. Выберите раздел:",
            keyboard=kb
        )


@bot.on_message()
async def echo(message: aiomax.Message):
    """Обрабатываем обычные сообщения."""
    text = message.body.text if message.body and message.body.text else ""

    if text.strip() == "/start":
        kb = buttons.KeyboardBuilder()
        kb.row(buttons.CallbackButton("📚 Библиотеки", "menu_libraries"))
        kb.row(buttons.CallbackButton("❓ Частые вопросы", "menu_faq"))
        kb.row(buttons.LinkButton("🎭 Афиша мероприятий", "https://ckd-pn.gosuslugi.ru/afisha/"))

        await message.reply(
            "Добро пожаловать! Выберите раздел:",
            keyboard=kb
        )
    else:
        await message.reply(text)


if __name__ == "__main__":
    print("Бот запущен...")
    bot.run()