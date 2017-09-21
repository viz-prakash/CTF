from pwn import *
padding=bytearray("0"*16)
padding.insert(0,'}') # this is known
possible_chars="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_" 
#failed with this possible_chars

def communicate(data):
    conn = remote("crypto.chal.csaw.io", port=1578)
    conn.sendlin(data)
    return conn.recvline()[53:]

def parse_response(response):
    return (response[:32], response[96:128])

def breaking():
    conn = remote("crypto.chal.csaw.io", port=1578)
    right_guess = ""
    for count in xrange(0, 26, 1):
        padding.insert(0,'?')
        print("=====================")
        for char in range(0x20, 0x7e):
            padding[0]=chr(char)
            conn.sendline(padding)
            enc_response = conn.recvline()[53:]
            guess = parse_response(enc_response)
            guess_part1 = guess[0]
            guess_part2 = guess[1]
            if guess_part1 == guess_part2:
                right_guess = chr(char) + right_guess
                print("flag so far: flag{0}{1}{2}".format('{', right_guess, '}'))
                print(':'.join("{:02x}".format(ord(c)) for c in right_guess))
                break;


if __name__ == "__main__":
    breaking()
