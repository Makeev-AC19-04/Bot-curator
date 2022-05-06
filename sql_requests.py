from mysql.connector import connect # Библиотека, отвечающая за взаимодействие с базой данных


def SendFaqMsg(): # Функция для формирования списка вопросов
    faqmsg='' # Формируемый текст для будущей отправки
    with connect( # Подключение к БД
	host = 'Tapok1337.mysql.pythonanywhere-services.com', # Имя хоста
	user = 'Tapok1337', # Имя пользователя
	password = 'irFNcv6xWPkFh!a',) as connection: # Пароль
    	selectfaq = 'SELECT * FROM Tapok1337$BotDB.faq;' # Выбираем все вопросы и ответы из таблицы
    	with connection.cursor() as cursor:
    		cursor.execute(selectfaq) # Выполняем команду и получаем данные из БД
    		for i in cursor:
    			faqmsg+=('в: ' + i[0] + '\n') # К вопросам относятся первые элементы строки,
    			faqmsg+=('о: ' + i[1] + '\n\n') # К ответам - вторые элементы строки
    return faqmsg


def AddFaq(question): # Обработчик новых вопросов (добавление нового вопроса/ответа в БД)
    with connect(
	host = 'Tapok1337.mysql.pythonanywhere-services.com',
	user = 'Tapok1337',
	password = 'irFNcv6xWPkFh!a',) as connection:
        addfaq = 'INSERT INTO Tapok1337$BotDB.faq (Question, Answer) VALUES ("' + question.split(': ')[1][:-2] + '", "' + question.split(': ')[2] + '")' # Формируем команду для БД
        with connection.cursor() as cursor:
            cursor.execute(addfaq) # Выполняем команду в среде БД
        connection.commit() # Фиксируем изменения в БД


def SendReviews(): # Формирование списка отзывов
    revmsg=''
    with connect(
    host = 'Tapok1337.mysql.pythonanywhere-services.com',
	user = 'Tapok1337',
	password = 'irFNcv6xWPkFh!a',) as connection:
	    selectrevs = 'SELECT * FROM Tapok1337$BotDB.reviews;'
	    with connection.cursor() as cursor:
	        cursor.execute(selectrevs)
	        for i in cursor:
	            revmsg+=('Дата: ' + str(i[1]) + '\n')
	            revmsg+=('Отзыв: ' + i[0] + '\n\n')
    return revmsg


def AddReview(review): # Обработчик новых вопросов (добавление нового отзыва в БД)
    with connect(
	host = 'Tapok1337.mysql.pythonanywhere-services.com',
	user = 'Tapok1337',
	password = 'irFNcv6xWPkFh!a',) as connection:
	    addrev = "INSERT INTO Tapok1337$BotDB.reviews (review, revdate) VALUES ('" + review + "',CURRENT_DATE())" # Формируем команду для БД
	    with connection.cursor() as cursor:
	        cursor.execute(addrev) # Выполняем команду в среде БД
	        connection.commit() # Фиксируем изменения в БД

def SendContacts(): # Формирование списка контактов старшекурсников
    contactsmsg='Список старшекурсников, которые готовы подробнее рассказать о нашем университете:\n'
    with connect(
    host = 'Tapok1337.mysql.pythonanywhere-services.com',
	user = 'Tapok1337',
	password = 'irFNcv6xWPkFh!a',) as connection:
	    selectcontacts = 'SELECT * FROM Tapok1337$BotDB.contacts;'
	    with connection.cursor() as cursor:
	        cursor.execute(selectcontacts)
	        for i in cursor:
	            contactsmsg+='@id' + str(i[0])
	            return contactsmsg


def AddContact(contact): # Добавление нового контакта в БД
    with connect(
	host = 'Tapok1337.mysql.pythonanywhere-services.com',
	user = 'Tapok1337',
	password = 'irFNcv6xWPkFh!a',) as connection:
	    addcontact = "INSERT INTO Tapok1337$BotDB.contacts (vk_id) VALUES ('" + str(contact) + "');"
	    with connection.cursor() as cursor:
	        cursor.execute(addcontact)
	        connection.commit()


def SendCurators(): # Формирование списка кураторов
    curatorsmsg=''
    with connect(
	host = 'Tapok1337.mysql.pythonanywhere-services.com',
	user = 'Tapok1337',
	password = 'irFNcv6xWPkFh!a',) as connection:
	    curators = 'SELECT * FROM Tapok1337$BotDB.curators;'
	    with connection.cursor() as cursor:
	        cursor.execute(curators)
	        for i in cursor:
	            curatorsmsg+='@' + str(i[0]) + ' \t\t' + str(i[1]) + '\n'
    return curatorsmsg