from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(data):
    
    og_data = data.encode('utf-8')
    
    encrypt_data = cipher.encrypt(og_data)
    
    return encrypt_data
    
    
def decrypt(data):
    decrypt_data = cipher.decrypt(data)
    decoded_data = decrypt_data.decode('utf-8')
    
    return decoded_data