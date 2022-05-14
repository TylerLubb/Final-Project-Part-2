#https://www.youtube.com/watch?v=iJ01q-sRJAw&ab_channel=NeuralNine
#Added gui and more advanced scoring
#Made it so if the password is strong enough, it takes you to a new page

possible_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

possible_capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

possible_symbols = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', ',', '.' '/', ':', ';' '<', '=', '>', '?',
                    '@', '[', '[', ']', '^', '_', '{', '|', '}', '~']


def status(p):
    password = p
    score = 0
    length = len(password)
    password_status = ''
    password_status1 = ''

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

    score += (total_digits / 2)
    score += (total_letters / 2)
    score += (total_symbols / 2)

    if length >= 8:
        if length <= 20:
            score += ((length - 8) / 2)
            if int(score) < 3:
                password_status = 'too weak'
            elif int(score) >= 3 and int(score) < 5:
                password_status = 'passable strength'
            elif int(score) >= 5 and int(score) < 7:
                password_status = 'moderate strength'
            else:
                password_status = 'strong'
        else:
            password_status = 'too long'

    else:
        password_status = 'too short'
    return password_status