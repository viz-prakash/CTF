# Pico-CTF 2014: Function Address

**Category:** Reverse Engineering
**Points:** 60
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)

## Write-up
[//]: # (> Your write up goes here.)
> To figure out the address of a function in given binary first we need to check whether PIE is enabled or disabled, because if enabled function address might get changed at every run.
> To check whether PIE is enable in a binary or not we can use:
```bash
 /usr/sbin/execstack -q problem
 - problem
 ```
\- represent PIE is disabled in binary.

> Now to get the address we can use gdb:

```bash
gdb problem
GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from problem...(no debugging symbols found)...done.
(gdb) p &find_string
$1 = (<text variable, no debug info> *) 0x8048444 <find_string>
(gdb) q
```
> Flag is : 8048444

## Other write-ups and resources

* None
