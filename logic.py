import string

possible_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

possible_capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

possible_symbols = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', ',', '.' '/', ':', ';' '<', '=', '>', '?',
                    '@', '[', '[', ']', '^', '_', '{', '|', '}', '~']


def password_check(p):
    password = p

    uppercase = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lowercase = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    characters = [uppercase, lowercase, special, digits]

    print(special)

    length = len(password)
    total_digits = 0
    total_letters = 0
    total_symbols = 0

    for p in password:
        if p in possible_digits:
            total_digits += 1
        if p in possible_capletters:
            total_letters += 1
        if p in possible_symbols:
            total_symbols += 1

    score = 0

    score += (total_digits / 2)
    score += (total_letters / 2)
    score += (total_symbols / 2)

    if length >= 8:

        if length <= 20:
            score += ((length - 8) / 2)
        else:
            print('Recommend shortening password')
            score -= (length - 8)
    else:
        print('password is too short')

    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1

    print(f'score is {int(score)}')

    password_status = ' '

    if int(score) < 4:
        password_status = 'Password is too weak'
    elif int(score) >= 4 and int(score) < 8:
        password_status = 'Password is passable strength'
    elif int(score) >= 8 and int(score) < 12:
        password_status = 'passowrd is moderate strength'
    else:
        password_status = 'password is strong'

    return password_status

if