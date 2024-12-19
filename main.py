# перед начало в терминале пишем pip install telebot
import telebot
import buttons
from buttons import extra_menu, main_menu

token = "8108747496:AAHXQtDdLsIsPkEa3ZxKVCYTRwvwvAsf8WY"
# создаем объект бота
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, f"привет этот бот является мини CV ",
                     reply_markup=buttons.main_menu())
    print(user_id)
@bot.message_handler(content_types=['text'])
def message_handler(message):
    if message.text == "Информация обо мне":
        bot.send_message(
            message.chat.id,
            "Выберите, что вас интересует:",
            reply_markup=extra_menu()
        )
    elif message.text == "Проекты создателя":
        bot.send_message(
            message.chat.id,
            "Ваша ссылка на ваш телеграм бот: 'https://t.me/CONVERTsumbot'")
    elif message.text == "Биография":
        bot.send_message(
            message.chat.id,
            '''
             name:Javokhir,
firstname: Uralov,
Age: 21,
six: male''')
    elif message.text == "Образование":
        bot.send_message(
            message.chat.id,
            "Техникум")
    elif message.text == "Назад в главное меню":
        bot.send_message(
            message.chat.id,
            "Выберите, что вас интересует:",
            reply_markup=buttons.main_menu())


# создаем команду для бесконечной работы бота
bot.infinity_polling()
# второй вариант
# bot.polling(non_stop=True)
