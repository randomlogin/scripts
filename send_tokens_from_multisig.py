import json
from web3 import Web3, HTTPProvider

provider = Web3(HTTPProvider('http://127.0.0.1:8545'))

TOKEN_CONTRACT_ADDRESS =   "0xFCAd0B19bB29D4674531d6f115237E16AfCE377c"
MULTISIG_ABI_FILENAME = "multisig.abi"
MULTISIG_CONTRACT_ADDRESS = "0xFCAd0B19bB29D4674531d6f115237E16AfCE377c"
SENDER_ADDRESS =   "0xFCAd0B19bB29D4674531d6f115237E16AfCE377c"
SENDER_PRIVATE_KEY = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
RECEIVER_ADDRESS =  utils.checksum_encode("0x0123456789abcDEF0123456789abCDef01234567")

NONCE = 173 #look at the last transaction at etherscan and take its nonce+1
CHAIN_ID = 1 #1 for mainnet, 3 for ropsten testnet
AMOUNT_OF_TOKENS_TO_SEND = 10000000000000000000000 #you have to lookup decimals by yourself, so 1 token with 18 decimals would be 1000000000000000000
GASPRICE = 14000000000 #4 Gwei
GASLIMIT = 300000

hex_amount = provider.toHex(AMOUNT_OF_TOKENS_TO_SEND)[2:]
tokens=("0"*(64-len(hex_amount)))+hex_amount

with open(MULTISIG_ABI_FILENAME, 'r') as abi_definition:
    abi = json.load(abi_definition)

multisig = provider.eth.contract(MULTISIG_CONTRACT_ADDRESS, abi=abi)

print("you're going to send", AMOUNT_OF_TOKENS_TO_SEND/10**18, "tokens")
print("\nto address:", RECEIVER_ADDRESS, "\nimplying token has 18 decimal places")

calldata = "a9059cbb" + "000000000000000000000000" + RECEIVER_ADDRESS[2:] + tokens #some low-level magic from ancient times when libraries were absent

tx = multisig.functions.submitTransaction(TOKEN_CONTRACT_ADDRESS, 0, calldata).buildTransaction({'from':SENDER_ADDRESS, 'gasPrice': GASPRICE, 'nonce':NONCE, 'gas':GASLIMIT, 'chainId':CHAIN_ID} )
signed_tx = provider.eth.account.signTransaction(tx, SENDER_PRIVATE_KEY)
hexdata = signed_tx['rawTransaction'].hex()
print('\nsigned TX:\n', hexdata, '\n')
