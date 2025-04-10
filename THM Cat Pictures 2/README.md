# Cat Pictures 2 CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Cat Pictures 2** CTF challenge on [TryHackMe](https://tryhackme.com/room/catpictures2). 
---

we see open ports: 22,80,222,1337,3000,8080

![scn](imgs/scn.png "scn")

feroxbuster scan but we dont have permissions for most of them

![ferox](imgs/ferox.png "ferox")

in one of the pictures we see Description: strip metadata

![d](imgs/d.png "d")

if we run exiftool on this picture we can find `:8080/REDACTED.txt`

![e](imgs/e.png "e")

from this txt file we got user and password

![n](imgs/n.png "n")

now we can login into gitea on port 3000, we can find first flag there

![git](imgs/git.png "git")

![g1](imgs/g1.png "g1")

![f](imgs/f.png "f")

if we head to port 1337 we can see actions that we can execute 

![1337](imgs/1337.png "1337")

by look at logs of the action, we see that ansible code is executing

![l](imgs/l.png "l")

we can modify it to include reverse shell

![c](imgs/c.png "c")

we got access as bismuth we can grab second flag, we also can grab his private key for stable access

![f2](imgs/f2.png "f2")

after transfering linpeas we see that we have vulnerable sudo version

![sd](imgs/sd.png "sd")

we can use this to exploit `https://github.com/blasty/CVE-2021-3156`

```
--- our machine ---
$ git clone https://github.com/blasty/CVE-2021-3156
$ tar -czvf exp.gz.tar CVE-2021-3156

--- victim machine ---
$ tar xopf exp.gz.tar
$ cd CVE-2021-3156/
$ make
$ ./sudo-hax-me-a-sandwich
$ ./sudo-hax-me-a-sandwich 1
```

now we have root access and root flag

![root](imgs/root.png "root")

# MACHINE PWNED
