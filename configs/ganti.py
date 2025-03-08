import json

with open('wallets.json', 'r') as file:
    wallets = json.load(file)

with open('farm.txt', 'w') as farm_file:
    for wallet in wallets:
        private_key = wallet.get('privateKey')
        if private_key:
            farm_file.write(private_key + '\n')

print("Private keys telah berhasil disalin ke farm.txt")
