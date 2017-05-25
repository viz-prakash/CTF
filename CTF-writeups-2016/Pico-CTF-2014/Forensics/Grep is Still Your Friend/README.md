# Pico-CTF 2014: Grep is Still Your Friend 

**Category:** Forensics
**Points:** 00
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)
> The police need help decrypting one of your father's files. Fortunately you know where he wrote down all his backup decryption keys as a backup (probably not the best security practice). You are looking for the key corresponding to daedaluscorp.txt.enc. The file is stored on the shell server at /problems/grepfriend/keys .

## Write-up
[//]: # (> Your write up goes here.)
> We know that /problems/grepfriend/keys have keys stored in it. Looking at its content we can see that it store keys in `key value` pair fashion. To get key for `daedaluscorp.txt.enc` we can use the command: `grep "daedaluscorp.txt.enc" /problems/grepfriend/keys` it will print the line where key is daedaluscorp.txt.enc. 
> This gives us the flag: `b2bee8664b754d0c85c4c0303134bca6`.


## Other write-ups and resources

* None
