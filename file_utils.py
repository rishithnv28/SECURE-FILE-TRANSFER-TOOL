import hashlib

def calculate_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def compare_checksums(file_path, received_checksum):
    calculated_checksum = calculate_checksum(file_path)
    return calculated_checksum == received_checksum
