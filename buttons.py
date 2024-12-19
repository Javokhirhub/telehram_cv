from telebot import types

def main_menu():
    # создаем пространство для кнопок
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # создаем кнопки

    button1 = types.KeyboardButton(text="Информация обо мне")

    button2 = types.KeyboardButton(text="Проекты создателя")

    # добавляем кнопку в пространство
    kb.add(button1, button2)
    return kb
def extra_menu():

    k = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1_1 = types.KeyboardButton(text="Биография")
    button1_2 = types.KeyboardButton(text="Образование")
    button1_3 = types.KeyboardButton(text="Назад в главное меню")
    k.add(button1_1, button1_2, button1_3)
    return k