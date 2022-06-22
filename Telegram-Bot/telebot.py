import django
import os
import respone as r

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

os.environ['DJANGO_SETTINGS_MODULE'] = 'PKOB.settings'
TOKEN = os.getenv('TOKEN')
django.setup()

from telegram.ext import *
from App_Soc.models import *
import re

#API_KEY = '5008641900:AAHjHIJEAt4EsA-eTGR0xjdyYjQ1ImVsuH4'
print('Bot started')

victim = "know about victim"
about = "know about pkob"
web = "know about website"

def start_command(update, context):
    #update.message.reply_text('Type "hi pkob" to get started!')
    buttons = [[KeyboardButton(victim)],[KeyboardButton(about)],[KeyboardButton(web)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to PKOB bot! What you want to know? (You can choose the option from KeyboardbButton)",
                             reply_markup=ReplyKeyboardMarkup(buttons))

def isValidIC(ic_text):
    regex = "(([[0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01]))([0-9]{2})([0-9]{4})";
    p = re.compile(regex)
    if (ic_text == ''):
        return False;
    m = re.match(p, ic_text)
    if m is None:
        return False
    else:
        return True

def handle_message(update, context):
    text = str(update.message.text).lower()
    respone = r.sample_responses(text)
    update.message.reply_text(respone)
#    text = str(update.message.text).lower()
#    ic,phone= text.split(" ")
#
#    if about in update.message.text:
#        update.message.reply_text( f"Pusat Kawalan Operasi Bencana (PKOB) is a system to help victims that suffered from floods disaster in the village Mukim Bujang Merbok, Kedah.")
#
#    if isValidIC(ic):
#            student_list = Question.objects.filter(ic_text=ic,phone_text=phone)
#            message = f""" Detail no found! Please enter again Ic Number and Phone Number. \n \n """
#            for student in student_list:
#                message = f""" This is victim's information: \n \n """
#                message += f"""Kad Pengenalan: {student.ic_text} \n Nombor Telefon: {student.phone_text} \n Nama: {student.name_text} \n Umur: {student.calculate_age()} \n """
#
#            update.message.reply_text(f"{message}")
#            return
#
#    if victim in update.message.text:
#             update.message.reply_text(f"Hi, {update['message']['chat']['first_name']} please enter Ic Number and Phone Number to get victim's information. \n(Example:990302014356 0136754893)")
#
#    if web in update.message.text:
#        update.message.reply_text(
#            f"Hi, {update['message']['chat']['first_name']} this is our website link: \n(https://pkob-272043-bot.herokuapp.com)")


if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling(1.0)
    updater.idle()