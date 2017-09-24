# CSAW-2017 Qualifiers: Another%32Xor

**Category:** Cryptography
**Points:** 100
**Total Solves:** 224
## Problem Description:

![Image](Another_Xor.PNG?raw=true "Problem Statement")

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)

## Write-up
[//]: # (> Your write up goes here.)
> This was the first first problme in Crypto category point wise so, I started with this. It is given with a program used for encryption, [cipher.py](cipher.py), and cipher [encrypted](encrypted) with it. Looking at the code in [cipher.py](cipher.py) tells that first argument is key and it is used to encrypt whateven given as second argument. `xor function` is simple it take 2 positional string arguments and xor them out, in bit different manner than simple xor but operation is anologous to xor, and generate a char for a char upto length of minimum of both the input strings. XOR operation is simple exlained below with plain_text(p), key(k), and cipher(c):
```
if:
	p xor k = c
then below hold true:
	c xor k = p and, 
	c xor p = k
```
To get the flag either argument-1 or argument-2 is required but problem doesn't provide any of those. We can solve it with any one of those as following: if key is known we can repeat the keys till the length of encrypted and call the `xor function` with this repeated keys and it will xor out the key from encrypted content and will give back the argument-2, if argument-2 is given simply xoring with `encrypted` will give back the key repeated till lenght of `encrypted`. This is just what I explained earlier property of xor operation. Now solution was easy if any of those was provided, but it is not. So, it needs to be figured out. It's known that flag will begin with `flag{` and it can be argument-1 or argument-2. If `flag{` is in argument-1, let's call it key, it will be repeated at least twice as key is also added to the argument-2 andlet's call it plain_text. Few things to note are: 

* With 'flag{` as key first five charcters of the output is going to be useful as it is sure that that is either present in key plain_text. For now, we can say that is going to be plain_text as we are assuming key starts with `flag{`. 
* 32 byte or char of md5 is also added to (plain_text + key) before encryption. So, actual length of plain_text and key will be len(encrypted) - 32. 

```
key = "flag{"
def decryption(filename):
	with open(filename) as handle:
		content = handle.read()
	content = content[:-1].decode('hex')
	deciphered = xor(content, repeat(key, len(content)))
	print(deciphered)

if __name__ == "__main__":
	decryption(sys.argv[1])
```

Adding above function at the end of file [encrypted](encrypted) and commenting out the encryption part can used to decryption. Running this program with input [encrypted](encrypted) gives this output:

```
Another Xor$ python cipher.py encrypted
Encoded content length: 137
Encoded content lenght with out md5: 105
plaintext + key: A quagl(<+K9}2mdR?&}Kbl)NhlP(/f}e/sitB>7ta~j5&a5-lx8(px%kfw#x y|fx =c}n3|#eivgya'k}7'!~zl{lt|fi$o.ed%`kn
md5: f<p;+><"%x$5%7w<"l%o!u.,na%#^ /
``` 

> Observing the output complementary part of `flag{` is `A qua`. Length of plain_text + key is 105.

*) The md5 part at the end will only consist of only HEX charcters, if key is repeated till the length of plain_text + key + md5, there is chance that at some place in the md5 this begining part of key would be used in xor operation, after the decryption that part should be hex chars. Since here 5 char long key is used we should get atleast 5 consecutive hex chars in last 32 bytes. If not we will switch the assumption, that means `flag{` is not in key it's in plain_text and complementary part `A qua` is begining of the key.

```
key = "flag{"
import string
def is_hex(s):
     hex_digits = set(string.hexdigits)
     # if s is long, then it is faster to check against a set
     return all(c in hex_digits for c in s)

def leaker(filename):
	with open(filename) as handle:
		content = handle.read()
	ciphertext = content[:-1].decode('hex')
	for i in xrange(105,len(ciphertext), 1):
		decoded = xor(ciphertext[i: i + len(key)], key)
		#print("{2}: {0}:hex {1}".format(decoded, ":".join("{:02x}".format(ord(c)) for c in decoded), i))
		#decoded.decode('hex')
		if is_hex(decoded):
			print("{2}: {0}:hex {1}".format(decoded, ":".join("{:02x}".format(ord(c)) for c in decoded), i))
```

Looking at the output we see that there is no where in the ouput where 5 hex chars or less than 5 from positions after 132 are occuring consecutively. And as per the hint in the problem that flag is in plain_text part not in key, let's switch the assumption and see the output whether it contains consicutive 5 chars or not. Only change will be `key = "A qua"` and output is :

```
134: df2:hex 64:66:32
```

> Observing this we can say that last 3 char of md5 were xored with `fla`. This means length of key*repetetions is 134. Possible factor of 134 are 1, 67, 134. Out of these 3 only possible length is 67, total length is 134 for key + plain_text. If key length  is 67 then plain_text length is 105-67 => 38. Once we got the lengths we can use this `A qua` at the 67th index and get original content from plain_text + key. As 67th position is happened to be in Key because plain_text is only 38 bytes long. The these 5 chars will be at  (67-38) = 29th position in key. Once we get the key at 29-33rd position we can leak another part of plain_text + key at 67 + 29 = 96th position which is key as it's after 38, it's position in key will be 96 - 38= 58th in key. Leaker function above can be used for this just need modify the indexes of operation. Using this continuously if we can leak parts from plain_text + key if it's after 38 it's in key part other it's plain part which is argument-2. Another thing to note is if we get to know the part key more than 38 we can leak the part of key from 1-28 as this will be between 39-66 in plain_text + key. We can utilize the intersection from plaint_text part as well as repeated key part to leak more parts of key. Once we get to know the first 38 chars of key we can pass it first decryption() function to get the key. Using this first 38 char of key is: `A quart jar of oil mixed with zinc oxi`. Passing this and hex decoded encrypted content to function decryption() gives the flag `flag{sti11_us3_da_x0r_for_my_s3cratz}`.

## Other write-ups and resources

* None
