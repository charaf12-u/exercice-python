import hashlib
from cryptography.fernet import Fernet

def find_original_text(encrypted_text, original_text):
    key = hashlib.sha256(original_text.encode()).digest()
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text.encode()).decode()
    return decrypted_text

encrypted_value = "gAAAAABg7wQxpfr9WwP8wH2DOjBt2ePZiJ6yvhg1oqwYiF4h3fjGq9q9nFj0vZpJ5w-2Bd7fK8zT8hGm0cYxjX9KhM8ILf8Kg=="
original_text = "SecretKey123"
decrypted_value = find_original_text(encrypted_value, original_text)
print("Decrypted Text:", decrypted_value)