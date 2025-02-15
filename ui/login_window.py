import sys
import os
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from ui.main_window import MainWindow
from ui.syn_ui import SocialSyncUI


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Titre de la fenêtre
        title_label = QLabel("Bienvenue !")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Champ pour le mot de passe
        password_label = QLabel("Mot de passe:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Entrez votre mot de passe")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)

        # Bouton de connexion
        login_button = QPushButton("Se connecter")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        self.setLayout(layout)

        # Style moderne
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
            }
            QLabel {
                font-size: 16px;
                color: #333;
                margin-bottom: 10px;
            }
            QLineEdit {
                border: 1px solid #ccc;
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 20px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

    def handle_login(self):
        password = self.password_input.text()
        file_path = "tokens.txt"

        if not os.path.exists(file_path):
            self.create_new_password_file(password, file_path)
        else:
            try:
                stored_hash, encrypted_tokens = self.read_file(file_path)
                if self.verify_password(password, stored_hash):
                    tokens = self.decrypt_tokens(password, encrypted_tokens)
                    if tokens:
                        QMessageBox.information(self, "Succès", "Connexion réussie!")
                        # Ouvrir la fenêtre principale ici
                        self.open_main_window()
                    else:
                        self.open_sync_window()
                        QMessageBox.warning(self, "Erreur", "pas de token")
                else:
                    QMessageBox.warning(self, "Erreur", "Mot de passe incorrect")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors du déchiffrement: {e}")


    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def open_sync_window(self):
        self.sync_window = SocialSyncUI()
        self.sync_window.show()
        self.close()


    def create_new_password_file(self, password, file_path):
        confirm_password, ok = QInputDialog.getText(self, "Créer un mot de passe", "Veuillez confirmer votre mot de passe:", QLineEdit.Password)
        if ok and confirm_password == password:
            # Créer un fichier avec le hachage du mot de passe et les jetons chiffrés
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            with open(file_path, 'w') as f:
                f.write(password_hash + "\n")

            QMessageBox.information(self, "Succès", "Fichier de mot de passe créé avec succès!")
        else:
            QMessageBox.warning(self, "Erreur", "Les mots de passe ne correspondent pas.")

    def read_file(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()

        stored_hash = lines[0].strip()
        encrypted_tokens = lines[1:]

        return stored_hash, encrypted_tokens

    def verify_password(self, password, stored_hash):
        print(hashlib.sha256(password.encode()).hexdigest())
        print(stored_hash)
        print(hashlib.sha256(password.encode()).hexdigest() == stored_hash)
        return hashlib.sha256(password.encode()).hexdigest() == stored_hash

    def decrypt_tokens(self, password, encrypted_tokens):
        decrypted_tokens = []

        for encrypted_token in encrypted_tokens:
            encrypted_token = base64.b64decode(encrypted_token.strip().encode())
            salt = encrypted_token[:16]
            iv = encrypted_token[16:32]
            encrypted_token = encrypted_token[32:]

            kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
            key = kdf.derive(password.encode())

            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            token = decryptor.update(encrypted_token) + decryptor.finalize()

            decrypted_tokens.append(token.decode())

        return decrypted_tokens

