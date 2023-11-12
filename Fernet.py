from cryptography.fernet import Fernet

def Encryption(input_file):
	# Generate a key for encryption (do this once and keep the key secret)
	key = b'ZMpTIe-1buNOGDFBFSlgLpRQ0GsiifWAPA7-LR2nntM='
	# Create a Fernet cipher object with the key
	cipher_suite = Fernet(key)

	output_file = "Encrypted_File.txt"

	with open(input_file, 'rb') as sourceFile, open(output_file, 'wb') as destFile:
		for line in sourceFile:
	    		# Encrypt the data
			encrypted_data = cipher_suite.encrypt(line)
			destFile.write(encrypted_data)
			destFile.write(b"\n")
		

	print(f"Encryption complete. Encrypted data is saved in '{output_file}'.")
	print(f"Encryption Key: {key.decode('utf-8')}")

