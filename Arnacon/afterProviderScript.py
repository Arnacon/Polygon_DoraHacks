import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from web3 import Web3
import requests
import providerScript as ps
# import keyPairIPFS as kpIPFS

# Connect to Polygon network
polygon_url = "https://polygon-mumbai-bor.publicnode.com"
w3 = Web3(Web3.HTTPProvider(polygon_url))

# Accessing to the details of the registerenet

###########################ENTER YOUR PRIVATE AND PUBLIC KEY HERE###########################
private_key = 
public_key = 
############################################################################################

w3.eth.defaultAccount = public_key

# Contract details (Blockchain)
contract_abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "approved",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "ApprovalForAll",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_fromTokenId",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_toTokenId",
				"type": "uint256"
			}
		],
		"name": "BatchMetadataUpdate",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "string",
				"name": "message",
				"type": "string"
			}
		],
		"name": "LogMessage",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_tokenId",
				"type": "uint256"
			}
		],
		"name": "MetadataUpdate",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			},
			{
				"internalType": "bytes",
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "setApprovalForAll",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_ownerAddress",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_userCID",
				"type": "string"
			}
		],
		"name": "Subscribe",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "key",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_CIDOfCredentials",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_nameFromProvider",
				"type": "string"
			}
		],
		"name": "updateMappingOfCredentialsAndGiven",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "addressToTokenId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "addressToUUID",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "currentUUID",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "getApproved",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "uuidOfUser",
				"type": "string"
			}
		],
		"name": "getCIDPK",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_address",
				"type": "address"
			}
		],
		"name": "getItemIds",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_address",
				"type": "address"
			}
		],
		"name": "getUUIDFromAddress",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			}
		],
		"name": "isApprovedForAll",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "ownerOf",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes4",
				"name": "interfaceId",
				"type": "bytes4"
			}
		],
		"name": "supportsInterface",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "tokenURI",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "uuidToTrio",
		"outputs": [
			{
				"internalType": "string",
				"name": "CIDPK",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "credentialsCID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "nameInTheServer",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
contract_address = '0x4E8154B1cee2fC72274e7c74a86bA612195dc44D'
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Connect to the ENS contract (domain --> UUID)
ens_contract_abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_domainName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_uuidOfUser",
				"type": "string"
			}
		],
		"name": "registerDomain",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "payable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_domainName",
				"type": "string"
			}
		],
		"name": "getUUIDBydomain",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
ens_contract_address = '0xA0B299b458E9c9D5c7d9169b5e10500c5ffc0940'
ens_contract = w3.eth.contract(address = ens_contract_address, abi = ens_contract_abi)

## Future upgrade for more then one accounts ( more then 1 UUID )
# ItemIds = contract.functions.getItemIds(public_key).call()
# ownerUUID = contract.functions.tokenURI(ItemIds[-1]).call()

# Getting the owner UUID in order to fetch from the mapping of the TRIO - UUID to CID of public key.
ownerUUID = contract.functions.getUUIDFromAddress(public_key).call()
credentials_file_cid = ps.fetch_credentials_from_provider(ownerUUID) # OTHER SCRIPT

# Read the private key from the file saved locally
private_key_path = "privateKey.txt"
with open(private_key_path, "r") as private_key_file:
    private_key_pem = private_key_file.read()
    
# Fetching the file content from IPFS contains all the data of the credentials and the given name by provider for calling encrypted
def fetchTheFileFromIPFS(credentionals_givenName_cid):
	# try:
	# 	client = ipfshttpclient.connect()
	# 	content = client.cat(credentionals_givenName_cid)
	
	# except:
	# 	print("error") 
           
	# return content

    #Connecting VIA web2 ( IPFS isn't working.. )
    try:
        url = "https://" + credentials_file_cid +".ipfs.dweb.link/"
        headers = {"User-Agent": "Mozilla/5.0"}  # Set a user agent header
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            content_from_ipfs = response.text
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")

    except:
        print("error fetching the public key from ipfs")
    
    return content_from_ipfs

# Calling the function
encrypted_file = fetchTheFileFromIPFS(credentials_file_cid) # the file encrypted from ipfs

# Converting the data from hexadecimal format back to the binary encrypted data
encrypted_bytes = bytes.fromhex(encrypted_file)

# Loading the private key in the right format in order to decrypt ( "RSA encryption with Optimal Asymmetric Encryption Padding (OAEP)" )
private_key_right = serialization.load_pem_private_key(
    private_key_pem.encode(),
    password=None,  # No password protection for the private key
    backend=default_backend()
)

# Decrypt the data back to the original format - bytes
decrypted_data = private_key_right.decrypt(
    encrypted_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Removes the local copy of the private key generated for the encryption
# os.remove(private_key_path)

# From bytes to String 
decrypted_string = decrypted_data.decode("utf-8")

# From String to dict in order to retrieve the data in a convient way 
dict_string = json.loads(decrypted_string)

# Fetching the given name from the provider in order to make the transaction to the blockchain to update the mappings
givenName = dict_string['givenName']

# Uploading the updated credentials and given name to the blockchain

try:
	transaction = contract.functions.updateMappingOfCredentialsAndGiven(ownerUUID, credentials_file_cid, givenName).build_transaction({
		'chainId': 80001,  
		'gas': 2000000,
		'gasPrice': Web3.to_wei('50', 'gwei'),
		'nonce': w3.eth.get_transaction_count(public_key),
	})
        
    # Sign the transaction
	signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)

	# Sending the signed transaction to the network:
	transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

	# Wait for the transaction to be mined
	transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
	
	print("The transaction was successfully executed on the blockchain network: \n" + polygon_url + " \n\nFor this user: \n" + public_key)
        
except:
    print("transaction failed")


# Registering the domain given by the provider to the blockchain in order to connect the domain to the UUID of the user
try:
	transaction = ens_contract.functions.registerDomain(givenName, ownerUUID).build_transaction({
		'chainId': 80001,  
		'gas': 2000000,
		'gasPrice': Web3.to_wei('50', 'gwei'),
		'nonce': w3.eth.get_transaction_count(public_key),
	})
        
    # Sign the transaction
	signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)

	# Sending the signed transaction to the network:
	transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

	# Wait for the transaction to be mined
	transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
	
	print("The transaction was successfully executed on the blockchain network: \n" + polygon_url + " \n\nFor this user: \n" + public_key)
        
except:
    print("transaction failed")