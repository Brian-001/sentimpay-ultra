from fastapi import APIRouter
from agents.coordinator_agent import CoordinatorAgent
from services.agentcash_service import AgentCashService
from core.logger import get_logs

router = APIRouter()

coordinator = CoordinatorAgent()
agentcash = AgentCashService()


@router.get("/")
async def root():
    return {"service": "SentimPay Ultra", "status": "running"}


@router.get("/run-agent")
async def run_agent(keyword: str = "AI"):

    result = coordinator.run_cycle(keyword)

    return {
        "message": "Agent cycle executed",
        "result": result
    }


@router.get("/wallet-balance")
async def wallet_balance():

    balance = agentcash.wallet_balance()

    return {
        "balance": balance
    }


@router.get("/logs")
async def logs():

    return get_logs()