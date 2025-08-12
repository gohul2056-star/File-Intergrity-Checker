import hashlib
import os

def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    return hash_sha256.hexdigest()

def monitor_file(file_path, stored_hash=None):
    """Monitor a file for changes by comparing hash values."""
    current_hash = calculate_file_hash(file_path)
    
    if current_hash is None:
        return
    
    if stored_hash is None:
        print(f"Initial hash for {file_path}: {current_hash}")
        return current_hash  
    
    if current_hash != stored_hash:
        print(f"File {file_path} has been modified!")
        print(f"Old hash: {stored_hash}")
        print(f"New hash: {current_hash}")
    else:
        print(f"No changes detected in {file_path}.")

if __name__ == "__main__":
    file_to_monitor = 'Day4 moving object.txt'  
    stored_hash = None

    while True:
        stored_hash = monitor_file(file_to_monitor, stored_hash)
        input("Press Enter to check again...") 
