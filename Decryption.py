from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

# ECC Key Exchange and Shared Secret Calculation
def compute_shared_secret(private_key_pem, peer_public_key_pem):
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    peer_public_key = serialization.load_pem_public_key(peer_public_key_pem)
    shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
    return shared_key

# Data Decryption
def decrypt_message(shared_key, ciphertext):
    # Use the shared_key as a symmetric key (e.g., for AES decryption)
    # Here, we use a simple XOR operation for illustration purposes
    decrypted_text = bytes([c ^ k for c, k in zip(ciphertext, shared_key)])
    return decrypted_text

# Load Encrypted Message from File
def load_encrypted_message(filename):
    with open(filename, 'rb') as encrypted_file:
        ciphertext = encrypted_file.read()
    return ciphertext

def admin_decrypt(user_type):
    try:
        if user_type == 'admin':
            private_key_pem = open('admin_private_key.pem', 'rb').read()
            peer_public_key_pem = open('admin_public_key.pem', 'rb').read()
            filename = 'admin_encrypted_message.bin'
        else:
            print("Invalid user type")
            return None

        shared_secret = compute_shared_secret(private_key_pem, peer_public_key_pem)
        ciphertext = load_encrypted_message(filename)
        decrypted_text = decrypt_message(shared_secret, ciphertext)
        return decrypted_text.decode()

    except FileNotFoundError:
        print(f"Key file not found for user type: {user_type}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def user_decrypt(user_type):
    try:
        if user_type == 'user':
            private_key_pem = open('user_private_key.pem', 'rb').read()
            peer_public_key_pem = open('user_public_key.pem', 'rb').read()
            filename = 'user_encrypted_message.bin'
        else:
            print("Invalid user type")
            return None

        shared_secret = compute_shared_secret(private_key_pem, peer_public_key_pem)
        ciphertext = load_encrypted_message(filename)
        decrypted_text = decrypt_message(shared_secret, ciphertext)
        return decrypted_text.decode()

    except FileNotFoundError:
        print(f"Key file not found for user type: {user_type}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def decrypt(user_type):    
    if user_type == 'admin':
        decrypted_text = admin_decrypt(user_type)
    elif user_type == 'user':
        decrypted_text = user_decrypt(user_type)
    else:
        decrypted_text = None
    
    if decrypted_text:
        print("Decrypted Message in backend:", decrypted_text)
        return decrypted_text
    else:
        print("Decryption failed in backend.")
        return False
