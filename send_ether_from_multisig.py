import json
from web3 import Web3, HTTPProvider
#comment utils lines, but then you have to paste the checksum address (has both capital and small letters)
import ethereum.utils as utils
provider = Web3(HTTPProvider('http://127.0.0.1:8545'))

MULTISIG_ABI_FILENAME = "multisig.abi"
MULTISIG_CONTRACT_ADDRESS = "0xFCAd0B19bB29D4674531d6f115237E16AfCE377c"
SENDER_ADDRESS =   "0xFCAd0B19bB29D4674531d6f115237E16AfCE377c"
SENDER_PRIVATE_KEY = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
RECEIVER_ADDRESS =  utils.checksum_encode("0x0123456789abcDEF0123456789abCDef01234567")

NONCE = 177 #look at the last transaction at etherscan and take its nonce+1
CHAIN_ID = 1 #1 for mainnet, 3 for ropsten testnet
GASPRICE = 4000000000 #4 Gwei
GASLIMIT = 190000
ETHER_AMOUNT = 4947000000000000000

print("You're sending {} ETH to {}".format(ETHER_AMOUNT/10**18, RECEIVER_ADDRESS))
print("Gas price: {} Gwei".format(GASPRICE/10**9))

with open(MULTISIG_ABI_FILENAME, 'r') as abi_definition:
    abi = json.load(abi_definition)

multisig = provider.eth.contract(MULTISIG_CONTRACT_ADDRESS, abi=abi)

tx = multisig.functions.submitTransaction(RECEIVER_ADDRESS, ETHER_AMOUNT, b'').buildTransaction({'from':SENDER_ADDRESS, 'gasPrice': GASPRICE, 'nonce':NONCE, 'gas':GASLIMIT, 'chainId':CHAIN_ID} )
signed_tx = provider.eth.account.signTransaction(tx, SENDER_PRIVATE_KEY)
hexdata = signed_tx['rawTransaction'].hex()
print('signed TX:\n', hexdata, '\n')
