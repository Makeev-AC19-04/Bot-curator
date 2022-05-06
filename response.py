import vk # Библиотека для загрузки api от вконтакте
import random # Данная библиотека нужна для генерации random_id (подробнее в https://dev.vk.com/method/messages.send)

session = vk.Session()
api = vk.API(session, v='5.95')

class Response: # Класс посылаемого ботом сообщения
    def __init__(self, message, keyboard):
        self.message = message # Определяем текст сообщения
        self.keyboard = open(r"/home/Tapok1337/mysite/json_buttons/"+keyboard, 'r').read() # Считываем файл клавиатуры как строку. Клавиатуры хранятся в папке
        pass                                                                                # /home/Tapok1337/mysite/json_buttons/, достаточно указать название файла

    def SendResponse(self, token, u_id): # Функция отправки сообщения
            return api.messages.send(access_token=token, user_id=str(u_id), message=self.message, random_id=random.getrandbits(64), keyboard=self.keyboard) # Метод отправки сообщения от vk.api, подробнее: https://dev.vk.com/method/messages.send
