# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 00:00:02 2023

@author: HP
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random

# Inicjalizacja klucza AES (128, 192 lub 256 bitów)
def key():
    keyArr = bytearray(16)
    for i in range(16):
        keyArr[i] = random.randint(0, 255)
    return bytes(keyArr)  # AES-128

# Inicjalizacja IV
def IV():
    ivArr = bytearray(16)
    for i in range(16):
        ivArr[i] = random.randint(0, 255)
    return bytes(ivArr)

iv = IV()
key = key()


def Encryption(plainText, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plainText, AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

def Decryption(cipherText, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(cipherText)
    return decrypted_data  # Usuwamy unpad, aby zachować wypełnienie

text = input("Podaj tekst jawny: ")
cipherText = Encryption(text.encode(), key, iv)
print("Zaszyfrowany tekst:", cipherText)

# Usuwa wypełnienie z odszyfrowanych danych
def remove_padding(data):
    padding_length = data[-1]
    return data[:-padding_length]

def padding_oracle(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted_data = cipher.decrypt(ciphertext)
        return True  # Jeśli deszyfrowanie się powiedzie, oznacza to prawidłowe wypełnienie
    except ValueError:
        return False  # Jeśli deszyfrowanie wywołało błąd, oznacza to nieprawidłowe wypełnienie

def padding_oracle_attack(ciphertext, key, iv):
    block_size = AES.block_size
    num_blocks = len(ciphertext) // block_size
    plaintext = bytearray(len(ciphertext))

    for block in range(1, num_blocks):
        modified_ciphertext = bytearray(ciphertext)
        for i in range(block_size):
            for guess in range(256):
                if i == block_size - 1 and guess == 1:
                    continue  # Pomijamy padding 0x01, ponieważ to jest prawidłowe wypełnienie
                modified_ciphertext[block * block_size - i - 1] ^= guess
                if padding_oracle(modified_ciphertext, key, iv):
                    # Znaleźliśmy bajt wypełnienia
                    original_byte = modified_ciphertext[block * block_size - i - 1] ^ (i + 1)
                    plaintext[block * block_size - i - 1] = original_byte
                    for j in range(i):
                        modified_ciphertext[block * block_size - j - 1] ^= i + 2  # Poprawiamy wypełnienie
                    break

    # Odszyfrowany tekst jako czytelny dla ludzi
    decoded_text_str = plaintext.decode('utf-8', errors='ignore')
    try:
        result = unpad(decoded_text_str.encode('utf-8'), AES.block_size)
        print("Odszyfrowane dane:", result.decode('utf-8'))
    except ValueError as e:
        print("Błąd deszyfrowywania:", e)

# Próbuj atakować
padding_oracle_attack(cipherText, key, iv)
