from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from KeyGeneration import generate_and_save_admin_keys 
from KeyGeneration import generate_and_save_user_keys

# @author Yasiru
# contact me: https://linktr.ee/yasiruchamuditha for more information.

# ECC Key Exchange and Shared Secret Calculation
def compute_shared_secret(private_key_pem, peer_public_key_pem):
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    peer_public_key = serialization.load_pem_public_key(peer_public_key_pem)
    shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
    return shared_key

# Data Encryption
def encrypt_message(shared_key, plaintext):
    # Use the shared_key as a symmetric key (e.g., for AES encryption)
    # Here, we use a simple XOR operation for illustration purposes
    ciphertext = bytes([p ^ k for p, k in zip(plaintext, shared_key)])
    return ciphertext

# Save Encrypted Message to File
def save_encrypted_message(ciphertext, filename):
    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(ciphertext)

#Encrypt method based on user type
def encrypt(message,user_type):
    try:
        if user_type == 'admin':
            generate_and_save_admin_keys()
            private_key_pem = open('admin_private_key.pem', 'rb').read()
            peer_public_key_pem = open('admin_public_key.pem', 'rb').read()
            filename = 'admin_encrypted_message.bin'
        elif user_type == 'user':
            generate_and_save_user_keys()
            private_key_pem = open('user_private_key.pem', 'rb').read()
            peer_public_key_pem = open('user_public_key.pem', 'rb').read()
            filename = 'user_encrypted_message.bin'
        else:
            print("Invalid user type")
            return False

        shared_secret = compute_shared_secret(private_key_pem, peer_public_key_pem)
        ciphertext = encrypt_message(shared_secret, message)
        save_encrypted_message(ciphertext, filename)
        
        print("Message encrypted and saved.")
        return True
    
    except FileNotFoundError:
        print(f"Key file not found for user type: {user_type}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    

