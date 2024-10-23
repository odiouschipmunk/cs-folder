import hashlib
import os

def generate_salt(length=16):
    """Generate a random salt."""
    return os.urandom(length)

def hash_with_salt(data, salt, hash_type='sha256'):
    """Generate a hash for the given data using the specified hash type and salt."""
    if hash_type not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported hash type: {hash_type}")
    
    hash_func = hashlib.new(hash_type)
    hash_func.update(salt + data.encode('utf-8'))
    return hash_func.hexdigest()

def generate_hash(data, hash_type='sha256', salt=None):
    """Generate a hash for the given data using the specified hash type and optional salt."""
    if salt is None:
        salt = generate_salt()
    elif isinstance(salt, str):
        salt = salt.encode('utf-8')
    
    hash_value = hash_with_salt(data, salt, hash_type)
    return hash_value, salt

# Example usage:
if __name__ == "__main__":
    data = "example data"
    hash_type = "sha256"
    
    # Generate hash with random salt
    hash_value, salt = generate_hash(data, hash_type)
    print(f"Hash: {hash_value}\nSalt: {salt.hex()}")
    
    # Generate hash with user-provided salt
    user_salt = "user_defined_salt"
    hash_value, salt = generate_hash(data, hash_type, user_salt)
    print(f"Hash: {hash_value}\nSalt: {salt.hex()}")