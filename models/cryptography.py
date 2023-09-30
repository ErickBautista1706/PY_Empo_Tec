from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64
import os

KEY_FILE = "key.txt"  # Nombre del archivo donde se almacenará la clave

class Cryptography:
    def __init__(self):
        self.key_length = 256
        self.key = self._load_or_generate_key()
        
    def print_key(self):
        print("Key:", self.key)
    
    def _generate_key(self):
        key = get_random_bytes(self.key_length // 8)
        return key

    def _store_key(self, key):
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

    def _load_or_generate_key(self):
        if os.path.exists(KEY_FILE):
            with open(KEY_FILE, "rb") as key_file:
                key = key_file.read()
        else:
            key = self._generate_key()
            self._store_key(key)
        return key

    def encrypt_data(self, data):
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
        encrypted_data = base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decoded_data = base64.b64decode(encrypted_data)
        nonce = decoded_data[:16]
        tag = decoded_data[16:32]
        ciphertext = decoded_data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_data.decode('utf-8')
