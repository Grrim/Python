# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:54:41 2023
@author: HP
"""

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random

def IV():
    ivArr = bytearray(16)
    for i in range(16):
        ivArr[i] = random.randint(0, 255)
    return bytes(ivArr)

def Encryption(plainText, key, iv):
    padding = pad(plainText, AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padding)
    print(ciphertext)
    return ciphertext

def Decryption(cipherText, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(cipherText)
    return is_valid_padding(decrypted_data)

def is_valid_padding(data):
    try:
        # Próbujemy odzyskać padding; unpad() zostanie uruchomione tylko, jeśli padding jest poprawny
        unpad(data, AES.block_size)
        return True
    except ValueError:
        # W przypadku błędnego paddingu zgłaszamy wyjątek
        return False
   
def get_intermediate_state(cipherText, key, iv, block_index):
    decipher = AES.new(key, AES.MODE_CBC, iv)
    last_block = cipherText[block_index * 16:(block_index + 1) * 16]
    intermediate_state = decipher.decrypt(last_block)
    return intermediate_state

def split_blocks(data):
    length = len(data)
    blocks = []
    for i in range(length // 16):
        blocks.append(data[i * 16:(i + 1) * 16])
    return blocks

def find_last_byte(ciphertext):
    ciphertext = bytearray(base64.b64decode(ciphertext))
    blocks = split_blocks(ciphertext)
    
    c_prime = bytearray([b for b in blocks[0]])
    
    plaintext_bytes = bytearray(0 for _ in range(16))
    
    for i in range(16):
        
        excepted_padding =  bytearray([0 for _ in range(16 - i)] + [(i + 1) for _ in range(i)])
        
        for byte in list(range(blocks[0][15-i] + 1, 256)) + list(range(0, blocks[0][15-i] + 1)):
            c_prime[15-i] = byte
            to_test = base64.b64encode(c_prime + blocks[1])
            
            try:
                if Decryption(base64.b64decode(to_test), key, iv):
                    plaintext_bytes = (byte ^ 0x01 ^ blocks[0][15])
                    break
            except ValueError:
                pass

    print(''.join([chr(b) for b in plaintext_bytes if b > 16]))


key = IV()
iv = IV()

text = "abcdefghijklmnoabcdefghijklmnop"

cipherText = Encryption(text.encode(), key, iv)
print(cipherText)
print(find_last_byte(base64.b64encode(cipherText)))  # Odpalamy funkcję z base64 zakodowanym ciphertextem
