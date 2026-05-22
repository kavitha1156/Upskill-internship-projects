from cryptography.fernet import Fernet
import os

KEY_PATH = "data/key.key"

def load_key():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as f:
            f.write(key)
        return key

    try:
        with open(KEY_PATH, "rb") as f:
            key = f.read()
        Fernet(key)  # validate
        return key
    except:
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as f:
            f.write(key)
        return key

key = load_key()
cipher = Fernet(key)

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()