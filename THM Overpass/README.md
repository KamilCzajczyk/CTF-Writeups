# Overpass CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Overpass** CTF challenge on [TryHackMe](https://tryhackme.com/room/overpass). 
---


scan

![scan](imgs/scan.png "scan")

![ferox](imgs/ferox.png "ferox")

found /admin login page

first tried SQLi, found files responisble for login handling `login.js` and `cookie.js`

![js](imgs/js.png "js")

i added cookie manually to check if it would work

![cookie](imgs/cookie.png "cookie")

gained access to /admin panel and got james ssh key

![adminpanel](imgs/adminpanel.png "adminpanel")


the key has a passphrase and the info on the panel says we should crack it

using `ssh2john > hash.txt` and then `john --wordlist=rockyou.txt hash` to crack a passphrase

now logged as james and grabbing user flag

![sshjames](imgs/sshjames.png "sshjames")

`todo.txt`:

![todo](imgs/todo.png "todo")

i checked hidden `.overpass` file to extract saved passwords, found one

![creds](imgs/creds.png "creds")

checked for `sudo -l` with that password but we cant use it

checked the /etc/crontab and found script that might be our PE factor

![cron](imgs/cron.png "cron")

the script makes web request to download file and then execute it with bash

the scirpt has host: overpass.thm so i checked the /etc/hosts, we can modify it, i will change the loopback address to my attacking machine address

![hosts1](imgs/hosts1.png "hosts1")

![hosts2](imgs/hosts2.png "hosts2")

we need to create the same file structure on local machine so creating `overpass/downloads/src` and inside it a reverse-shell script called buildscript.sh

![revgen](imgs/revgen.png "revgen")

started the simple python server in overpass and also starting nc listiner to catch revshell

now we need to wait for cron

![http](imgs/http.png "http")

we got root access and root flag

![root](imgs/root.png "root")

## SYSTEM PWNED
