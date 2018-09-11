pragma solidity ^0.4.0;
// the source code is written for Solidity version 0.4.0 or anything newer that does not break functionality
// This is to ensure that the contract is not compilable with a new (breaking) compiler version,
// where it could behave differently.

// A contract in the sense of Solidity is a collection of code (its functions) and data (its state)
// that resides at a specific address on the Ethereum blockchain.

contract SimpleStorage {
    uint storageData;

    function set(uint x) public {
        storageData = x;
    }

    function get() public view returns (uint){
        return storageData;
    }
}