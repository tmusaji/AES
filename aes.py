from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os


def generate_key():
    return get_random_bytes(32)  


def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    

    with open(input_file, 'rb') as f:
        file_data = f.read()

    
    padded_data = pad(file_data, AES.block_size)

    
    encrypted_data = cipher.encrypt(padded_data)
    
    
    with open(output_file, 'wb') as f:
        f.write(cipher.iv)  
        f.write(encrypted_data)

    print(f"File encrypted successfully, saved as {output_file}")

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  
        encrypted_data = f.read()


    cipher = AES.new(key, AES.MODE_CBC, iv)

    
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)


    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

    print(f"File decrypted successfully, saved as {output_file}")


if _name_ == "_main_":
    key = generate_key()

    input_file = 'example.txt'  
    encrypted_file = 'example_encrypted.bin'
    decrypted_file = 'example_decrypted.txt'

    
    encrypt_file(input_file, encrypted_file, key)
    decrypt_file(encrypted_file, decrypted_file, key)
