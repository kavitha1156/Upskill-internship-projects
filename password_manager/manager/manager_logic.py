from manager.crypto import encrypt_password, decrypt_password
from manager.storage import load_data, save_data
from manager.generator import generate_password

def add_password(site, username, password=None):
    if not password:
        password = generate_password()

    encrypted = encrypt_password(password)

    data = load_data()
    data[site] = {"username": username, "password": encrypted}
    save_data(data)

    return password

def get_password(site):
    data = load_data()

    if site in data:
        decrypted = decrypt_password(data[site]["password"])
        return data[site]["username"], decrypted

    return None, None

def delete_password(site):
    data = load_data()

    if site in data:
        del data[site]
        save_data(data)
        return True
    return False

def list_sites():
    return list(load_data().keys())