import os
from web3 import Web3
import requests
import json
import random # to create the user 10 random charachers username + password
import string # to make it for a string the random
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend


# Connect to Polygon network
polygon_url = "https://polygon-mumbai-bor.publicnode.com"
w3 = Web3(Web3.HTTPProvider(polygon_url))

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
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Uploadinga a file to ipfs 
# --Return-- CID number of the file uploaded
def upload_file_to_ipfs(file_path_to_upload):
    url = "https://api.web3.storage/upload"
	# In order to upload to IPFS I listed in web3.storage recieved a token and then used this token in order to upload and recieve a cid number of the file.
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
        print(f"File uploaded successfully. CID: {cid}")
    else:
        print("File upload failed.")

    return cid

# Retreving the public key from IPFS
# Generating credentials for the user ---> (1) User ID
#                                          (2) User password
#										   (3) User domain
#										   (4) Given name from the provider
# Uploading this data encrypted with the public key recieved from the IPFS server that the user uploaded while initiating the registeration
# --Return-- CID of the file uploaded to IPFS
def fetch_credentials_from_provider(uuid_of_user):
	trioVar = contract.functions.uuidToTrio(uuid_of_user).call() # fetch the trio mapping from the Block-Chain
	CIDOfPublicKey = trioVar[0] # takes the CID of the ipfs file that inside the public key for encrpytion

	# Generating a random credentials for the user with the corresponding domain and user
	random_user = generate_random_string(10)
	random_password = generate_random_string(10)

	userDomain = "cellact.com" # IP / DNS
	userGivenFromProviderName = "jonathan.phone"

	# Create a dictionary with four string values
	data = {
		"userID": random_user,
		"userPass": random_password,
		"userDomain": userDomain,
		"givenName": userGivenFromProviderName
	}

    # Get the content of the file from IPFS using the CID of the public key uploaded from the keyPairIPFS script.
    # try:    
        # access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweEE4QjVBMGIxNzY3NWQ4RjE5ODZBODk4YjE2REQyZWIyODNCOTIxM0QiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2OTI3MDI1MDU2MjcsIm5hbWUiOiJKb25hS2FuZGVsVCJ9.hRH2nbQsGlK6T5f8xyEDmgmX-h8JSIsSrSaIlWc1E9o"

        # # Construct the API endpoint URL
        # endpoint = f"https://api.web3.storage/ipfs/{CIDOfPublicKey}"

        # # Set the authorization header with your access token
        # headers = {"Authorization": f"Bearer {access_token}"}

        # # Make a GET request to retrieve the content
        # response = requests.get(endpoint, headers=headers)

        # if response.status_code == 200:
        #     public_key_from_ipfs = response.content
        #     print("Content of the cid for the public key:", public_key_from_ipfs)

        # print(response.content)


	# Gets the public key from the IPFS decentralized server
	try:
		url = "https://" + CIDOfPublicKey + ".ipfs.dweb.link/"
		headers = {"User-Agent": "Mozilla/5.0"}  # Set a user agent header
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			public_key_from_ipfs = response.text
		else:
			print(f"Failed to retrieve the public key from IPFS. Status code: {response.status_code}")
	except:
		print("error fetching the public key from ipfs")
	

	# # Convert the data to JSON string
	data_to_encrypt = json.dumps(data).encode()

	# Load the PEM public key from ipfs
	public_key = serialization.load_pem_public_key(public_key_from_ipfs.encode(), backend=default_backend())

	# Encrypt the data using the public key - "RSA encryption with Optimal Asymmetric Encryption Padding (OAEP)"
	encrypted_data = public_key.encrypt(
		data_to_encrypt,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
		)
	)

	# Converting the data to Hexadecimal format
	encrypted_base64 = encrypted_data.hex()

	# Writing the results of the encryption file in hexadecimal format to a json file in order to upload it again to ipfs
	encrypted_file_path = "encrypted_data.json"
	with open(encrypted_file_path, "w") as encrypted_file:
		encrypted_file.write(encrypted_base64)

	# Uploading the file to IPFS using the path (saved locally) and then retreving from it the CID connected to the ipfs server
	cid = upload_file_to_ipfs(encrypted_file_path) 

	# Removes the json encrypted file from the computer
	os.remove(encrypted_file_path)

	return cid

# Generating random string ( for Username and Password)
def generate_random_string(length):
    return ''.join(random.choices(string.digits, k=length))