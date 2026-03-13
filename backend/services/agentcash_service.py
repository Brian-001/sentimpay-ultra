import agentcash
from core.config import settings

client = agentcash.Client(api_key=settings.AGENTCASH_API_KEY)

class AgentCashService:

    def send_payment(self, task, amount):

        tx = client.payments.create(
            amount=amount,
            currency="USDC",
            recipient="service_vault",
            memo=f"SentimPay payment for {task}"
        )

        return tx

    def wallet_balance(self):

        return client.wallet.balance()