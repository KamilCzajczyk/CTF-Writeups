# Lian_Yu CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Lian_Yu** CTF challenge on [TryHackMe](https://tryhackme.com/room/lianyu). 
---


found 3 open ports 21, 22, 80

![scan](imgs/scan.png "scan")

using feroxbuster to find hidden files

![ferox](imgs/ferox.png "ferox")

we found `/island` and `/island/2100`

we found `vigilante` code word and its valid login for ftp , now we need to find a password

![vig](imgs/vig.png "vig")

we see info about `.ticket` file, I will use ffuf to try to find this file

![tick](imgs/tick.png "tick")

```
ffuf -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt:FUZZ -u http://$IP/island/2100/FUZZ.ticket 
```

![ffuf](imgs/ffuf.png "ffuf")

we found token, we got hint that the password might be base ecoded, i tested on cyberchef and found that ic could be base58

![ga](imgs/ga.png "ga")

we can login to ftp now, and we found 3 files image

![ftp1](imgs/ftp1.png "ftp1")

i also checked the folder parent folder in ftp `cd ..` and found 2 directories, one looks like the user we logged as and there is another now, maybe it will be our ssh login for next steps `slade`

![ftp2](imgs/ftp2.png "ftp2")

the `Leave_me_alone.png` was corupted, i used ghex to change the first bytes to match correct png standard, now we can open png as normal image

![hex](imgs/hex.png "hex")

now we have password for something

![pic](imgs/pic.png "pic")

`.jpg` file stands out because you cant hide files inside png files with steghide

after using 

```
steghide extract -sf aa.jpg 
```

we found hidden `ss.zip` zip file

after extracting we found the hidden file name : shado, containing probably a password

we got user access and found user flag

![user](imgs/user.png "user")

checking `sudo -l` and we might found our PE factor

![sudol](imgs/sudol.png "sudol")

after checking GTFObins and using this one-liner

![gtfo](imgs/gtfo.png "gtfo")

```
sudo /usr/bin/pkexec /bin/bash 
```

we have root access and root flag

![root](imgs/root.png "root")

# MACHINE PWNED
