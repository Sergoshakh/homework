def send_email(message, recipient,*, sender='university.help@gmail.com'):
    recipient = recipient.lower()
    sender = sender.lower()
    
    if recipient.count('@') == 1:
        if recipient[-1:-4:-1] == 'ur.' or recipient[-1:-5:-1] == 'moc.' or recipient[-1:-5:-1] == 'ten.':
            if sender == recipient:
                print('Невозможно отправить письмо самому себе!')
                return
            if sender == 'university.help@gmail.com':
                print(f'Письмо c текстом "{message}" успешно отправлено с адреса "{sender}" на адрес "{recipient}"')
            else:
                if sender.count('@') == 1:
                    if sender[-1:-4:-1] == 'ur.' or sender[-1:-5:-1] == 'moc.' or sender[-1:-5:-1] == 'ten.':
                        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо с текстом "{message}" отправлено с адреса "{sender}" на адрес "{recipient}"')
                    else:
                        print(f'Невозможно отправить письмо с адреса "{sender}"')
                        return       
                else:
                   print(f'Невозможно отправить письмо с адреса "{sender}"')
                   return       
            return
        else:
            print(f'Некорректно введён адрес получателя "{recipient}"')
            return       
    else:
        print(f'Некорректно введён адрес получателя "{recipient}"')
        return

print('    * * *')
print('')
list_ = send_email('Проверка связи!', 'Sergo@mAil.com')
print('')
list_ = send_email('Проверка связи!', 'Sergo@@mAil.com')
print('')
list_ = send_email('Проверка связи!', 'SergomAil.com')
print('')
list_ = send_email('Проверка связи!', 'Sergo@mAil.org')
print('')
list_ = send_email('Просто привет!', 'university.help@gmail.com')
print('')
list_ = send_email('Просто привет от куратора!', 'Sergo@mAil.ru', sender='university.curator@gmail.com')
print('')
list_ = send_email('Просто привет!', 'Sergo@mAil.com', sender='unknown.sender@mail.uk')
print('')
print('End of lesson')
