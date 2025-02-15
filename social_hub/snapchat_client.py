from snapchat import Snapchat

class SnapchatClient:
    def __init__(self, username, password):
        """
        Initialise le client Snapchat avec un nom d'utilisateur et un mot de passe.

        :param username: Nom d'utilisateur Snapchat.
        :param password: Mot de passe Snapchat.
        """
        self.snapchat = Snapchat()
        self.snapchat.login(username, password)

    def send_snap(self, recipient, image_path, caption=""):
        """
        Envoie un snap à un destinataire.

        :param recipient: Nom d'utilisateur du destinataire.
        :param image_path: Chemin vers l'image à envoyer.
        :param caption: Légende du snap.
        :return: True si le snap a été envoyé avec succès, False sinon.
        """
        try:
            self.snapchat.send(image_path, recipients=[recipient], caption=caption)
            return True
        except Exception as e:
            print(f"Erreur lors de l'envoi du snap: {e}")
            return False

    def get_friends(self):
        """
        Récupère la liste des amis.

        :return: Liste des noms d'utilisateur des amis.
        """
        try:
            friends = self.snapchat.get_friends()
            return [friend['name'] for friend in friends]
        except Exception as e:
            print(f"Erreur lors de la récupération des amis: {e}")
            return None

    def get_snap_history(self):
        """
        Récupère l'historique des snaps envoyés et reçus.

        :return: Historique des snaps.
        """
        try:
            history = self.snapchat.get_snaps()
            return history
        except Exception as e:
            print(f"Erreur lors de la récupération de l'historique des snaps: {e}")
            return None

# Exemple d'utilisation
if __name__ == "__main__":
    USERNAME = 'votre_nom_utilisateur'
    PASSWORD = 'votre_mot_de_passe'

    client = SnapchatClient(USERNAME, PASSWORD)

    # Envoyer un snap
    success = client.send_snap('nom_utilisateur_destinataire', 'path/to/image.jpg', 'Bonjour !')
    print("Snap envoyé avec succès:", success)

    # Récupérer la liste des amis
    friends = client.get_friends()
    print("Liste des amis:", friends)

    # Récupérer l'historique des snaps
    snap_history = client.get_snap_history()
    print("Historique des snaps:", snap_history)
