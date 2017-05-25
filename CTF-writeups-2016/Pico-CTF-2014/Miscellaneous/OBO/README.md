# Pico-CTF 2014: OBO

**Category:** Miscellaneous
**Points:** 90
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)
> This password changing program was written by an inexperienced C programmer. Can you some find bugs and exploit them to get the flag? The problem can be found at /home/obo/ on the shell server, and the source code can be downloaded [here](obo.c)

## Write-up
[//]: # (> Your write up goes here.)
> [obo.c](obo.c) contains two bugs,

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

const char *password_file_path = "/home/obo/password.txt";

int hex_table[256];

void generate_hex_table(void) {
  int i;
  for (i = 0; i <= 256; ++i) {
    hex_table[i] = -1;
  }

  for (i = 0; i <= 10; ++i) {
    hex_table['0' + i] = i;
  }

  for (i = 0; i <= 6; ++i) {
    hex_table['a' + i] = 10 + i;
  }

  for (i = 0; i <= 6; ++i) {
    hex_table['A' + i] = 10 + i;
  }

  // I don't know why, but I was getting errors, and this fixes it.
  hex_table[0] = 0;
}

int read_password(FILE *file, char *password, size_t n) {
  fgets(password, n, file);
  password[strcspn(password, "\n")] = '\0';
}

void change_password(char *password) {
  char cmd[128];
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  // C is too hard, so I did the password changing in Python.
  snprintf(cmd, sizeof(cmd), "python set_password.py \"%s\"", password);
  system(cmd);
}

int main(int argc, char **argv) {
  int i;
  FILE *password_file;
  int digits[16] = {0};
  char password[64];
  char new_password[64];
  char confirm_password[64];

  generate_hex_table();

  password_file = fopen(password_file_path, "r");
  if (password_file == NULL) {
    perror("fopen");
    return 1;
  }
  read_password(password_file, password, sizeof(password));
  fclose(password_file);

  printf("New password: ");
  fflush(stdout);
  read_password(stdin, new_password, sizeof(new_password));
  for (i = 0; i <= strlen(new_password); ++i) {
    int index = hex_table[(unsigned char) new_password[i]];
    if (index == -1) {
      printf("Invalid character: %c\n", new_password[i]);
      exit(1);
    }
    digits[index] = 1;
  }

  for (i = 0; i <= 16; ++i) {
    if (digits[i] == 0) {
      printf("Password is not complex enough: %d\n", i);
      return 1;
    }
  }

  printf("Confirm old password: ");
  fflush(stdout);
  read_password(stdin, confirm_password, sizeof(confirm_password));
  if (strcmp(confirm_password, password) != 0) {
    printf("Old password is incorrect.\n");
    return 1;
  }

  change_password(new_password);
  printf("Password changed!\n");
  return 0;
}
```

from program it seems like programmer was trying to make a program which check that your password should have all the HEX chars 0-9\[A-F\]or\[a-f] but by `<=16` condition he allowed [A-G]chars. 
> Additional error is when string is contains char 0 which also means NULL or '\0' in C program will exit with status -1 because hex mapping return -1, causing the program to exit even if user have entered a valid password satisfying the constraints. 
> TO enter a password which satisfy the contraint of program we can give input like `0123456789ABCDEFG` then byte[16] will override the password varaible with hex value of 1. And then when confirm password is asked we can give \1 which will mathch with overriden password. After this control directly goes to change_password function which makes a system call : `python set_password.py "0123456789ABCDEFG"`.

```c
snprintf(cmd, sizeof(cmd), "python set_password.py \"%s\"", password);
system(cmd);
```
> To get the flag we can add shell script with name python which prints flag, because our obo binary is executed with special permission, not with permission of user. 
> Create a binary as ~/python and its content is :
```bash
cat ~/python
#!/bin/bash
cat /home/obo/flag.txt
```
> It only cat the content of /home/obo/flag.txt. Once our script is ready we need to add it to `PATH` as `PATH=/home_users/your_username/:$PATH`
> Once PATH is set can execute obo as : ` /usr/bin/python -c 'print "0123456789ABCDEFG"' and it prints the flag as : **watch_your_bounds** 

## Other write-ups and resources

* None
