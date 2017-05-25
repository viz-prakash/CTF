# Pico-CTF 2014: Supercow

**Category:** Forensics
**Points:** 40
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)
Daedalus Corp. has a special utility for printing .cow files at /home/daedalus/supercow. Can you figure out how to get it to print out the flag?

## Write-up
[//]: # (> Your write up goes here.)
> Looking at the code present in supercow.c file it easy to comprehend that `supercow` binary present in directory /home/daedalus/supercow is utility which prints files with extension .cow and one aditional thing about this binary is it runs with the permisions of problem setter not with user accessing it. Looking in the directory we can see there is file name flag.txt which probably have the flag but other users don't have the read and write permission to it so we can't directly cat the content of it. We can use the supercow binary for reading it but, extension of our target file is `.txt` so we can't directly print its content. Additionally we only have read permission in the directory, so we can't rename the flag.txt to flag.cow to print it's content using supercow binary. What we can do is we can create a link for flag.txt in directory where we have read write access. 

> We can create link with command `ln -s flag.txt ~/flag.cow`. After creating the link pass the ~/flag.cow to supercow binary as: `supercow ~/flag.cow` and it print the content of flag.txt. Flag is `cows_drive_mooooving_vans`.

## Other write-ups and resources

* None
