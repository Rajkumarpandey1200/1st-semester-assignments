
plaintext = "HELLO"
key = "JOKJO"

if len(plaintext) != len(key):
    raise ValueError("Plaintext and key must have the same length")
plaintext= plaintext.lower()
key=key.lower()

ciphertext = ""
for i in range(len(plaintext)):
    char_plaintext = plaintext[i]
    char_key = key[i]

    encrypted_char = chr((ord(char_plaintext) - ord('a') + ord(char_key) - ord('a')) % 26 + ord('a'))
    ciphertext += encrypted_char

print("Plaintext:",plaintext)
print("Key: ", key)
print("Ciphertext:", ciphertext)
