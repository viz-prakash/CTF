import gmpy2, libnum, binascii
import key_data
import sys

def main():
	f=open(sys.argv[1], "r")
	cipher_str=f.read()
	print "cipher going to be decrypted: ", cipher_str
	cipher=int(cipher_str,16)
	msg=gmpy2.powmod(cipher,key_data.d,key_data.N)
	print "decrypted string : ", libnum.n2s(msg)

if __name__ == "__main__":
	main()
