# AlexCTF 2017: CR3

**Category:** Cryptography
**Points:** 150
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c).)
> What is this encryption?

> Fady assumed this time that you will be so n00b to tell what encryption he is using
he send the following note to his friend in plain sight :

> p=0xa6055ec186de51800ddd6fcbf0192384ff42d707a55f57af4fcfb0d1dc7bd97055e8275cd4b78ec63c5d592f567c66393a061324aa2e6a8d8fc2a910cbee1ed9

> q=0xfa0f9463ea0a93b929c099320d31c277e0b0dbc65b189ed76124f5a1218f5d91fd0102a4c8de11f28be5e4d0ae91ab319f4537e97ed74bc663e972a4a9119307

> e=0x6d1fdab4ce3217b3fc32c9ed480a31d067fd57d93a9ab52b472dc393ab7852fbcb11abbebfd6aaae8032db1316dc22d3f7c3d631e24df13ef23d3b381a1c3e04abcc745d402ee3a031ac2718fae63b240837b4f657f29ca4702da9af22a3a019d68904a969ddb01bcf941df70af042f4fae5cbeb9c2151b324f387e525094c41

> c=0x7fe1a4f743675d1987d25d38111fae0f78bbea6852cba5beda47db76d119a3efe24cb04b9449f53becd43b0b46e269826a983f832abb53b7a7e24a43ad15378344ed5c20f51e268186d24c76050c1e73647523bd5f91d9b6ad3e86bbf9126588b1dee21e6997372e36c3e74284734748891829665086e0dc523ed23c386bb520

> He is underestimating our crypto skills!

## Write-up
[//]: # (> Your write up goes here.)
(TODO)
> We are given p, q (prime numbers), e(public key), and c(encrypted message), looking at these values it's clear that encryption in use is RSA. First things that comes to mind after looking at RSA construct is, if we can decrypt the encrypted part that might give us the flag. Let's proceed on our guess.

> We are given p, q, e, and c. Unkowns are N(Moduls), Toteint, and d(private part). Let's proceed step by step. We can calculate N easily from given p and q. Similarly we can calculate totient function (phi) as (p-1)(q-1). After calculating phi we can get d from de % phi = 1. Once we got the d we can decrypt the message c^d mod N. Python script to so is below:

```python
#!/usr/bin/python
import libnum

p="0xa6055ec186de51800ddd6fcbf0192384ff42d707a55f57af4fcfb0d1dc7bd97055e8275cd4b78ec63c5d592f567c66393a061324aa2e6a8d8fc2a910cbee1ed9"
p_int=int(p,16)
q="0xfa0f9463ea0a93b929c099320d31c277e0b0dbc65b189ed76124f5a1218f5d91fd0102a4c8de11f28be5e4d0ae91ab319f4537e97ed74bc663e972a4a9119307"
q_int=int(q,16)
e="0x6d1fdab4ce3217b3fc32c9ed480a31d067fd57d93a9ab52b472dc393ab7852fbcb11abbebfd6aaae8032db1316dc22d3f7c3d631e24df13ef23d3b381a1c3e04abcc745d402ee3a031ac2718fae63b240837b4f657f29ca4702da9af22a3a019d68904a969ddb01bcf941df70af042f4fae5cbeb9c2151b324f387e525094c41"
e_int=int(e,16)
c="0x7fe1a4f743675d1987d25d38111fae0f78bbea6852cba5beda47db76d119a3efe24cb04b9449f53becd43b0b46e269826a983f832abb53b7a7e24a43ad15378344ed5c20f51e268186d24c76050c1e73647523bd5f91d9b6ad3e86bbf9126588b1dee21e6997372e36c3e74284734748891829665086e0dc523ed23c386bb520"
c_int=int(c,16)
N=(p_int * q_int)
phi=(p_int - 1 ) * (q_int - 1)
d_int = libnum.invmod(e_int, phi) # de%phi= 1 or de = 1 (mod phi)
m=pow(c_int, d_int, N)
print "Decrypted Message (M) : {}".format(m)
hex_m=hex(m)
print "Decrypted Message (M) in hex : {}".format(hex_m)
print hex(m)[2:-1].decode("hex")
```

> Flag is **ALEXCTF{RS4_I5_E55ENT1AL_T0_D0_BY_H4ND}**

## Other write-ups and resources

* None
