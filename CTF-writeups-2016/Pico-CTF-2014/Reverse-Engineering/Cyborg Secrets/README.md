# Pico-CTF 2014: Cyborg Secrets

**Category:** Reverse Engineering
**Points:** 80
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c)
> You found a password protected binary on the cyborg relating to its defensive security systems. Find the password and get the shutdown code! You can find it on the shell server at /home/cyborgsecrets/cyborg-defense or you can download it [here](https://picoctf.com/problem-static/reversing/cyborg-secrets/cyborg_defense). 

> **Hint** : I wonder if they hardcoded the password string.

## Write-up
[//]: # (> Your write up goes here.)
> As the hint suggest password might be hardcoded in program. Probably extracting all the strings from binary might give us password.

```bash
tdP
/lib/ld-linux.so.2
libc.so.6
_IO_stdin_used
puts
putchar
printf
strcmp
__libc_start_main
__gmon_start__
GLIBC_2.0
PTRh0
[^_]
ZogH
TODO: REMOVE DEBUG PASSWORD!
DEBUG PASSWORD: 2manyHacks_Debug_Admin_Test
______               _       _             _____
|  _  \             | |     | |           /  __ \
| | | |__ _  ___  __| | __ _| |_   _ ___  | /  \/ ___  _ __ _ __
| | | / _` |/ _ \/ _` |/ _` | | | | / __| | |    / _ \| '__| '_ \
| |/ / (_| |  __/ (_| | (_| | | |_| \__ \ | \__/\ (_) | |  | |_) |
|___/ \__,_|\___|\__,_|\__,_|_|\__,_|___/  \____/\___/|_|  | .__/
                                                           | |
                                                           |_|
Please include a password command line argument.
Password: %s
2manyHacks_Debug_Admin_Test
Access Denied
Authorization successful.
;*2$"
GCC: (Ubuntu 4.8.4-2ubuntu1~14.04) 4.8.4
GCC: (Ubuntu 4.8.2-19ubuntu1) 4.8.2
```

> We can see a password like string ``2manyHacks_Debug_Admin_Test``. Executing the binary with this as argument gives us the flag.

```bash
./cyborg_defense 2manyHacks_Debug_Admin_Test
______               _       _             _____
|  _  \             | |     | |           /  __ \
| | | |__ _  ___  __| | __ _| |_   _ ___  | /  \/ ___  _ __ _ __
| | | / _` |/ _ \/ _` |/ _` | | | | / __| | |    / _ \| '__| '_ \
| |/ / (_| |  __/ (_| | (_| | | |_| \__ \ | \__/\ (_) | |  | |_) |
|___/ \__,_|\___|\__,_|\__,_|_|\__,_|___/  \____/\___/|_|  | .__/
                                                           | |
                                                           |_|
Password: 2manyHacks_Debug_Admin_Test
Authorization successful.
403-shutdown-for-what
```

> Flag is **403-shutdown-for-what**

## Other write-ups and resources

* None
