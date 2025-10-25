# encryption test

# Simple XOR Encryption / Decryption
def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

# Test
key = 129
message = "Temperature:25C"

encrypted = xor_encrypt_decrypt(message, key)
print("Encrypted:", encrypted)

decrypted = xor_encrypt_decrypt(encrypted, key)
print("Decrypted:", decrypted)
