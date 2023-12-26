import string

def encrypt (plain_text,key):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    encryption_txt=""
    for char in plain_text:
        if char.lower() in alphabet:
            index = (alphabet.index(char.lower()) + key)%26
            encryption_txt += alphabet[index]
        else:
            encryption_txt += char
    return encryption_txt
plain_text =input("Enter plain text :")
key=int(input("Enter the key :"))

cipher_txt =encrypt (plain_text,key)
print("plain text",plain_text)
print("cipher text :",cipher_txt)

# import string

# def encrypt(plain_text, key):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     encryption_txt = ""
#     for char in plain_text:
#         if char.lower() in alphabet:
#             index = (alphabet.index(char.lower()) + key) % 26
#             encryption_txt += alphabet[index]
#         else:
#             encryption_txt += char
#     return encryption_txt

# plain_text = input("Enter plain text: ")
# key = int(input("Enter the key: "))

# cipher_txt = encrypt(plain_text, key)
# print("Plain text:", plain_text)
# print("Cipher text:", cipher_txt)
