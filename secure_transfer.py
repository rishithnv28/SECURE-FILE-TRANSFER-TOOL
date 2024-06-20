import socket
import argparse
from encryption import encrypt_file, decrypt_file
from file_utils import calculate_checksum, compare_checksums, read_key

def send_file(file_path, file_name, receiver_mac):
    key = read_key()
    encrypted_file_path = f"{file_path}.enc"
    encrypt_file(file_path, encrypted_file_path, key)
    checksum = calculate_checksum(file_path)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = resolve_mac_to_ip(receiver_mac)
    s.connect((ip, 12345))

    with open(encrypted_file_path, 'rb') as f:
        data = f.read()
        s.sendall(data)

    s.sendall(checksum.encode())
    s.close()

def receive_file(save_path):
    key = read_key()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 12345))
    s.listen(1)
    conn, addr = s.accept()

    encrypted_file_path = f"{save_path}.enc"
    with open(encrypted_file_path, 'wb') as f:
        data = conn.recv(1024)
        while data:
            f.write(data)
            data = conn.recv(1024)
    
    conn.close()

    checksum = encrypted_file_path[-64:]
    encrypted_file_path = encrypted_file_path[:-64]
    
    decrypt_file(encrypted_file_path, save_path, key)

    if compare_checksums(save_path, checksum):
        print("File received and verified successfully.")
    else:
        print("File received but verification failed.")

def resolve_mac_to_ip(mac):
    # Dummy function for MAC to IP resolution
    return "192.168.1.100"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Secure File Transfer Application")
    subparsers = parser.add_subparsers(dest="command")

    send_parser = subparsers.add_parser("send")
    send_parser.add_argument("file_path", type=str, help="Path to the file to send")
    send_parser.add_argument("file_name", type=str, help="Name of the file to send")
    send_parser.add_argument("receiver_mac", type=str, help="MAC address of the receiver")

    receive_parser = subparsers.add_parser("receive")
    receive_parser.add_argument("save_path", type=str, help="Path to save the received file")

    args = parser.parse_args()
    
    if args.command == "send":
        send_file(args.file_path, args.file_name, args.receiver_mac)
    elif args.command == "receive":
        receive_file(args.save_path)
