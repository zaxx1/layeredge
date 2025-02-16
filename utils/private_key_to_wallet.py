from web3 import AsyncWeb3
w3 = AsyncWeb3()

def private_key_to_wallet(private_key: str):
    return w3.eth.account.from_key(private_key).address