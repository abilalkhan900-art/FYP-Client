import os
import socket
import hashlib
import random
import string

DATA_DIR = "/serverdata"
FILE_PATH = os.path.join(DATA_DIR, "data.txt")

def generate_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    data = ''.join(random.choices(string.ascii_letters, k=1024))
    with open(FILE_PATH, "w") as f:
        f.write(data)
    return data.encode()

def calculate_checksum(data):
    return hashlib.sha256(data).hexdigest()

def start_server():
    host = "0.0.0.0"
    port = 5000

    with socket.socket() as s:
        s.bind((host, port))
        s.listen(1)
        print("Server listening...")

        conn, addr = s.accept()
        with conn:
            print("Connected:", addr)
            data = generate_file()
            checksum = calculate_checksum(data)

            conn.sendall(checksum.encode() + b"\n")
            conn.sendall(data)

if __name__ == "__main__":
    start_server()
