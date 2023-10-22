import string
import encrypt
import decrypt


def check_input_mode(s):
    if s in ['e', 'd']:
        return s
    print("Invalid mode (encrypt/decrypt)")
    raise TypeError


def check_text(s):
    s = encrypt.remove_spaces(s)
    if s.isalpha():
        return s
    print("Invalid input text")
    print("\n<text> contains only 'a'-'z' and 'A'-'Z'")
    raise TypeError


def check_key(s):
    s = encrypt.remove_spaces(s)
    if s.isalpha() and len(s) >= 7:
        return s
    print("Invalid key")
    print("<key> contains only 'a'-'z' and 'A'-'Z' and key length >= 7")
    raise TypeError


print('CR Laboratory #3: Playfair algorithm')
print('====================================')
print("To ENCRYPT enter 'e'")
print("To DECRYPT enter 'd'")


mode = check_input_mode(str(input('\n>>> ')))
text = check_text(str(input("Enter plain text: ")))
key = check_key(str(input("Enter key: ")))
print('====================================')
if mode == 'e':
    print(encrypt.encrypt_playfair(text, key))
else:
    print(decrypt.decrypt_playfair(text, key))


