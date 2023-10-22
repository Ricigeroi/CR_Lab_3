import string

import encrypt
import decrypt


def check_input(user_input):
    user_input = user_input.split()
    if len(user_input) == 3:
        mode, text, key = user_input[0], user_input[1], user_input[2]

        if mode in ['e', 'd']:
            if text.isalpha():
                if key.isalpha() and len(key) >= 7:
                    return mode, text, key
                else:
                    print("Invalid key format")
            else:
                print("Invalid text format")
        else:
            print("Invalid mode (encrypt/decrypt)")

    print('Invalid input error.')
    raise TypeError

print('\n\n\n')
print('CR Laboratory #3: Playfair algorithm')
print('====================================')
print('To ENCRYPT enter:')
print('\t\te <text> <key>')

print('To DECRYPT enter:')
print('\t\td <text> <key>')

print("\n<text> contains only 'a'-'z' and 'A'-'Z' \n<key> length >= 7")
print('====================================')
user_input = str(input('>>> '))

mode, text, key = check_input(user_input)

if mode == 'e':
    print(encrypt.encrypt_playfair(text, key))
else:
    print(decrypt.decrypt_playfair(text, key))


