from openai import OpenAI
from core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class SentimentService:

    def analyze(self, posts):

        if not posts:
            return {"sentiment": "neutral", "score": 0}

        text = "\n".join([p["title"] for p in posts])

        prompt = f"""
        Analyze the sentiment of these social media posts.

        Return:
        sentiment: positive/neutral/negative
        score: number between -1 and 1

        Posts:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a sentiment analysis engine."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content