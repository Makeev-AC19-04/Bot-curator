from flask import Flask, request
import json
import MessageHandler # Обработчик сообщений
token = '28969a13367e55a0efd55bcbc148db27dec17f6030191024f3c67f71484cf83cce04b154ae1b84a9037e7' # Токен бота
confirmation_token = '925c0dda' # Токен для подтверждения работоспособности бота для VK

app = Flask(__name__)

@app.route('/')                 # Проверка работоспособности сервера: при переходе
def hi_world():                 # на https://tapok1337.pythonanywhere.com/ выведет строку:
    return 'Сервер работает!'


@app.route('/', methods=['POST']) #Обработчик запросов от вк
def processing():
    data = json.loads(request.data) # Формируем словарь из POST запроса
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation': # На запрос-подтверждение возвращает токен для подтверждения
        return confirmation_token
    elif data['type'] == 'message_new': # На запрос о новом сообщении передаем его в обработчик сообщений
        MessageHandler.send_message(data['object']['from_id'], token, data['object']['text'])
        return 'ok'