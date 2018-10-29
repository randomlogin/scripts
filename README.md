Usage: `python3 send_ether_from_address.py`

Here are some scripts I'm using myself. 

Titles are pretty self-descriptive.
One of them justs sends the ether from address. 
The second submits a transaction to the multisignature wallet to send ether from this multisignature wallet.
The third sumbits a transaction to the mulsitignature wallet to send tokens from this mulsitignature wallet.


None of the scripts sends transaction to any node, instead they print the hexadecimal value which can be sent to any node.
For example it can be broadcasted through https://etherscan.io/pushTx . 

Each script signs transaction, so you need to know the private key of the send. Other parameters as gas price and gas
value and nonce should be also entered manually. The examples of how all the fields look like (address, private key,
nonce, gas price) are set in the code.

Be careful with handling the private keys, they should not be uploaded to any storage and given to anyone.
