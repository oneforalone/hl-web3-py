import pytest
from web3 import Web3

from hl_web3.utils.constants import ACTION_VERSION
from hl_web3.utils.miscs import get_raw_action
from hl_web3.utils.types import ActionType


def test_abi_encode_with_selector():
    func_sig = "sendRawAction(bytes)"
    func_selector = Web3.keccak(text=func_sig)[:4]
    assert func_selector == bytes.fromhex("17938E13")


@pytest.mark.parametrize(
    "action_id, action",
    [
        pytest.param(1, bytes(), id="Action 1"),
        pytest.param(2, bytes(), id="Action 2"),
        pytest.param(3, bytes(), id="Action 3"),
        pytest.param(4, bytes(), id="Action 4"),
        pytest.param(5, bytes(), id="Action 5"),
        pytest.param(6, bytes(), id="Action 6"),
        pytest.param(7, bytes(), id="Action 7"),
        pytest.param(8, bytes(), id="Action 8"),
        pytest.param(9, bytes(), id="Action 9"),
        pytest.param(10, bytes(), id="Action 10"),
        pytest.param(11, bytes(), id="Action 11"),
        # invalid action_id
        pytest.param(0, bytes(), id="action_id=0", marks=pytest.mark.xfail),
        pytest.param(12, bytes(), id="action_id=12", marks=pytest.mark.xfail),
        pytest.param(-1, bytes(), id="action_id=-1", marks=pytest.mark.xfail),
        pytest.param("abc", bytes(), id="action_id=abc", marks=pytest.mark.xfail),
        pytest.param(1.0, bytes(), id="action_id=1.0", marks=pytest.mark.xfail),
        pytest.param(True, bytes(), id="action_id=True", marks=pytest.mark.xfail),
        pytest.param(1, "", id="action=''", marks=pytest.mark.xfail),
    ],
)
def test_get_raw_action(action_id: int, action: bytes):
    action_type = ActionType(action_id)
    raw_action = get_raw_action(action_type, action)
    header = raw_action[:4]
    assert header[0] == ACTION_VERSION
    assert header[1] == 0x00
    assert header[2] == 0x00
    assert header[3] == action_id
