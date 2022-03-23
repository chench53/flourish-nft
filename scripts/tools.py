import os
import requests

from brownie import (
    Contract,
    accounts, 
    network, 
    config
)
from web3 import Web3

LOCAL_BLOCKCHAIN = ['hardhat', 'development', 'ganache-local', 'mainnet-fork']
OPENSEA = "https://testnets.opensea.io/assets/{}/{}"
IPFS_URL = os.getenv("IPFS_URL")
IPFS_GATEWAY = os.getenv("IPFS_GATEWAY")

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN:
        return accounts[0]
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])
    return None

def upload_to_ipfs(file_name, file_content):
    """
        ipfs daemon
    """
    endpoint = "/api/v0/add"
    response = requests.post(IPFS_URL+endpoint, files={'filename': file_content})
    ipfs_hash = response.json()["Hash"]
    url = f"{IPFS_GATEWAY}/ipfs/{ipfs_hash}?filename={file_name}"
    print(url)
    return url