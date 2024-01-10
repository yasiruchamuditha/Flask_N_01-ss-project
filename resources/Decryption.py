from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec


# @author Yasiru
# contact me: https://linktr.ee/yasiruchamuditha for more information.

# ECC Key Exchange and Shared Secret Calculation
def compute_shared_secret(private_key_pem, peer_public_key_pem):
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    peer_public_key = serialization.load_pem_public_key(peer_public_key_pem)
    shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
    return shared_key

# Data Decryption
def decrypt_message(shared_key, ciphertext):
    # Use a proper symmetric encryption algorithm here, such as AES
    # For illustration purposes, this XOR operation is not secure.
    # Replace it with actual decryption logic.
    decrypted_text = bytes([c ^ k for c, k in zip(ciphertext, shared_key)])
    return decrypted_text

# Load Encrypted Message from File
def load_encrypted_message(filename):
    try:
        with open(filename, 'rb') as encrypted_file:
            ciphertext = encrypted_file.read()
        return ciphertext
    except FileNotFoundError:
        print(f"Encrypted message file not found: {filename}")
        return None

#admin decrypt method
def admin_decrypt(userrole):
    try:
        if userrole == 'admin':
            private_key_pem = open('admin_private_key.pem', 'rb').read()
            peer_public_key_pem = open('admin_public_key.pem', 'rb').read()
            filename = 'admin_encrypted_message.bin'
        else:
            print("Invalid user type")
            return None

        shared_secret = compute_shared_secret(private_key_pem, peer_public_key_pem)
        ciphertext = load_encrypted_message(filename)
        
        if ciphertext is not None:
            decrypted_text = decrypt_message(shared_secret, ciphertext)
            return decrypted_text.decode()
        else:
            return None

    except FileNotFoundError:
        print(f"Key file not found for user type: {userrole}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
    
#user decrypt method
def user_decrypt(userrole):
    try:
        if userrole == 'user':
            private_key_pem = open('user_private_key.pem', 'rb').read()
            peer_public_key_pem = open('user_public_key.pem', 'rb').read()
            filename = 'user_encrypted_message.bin'
        else:
            print("Invalid user type")
            return None

        shared_secret = compute_shared_secret(private_key_pem, peer_public_key_pem)
        ciphertext = load_encrypted_message(filename)
        
        if ciphertext is not None:
            decrypted_text = decrypt_message(shared_secret, ciphertext)
            return decrypted_text.decode()
        else:
            return None

    except FileNotFoundError:
        print(f"Key file not found for user type: {userrole}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None



#Desrypt method based on user role
def decrypt(userrole):    
    if userrole == 'admin':
        decrypted_text = admin_decrypt(userrole)
    elif userrole == 'user':
        decrypted_text = user_decrypt(userrole)
    else:
        decrypted_text = None
    
    if decrypted_text:
        print("Decrypted Message in backend:", decrypted_text)
        return decrypted_text
    else:
        print("Decryption failed in backend.")
        return None

