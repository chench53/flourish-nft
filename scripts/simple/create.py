import time

from brownie import (
    accounts,
    config,
    Simple,
)
from ..tools import get_account, OPENSEA

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    simple = Simple[-1]
    tx = simple.createCollectible("None", {"from": dev})
    tx.wait(1)
    print(f'view nft at {OPENSEA.format(simple.address, simple.tokenCounter() - 1)}')
