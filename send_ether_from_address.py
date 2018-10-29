from web3 import Web3, HTTPProvider

provider = Web3(HTTPProvider('http://127.0.0.1:8545'))

SENDER_ADDRESS =   "0xFCAd0B19bB29D4674531d6f115237E16AfCE377c"
SENDER_PRIVATE_KEY = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
RECEIVER_ADDRESS = "0x0123456789abcDEF0123456789abCDef01234567"

NONCE = 162 #look at the last OUTGOING transaction at etherscan and take its nonce+1
CHAIN_ID = 1 #1 for mainnet, 3 for ropsten testnet

GASPRICE = 5*10**9 #4 Gwei
GASLIMIT = 21000

val = 500000000000000000 #value in wei

tx ={'from':SENDER_ADDRESS, 'gasPrice': GASPRICE, 'nonce':NONCE, 'gas':GASLIMIT, 'chainId':CHAIN_ID, 'to':RECEIVER_ADDRESS, 'value':val}

signed_tx = provider.eth.account.signTransaction(tx, SENDER_PRIVATE_KEY)
hexdata = signed_tx['rawTransaction'].hex()
print('signed TX:\n', hexdata, '\n') #this will print the transaction raw hex, which can be sent to any node
