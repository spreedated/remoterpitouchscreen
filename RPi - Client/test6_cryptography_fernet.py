from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# print(key)
key ='kLAyNzxyEGUR6kdVfunVXPt9iqxxejgqxsroRFrm3yQ='

#Encode
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b'<yourpasshere>')   #required to be bytes
print(ciphered_text)

#Decode
# ciphered_text = b'gAAAAABc_epM2hq8XsqtQBZn1bFb5q8X_5dX0rpQ-4FIPnLVj45xOvZAR2pml18idfbDpedAM0J1Ds28EcdLAz6TI-Tgtwfh0SolociwKap60bqAnrMnQ4k='
#
# unciphered_text = (Fernet(key).decrypt(ciphered_text))
# print(unciphered_text.decode("utf-8"))
