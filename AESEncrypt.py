from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
import base64

def binEncrypt(ori, pwd):

	h = SHA256.new()
	h.update(pwd)
	key = (h.hexdigest())

	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key[:32], AES.MODE_CFB, iv)
	msg = iv + cipher.encrypt((ori))

	return base64.b64encode(msg)


def binDecrypt(msg, pwd):

	h = SHA256.new()
	h.update(pwd)
	key = (h.hexdigest())

	msg_ori = base64.b64decode(msg)
	iv = msg_ori[:AES.block_size]
	decipher = AES.new(key[:32], AES.MODE_CFB, iv)
	ori = decipher.decrypt((msg_ori[AES.block_size:]))

	return ori


if __name__ == '__main__':

	test = 'Today is 2017.09.12'
	msg = binEncrypt(test, '123456')
	print msg
	print binDecrypt(msg, '123456')
