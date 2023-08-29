// SPDX-License-Identifier: MIT

pragma solidity ^0.8.18;

contract domainToUUID {
	
    constructor() payable{}

    mapping ( string => string ) private domainToUUIDMap;

    string[] private domainList;

    function registerDomain(string memory _domainName , string memory _uuidOfUser) public {
        domainToUUIDMap[_domainName] = _uuidOfUser; // list the UUID under the domain given
        domainList.push(_domainName); // write the domain in the domainList
    }

    function getUUIDBydomain(string memory _domainName) public view returns (string memory) {
        return domainToUUIDMap[_domainName];
    }
}
