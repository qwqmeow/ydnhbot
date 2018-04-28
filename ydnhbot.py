#!/usr/bin/env python
# coding:utf-8
import sys
import shutil
import logging
import os
from compound_images import compound_image

import telebot
import requests

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

reload(sys)
sys.setdefaultencoding('utf8')


start_text = """
发送要合成的图片,以图片方式发送,在caption写上对话框要填的字（最多三个字，多了装不下，比如写“大佬了”，对话框就会填上“大佬了”）
"""

TOKEN = '<bot token>'
bot = telebot.TeleBot(TOKEN)
cwd = os.getcwd()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):

    bot.send_message(msg.chat.id, start_text)


@bot.message_handler(func=lambda m: True)
def send_welcome(msg):

    if not msg.photo == 'None':
        bot.send_message(msg.chat.id, start_text)
        return


@bot.message_handler(content_types=['photo'])
def img(msg):
    if not msg.chat.type == 'private':
        return

    print str(msg)
    photo = msg.photo
    text = msg.caption

    if len(photo) == 2:
        small_img_file_id = photo[0].file_id
        big_img_file_id = photo[1].file_id
    else:
        big_img_file_id = photo[0].file_id

    big_img_file_path = bot.get_file(file_id=big_img_file_id).file_path
    input_file_name = big_img_file_path.split('/')[-1]

    input_file_url = 'https://api.telegram.org/file/bot{}/{}'.format(
        TOKEN, big_img_file_path)
    print input_file_url
    response = requests.get(input_file_url, stream=True)

    with open(input_file_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print '\n[*] input image saved!'

    compound_image(input_file_name, text)
    print '\n[*] out image finish!'
    os.remove(cwd+'/{}'.format(input_file_name))

    out_file = 'out.png'

    with open(cwd+'/{}'.format(out_file), 'rb') as f:
        bot.send_photo(msg.chat.id, photo=f)


bot.polling(True)
