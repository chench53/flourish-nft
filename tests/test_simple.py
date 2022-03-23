import pytest

from brownie import Simple, network, config
from scripts.tools import get_account, LOCAL_BLOCKCHAIN

def test_set_uri():
    if network.show_active() in LOCAL_BLOCKCHAIN:
        pytest.skip("Only for integration testing")

