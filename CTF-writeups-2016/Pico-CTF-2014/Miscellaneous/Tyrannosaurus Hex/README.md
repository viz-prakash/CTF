# Pico-CTF 2014: Tyrannosaurus Hex

**Category:** Miscellaneous
**Points:** 10
**Total Solves:** Not Available
## Problem Description:
> The contents of the flash drive appear to be password protected. On the back of the flash drive, you see the hexadecimal number 0x4355a5e6 scribbled in ink. The password prompt, however, only accepts decimal numbers. What number should you enter?
[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c).)

## Write-up
[//]: # (> Your write up goes here.)
As question suggests, we are presented with hexadecimal number and we need to give input decimal number as a password, so we need to convert the `hexadecimal number` to `Decimal number`. For conversion we can use [ WolframAlpha](http://www.wolframalpha.com/), conversion of 0x4355a5e6 in decimal is `1129686502`.

## Other write-ups and resources

* None
