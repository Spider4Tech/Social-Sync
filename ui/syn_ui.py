import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SocialSyncUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Social Sync")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Titre de la fenêtre
        title_label = QLabel("Connectez vos comptes")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Boutons pour chaque réseau social
        social_media = {
            "Facebook": self.connect_facebook,
            "Twitter": self.connect_twitter,
            "Instagram": self.connect_instagram,
            "Snapchat": self.connect_snapchat,
            "TikTok": self.connect_tiktok
        }

        for name, func in social_media.items():
            button = QPushButton(name)
            button.clicked.connect(func)
            layout.addWidget(button)

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
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 5px;
                font-size: 16px;
                margin-bottom: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

    def connect_facebook(self):
        QMessageBox.information(self, "Facebook", "Connectez votre compte Facebook ici.")
        # Ajoutez ici la logique pour connecter à Facebook

    def connect_twitter(self):
        QMessageBox.information(self, "Twitter", "Connectez votre compte Twitter ici.")
        # Ajoutez ici la logique pour connecter à Twitter

    def connect_instagram(self):
        QMessageBox.information(self, "Instagram", "Connectez votre compte Instagram ici.")
        # Ajoutez ici la logique pour connecter à Instagram

    def connect_snapchat(self):
        QMessageBox.information(self, "Snapchat", "Connectez votre compte Snapchat ici.")
        # Ajoutez ici la logique pour connecter à Snapchat

    def connect_tiktok(self):
        QMessageBox.information(self, "TikTok", "Connectez votre compte TikTok ici.")
        # Ajoutez ici la logique pour connecter à TikTok

