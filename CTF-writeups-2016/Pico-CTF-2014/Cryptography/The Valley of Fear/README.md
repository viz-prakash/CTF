# Pico-CTF 2014: The Valley of Fear 

**Category:** Cryptography
**Points:** 20
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c).)
> The hard drive may be corrupted, but you were able to recover [a small chunk of text](book.txt). Scribbled on the back of the hard drive is a set of mysterious numbers. Can you discover the meaning behind these numbers? (1, 9, 4) (4, 2, 8) (4, 8, 3) (7, 1, 5) (8, 10, 1)

## Write-up
[//]: # (> Your write up goes here.)
> These number in a set represent a word in given text (Paragraph #, Line #, Word #) : First number in set as Paragraph of the Text, Second number as Line in that paragraph, and third as location of actual word in that Line.

> After looking up the words for given triplets, it turns out to be: `The flag is Ceremonial plates`. Flag is `Ceremonial plates`.

## Other write-ups and resources

* None
