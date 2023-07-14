
def encrypt(plaintext, shift):
    encrypted_text = ""
    plaintext = plaintext.lower()
    shift = shift % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    for i in plaintext:
        if i .isalpha() == True:
            index = alphabet.index(i)
            encrypted_text = encrypted_text + shifted_alphabet[index]
        else:
            encrypted_text = encrypted_text + i
    print(encrypted_text)    

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    encrypted_text = encrypted_text.lower()
    shift = shift % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    for i in encrypted_text:
        if i .isalpha() == True:
            index = shifted_alphabet.index(i)
            decrypted_text = decrypted_text + alphabet[index]
        else:
            decrypted_text = decrypted_text + i
    print(decrypted_text)    
    
