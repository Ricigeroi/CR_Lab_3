def to_lower_case(plain):
    # Convert all the characters of a string to lowercase
    return plain.lower()


def remove_spaces(plain):
    # Remove all spaces in a string
    # can be extended to remove punctuation
    return ''.join(plain.split())


def generateKeyTable(key):
    # generates the 6x5 key square
    key_t = [['' for i in range(5)] for j in range(6)]
    dicty = {'a': 0, 'ă': 0, 'â': 0, 'b': 0, 'c': 0, 'd': 0,
             'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'î': 0,
             'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
             'p': 0, 'r': 0, 's': 0, 'ș': 0, 't': 0, 'ț': 0,
             'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for i in range(len(key)):
        if key[i] != 'q':
            dicty[key[i]] = 2
    dicty['q'] = 1

    i, j, k = 0, 0, 0
    while k < len(key):
        if dicty[key[k]] == 2:
            dicty[key[k]] -= 1
            key_t[i][j] = key[k]
            j += 1
            if j == 5:
                i += 1
                j = 0
        k += 1

    for k in dicty.keys():
        if dicty[k] == 0:
            key_t[i][j] = k
            j += 1
            if j == 5:
                i += 1
                j = 0

    return key_t


def search(key_t, a, b):
    # Search for the characters of a digraph in the key square and return their position
    arr = [0, 0, 0, 0]

    if a == 'q':
        a = 'u'
    elif b == 'q':
        b = 'u'

    for i in range(6):
        for j in range(5):
            if key_t[i][j] == a:
                arr[0], arr[1] = i, j
            elif key_t[i][j] == b:
                arr[2], arr[3] = i, j

    return arr


def mod5(a):
    # Function to find the modulus with 5
    if a < 0:
        a += 5
    return a % 5


def mod6(a):
    # Function to find the modulus with 6
    if a < 0:
        a += 6
    return a % 6


def decrypt(cipher_text, key_t):
    # Function to decrypt
    ps = len(cipher_text)
    i = 0
    while i < ps:
        coords = search(key_t, cipher_text[i], cipher_text[i + 1])
        if coords[0] == coords[2]:
            cipher_text = cipher_text[:i] + key_t[coords[0]][mod5(coords[1] - 1)] + key_t[coords[0]][mod5(coords[3] - 1)] + cipher_text[i + 2:]
        elif coords[1] == coords[3]:
            cipher_text = cipher_text[:i] + key_t[mod6(coords[0] - 1)][coords[1]] + key_t[mod6(coords[2] - 1)][coords[1]] + cipher_text[i + 2:]
        else:
            cipher_text = cipher_text[:i] + key_t[coords[0]][coords[3]] + key_t[coords[2]][coords[1]] + cipher_text[i + 2:]
        i += 2

    return cipher_text


def decrypt_playfair(text, key):
    print("Plain text:", text)
    print("Key text: ", key)

    key = remove_spaces(to_lower_case(key))
    user_input = remove_spaces(to_lower_case(text))
    key_t = generateKeyTable(key)

    print('Matrix:')
    for item in key_t:
        print(item)

    # encrypt using Playfair Cipher
    return decrypt(user_input, key_t)



