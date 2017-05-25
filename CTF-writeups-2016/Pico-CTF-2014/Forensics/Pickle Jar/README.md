# Pico-CTF 2014: Pickle Jar

**Category:** Forensics
**Points:** 30
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)
> The police station offers free pickles to police officers. However, someone stole the pickles from the pickle jar! You find a [clue](pickle.jar) on a USB drive left at the scene of the crime.

## Write-up
[//]: # (> Your write up goes here.)
> After downloading the clue it turns out to be a jar named pickle.jar. Jar is just a java archive, to get the content inside of jar We can use any decompiler, offline one like JD(Java decompiler) or any online one like [online decompiler](http://www.javadecompilers.com/). Or simply we can start from uncompressing the jar by any uncompressing program like 7zip, after extracting the jar we got a directory named [com](com) and a file named [pickle.p](pickle.p). Contents inside the pickle.p file is: `S'YOUSTOLETHEPICKLES'p0.` 

> Flag is `YOUSTOLETHEPICKLES`.

## Other write-ups and resources

* None
