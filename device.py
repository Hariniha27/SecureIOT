#!/usr/bin/env python3
import socket, struct, time, json, os, random
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

SERVER_HOST, SERVER_PORT = "127.0.0.1", 9000

def send_bytes(s, b): s.sendall(struct.pack("!I", len(b)) + b)
def recv_bytes(s):
    hdr = s.recv(4)
    if not hdr: return None
    (n,) = struct.unpack("!I", hdr)
    data = b""
    while len(data) < n:
        chunk = s.recv(n - len(data))
        if not chunk: raise ConnectionError("socket closed")
        data += chunk
    return data

def derive_shared_key(priv, peer_pub_bytes):
    peer_pub = x25519.X25519PublicKey.from_public_bytes(peer_pub_bytes)
    shared = priv.exchange(peer_pub)
    hkdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"iot-secure-comm")
    return hkdf.derive(shared)

def simulate_telemetry():
    return {
        "type": "telemetry",
        "device_id": "device-001",
        "ts": int(time.time()),
        "temperature": round(20 + random.random()*10, 2),
        "humidity": round(30 + random.random()*40, 2),
        "battery": round(50 + random.random()*50, 2)
    }

def run_device():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_HOST, SERVER_PORT))
    server_pub = recv_bytes(s)
    priv = x25519.X25519PrivateKey.generate()
    pub = priv.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    send_bytes(s, pub)
    key = derive_shared_key(priv, server_pub)
    aesgcm = AESGCM(key)

    for _ in range(5):
        data = json.dumps(simulate_telemetry()).encode()
        nonce = os.urandom(12)
        ct = aesgcm.encrypt(nonce, data, None)
        send_bytes(s, nonce + ct)
        ack_packet = recv_bytes(s)
        ack_nonce, ack_ct = ack_packet[:12], ack_packet[12:]
        ack = aesgcm.decrypt(ack_nonce, ack_ct, None)
        print("ACK:", ack.decode())
        time.sleep(1)
    s.close()

if __name__ == "__main__":
    run_device()
