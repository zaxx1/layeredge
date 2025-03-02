from web3 import AsyncWeb3
w3 = AsyncWeb3()

class Account:
    def __init__(self, private_key: str, ua: str = None):
        self.evm_account = w3.eth.account.from_key(private_key)
        self.private_key: str = private_key
        self.wallet_address: str = self.evm_account.address
        self.ua = ua
