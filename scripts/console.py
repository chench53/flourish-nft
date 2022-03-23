from brownie import (
    Simple,
)
from web3 import Web3

from .tools import get_account, OPENSEA

def main():
    simple = Simple[-1]
    # print(simple.tokenCounter())
    print(simple.ownerOf(1))
    print(simple.tokenURI(1))
