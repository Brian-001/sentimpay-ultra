import praw
from core.config import settings

reddit = praw.Reddit(
    client_id=settings.REDDIT_CLIENT_ID,
    client_secret=settings.REDDIT_CLIENT_SECRET,
    user_agent=settings.REDDIT_USER_AGENT
)

class DataAgent:

    def collect_posts(self, keyword):

        posts = []

        for post in reddit.subreddit("all").search(keyword, limit=20):

            posts.append({
                "title": post.title,
                "score": post.score
            })

        return posts