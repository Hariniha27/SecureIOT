# client.py
from encryption import xor_encrypt_decrypt
import socket
import time

HOST = '127.0.0.1'  # Server IP (localhost)
PORT = 65432
key = 129            # Same key as server

data_list = ["Temperature:25C", "Humidity:60%", "Traffic:High"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for data in data_list:
        encrypted_data = xor_encrypt_decrypt(data, key)
        s.sendall(encrypted_data.encode())
        print(f"Sent encrypted: {encrypted_data}")
        time.sleep(1)  # wait 1 second before sending next
