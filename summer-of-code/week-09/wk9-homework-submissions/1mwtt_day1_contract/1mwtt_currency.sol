pragma solidity >0.4.24;

// The following contract will implement the simplest form of a cryptocurrency.
// It is possible to generate coins out of thin air, but only the person that created the contract will be able to do
// that (it is easy to implement a different issuance scheme).
// Furthermore, anyone can send coins to each other without a need for registering with username and password —
// all you need is an Ethereum keypair.

contract Coin {
    // The keyword "public" makes those variables
    // easily readable from outside.
    // state variable of type address 160-bit value that does not allow any arithmetic operations
    address public minter;

    // The type maps addresses to unsigned integers.
    // Mappings can be seen as hash tables which are virtually initialized such that every possible key exists
    // from the start and is mapped to a value whose byte-representation is all zeros.
    mapping (address => uint) public balances;

    // Events allow light clients to react to
    // changes efficiently.
    event Sent(address from, address to, uint amount);

    // This is the constructor whose code is
    // run only when the contract is created.
    // When a contract is created the constructor
    // permanently stores the address of the person creating the contract:
    // msg (together with tx and block) is a magic global variable that contains
    // some properties which allow access to the blockchain.
    // msg.sender is always the address where the current (external) function call came from.
    constructor() public {
        minter = msg.sender;
    }

    // Finally, the functions that will actually end up with the contract
    // and can be called by users and contracts alike are mint and send.

    function mint(address receiver, uint amount) public {
        // If mint is called by anyone except the account that created the contract, nothing will happen.
        require(msg.sender == minter);  // if (msg.sender != minter) return;
        require(amount < 1e60);
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        // send can be used by anyone (who already has some of these coins) to send coins to anyone else.
        require(amount <= balances[msg.sender], "Insufficient balance.");  // if (balances[msg.sender] < amount) "Insufficient balance.";
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
}

// N.B. Note that if you use this contract to send coins to an address,
// you will not see anything when you look at that address on a blockchain explorer,
// because the fact that you sent coins and the changed balances are only stored
// in the data storage of this particular coin contract.
// By the use of events it is relatively easy to create a “blockchain explorer”
// that tracks transactions and balances of your new coin.