import praw
from core.config import settings


class RedditService:

    def __init__(self):

        self.reddit = praw.Reddit(
            client_id=settings.REDDIT_CLIENT_ID,
            client_secret=settings.REDDIT_CLIENT_SECRET,
            user_agent=settings.REDDIT_USER_AGENT
        )

    def search_posts(self, keyword, limit=20):

        results = []

        for post in self.reddit.subreddit("all").search(keyword, limit=limit):

            results.append({
                "title": post.title,
                "score": post.score,
                "url": post.url,
                "created": post.created_utc
            })

        return results