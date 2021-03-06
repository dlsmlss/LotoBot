from telebot import types

from utils import create_payment_link



# ==============================================================
# User Interface

def start_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('🏡 Личный кабинет'))
    markup.row(types.KeyboardButton('🎲 Розыгрыши'))
    markup.row(types.KeyboardButton('📞 Контакты'))

    return markup


def user_help_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('📜 Помощь', callback_data='user_help'))

    return markup


def private_room_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('📥 Пополнить счет'))
    markup.row(types.KeyboardButton('📤 Вывод средств'))
    markup.row(types.KeyboardButton('↩️ Назад'))

    return markup


def raise_money_account_menu(user_id, rubles, kopeck):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('💸 Пополнить!', url=create_payment_link(user_id, rubles, kopeck)))

    return markup


def check_raise_money_account_menu(msg_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🔄 Обновить информацию об оплате', callback_data='check_money_' + str(msg_id)))

    return markup


def create_qiwi_acc_menu(amount, qiwi_acc):
    markup = types.InlineKeyboardMarkup()
    for i in qiwi_acc:
        markup.add(types.InlineKeyboardButton(i, callback_data='pass_qiwi_acc_' + str(amount) + '_' + i),
                   types.InlineKeyboardButton('❌ Удалить', callback_data='delt_qiwi_acc_' + str(amount) + '_'+i))
    markup.add(types.InlineKeyboardButton('💳 Добавить новый кошелёк', callback_data='pass_qiwi_acc_'+str(amount)+'_+0'))

    return markup


def check_save_qiwi_acc_menu(amount, qiwi_acc):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('✅ Да!', callback_data='save_qiwi_acc_' + str(amount) + '_' + qiwi_acc),
               types.InlineKeyboardButton('❎ Нет', callback_data='pass_qiwi_acc_' + str(amount) + '_' + qiwi_acc))

    return markup


def get_started_spoof_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('➡️ Участвовать! ⬅️', callback_data='get_started'))

    return markup




# ==============================================================
# Admin Interface

def start_admin_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('🎲 Розыгрыш'))
    markup.row(types.KeyboardButton('📊 Статистика'))
    markup.row(types.KeyboardButton('↩️ Вернуться в главное меню'))

    return markup


def start_spoof_admin_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('🏁 Завершить розыгрыш'))
    markup.row(types.KeyboardButton('↩️ Назад'))

    return markup


def cancel_spoof_admin_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('❌ Отмена'))

    return markup


def decide_start_spoof_admin_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('🚀 Начать розыгрыш'))
    markup.row(types.KeyboardButton('❌ Отмена'))

    return markup


def end_spoof_without_winners_admin_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('✅ Да ', callback_data='end_without_winners_yes'),
               types.InlineKeyboardButton('❎ Нет', callback_data='end_without_winners_no'))

    return markup