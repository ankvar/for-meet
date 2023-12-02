def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


message = "Szia! Ez egy titkosított üzenet"
shift_value = 1

encrypted_message = caesar_encrypt(message,shift_value)
print("Encrypted: ", encrypted_message)            

decrypted_message = caesar_decrypt(encrypted_message,shift_value)
print("Decrypted: ", decrypted_message)            