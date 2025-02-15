from TikTokApi import TikTokApi

class TikTokClient:
    def __init__(self, ms_token):
        """
        Initialise le client TikTok avec un jeton d'accès.

        :param ms_token: Jeton d'accès pour l'API TikTok.
        """
        self.api = TikTokApi.get_instance(custom_verifyFp="verifyFp", ms_token=ms_token)

    def get_user_info(self, username):
        """
        Récupère les informations de base du profil utilisateur.

        :param username: Nom d'utilisateur TikTok.
        :return: Dictionnaire contenant les informations du profil.
        """
        try:
            user = self.api.getUser(username)
            return {
                "user_id": user["userInfo"]["user"]["id"],
                "username": user["userInfo"]["user"]["uniqueId"],
                "nickname": user["userInfo"]["user"]["nickname"],
                "bio": user["userInfo"]["user"]["signature"],
                "followers": user["userInfo"]["stats"]["followerCount"],
                "following": user["userInfo"]["stats"]["followingCount"],
                "likes": user["userInfo"]["stats"]["heartCount"],
                "video_count": user["userInfo"]["stats"]["videoCount"]
            }
        except Exception as e:
            print(f"Erreur lors de la récupération des informations du profil: {e}")
            return None

    def get_user_videos(self, username, count=5):
        """
        Récupère les vidéos récentes de l'utilisateur.

        :param username: Nom d'utilisateur TikTok.
        :param count: Nombre de vidéos à récupérer.
        :return: Liste des vidéos.
        """
        try:
            videos = self.api.byUsername(username, count=count)
            return [{"id": video["id"], "desc": video["desc"], "video_url": video["video"]["downloadAddr"]} for video in videos]
        except Exception as e:
            print(f"Erreur lors de la récupération des vidéos: {e}")
            return None

    def get_video_info(self, video_id):
        """
        Récupère les informations d'une vidéo spécifique.

        :param video_id: ID de la vidéo TikTok.
        :return: Dictionnaire contenant les informations de la vidéo.
        """
        try:
            video = self.api.getVideoInfo(video_id)
            return {
                "id": video["itemInfo"]["itemStruct"]["id"],
                "desc": video["itemInfo"]["itemStruct"]["desc"],
                "video_url": video["itemInfo"]["itemStruct"]["video"]["downloadAddr"],
                "likes": video["itemInfo"]["itemStruct"]["stats"]["diggCount"],
                "shares": video["itemInfo"]["itemStruct"]["stats"]["shareCount"],
                "comments": video["itemInfo"]["itemStruct"]["stats"]["commentCount"]
            }
        except Exception as e:
            print(f"Erreur lors de la récupération des informations de la vidéo: {e}")
            return None

# Exemple d'utilisation
if __name__ == "__main__":
    MS_TOKEN = 'votre_ms_token'

    client = TikTokClient(MS_TOKEN)

    user_info = client.get_user_info('nom_utilisateur_cible')
    print("Informations du profil:", user_info)

    user_videos = client.get_user_videos('nom_utilisateur_cible')
    print("Vidéos récentes:", user_videos)

    video_info = client.get_video_info('id_de_la_video')
    print("Informations de la vidéo:", video_info)
