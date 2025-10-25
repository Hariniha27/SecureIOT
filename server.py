# server.py
from encryption import xor_encrypt_decrypt
import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on
key = 129           # Same encryption key as client

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening on", HOST, ":", PORT)
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)  # Receive data
            if not data:
                break
            decrypted_data = xor_encrypt_decrypt(data.decode(), key)
            print(f"Received decrypted: {decrypted_data}")
