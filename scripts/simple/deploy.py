from brownie import (
    Simple,
)
from web3 import Web3

from ..tools import get_account, OPENSEA


def deploy_create():
    account = get_account()
    simple = Simple.deploy({"from": account})
    tx = simple.createCollectible("None", {"from": account})
    tx.wait(1)
    # wait 20 minutes
    print(f'view nft at {OPENSEA.format(simple.address, simple.tokenCounter() - 1)}')
    return simple

def main():
    deploy_create()
