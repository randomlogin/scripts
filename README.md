# Overview
Here are some scripts I'm using myself. 

Titles are pretty self-descriptive.
1. One of them just sends the ether from address. 
2. The second submits a transaction to the multisignature wallet to send ether from this multisignature wallet.
3. The third sumbits a transaction to the mulsitignature wallet to send tokens from this mulsitignature wallet.

# Usage
None of the scripts sends transaction to any node, instead they print the hexadecimal value which can be sent to any node.
For example it can be broadcasted through https://etherscan.io/pushTx. 

Each script signs transaction, so you need to know the private key of the sender. Other parameters such as gas price and gas
value and nonce should be also entered manually. The examples of how all the fields look like (address, private key,
nonce, gas price) are set in the code.

Be careful with handling the private keys, they should not be uploaded to any storage and given to anyone. Of course
example private key in the code is fake.

Once you set the correct parameters, simply run the python script.

`python3 send_ether_from_address.py`

# Dependencies

web3py

Also scripts use `ethereum.utils` to get the chekcsum address, however it can be done manually for example by looking at
address on the etherscan.
