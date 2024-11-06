from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'012b456749ABCdEF'
iv = b'1234567890AsCDhF'

def Encryption(plainText, key, iv):
    padding = pad(plainText, AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padding)
    print(padding)
    return ciphertext

def Decryption(cipherText, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(cipherText)
    return unpad(decrypted_data, AES.block_size)

def split_blocks(data):
    length = len(data)
    blocks = []
    for i in range(length // 16):
        blocks.append(data[i * 16:(i + 1) * 16])
    return blocks

def xor(ba1, ba2):
    return bytearray([a ^ b for a, b in zip(ba1, ba2)])

def find_bytes(blocks):
    c_prime = bytearray([b for b in blocks[0]])
    plaintext_bytes = bytearray([0 for _ in range(16)])

    for i in range(16):
        expected_padding = bytearray([0 for _ in range(16 - i)] + [(i + 1) for _ in range(i)])
        c_prime = xor(xor(expected_padding, plaintext_bytes), blocks[0])

        for byte in list(range(blocks[0][15 - i] + 1, 256)) + list(range(0, blocks[0][15] + 1)):
            c_prime[15 - i] = byte
            to_test = c_prime + blocks[1]
            try:
                Decryption(to_test, key, iv)
                plaintext_bytes[15 - i] = (byte ^ (i + 1) ^ blocks[0][15 - i])
                break
            except ValueError:
                pass
    return ''.join([chr(b) for b in plaintext_bytes if b > 16])

def find_plain_text(ciphertext):
    ciphertext = bytearray(ciphertext)
    blocks = split_blocks(ciphertext)

    plaintext = ""

    for i in range(len(blocks) - 1):
        plaintext += find_bytes([blocks[i], blocks[i + 1]])
        
    return plaintext

text = "This is a super secret string. For real."
cbc_text = split_blocks(text)
print(cbc_text)
cipherText = Encryption(text.encode(), key, iv)
paddingOracle = find_plain_text(cipherText)
print(paddingOracle)
