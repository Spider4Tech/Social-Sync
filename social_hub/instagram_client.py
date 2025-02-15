import instaloader

class InstagramClient:
    def __init__(self, username, password):
        self.loader = instaloader.Instaloader()
        self.loader.login(username, password)

    def get_profile_info(self, username):
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)
            return {
                "username": profile.username,
                "user_id": profile.userid,
                "full_name": profile.full_name,
                "biography": profile.biography,
                "followers": profile.followers,
                "followees": profile.followees,
                "profile_pic_url": profile.profile_pic_url
            }
        except instaloader.InstaloaderException as e:
            print(f"Erreur: {e}")
            return None

    def download_posts(self, username, num_posts):
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)
            posts = profile.get_posts()
            for i, post in enumerate(posts):
                if i >= num_posts:
                    break
                self.loader.download_post(post, target=username)
        except instaloader.InstaloaderException as e:
            print(f"Erreur: {e}")

    def get_followers(self, username):
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)
            followers = profile.get_followers()
            return [follower.username for follower in followers]
        except instaloader.InstaloaderException as e:
            print(f"Erreur: {e}")
            return None

    def get_followees(self, username):
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)
            followees = profile.get_followees()
            return [followee.username for followee in followees]
        except instaloader.InstaloaderException as e:
            print(f"Erreur: {e}")
            return None

# Exemple d'utilisation
if __name__ == "__main__":
    USERNAME = 'votre_nom_utilisateur'
    PASSWORD = 'votre_mot_de_passe'

    client = InstagramClient(USERNAME, PASSWORD)

    profile_info = client.get_profile_info('nom_utilisateur_cible')
    print("Informations du profil:", profile_info)

    client.download_posts('nom_utilisateur_cible', 5)

    followers = client.get_followers('nom_utilisateur_cible')
    print("Followers:", followers)

    followees = client.get_followees('nom_utilisateur_cible')
    print("Followees:", followees)
