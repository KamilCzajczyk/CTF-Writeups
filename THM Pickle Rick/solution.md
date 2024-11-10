# Pickle Rick CTF - TryHackMe Room

#### This repository documents my walkthrough for the **Pickle Rick** CTF challenge on [TryHackMe](https://tryhackme.com/r/room/picklerick). 
---
## Simple nmap enumeration

![NMAP](imgs/nmap.png "nmap")

```
nmap -sV TARGET_IP
```
Ports `22 ssh` and `80 http` open

This is how the website looks


![home](imgs/home.png "home")


Znalazłem interesujacy fragment kodu zródłowego, ktos zostawił komentarz który może sugerować login do serwisu `login: R1ckRul3s`


![home](imgs/home_comment.png "home")

I always check `robots.txt` to see if there is something interesting

![robots](imgs/robots.png "robots")

In robots.txt there is `Wubbalubbadubdub` string


I use `dirbuster` to check hidden directories


![dirbuster](imgs/dirbuster.png "dirbuster")

Found `portal.php` and `login.php`

In login form I use previously obtained words as `login: R1ckRul3s password: Wubbalubbadubdub` and i gain access, Im redirected to `portal.php`

![portal](imgs/portal.png "portal")

Gained access to command line, great ! 

 `ls` and `sudo -l` to check what is going on

![ls](imgs/ls.png "ls")

![sudo](imgs/sudol.png "sudo")

> [!IMPORTANT]
> Perfect we can run `sudo` without password

First we read the `clue.txt` and `Sup3rS3cretPickl3Ingred.txt`, but there is a problem the `cat`, `head`, `tail` commands are blocked

`less` command seems to work, we can also use `grep . *`

![clue](imgs/clue.png "clue")
```
sudo less clue.txt
```

![supersecret](imgs/supersecret.png "supersecret")
```
sudo less Sup3rS3cretPickl3Ingred.txt
```

> [!IMPORTANT]
> We obtained our first `FLAG 1 : mr. meeseek hair`
