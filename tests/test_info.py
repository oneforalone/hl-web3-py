import pytest

from hl_web3.info import Info

coin = "BTC"  # btc coin name in hl testnet
asset = 3  # btc perp index in hl testnet
spot = 50  # btc spot index in hl testnet, coin name: @50
token = 69  # btc spot token index in hl testnet
user = "0xA1406199484382D1913B6fc3CbFE70440C533b68"
hlp = "0xa15099a30BBf2e68942d6F4c43d70D04FAEab0A0"  # HLP vault


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_position(info: Info):
    pos = await info.get_user_position(user, asset)
    print(pos, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_spot_balance(info: Info):
    balance = await info.get_user_spot_balance(user, spot)
    print(balance, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_vault_equity(info: Info):
    equity = await info.get_user_vault_equity(user, hlp)
    print(equity, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_delegations(info: Info):
    delegations = await info.get_user_delegations(user)
    print(delegations, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_delegator_summary(info: Info):
    summary = await info.get_user_delegator_summary(user)
    print(summary, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_withdrawable(info: Info):
    amount = await info.get_user_withdrawable(user)
    print(amount, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_mark_px(info: Info):
    px = await info.get_mark_px(asset)
    print(px, end=" ")
    assert px > 0


@pytest.mark.asyncio(loop_scope="session")
async def test_get_oracle_px(info: Info):
    px = await info.get_oracle_px(asset)
    print(px, end=" ")
    assert px > 0


@pytest.mark.asyncio(loop_scope="session")
async def test_get_spot_px(info: Info):
    px = await info.get_spot_px(spot)
    print(px, end=" ")
    assert px > 0


@pytest.mark.asyncio(loop_scope="session")
async def test_get_block_number(info: Info):
    blk_number = await info.get_block_number()
    print(blk_number, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_perp_asset_info(info: Info):
    perp_asset = await info.get_perp_asset_info(asset)
    print(perp_asset, end=" ")
    assert perp_asset.coin == coin


@pytest.mark.asyncio(loop_scope="session")
async def test_get_spot_info(info: Info):
    spot_info = await info.get_spot_info(spot)
    print(spot_info, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_token_info(info: Info):
    token_info = await info.get_token_info(token)
    print(token_info, end=" ")
    assert token_info.name == coin


@pytest.mark.asyncio(loop_scope="session")
async def test_get_token_supply(info: Info):
    supply = await info.get_token_supply(token)
    print(supply, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_bbo(info: Info):
    bbo = await info.get_bbo(asset)
    print(bbo, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_margin_summary(info: Info):
    dex = 0
    summary = await info.get_user_margin_summary(dex, user)
    print(summary, end=" ")


@pytest.mark.asyncio(loop_scope="session")
async def test_is_core_user(info: Info):
    is_core_user = await info.is_core_user(user)
    print(is_core_user, end=" ")
