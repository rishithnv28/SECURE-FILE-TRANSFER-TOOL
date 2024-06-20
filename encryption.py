from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import os

def read_key():
    password = b"supersecretpassword"
    salt = os.urandom(16)
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    return key

def encrypt_file(file_path, encrypted_file_path, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + ciphertext)

def decrypt_file(encrypted_file_path, decrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(decrypted_file_path, 'wb') as f:
        f.write(plaintext)
