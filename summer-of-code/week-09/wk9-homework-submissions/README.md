# 1 Million Women To Tech

## Week 9 Blockchain Homework

Please find the unlisted video of Solidity Dev Environment Set Up at https://youtu.be/uKtln8upB5g

### 4. Starting private node

Create a `password.sec` file in your `~/blockchain/private` and type in the previously stated network password.

From the `wk9-homework-submissions` folder run:

`./startmynode.sh`

### 5. Initializing console for private node

From the `wk9-homework-submissions` folder run:

`geth attach ipc:./private/geth.ipc`

This will open console for running geth instance, its JavaScript console where you can execute various geth commands from the console for more details on commands refer to the next section.

### 6. Commonly used commands for geth console

Below are the list of commands which are most commonly used:
  * eth.accounts – Shows list of accounts which are registered on ethereum node
  * eth.coinbase – Shows address of the main account which is used for mining
  * eth.getBalance(eth.accounts[1]) – Shows the balance of account at 1st index in accounts array on node
  * miner.start() – To start mining process on node
  * miner.stop() – To stop mining process on node

For more commands please refer to the below link:
https://github.com/ethereum/wiki/wiki/JavaScript-API

### 7. Making transactions between two accounts and checking their balances

1. Get list of accounts on node:

   `eth.accounts`

1. To get the coinbase account address:

   `eth.coinbase`

1. Check balance of the coinbase account:

   `web3.fromWei(eth.getBalance(eth.coinbase), 'ether')`

1. Now get balance of another account:exit

   `web3.fromWei(eth.getBalance(eth.accounts[1]), 'ether')`

1. In order to exchange cryptocurrency i.e. to send ether among accounts use below command:

   `web3.eth.sendTransaction({from:eth.accounts[0], to:eth.accounts[1], value: web3.toWei(10,"ether")})`

1. Now check balances for both accounts as shown in below image:

   `web3.fromWei(eth.getBalance(eth.coinbase), 'ether')`

   and

   `web3.fromWei(eth.getBalance(eth.accounts[1]), 'ether')`

### 8. Stop private node

To stop your private node you can press `Ctrl + C`

Above command will interrupt and start shutting down private node.
It also closes HTTP and IPC endpoint and rest of items like ethereum protocol, transaction pool and database closed.

### 9. Stop console for private node

To stop your private node's console you can type `exit`

# References
* https://walkingtree.tech/setting-ethereum-development-environment-macos/
* https://walkingtree.tech/setup-private-ethereum-node-on-macos/
* https://github.com/ethereum/go-ethereum
* https://github.com/ethereum/wiki/wiki/JavaScript-API
* https://github.com/ethereum/go-ethereum/wiki/Command-Line-Options
* https://arvanaghi.com/blog/explaining-the-genesis-block-in-ethereum/
* https://medium.com/compound-finance/the-beginners-guide-to-using-an-ethereum-test-network-95bbbc85fc1d