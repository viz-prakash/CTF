# Pico-CTF 2014: Snapcat

**Category:** Forensics
**Points:** 80
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c).)
> It was found that a Daedalus employee was storing his personal files on a work computer. Unfortunately, he corrupted the filesystem before we could prove it. Can you take a look? Download [here](https://picoctf.com/problem-static/forensics/snapcat/disk.img).

## Write-up
[//]: # (> Your write up goes here.)
> We run string command over disk.img to see what are the contents inside it and make any guess based on that.
```bash
string disk.img | less

PICTURES
driEEEE
ziEE
.
dniEEEE
niEE
..
dniEEEE
niEE
BILLY   JPG
driEEEE
riEE
LAG    JPG
driEEEE
riEE1
FUZZY   JPG
driEEEE
riEE8
PEW     JPG
driEEEE
riEE
PRECIOUSJPG
driEEEE
riEE
JFIF
ABR#Qabr
3CScq
2ABRb
#3Qarq
+Y!'
ZBY
7V,|
9! P)Z
tV>D
$1ud
z %;
K&Mv
PF]$^
/ygb
LCce
"+Iy
1saV
bRGw&
u6JQ
KOZ!B%
"}y(
{u3HW
)c'g
N9?z
Cb;T
OgO/uK
[5![
Y21f
!gGf
Y|Ip:}J
%Jc|
umYEc7
:
```
> We can see that there are some PICTURES in it. We can use `foremost` to extract files from it using the file headers. `foremost` is a binary which extract files based on the header signatures Running formost on disk.img gives us bunch of images.
```bash 
foremost disk.img
Processing: disk.img
|*|
```
> It extracts some jpg images in [output](output) directory. Looking at images we get the flag in image ![output/jpg/00000237](ouput/jpg/00000237).

> Flag is : **i_can_has_cheezburger**

## Other write-ups and resources

* None
