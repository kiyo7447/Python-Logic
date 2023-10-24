# $ pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(s):
    # PKCS5 padding
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # ECB mode is not secure, consider using AES.MODE_CBC or other modes
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text.encode('utf-8'))
    return ciphertext.hex()

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # ECB mode is not secure, consider using AES.MODE_CBC or other modes
    decrypted_bytes = cipher.decrypt(bytes.fromhex(ciphertext))
    decrypted_text = unpad(decrypted_bytes.decode('utf-8'))
    return decrypted_text

# Generate a random 256-bit key
key = get_random_bytes(32)

# Encrypt and decrypt a message
message = "Hello, World!"
encrypted_message = aes_encrypt(message, key)
decrypted_message = aes_decrypt(encrypted_message, key)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
