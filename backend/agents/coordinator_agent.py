from agents.data_agent import DataAgent
from agents.sentiment_agent import SentimentAgent
from agents.budget_agent import BudgetAgent
from services.agentcash_service import AgentCashService

class CoordinatorAgent:

    def __init__(self):

        self.data_agent = DataAgent()
        self.sentiment_agent = SentimentAgent()
        self.budget_agent = BudgetAgent()
        self.payment = AgentCashService()

    def run_cycle(self, keyword):

        posts = self.data_agent.collect_posts(keyword)

        if len(posts) < 5:
            return "Low activity"

        cost = 0.05

        if not self.budget_agent.can_spend(cost):
            return "Budget exceeded"

        tx = self.payment.send_payment("sentiment_analysis", cost)

        sentiment = self.sentiment_agent.analyze(posts)

        self.budget_agent.record_spend(cost)

        return {
            "transaction": tx.id,
            "sentiment": sentiment
        }