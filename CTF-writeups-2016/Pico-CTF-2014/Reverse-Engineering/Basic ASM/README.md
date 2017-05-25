# Pico-CTF 2014: Basic ASM

**Category:** Reverse Engineering
**Points:** 60
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)
> We found this program snippet.txt, but we're having some trouble figuring it out. What's the value of %eax when the last instruction (the NOP) runs?

## Write-up
[//]: # (> Your write up goes here.)
> We need to figure out the value of %eax and that will be our flag.

```asm
# This file is in AT&T syntax - see http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
# and http://en.wikipedia.org/wiki/X86_assembly_language#Syntax. Both gdb and objdump produce
# AT&T syntax by default.
MOV $19160,%ebx
MOV $23587,%eax
MOV $14051,%ecx
CMP %eax,%ebx
JL L1
JMP L2
L1:
IMUL %eax,%ebx
ADD %eax,%ebx
MOV %ebx,%eax
SUB %ecx,%eax
JMP L3
L2:
IMUL %eax,%ebx
SUB %eax,%ebx
MOV %ebx,%eax
ADD %ecx,%eax
L3:
NOP
```
> What program trying to do is it first store values in registers eax and ebx. Then compare %eax register with %ebx register.
In AT&T syntax, the operation checks if the second element is less than the first element. 
If this is true it follows the first jump statement, and if it is false, it jumps to the second jump statement. 
In this case %ebx is less than %eax (19160 < 23587), so the program follows the path into the L1 function. 
Then it multiplies eax and ebx and stores the result in ebx, so ebx have now 451926920.
Then it subtract eax which have 23587 and from ebx and store it to ebx so ebx has 451903333.
Next it add ecx which has 14051 to eax after copying value of ebx to eax, now eax has 451917384.

> Flag is : **451917384**.

## Other write-ups and resources

* None
