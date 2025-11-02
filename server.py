#!/usr/bin/env python3
import socket, struct, threading, json, os
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

HOST, PORT = "0.0.0.0", 9000

def send_bytes(conn, b): conn.sendall(struct.pack("!I", len(b)) + b)
def recv_bytes(conn):
    hdr = conn.recv(4)
    if not hdr: return None
    (n,) = struct.unpack("!I", hdr)
    data = b""
    while len(data) < n:
        chunk = conn.recv(n - len(data))
        if not chunk: raise ConnectionError("socket closed during recv")
        data += chunk
    return data

def derive_shared_key(priv, peer_pub_bytes):
    peer_pub = x25519.X25519PublicKey.from_public_bytes(peer_pub_bytes)
    shared = priv.exchange(peer_pub)
    hkdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"iot-secure-comm")
    return hkdf.derive(shared)

def handle_client(conn, addr):
    try:
        priv = x25519.X25519PrivateKey.generate()
        pub = priv.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        send_bytes(conn, pub)
        client_pub = recv_bytes(conn)
        if client_pub is None: raise ConnectionError("client closed")
        key = derive_shared_key(priv, client_pub)
        aesgcm = AESGCM(key)

        while True:
            enc_packet = recv_bytes(conn)
            if enc_packet is None: break
            nonce, ciphertext = enc_packet[:12], enc_packet[12:]
            plaintext = aesgcm.decrypt(nonce, ciphertext, None)
            msg = plaintext.decode()
            obj = json.loads(msg)
            print(f"[{addr}] received:", obj)

            ack = json.dumps({"status": "ok", "received": obj.get("type", "telemetry")}).encode()
            ack_nonce = os.urandom(12)
            ack_ct = aesgcm.encrypt(ack_nonce, ack, None)
            send_bytes(conn, ack_nonce + ack_ct)
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
        print("Closed:", addr)

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT)); s.listen(5)
    print(f"Server running on {HOST}:{PORT}")
    try:
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        print("Server stopped")
    finally: s.close()

if __name__ == "__main__":
    start_server()
