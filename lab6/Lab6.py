from Crypto.Cipher import DES3
import random


def examination(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


def encrypt(text, des):
    return des.encrypt(text.encode('utf-8'))


def decrypt(text, des):
    return des.decrypt(text).decode().rstrip('')


def key_generation():
    symbols = list('qwertyuiopasdfghjklzxcvbnm1234567890+-/*.,<>/?\|_!@#$%^&()~')
    key_list = ''
    for i in range(24):
        key_list += random.choice(symbols)
    return bytes(str(key_list), encoding='utf-8')


counter = True
key = key_generation()
while counter:
    mode = input('Enter 1 if you want to encrypt the text: ')
    if mode == '1':
        text = input('Enter the text you want to encrypt: ')
        right_text = examination(text)

        des = DES3.new(key, DES3.MODE_ECB)

        encrypted_text = encrypt(right_text, des)
        output_encrypted_text = input('To display encrypted text enter 1 ')
        if output_encrypted_text == '1':
            print('Encrypted text: ', encrypted_text)

        decrypted_text = decrypt(encrypted_text, des)
        output_decrypted_text = input('To display decrypted text enter 1 ')
        if output_decrypted_text == '1':
            print('Decrypted text: ', decrypted_text)

        text = input('To save key enter 1, to generate new key enter 2: ')
        if text == '2':
            key = key_generation()

    else:
        counter = False
