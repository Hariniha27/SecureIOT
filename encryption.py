# encryption.py

# Simple XOR Encryption / Decryption
def xor_encrypt_decrypt(data, key):
    """
    Encrypts or decrypts a string using XOR with a single-byte key.

    Args:
        data (str): The input string to encrypt or decrypt.
        key (int): An integer key (0-255).

    Returns:
        str: The encrypted or decrypted string.
    """
    return ''.join(chr(ord(c) ^ key) for c in data)
