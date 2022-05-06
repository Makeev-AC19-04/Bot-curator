from response import Response # Класс Response отвечает за отправку сообщения
import texts # В файле texts.py хранятся сообщения, отправляемые ботом, и команды, на которые бот будет реагировать
import sql_requests # В файле sql_requests.py хранятся функции, отовечающие за взаимодействие с базой данных


# ___________________________________________________Формируем словарь ответов: ключи к каждому ответу хранятся в texts.py

MenuResponse = Response(texts.MenuText, 'menu.json') # В элемент класса Response передаем текст и клавиатуру, посылаемые ботом

EntranceResponse = Response(texts.EntranceText, 'menu.json')

NotunderstandResponse = Response(texts.NotunderstandText, 'menu.json')

AboutfacultyResponse = Response(texts.AboutfacultyText, 'menu.json')

FaqResponse = Response(sql_requests.SendFaqMsg(), 'menu.json')

NewQuestionResponse = Response(texts.NewQuestionText, 'menu.json')

CommunicateResponse = Response(sql_requests.SendContacts(), 'menu.json')

ReviewResponse = Response(sql_requests.SendReviews(), 'menu.json')

CuratorResponse = Response(sql_requests.SendCurators(), 'menu.json')

GuideResponse = Response(texts.GuideText, 'menu.json')

NewReviewResponse = Response(texts.NewReviewText, 'menu.json')

NewContactResponse = Response(texts.NewContactText, 'menu.json')

Responses = {
texts.Menu0Key: MenuResponse,
texts.Menu2Key:MenuResponse,
texts.EntranceKey: EntranceResponse,
texts.AboutfacultyKey: AboutfacultyResponse,
texts.FaqKey: FaqResponse,
texts.CommunicateKey:CommunicateResponse,
texts.ReviewKey: ReviewResponse,
texts.CuratorKey: CuratorResponse,
texts.NewQuestionKey: NewQuestionResponse,
texts.GuideKey: GuideResponse,
texts.NewReviewKey: NewReviewResponse,
texts.NewContactKey: NewContactResponse
}
# ___________________________________________________

def send_message(user_id, token, message): # Адресация сообщения к соответствующему ответу
    if message.lower()[:37] in Responses: # Если сообщение содержит ключ из словаря ответов, то отправляем ответ, соответствующий ключу
        if message.lower()[:37] == texts.NewQuestionKey: # Если сообщение содержит ключ для записи вопроса, то передаем его в обработчик новых вопросов
            sql_requests.AddFaq(message[38:])
        elif message.lower()[:37] == texts.NewReviewKey: # Если сообщение содержит ключ для записи отзыва, то передаем его в обработчик новых отзывов
            sql_requests.AddReview(message[38:])
        elif message.lower()[:37] == texts.NewContactKey: # Если сообщение содержит ключ для записи контакта, то передаем его в обработчик контактов
            sql_requests.AddContact(user_id) # Сохраняем id пользователя для дальнейшей отправки в список старшекурсников
        Responses[message.lower()[:37]].SendResponse(token, user_id)
    else: # Если сообщение НЕ содержит ключ из словаря ответов, то отправляем ответ, что бот не понял команды
        NotunderstandResponse.SendResponse(token, user_id)
