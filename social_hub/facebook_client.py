import facebook
import requests

class FacebookClient:
    def __init__(self, access_token):
        """
        Initialise le client Facebook avec un jeton d'accès.

        :param access_token: Jeton d'accès pour l'API Facebook.
        """
        self.graph = facebook.GraphAPI(access_token)

    def get_user_info(self):
        """
        Récupère les informations de base du profil utilisateur.

        :return: Dictionnaire contenant les informations du profil.
        """
        try:
            profile = self.graph.get_object("me", fields='id,name,email')
            return profile
        except facebook.GraphAPIError as e:
            print(f"Erreur lors de la récupération des informations du profil: {e}")
            return None

    def post_status_update(self, message):
        """
        Publie un message sur le mur de l'utilisateur.

        :param message: Message à publier.
        :return: ID du message publié.
        """
        try:
            response = self.graph.put_object("me", "feed", message=message)
            return response['id']
        except facebook.GraphAPIError as e:
            print(f"Erreur lors de la publication du message: {e}")
            return None

    def get_friends(self):
        """
        Récupère la liste des amis de l'utilisateur.

        :return: Liste des amis.
        """
        try:
            friends = self.graph.get_connections("me", "friends")
            return friends['data']
        except facebook.GraphAPIError as e:
            print(f"Erreur lors de la récupération des amis: {e}")
            return None

    def get_user_posts(self):
        """
        Récupère les publications récentes de l'utilisateur.

        :return: Liste des publications.
        """
        try:
            posts = self.graph.get_connections("me", "posts")
            return posts['data']
        except facebook.GraphAPIError as e:
            print(f"Erreur lors de la récupération des publications: {e}")
            return None




# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez par votre jeton d'accès
    ACCESS_TOKEN = 'votre_jeton_d_acces'

    client = FacebookClient(ACCESS_TOKEN)

    # Récupérer les informations du profil
    user_info = client.get_user_info()
    print("Informations du profil:", user_info)

    # Publier un message
    post_id = client.post_status_update("Bonjour, ceci est un test depuis mon application Python!")
    print("ID du message publié:", post_id)

    # Récupérer la liste des amis
    friends = client.get_friends()
    print("Liste des amis:", friends)

    # Récupérer les publications récentes
    posts = client.get_user_posts()
    print("Publications récentes:", posts)