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
    print(padding)
    return ciphertext

def Decryption(cipherText, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(cipherText), AES.block_size)
    return decrypted_data

def get_intermediate_state(cipherText, key, iv, block_index):
    decipher = AES.new(key, AES.MODE_CBC, iv)
    last_block = cipherText[block_index * 16:(block_index + 1) * 16]
    intermediate_state = decipher.decrypt(last_block)
    return intermediate_state

def is_valid_padding(data):
    try:
        # Próbujemy odzyskać padding; unpad() zostanie uruchomione tylko, jeśli padding jest poprawny
        unpad(data, AES.block_size)
        return True
    except ValueError:
        return False

key = b'\xbe\xcc\xe7\x85\xc2a\x8d\xed\xf5\xc4\xdb6\xc3\xa8#W'
iv = b'\xc1\xf7\x80G\x17\x03\x9b\xfb\xadl\xd8\x82H=h\x0b'

text = "Kryptologia semestr zimowy 2021/2022, znowu stacjonarnie w 119 WI2 :) :)"
cipherText = Encryption(text.encode(), key, iv)
# Konwertuj zaszyfrowany tekst na reprezentację szesnastkową w blokach 16 bajtów
cipherText_hex_blocks = [cipherText[i:i+16].hex() for i in range(0, len(cipherText), 16)]

# Wyświetl zaszyfrowany tekst w formie bloków heksadecymalnych
for block in cipherText_hex_blocks:
    print(block)

block_index = len(cipherText) // 16 - 1  # Ostatni blok

# Pobieranie stanu pośredniego ostatniego bloku
intermediate_state = get_intermediate_state(cipherText, key, iv, block_index)

# Operacja XOR z wartościami od 0 do 255
valid_padding_values = []
for i in range(256):
    modified_state = bytes([intermediate_state[0] ^ i]) + intermediate_state[1:]
    modified_block = AES.new(key, AES.MODE_CBC, iv).encrypt(modified_state)
    modified_ciphertext = (
        cipherText[:block_index * 16] +
        modified_block +
        cipherText[(block_index + 1) * 16:]
    )
    if is_valid_padding(modified_ciphertext):
        valid_padding_values.append(i)

print("Wartości z poprawnym paddingiem:", valid_padding_values)
