# Library CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Library** CTF challenge on [TryHackMe](https://tryhackme.com/r/room/bsidesgtlibrary). 
---

Nmap scan


![nmap](imgs/nmap.png "nmap")

Main page: 

![page](imgs/page.png "page")

`Robots.txt`:

![robots](imgs/robots.png "robots")

`Rockyou` string might suggest easy crackable password

I will try to use `hydra` to try to login to `ssh` as meliodas

```bash
hydra -l meliodas -P /usr/share/wordlists/rockyou.txt 10.10.127.137 ssh -t 4

```

![hydra](imgs/hydra.png "hydra")

SSH connection:

![ssh](imgs/ssh.png "ssh")


> [!IMPORTANT]
> `Meliodas` password : `iloveyou1`
> 
> First flag from `user.txt` : `6d488cbb3f111d135722c33cb635f4ec`

