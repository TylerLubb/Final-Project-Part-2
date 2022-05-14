# https://www.youtube.com/watch?v=iJ01q-sRJAw&ab_channel=NeuralNine
# Added gui and more advanced scoring
# Made it so if the password is strong enough, it takes you to a new page

possible_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

possible_capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

possible_symbols = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', ',', '.' '/', ':', ';' '<', '=', '>', '?',
                    '@', '[', '[', ']', '^', '_', '{', '|', '}', '~']


def status(p):
    password = p
    strength = 0
    length = len(password)
    password_status = ''

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

    strength += (total_digits / 2)
    strength += (total_letters / 2)
    strength += (total_symbols / 2)

    if length >= 8:
        if length <= 20:
            strength += ((length - 8) / 2)
            if int(strength) < 3:
                password_status = 'too weak'
            elif int(strength) >= 3 and int(strength) < 5:
                password_status = 'passable strength'
            elif int(strength) >= 5 and int(strength) < 7:
                password_status = 'strong'
            else:
                password_status = 'very strong'
        else:
            password_status = 'too long'
    else:
        password_status = 'too short'
    return password_status


def score(strength):
    for score in strength:
        return score
