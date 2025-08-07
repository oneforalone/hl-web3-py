import pytest

from hl_web3.endpoint import Endpoint


@pytest.mark.parametrize(
    "rpc_url",
    [
        pytest.param("https://rpc.hyperliquid-testnet.xyz/evm", id="HTTPS"),
        pytest.param("wss://rpc.hyperliquid-testnet.xyz/evm", id="WebSocket"),
        pytest.param("~/Library/Ethereum/geth.ipc", id="IPC", marks=pytest.mark.xfail),
    ],
)
def test_endpoint(rpc_url: str):
    ep = Endpoint(rpc_url)
    assert ep._w3 is not None
