import re
from LiteVkApi import Client
import pyautogui
import pyscreeze
from time import sleep
token = '' #bot token
groupID = 0000000 #Group with bot
vk_session = Client.login(token, groupID)
while True:
    if vk_session.check_new_msg():
        event = vk_session.get_event()
        eventxt, userid = event.text, event.user_id
        exists_cords = re.match(r'\d*\.\d*', eventxt)
        if exists_cords != None:
            try:
                cords = exists_cords.group(0).split('.')
                print(cords)
                pyautogui.click(int(cords[0]), int(cords[1]))
                sleep(0.7)
                my_screen = pyscreeze.screenshot()
                my_screen.save('./screen.png')
                vk_session.send_photo(file_names = ('./screen.png'), userid = userid, msg = 'Спасибо<3')
            except Exception:
                vk_session.msg('Слишком большая координата', userid)
        if eventxt == 'Начать':
            vk_session.msg('Это бот, который кликает по экрану по заданным координатам [x,y]', userid)