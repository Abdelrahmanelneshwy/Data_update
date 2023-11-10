from cryptography.fernet import Fernet

def Decryption(input_file):
# Provide the Fernet key (replace with the actual key used for encryption)
	key = b'ZMpTIe-1buNOGDFBFSlgLpRQ0GsiifWAPA7-LR2nntM='

	# Create a Fernet cipher object with the key
	cipher_suite = Fernet(key)

	# Data to be decrypted
	output_file = "update.txt"

	with open(input_file, 'rb') as sourceFile, open(output_file, 'wb') as destFile:
		for line in sourceFile:
			try:
				# Decrypt the data and write it to the destination file
				decrypted_data = cipher_suite.decrypt(line)
				print(line)
				print(decrypted_data)
				destFile.write(decrypted_data)
			except Exception as e:
				print(f"Error decrypting: {e}")

		print(f"Decryption complete. Decrypted data is saved in '{output_file}'.")

Decryption("update.txt")
