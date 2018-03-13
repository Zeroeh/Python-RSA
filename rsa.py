#!/usr/bin/env python3

#with python3, do 'sudo pip3 install cryptodome' not sure if it's 100% required though

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

__author__ = 'Zeroeh'

#need to be byte strings
player_email = b'email@mail.com'
player_password = b'password123'

pub_key = ("-----BEGIN PUBLIC KEY-----\n"
			"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDCKFctVrhfF3m2Kes0FBL/JFeO\n"
			"cmNg9eJz8k/hQy1kadD+XFUpluRqa//Uxp2s9W2qE0EoUCu59ugcf/p7lGuL99Uo\n"
			"SGmQEynkBvZct+/M40L0E0rZ4BVgzLOJmIbXMp0J4PnPcb6VLZvxazGcmSfjauC7\n"
			"F3yWYqUbZd/HCBtawwIDAQAB\n"
			"-----END PUBLIC KEY-----")

def main():
	pub_key_obj = RSA.importKey(pub_key)
	
	cipher = PKCS1_OAEP.new(pub_key_obj)

	enc_msg = cipher.encrypt(player_password)

	nemsg = base64.b64encode(enc_msg)

	print(enc_msg.hex())
	print(nemsg)

if __name__ == '__main__':
	main()
