import re

def check(mail):
    if  '@' in mail and '.' in mail:
        if re.fullmatch(r'[a-zA-Z0-9@.]+', mail):
            print('ДА')
        else:
            print('НЕТ')
    else:
        print('НЕТ, MAYBY')

check(input())