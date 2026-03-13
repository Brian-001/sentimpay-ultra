from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

class SentimentAgent:

    def analyze(self, posts):

        text = "\n".join([p["title"] for p in posts])

        prompt = f"""
        Determine sentiment of the following posts:

        {text}

        Return score from -1 to 1
        """

        result = llm.predict(prompt)

        return result