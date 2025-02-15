from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

def encrypt_tokens(password, tokens, output_file):
    # Dériver une clé à partir du mot de passe
    salt = os.urandom(16)
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    key = kdf.derive(password.encode())

    # Générer un vecteur d'initialisation (IV)
    iv = os.urandom(16)

    # Chiffrer les jetons avec AES
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_tokens = encryptor.update(tokens.encode()) + encryptor.finalize()

    # Stocker les données chiffrées dans un fichier
    with open(output_file, 'wb') as f:
        f.write(base64.b64encode(salt + iv + encrypted_tokens))

# Exemple d'utilisation
tokens = "votre_jeton_facebook;votre_jeton_twitter;votre_jeton_instagram"
password = "votre_mot_de_passe"
encrypt_tokens(password, tokens, "tokens.txt")
