# ROT13 Encryption Method
# Function to encrypt a message using ROT13 algorithm
def rot13_encrypt(x):
    encrypted = ''
    for char in x:
        if 'A' <= char <= 'Z':  # If the character is uppercase alphabet
            encrypted += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))  # It is transformed using ROT13 encryption
            
        elif 'a' <= char <= 'z':  # If the character is lowercase alphabet
            encrypted += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))  # It is transformed using ROT13 encryption
            
        else:  # If the character is not an alphabet letter
            encrypted += char  # It remains unchanged and is added as it is
            
    return encrypted

# Prompt the user to input the message to be encrypted
message = input("Enter your message: ")

# Encrypt the message and print the encrypted text
encrypted_message = rot13_encrypt(message)
print("Encrypted Message:", encrypted_message)

# Function to decrypt a ROT13 encrypted message
def rot13_decrypt(x):
    decrypted = ''
    for char in x:
        if 'A' <= char <= 'Z':  # If the character is uppercase alphabet
            decrypted += chr(((ord(char) - ord('A') - 13) % 26) + ord('A'))  # It is transformed using ROT13 decryption
            
        elif 'a' <= char <= 'z':  # If the character is lowercase alphabet
            decrypted += chr(((ord(char) - ord('a') - 13) % 26) + ord('a'))  # It is transformed using ROT13 decryption
            
        else:  # If the character is not an alphabet letter
            decrypted += char  # It remains unchanged and is added as it is
            
    return decrypted

# Decrypt the encrypted message and print the decrypted text
decrypted_message = rot13_decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message)
