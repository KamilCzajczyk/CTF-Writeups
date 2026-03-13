# Data CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Data** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/Data). 
---

we see open ports 22 and 3000

![ss](imgs/ss.png "ss")

using nmap to gain more info

![nm](imgs/nm.png "nm")

on port 3000 there is grafana instance running, we also see that the version is outdated and vulnerable to LFI via CVE-2021-43798

![www](imgs/www.png "www")

we can use the exploit from https://github.com/K3ysTr0K3R/CVE-2021-43798-EXPLOIT/blob/main/CVE-2021-43798.py to test for LFI

![exp](imgs/exp.png "exp")

we see that the program dumped the file using this url

```
http://IP:3000/public/plugins/alertlist/../../../../../../../../../../../../../../../../../../../etc/passwd
```

we can now curl the `/etc/passwd`

![crl](imgs/crl.png "crl")

we can also curl the grafana database from `/var/lib/grafana/grafana.db`

![gr](imgs/gr.png "gr")

we also can dump other OS files 

![zp](imgs/zp.png "zp")

after dumping database we can look inside using sqlite3

we can find user table, so we can dump users data

![sql](imgs/sql.png "sql")

default mode of password hashing in grafana is PBKDF2-HMAC-SHA256 with 10000 iterations

now we prepare the file for hashcat with this template: `user:sha26:iterations:base64_salt:base64_hash`

![h3](imgs/h3.png "h3")

now we are ready to crack

![hs](imgs/hs.png "hs")

we found some password, we can try to login as boris via ssh, it works we can grab user flag

![user](imgs/user.png "user")

we can check sudo permissions

![sl](imgs/sl.png "sl")

we can run ps to check docker process running

![ps](imgs/ps.png "ps")

by running ps we know the grafana container id that we will use to escape

we can use this command to start our escape:

```
sudo /snap/bin/docker exec -u 0 --privileged -it e6ff5b1 /bin/sh 
```

we entered running grafana instance as root user in privileged mode

then we can check devices with `fdisk -l`

then we created new directory `/mnt/host` and mounted sda1 there using `mount /dev/sda1 /mnt/host`

then we change main catalog with `chroot /mnt/host /bin/bash` 

![rt](imgs/rt.png "rt")

we can add our ssh public key to gain true root access

![ssh](imgs/ssh.png "ssh")

now we have true root access via ssh

![rrr](imgs/rrr.png "rrr")

# MACHINE PWNED