// SPDX-License-Identifier: MIT

pragma solidity ^0.8.18;

contract hello {
	
    constructor() payable{}

    mapping ( string => address ) private domainToAddress;
    mapping ( string => address ) private domainToDeployerAddress;

    string[] private domainList;
    

    function registerENS(string memory _domainName , address _addressOfdomain) public {
        if (validateAddress(_addressOfdomain))
        {
            if (!isDomainRegistered(_domainName)) // if the domain is already in the system
            {
                domainToAddress[_domainName] = _addressOfdomain; // list the address under the domain given
                domainToDeployerAddress[_domainName] = msg.sender; // map the first deployer address -> owner
                domainList.push(_domainName); // write the domain in the domainList
            }
            else 
            {
                revert("There is already a domain like that in the system, please try again.");
            }
        }
        else 
        {
            revert("Invalid address format");
        }
    }

    function updateAddress(string memory _domainName, address _newAddressForDomain) public {
        if (isDomainRegistered(_domainName)) {
            if(validateAddress(_newAddressForDomain)){
                if(msg.sender == domainToDeployerAddress[_domainName]){
                    domainToAddress[_domainName] = _newAddressForDomain;
                }
                else {
                    revert("You're not the owner, go away!");
                }
            }
            else {
                revert("Invalid address");
            }
        }
        else {
                revert("Invalid domain name");
        }
    }

    function isDomainRegistered(string memory _domainName) private view returns (bool) {// checks if the domain is already registered 
        for( uint i = 0 ; i < domainList.length; i++){
            if (compareStrings(domainList[i], _domainName)) {
                return true;
            }
        }
        return false;
    }

    function compareStrings(string memory a, string memory b) private pure returns (bool) {
        return keccak256(abi.encodePacked(a)) == keccak256(abi.encodePacked(b));
    }

    function validateAddress(address _addressToValidate) private pure returns (bool){ // Ethereum account or contract on the Ethereum network. It only ensures that the address is in the expected format
        return _addressToValidate != address(0);
    }

    function getAddressBydomain(string memory _domainName) public view returns (address) {
        return domainToAddress[_domainName];
    }

    function isAddressRegistered(address _addr) private view returns (bool) {
        for (uint256 i = 0; i < domainList.length; i++) {
            if (domainToAddress[domainList[i]] == _addr) {
                return true;
            }
        }
        return false;
    }
}