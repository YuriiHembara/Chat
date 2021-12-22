def myencode(message):
    result = ''
    alfavit = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ' \
               'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' \
               '1234567890*()-=+/!@#:;'
    krok = 5
    for i in message:
        place = alfavit.find(i)
        new_place = place + krok
        if i in alfavit:
            result += alfavit[new_place]
        else:
            result += i
    return(result)
def mydecode(message):
    result = ''
    alfavit = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ' \
               'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' \
               '1234567890*()-=+/!@#:;'
    krok = -5
    for i in message:
        place = alfavit.find(i)
        new_place = place + krok
        if i in alfavit:
            result += alfavit[new_place]
        else:
            result += i
    return(result)


