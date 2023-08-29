from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from web3 import Web3
import requests
import os

# Connect to Polygon network
polygon_url = "https://polygon-mumbai-bor.publicnode.com"
w3 = Web3(Web3.HTTPProvider(polygon_url))

# Accessing to the details of the registerenet

###########################ENTER YOUR PRIVATE AND PUBLIC KEY HERE###########################
private_key = 
public_key = 
############################################################################################

# connect to the subscribers contract
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
w3.eth.defaultAccount = public_key
contract = w3.eth.contract(address=contract_address, abi=contract_abi)


#Generating a private key using the RSA method
privateKeyGenerated = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Get the corresponding public key
publicKeyGenerated = privateKeyGenerated.public_key()

# Serialize the private key to PEM format
private_key_pem = privateKeyGenerated.private_bytes(
    encoding= serialization.Encoding.PEM,
    format = serialization.PrivateFormat.PKCS8,
    encryption_algorithm = serialization.NoEncryption()  # No encryption for private key
)

# Serialize the public key to PEM format
public_key_pem = privateKeyGenerated.public_key().public_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PublicFormat.SubjectPublicKeyInfo
)

# Specify the file name
file_name_private = "privateKey.txt"

# Saves the private key generated locally in order to decrypt the data later
# --Return-- void
def savePrivateKeyLocally(private_key_pem_format):
	private_key_after_cutting = private_key_pem_format.decode('utf-8')
	try:
		with open(file_name_private, "w") as private_key_file:
			private_key_file.write(private_key_after_cutting)
		print("The generated private key has been successfully saved to the computer. \nFile name: privateKey.txt\n")
		
	except Exception as e:
		print("An error occurred while saving the file: ", e)

savePrivateKeyLocally(private_key_pem)


file_name_public = "publicKey.txt"

with open(file_name_public, "w") as public_key_file:
    public_key_file.write(public_key_pem.decode('utf-8'))

# Uploadinga a file to ipfs 
# --Return-- CID number of the file uploaded
def upload_file_to_ipfs(file_path_to_upload):
    url = "https://api.web3.storage/upload"
    cid = 0
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweEE4QjVBMGIxNzY3NWQ4RjE5ODZBODk4YjE2REQyZWIyODNCOTIxM0QiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2OTI3MDI1MDU2MjcsIm5hbWUiOiJKb25hS2FuZGVsVCJ9.hRH2nbQsGlK6T5f8xyEDmgmX-h8JSIsSrSaIlWc1E9o"
    }
    files = {
        "file": open(file_path_to_upload, "rb")
    }

    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        response_json = response.json()
        cid = response_json["cid"]
        print(f"The generated public key has been successfully uploaded to IPFS. \nCID: {cid}\n")
    else:
        print("File upload failed.")

    return cid

# Uploads the public key generated to the IPFS server
cid = upload_file_to_ipfs(file_name_public) 

# Removes the localy copy of the file
os.remove(file_name_public)

# Making a tranasaction to the subscribers contract in order to list the user public key ( owner )
# and the CID of the file uploaded to IPFS containing the generated public key for encryption purposes.
try:
	transaction = contract.functions.Subscribe(public_key, cid).build_transaction({
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