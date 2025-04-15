# def verification(login, password, success, failure):
#     latin_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#     text = ['в пароле нет ни одной буквы', 'в пароле нет ни одной заглавной буквы',
#             'в пароле нет ни одной строчной буквы', 'в пароле нет ни одной цифры']
#     check = [any(map(lambda x: x in latin_letters, password)), any(map(lambda x: x.isupper() and x in latin_letters, password)),
#              any(map(lambda x: x.islower() and x in latin_letters, password)), any(map(lambda x: x.isdigit(), password))]
#     if all(check):
#         return success(login)
#     else:
#         return failure(login, text[check.index(False)])


def verification(login, password, success, failure):
    vd = {str.isalpha: 'в пароле нет ни одной буквы',
          str.islower: 'в пароле нет ни одной строчной буквы',
          str.isupper: 'в пароле нет ни одной заглавной буквы',
          str.isdigit: 'в пароле нет ни одной цифры'}
    for f in vd:
        if not any(f(i) for i in password):
            return failure(login, vd[f])
    success(login)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)
