import time
import json
import io

from brownie import (
    Simple,
    accounts,
    config,
)

from ..tools import get_account, upload_to_ipfs, OPENSEA
from metadata import sample_metadata

def main():
    simple = Simple[-1]
    nft_name = 'lamp-a'
    metadata_uri = gen_metadata(nft_name)
    set_tokenURI(1, simple, metadata_uri)

def gen_metadata(nft_name):
    nft_name = 'lamp-a'
    image_path = f'./img/{nft_name}.jpg'
    with open(image_path, "rb") as f:
        file_content = f.read()
        file_name = image_path.split('/')[-1]
        image_uri = upload_to_ipfs(file_name, file_content)
    metadata = sample_metadata.metadata_template
    metadata['name'] = nft_name
    metadata['image'] = image_uri
    metadata_uri = upload_to_ipfs(f'{nft_name}.json', json.dumps(metadata))
    # print(metadata_uri)
    return metadata_uri


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
