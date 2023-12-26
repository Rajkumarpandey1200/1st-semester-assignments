def encrypt(text, shift): 
    text = text.lower() 
    text = text.replace(" ","") 
    encrypted_text = ""
    for char in text : 
        if char.islower(): 
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97) 
        else : 
            encrypted_text += char 
    return encrypted_text 

def decrypt(text1, shift): 
    text1 = text1.lower() 
    decrypted_text = ""
    for char in text1: 
        if char.islower(): 
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97) 
        else: 
            decrypted_text += char 
    return decrypted_text 

message = str(input("ENTER THE PLAIN TEXT = ")) 
key = 3
cipher = encrypt(message, key) 
print(f"THE PLAIN TEXT = {message}") 
print(f"KEY VALUE = {key}") 
print(f"THE CIPHER TEXT OF THE GIVEN PLAIN TEXT = {cipher}")

cipher_text = cipher 
key1 = key 
decrypted_message = decrypt(cipher_text, key1) 
print(f"THE GIVEN CIPHER TEXT = {cipher_text}") 
print(f"THE PLAIN TEXT OF THE GIVEN CIPHER TEXT = {decrypted_message}")
