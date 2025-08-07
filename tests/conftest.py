import os
from typing import AsyncGenerator

import dotenv
import pytest

from hl_web3.exchange import Exchange
from hl_web3.info import Info
from hl_web3.utils.constants import HL_RPC_URL, HL_TESTNET_RPC_URL  # noqa: F401

dotenv.load_dotenv()
private_key = os.getenv("PRIVATE_KEY", "")


@pytest.fixture(scope="session")
async def info() -> AsyncGenerator[Info, None]:
    try:
        yield Info(HL_TESTNET_RPC_URL)
    except Exception as e:
        pytest.fail(f"Failed to connect to RPC: {e}")


@pytest.fixture(scope="session")
async def exchange() -> AsyncGenerator[Exchange, None]:
    try:
        yield Exchange(HL_TESTNET_RPC_URL, private_key)
    except Exception as e:
        pytest.fail(f"Failed to connect to RPC: {e}")
