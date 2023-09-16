from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

# ECC Key Generation and Saving to PEM Files for Admin
def generate_and_save_admin_keys():
    private_key = ec.generate_private_key(ec.SECP256R1())  # Use a suitable elliptic curve

    # Serialize and save the private key to a .pem file
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    with open('admin_private_key.pem', 'wb') as private_key_file:
        private_key_file.write(private_pem)

    # Get and serialize the public key
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save the public key to a .pem file
    with open('admin_public_key.pem', 'wb') as public_key_file:
        public_key_file.write(public_pem)

# ECC Key Generation and Saving to PEM Files for User
def generate_and_save_user_keys():
    private_key = ec.generate_private_key(ec.SECP256R1())  # Use a suitable elliptic curve

    # Serialize and save the private key to a .pem file
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    with open('user_private_key.pem', 'wb') as private_key_file:
        private_key_file.write(private_pem)

    # Get and serialize the public key
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save the public key to a .pem file
    with open('user_public_key.pem', 'wb') as public_key_file:
        public_key_file.write(public_pem)
