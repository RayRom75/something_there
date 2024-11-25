#!/usr/bin/env python3

def proverka_email(email, domeny=(".com", ".ru", ".net")):
    at_symbol = email.count("@")

    if (at_symbol != 1):
        return False

    sub_domen = email.split("@")[1]
    if not sub_domen.endswith(domeny):
        return False

    return True

def send_email(message, recipient, sender="university.help@gmail.com"):
    recipient = recipient.lower()
    sender = sender.lower()

    if not proverka_email(recipient) or not proverka_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
