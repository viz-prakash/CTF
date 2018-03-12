#!/usr/bin/env python
from Crypto.Cipher import AES
import os
import sys 
import re 

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

def xorit(s1, s2):
    print "in xorit"
    print s1
    print s2
    output = ""
    for i in range(len(s1)/2):
        #print i
        temp = "%02X" % (ord(s1[i*2: i*2+2].decode('hex')) ^ ord(s2[i*2: i*2+2].decode('hex')))
        #print temp
        output +=temp
    print output
    return output

class FlagGetter:
  def __init__(self):
    
    self.key = os.urandom(16)
    self.blocksize = 16
  
  def _pad(self,string):
    padlen = self.blocksize - (len(string) % self.blocksize)
    return string + ( chr(padlen) * padlen)
  
  def _unpad(self,string):
    padlen = string[-1]
    return string[:-ord(padlen)]

  def getUserInput(self):
    line = sys.stdin.readline()
    return re.sub("[^A-Za-z0-9]","",line)

  def auth_token(self):
    print "Input your username"
    username = self.getUserInput()
    
    print "Input your password"
    password = self.getUserInput()
    
    iv = os.urandom(16)
    cipher = AES.new( self.key, AES.MODE_CBC, iv)
    string = self._pad( "username:" + username + ";password:" + password + ";type:user" )
    return (iv + cipher.encrypt(string)).encode('hex')

  def getFlag(self):
    flag = "flag{testestest}"
    if self.checkAdmin():
      print "Flag: '" + flag + "'"
      return True
   
    print "Sorry only admins can get flags"
    return False

  def checkAdmin(self):
    print "What was your profile again?"
    enc = self.getUserInput()
    if ( len(enc) < 32 ) or ( len(enc) % 32 > 0 ):
      print "Profile not valid"
      return False
    enc = enc.decode('hex')

    iv = enc[:16]
    profile = enc[16:]
    
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    plain = cipher.decrypt(profile)
    parts = self._unpad(plain).split(";")

    print "DEBUG: plain = " + str(plain)
    print "DEBUG: iv = " + iv.encode('hex')
    print "DEBUG: key = ", self.key.encode('hex')

    for p in parts:
      pair = p.split(':')

      if pair[0] == 'type' and pair[1] == 'admin':
        return True
    
    return False

def xor_string_n_hexstr(expected_out, seed):
    guessed = ""
    for i in range(len(seed)/2):
        hex_ch = seed[i*2:i*2+2]
        for j in range(255):
            if ord(expected_out[i]) == j ^ ord(hex_ch.decode("hex")):
                guessed += "{:02X}".format(j)
                break
    return guessed


fg = FlagGetter()
aut = fg.auth_token()

###solution starts here##
print aut
full_iv = aut[:32]
print "full iv: " + aut[:32]
last_5 = aut[22:32]

"""
we want to know what is decipherd content of last six bytes,
which can be calculated by xoring the known expected out and IV used,
We know the IV, as it's last six bytes of previous block.
"""
iv_for_block2 = aut[32+20: 64]
"""
block two that is going to be decrypted.
Our only interest is last 6 bytes which is known: user\x2\x2
"""
deciphered_block2 = xor_string_n_hexstr("user" + chr(2) + chr(2), iv_for_block2)
"""
Now we want to change the IV in such way that when xored with dechpherd block 2,
it's results in just admin\x1 instead of "user\x2\x2". \x1 is important as it
will only chop out \x1 from the end after unpadding, as this is the last block.
"""
expected_block1_out = xor_string_n_hexstr("admin" + chr(1), deciphered_block2)

aut = aut[:32+ 20] + expected_block1_out + aut[64:]
print "new input: " + aut
###Solution ends here ###
NumTries = 10
for i in range(0, NumTries):
  if fg.getFlag():
    break
  print "Let's try that again... (" + str(9 - i) + " Attempts remaining)" 

