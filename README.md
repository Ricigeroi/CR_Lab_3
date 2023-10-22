# CR_Lab_3: Playfair Cipher Algorithm

This repository contains an implementation of the Playfair cipher algorithm. The Playfair cipher is a manual symmetric encryption technique and was the first literal digraph substitution cipher.

## Files in the Repository

- [`main.py`](https://github.com/Ricigeroi/CR_Lab_3/blob/master/main.py): The main driver script that takes user input for encryption or decryption mode, the text, and the key. It then calls the appropriate functions from the `encrypt.py` or `decrypt.py` files to perform the desired operation.

- [`encrypt.py`](https://github.com/Ricigeroi/CR_Lab_3/blob/master/encrypt.py): Contains functions to encrypt a given plaintext using the Playfair cipher algorithm. It includes functions to generate the key table, search for characters in the key table, and apply the row, column, and rectangle rules of the Playfair cipher.

- [`decrypt.py`](https://github.com/Ricigeroi/CR_Lab_3/blob/master/decrypt.py): Contains functions to decrypt a given ciphertext using the Playfair cipher algorithm. It includes functions to generate the key table, search for characters in the key table, and apply the decryption rules of the Playfair cipher.

## How to Use

1. Run the `main.py` script.
2. Choose the mode (encryption or decryption).
3. Enter the text to be encrypted or decrypted.
4. Enter the key to be used for the encryption or decryption process.
5. The script will display the encrypted or decrypted text.

## Note

Ensure that the text and key provided adhere to the constraints mentioned in the scripts.  
Specifically, the text should contain only romanian letters, the key should contain only alphabetic characters and have a length of at least 7 characters.
