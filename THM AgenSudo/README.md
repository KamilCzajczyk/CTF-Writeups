# Agent Sudo CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Agent Sudo** CTF challenge on [TryHackMe](https://tryhackme.com/room/agentsudoctf). 
---

nmap scan 

![nmap](imgs/nmap.png "nmap")

![1](imgs/1.png "1")

on the website we see note from agent `R` telling us that we should change user-agent to our own codename, i think that other codenames could also be one letter so i created a file with all the letters and prepared sniper attack in burpsuite

![burp1](imgs/burp1.png "burp1")

there is one odd response with 302 code suggesting redirection 

![burp2](imgs/burp2.png "burp2")

now checking the website as `user-agent: C` and we see a note to `chris` (having a weak password) we also know about potential agent `J`
i tried changing user-agent to J but it doesnt seem to work

![note1](imgs/note1.png "note1")

didnt find hidden folders with feroxbuster

tryhackme suggest to find FTP password so i will try log in as chris to ftp (chris should hace weak password)

![crack](imgs/crack.png "crack")

it worked only for FTP

![ftp](imgs/ftp.png "ftp")

few files including 2 images and a txt note

![note2](imgs/note2.png "note2")

note says that password is hidden inside image

after using binwalk we see that there is something in file `cutie.png`

![binwalk](imgs/binwalk.png "binwalk")

extracting files with `binwalk -e cutie.png`

there are 3 file `365` `365.zlib` oraz `8702.zip`, zlib and zip files are password protected so i will try JohnTheRipper

![john](imgs/john.png "john")

we cracked the hash and now we have password to zip file

![john2](imgs/john2.png "john2")

`7z x 8702.zip`

we have another note `To_agentR.txt`

![note3](imgs/note3.png "note3")

string QXJlYTUx is decoded to Area51 from base64

tryhackme says we need to find `STEG password` , so there should a message hidden inside a file (probably the other picture), i will try the Area51 as a password 

```
steghide extract -sf cute-alien.jpg 
```

in `cute-alien.jpg` was hiding `message.txt`

![note4](imgs/note4.png "note4")

ok so now we know that next known user is james and we got his password

trying to ssh as james worked and now we got user flag

![user](imgs/user.png "user")

we also need to provide the name of the incident from photo, just using google image searching and finding foxnews article, the answer is `Roswell alien autopsy` 

i started with linpeas to find PE factor

![linpeas](imgs/linpeas.png "linpeas")

found nothing interesting but `sudo -l` output is intriguing

found the `CVE-2019-14287 -> sudo Vulnerability Allows Bypass of User Restrictions`

![cve](imgs/cve.png "cve")

our machine sudo version is 1.8.21p so its vulnerable 

we just need to run simple command

```
$ sudo -u#-1 /bin/bash
```
and now we are root and we can grab a root flag and we also know the answer to the last question, who is agent R


![root](imgs/root.png "root")

## MACHINE PWNED
