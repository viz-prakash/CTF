# Pico-CTF 2014: Intercepted Post 

**Category:** Forensics
**Points:** 40
**Total Solves:** Not Available
## Problem Description:
We intercepted some of your Dad's web activity. Can you get a password from his [traffic](https://picoctf.com/problem-static/forensics/intercepted-post/intercept.pcap)?. You can also view the traffic on [CloudShark](https://www.cloudshark.org/captures/5d19d8de342c).

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c).)

## Write-up
[//]: # (> Your write up goes here.)
Looking at the traffic in networks captured packets, we can see there is HTTP communication going on. In a http communicaiton normal way of doing communicaiton is first HTTP get to get the login page and then HTTP post with Username and Password. Looking for a HTTP POST requst packet with username and password, after HTTP GET request gives will give us the flag as `flag%7Bpl%24_%24%24l_y0ur_l0g1n_form%24%7D`. Using any Unicode to ascii converter we get the Flag is `pl$_$$l_y0ur_l0g1n_form$`. ![HTTP Post Request](/cloudshark-capture?raw=true "HTTP Post Requst Packet content")

## Other write-ups and resources

* None
