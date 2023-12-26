def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
message = input("ENTER THE PLAIN TEXT = ")
key = int(input("ENTER THE KEY VALUE = "))

# Encryption
cipher = encrypt(message, key)
print(f"THE CIPHER TEXT OF THE GIVEN PLAIN TEXT = {cipher}")

# Decryption
decrypted_message = decrypt(cipher, key)
print(f"THE DECRYPTED TEXT OF THE GIVEN CIPHER TEXT = {decrypted_message}")
