# Star Wars CTF: 1 - Vulnhub Machine
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Star Wars CTF: 1** CTF challenge on [Vulnhub](https://www.vulnhub.com/entry/star-wars-ctf-1,528/). 
---

after importing machine to VirtualBox we need to change network settings, then we can scan our network for this machine IP 

```
nmap 192.168.X.X/24
```

then by having IP address we can perform proper scan, from it we know about open ports 22 and 80

![scn](imgs/scn.png "scn")

this is the website, we shall find a password

![pg](imgs/pg.png "pg")

if we take a look at the source code we see a comment saying that password is in some encoded string

![cm](imgs/cm.png "cm")

we can decode it using cyberchef (base64 -> binary) 

![cs](imgs/cs.png "cs")

from gobuster scan we found a few hidden folders

![go](imgs/go.png "go")

i also checked robots.txt

![rb](imgs/rb.png "rb")

we now know about folder /r2d2, but there is nothing interesting for now

![r2](imgs/r2.png "r2")

we found users.js containing possible users

![us](imgs/us.png "us")

i went back to yoda images and try steganography and it worked

![steg](imgs/steg.png "steg")

now we have users and password

we can login as han via ssh

![han](imgs/han.png "han")

we know about other users: skywalker and Darth

linpeas found some old commands in .bash_history

![l](imgs/l.png "l")

lookig at whole .bash_history file we see a mention about cewl, r2d2, anakin, Darth

![bh](imgs/bh.png "bh")

we can use cewl to create wordlist from folder /r2d2

```
cewl http://192.168.X.X/r2d2 > words.txt
```

now we can try to use hydra to login as skywalker

```
hydra -l skywalker -P words.txt ssh://$IP
```

![hd](imgs/hd.png "hd")

it worked we have access as skywalker

![sk](imgs/sk.png "sk")

in the note we see something about job, so it might be suggesting a cronjob, but there is nothing interesting in crontab for now

![nt](imgs/nt.png "nt")

by looking at bash_history again we found some more old commands

![bhh](imgs/bhh.png "bhh")

we found the second half of some string, I tried to use the full string to login as Darth and it worked we now have access as Darth

![dr](imgs/dr.png "dr")

now i checked sudo -l output

![sd](imgs/sd.png "sd")

we can execute nmap as root

we can replicate the GTFObins method to become root

![gt](imgs/gt.png "gt")

```
$ TF=$(mktemp)
$ echo 'os.execute("/bin/sh")' > $TF
$ sudo nmap --script=$TF
```

now we have root access and root flag

![rt](imgs/rt.png "rt")

# MACHINE PWNED
