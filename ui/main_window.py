import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QCheckBox,
                             QLabel, QLineEdit, QPushButton, QWidget, QFileDialog)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Social Media Manager")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # Logos des réseaux sociaux avec cases à cocher
        social_media_layout = QHBoxLayout()
        social_media_data = [
            ("Facebook", "path/to/facebook_logo.png"),
            ("Twitter", "path/to/twitter_logo.png"),
            ("Instagram", "path/to/instagram_logo.png"),
            ("Snapchat", "path/to/snapchat_logo.png"),
            ("TikTok", "path/to/tiktok_logo.png")
        ]

        for name, logo_path in social_media_data:
            checkbox = QCheckBox(name)
            logo_label = QLabel()
            pixmap = QPixmap(logo_path).scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(pixmap)

            layout = QVBoxLayout()
            layout.addWidget(checkbox)
            layout.addWidget(logo_label)
            layout.setAlignment(Qt.AlignCenter)

            social_media_layout.addLayout(layout)

        main_layout.addLayout(social_media_layout)

        # Champs pour le titre et la description
        title_label = QLabel("Titre:")
        self.title_input = QLineEdit()
        description_label = QLabel("Description:")
        self.description_input = QLineEdit()

        main_layout.addWidget(title_label)
        main_layout.addWidget(self.title_input)
        main_layout.addWidget(description_label)
        main_layout.addWidget(self.description_input)

        # Bouton pour uploader un média
        upload_button = QPushButton("Uploader un média")
        upload_button.clicked.connect(self.upload_media)
        main_layout.addWidget(upload_button)

        # Style moderne
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit {
                border: 1px solid #ccc;
                padding: 5px;
                border-radius: 3px;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

    def upload_media(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Uploader un média", "", "Images (*.png *.xpm *.jpg *.jpeg);;Vidéos (*.mp4 *.avi)", options=options)
        if file_name:
            print(f"Fichier sélectionné: {file_name}")