import pytest
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3

from hl_web3.exchange import Exchange
from hl_web3.utils.constants import SCALE_FACTOR
from hl_web3.utils.types import Tif

asset = 3  # BTC perp
cloid = 7  # custom cloid
hlp = "0xa15099a30BBf2e68942d6F4c43d70D04FAEab0A0"
hypurr_validator = "0x946bf3135c7d15e4462b510f74b6e304aabb5b21"


# action 1
@pytest.mark.asyncio(loop_scope="session")
async def test_place_order(exchange: Exchange):
    is_buy = False
    px = int(115_000 * SCALE_FACTOR)
    sz = int(0.0001 * SCALE_FACTOR)
    ro = True
    tif = Tif.Alo
    tx = await exchange.place_order(asset, is_buy, px, sz, ro, tif, cloid)
    print(tx, end=" ")
    assert tx is not None


# action 2
@pytest.mark.asyncio(loop_scope="session")
async def test_vault_transfer(exchange: Exchange):
    is_deposit = True
    usd = int(8.18 * 10**6)  # USD decimals is 6
    tx = await exchange.vault_transfer(hlp, is_deposit, usd)
    print(tx, end=" ")
    assert tx is not None


# action 3
@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.skip(reason="In-sufficient HYPE to delegate")
async def test_token_delegate(exchange: Exchange):
    amount = Web3.to_wei(1, "ether")  # 1 HYPE
    tx = await exchange.token_delegate(hypurr_validator, amount, is_undelegate=True)
    print(tx, end=" ")


# action 4
@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.skip(reason="In-sufficient HYPE to stake")
async def test_staking_deposit(exchange: Exchange):
    amount = Web3.to_wei(1, "ether")  # 1 HYPE
    tx = await exchange.staking_deposit(amount)
    print(tx, end=" ")


# action 5
@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.skip(reason="Staking balance is 0")
async def test_staking_withdraw(exchange: Exchange):
    amount = Web3.to_wei(1, "ether")  # 1 HYPE
    tx = await exchange.staking_withdraw(amount)
    print(tx, end=" ")


# action 6
@pytest.mark.asyncio(loop_scope="session")
async def test_spot_send(exchange: Exchange):
    # transfer 8.18 USDC to destination address
    dest = "0x37071047F9edbB2d7FDDD32d2F00E7c897919e85"
    token = 0
    amount = int(8.18 * 10**6)
    tx = await exchange.spot_send(dest, token, amount)
    print(tx, end=" ")


# action 7
@pytest.mark.asyncio(loop_scope="session")
async def test_send_usd_class_transfer(exchange: Exchange):
    to_perp = True
    amount = int(8.18 * 10**6)  # USD decimals is 6
    tx = await exchange.send_usd_class_transfer(amount, to_perp)
    print(tx, end=" ")
    assert tx is not None


# action 8
@pytest.mark.asyncio(loop_scope="session")
async def test_finalize_evm_contract(exchange: Exchange):
    # TODO: Figure out how Finalize EVM Contract works
    pass


# action 9
@pytest.mark.asyncio(loop_scope="session")
async def test_add_api_wallet(exchange: Exchange):
    wallet: LocalAccount = Account.create()
    api_address = wallet.address
    api_private_key = wallet.key.hex()
    name = "hl_web3_test"
    tx = await exchange.add_api_wallet(api_address, name)
    print(
        f"Created api wallet: {api_address}, private key: {api_private_key}, tx: {tx}",
        end=" ",
    )


# action 10
@pytest.mark.asyncio(loop_scope="session")
async def test_cancel_order_by_oid(exchange: Exchange):
    # Note: get the order id via HTTP API, or frontend request response
    oid = 37253285146
    tx = await exchange.cancel_order_by_oid(asset, oid)
    print(tx, end=" ")


# action 11
@pytest.mark.asyncio(loop_scope="session")
async def test_cancel_order_by_cloid(exchange: Exchange):
    tx = await exchange.cancel_order_by_cloid(asset, cloid)
    print(tx, end=" ")
