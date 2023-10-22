def to_lower_case(text):
    return text.lower()


# Function to remove all spaces in a string
def remove_spaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText


# Function to group 2 elements of a string
# as a list element
def diagraph(text):
    diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        diagraph.append(text[group:i])

        group = i
    diagraph.append(text[group:])
    return diagraph


# Function to fill a letter in a string element
# If 2 letters in the same string matches
def filler_letter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = filler_letter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k - 1, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = filler_letter(new_word)
                break
            else:
                new_word = text
    return new_word


list1 = ['a', 'ă', 'â', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'î', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 'ș', 't', 'ț', 'u', 'v', 'w', 'x', 'y', 'z']


# Function to generate the 5x5 key square matrix


def generate_key_table(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    comp_elements = []
    for i in key_letters:
        if i not in comp_elements:
            comp_elements.append(i)
    for i in list1:
        if i not in comp_elements:
            comp_elements.append(i)

    matrix = []
    while comp_elements != []:
        matrix.append(comp_elements[:5])
        comp_elements = comp_elements[5:]

    return matrix


def search(mat, element):
    for i in range(6):
        for j in range(5):
            if mat[i][j] == element:
                return i, j


def encrypt_row_rule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c + 1]

    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c + 1]

    return char1, char2


def encrypt_column_rule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 5:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r + 1][e1c]

    char2 = ''
    if e2r == 5:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r + 1][e2c]

    return char1, char2


def encrypt_rectangle_rule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2


def encrypt_by_playfair_cipher(Matrix, plainList):
    cipher_text = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_row_rule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            # Get 2 letter cipherText
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_column_rule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_rectangle_rule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        cipher = c1 + c2
        cipher_text.append(cipher)
    return cipher_text


text_Plain = 'teatru gastronomic'


text_Plain = remove_spaces(to_lower_case(text_Plain))
PlainTextList = diagraph(filler_letter(text_Plain))
if len(PlainTextList[-1]) != 2:
    PlainTextList[-1] = PlainTextList[-1] + 'z'

key = "First Amendment"
print("Key text:", key)
key = remove_spaces(to_lower_case(key))
Matrix = generate_key_table(key, list1)

print("Matrix:")
for item in Matrix:
    print(item)

print("Pairs:", PlainTextList)

CipherList = encrypt_by_playfair_cipher(Matrix, PlainTextList)
CipherText = ""
for i in CipherList:
    CipherText += i
print("CipherText:", CipherText)


