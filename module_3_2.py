def send_email(message, recipient, sender = "university.help@gmail.com"):
    list_no = ['@', '.com', '.ru','.net']
    count = 0

    for i in list_no:
        if i in recipient:
            count += 1
    for k in list_no:
        if k in sender:
            count += 1

    if count < 4 :
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    else:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
