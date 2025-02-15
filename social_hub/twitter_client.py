import tweepy

class TwitterClient:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_user_timeline(self, username, count=5):
        try:
            tweets = self.api.user_timeline(screen_name=username, count=count)
            return [{"text": tweet.text, "created_at": tweet.created_at} for tweet in tweets]
        except tweepy.TweepyException as e:
            print(f"Erreur: {e}")
            return None

    def post_tweet(self, message):
        try:
            tweet = self.api.update_status(message)
            return tweet.id
        except tweepy.TweepyException as e:
            print(f"Erreur: {e}")
            return None

    def get_followers(self, username, count=5):
        try:
            followers = self.api.followers(screen_name=username, count=count)
            return [follower.screen_name for follower in followers]
        except tweepy.TweepyException as e:
            print(f"Erreur: {e}")
            return None

    def get_following(self, username, count=5):
        try:
            following = self.api.friends(screen_name=username, count=count)
            return [friend.screen_name for friend in following]
        except tweepy.TweepyException as e:
            print(f"Erreur: {e}")
            return None

# Exemple d'utilisation
if __name__ == "__main__":
    API_KEY = 'votre_api_key'
    API_SECRET_KEY = 'votre_api_secret_key'
    ACCESS_TOKEN = 'votre_access_token'
    ACCESS_TOKEN_SECRET = 'votre_access_token_secret'

    client = TwitterClient(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    timeline = client.get_user_timeline('nom_utilisateur_cible')
    print("Timeline:", timeline)

    tweet_id = client.post_tweet("Bonjour, ceci est un test depuis mon application Python!")
    print("ID du tweet publié:", tweet_id)

    followers = client.get_followers('nom_utilisateur_cible')
    print("Followers:", followers)

    following = client.get_following('nom_utilisateur_cible')
    print("Following:", following)
