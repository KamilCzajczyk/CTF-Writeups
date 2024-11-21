# Team CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Team** CTF challenge on [TryHackMe](https://tryhackme.com/r/room/teamcw). 
---
Using nmap to find open ports

![nmap](imgs/nmap.png "nmap")

Open ports `21 ftp`,`22 ssh` and `80 http`

Using gobuster to find directories

```
gobuster dir -w /snap/seclists/current/Discovery/Web-Content/common.txt -u http://10.10.130.165   
```
![gobuster-basic](imgs/gobuster-basic.png "gobuster-basic")

No interesting directories

Main page is Apche default page but with a twist, the `<title>` is changed

![title](imgs/title.png "title")

Adding team.thm to /etc/hosts

![hosts1](imgs/hosts1.png "hosts1")

team.thm webpage

![team-web](imgs/team-web.png "team-web")

Using gobuster again

```
gobuster dir -w /snap/seclists/current/Discovery/Web-Content/common.txt -u http://team.thm
```

![gobuster-team](imgs/gobuster-team.png "gobuster-team")

Gobuster found `robots.txt` with `dale` string 

![robots](imgs/robots.png "robots")

Using ffuf to enumerate vhosts

```
ffuf -w /snap/seclists/current/Discovery/DNS/subdomains-top1million-20000.txt -u http://team.thm/ -H "Host: FUZZ.team.thm" -fs 11366
```

![vhost-ffuf](imgs/vhost-ffuf.png "vhost-ffuf")

Editing /etc/hosts again and adding `dev.team.htm`

dev.team.thm webpage

![dev-site](imgs/dev-site.png "dev-site")

![dev-src](imgs/dev-src.png "dev-src")

Possible file inclusion, changing URL to /etc/passwd as example


```
http://dev.team.thm/script.php?page=/etc/passwd
```

![lfi-passwd](imgs/lfi-passwd.png "lfi-passwd")

notable users `dale` and `gyles`

I tried diffrent common configuration files for FTP and SSH and found Dale `openSSH private key`

```
http://dev.team.thm/script.php?page=/etc/ssh/sshd_config
```

![sshd](imgs/sshd.png "sshd")

Login to ssh with a private key as dale, remember to `chmod 600` key

![user-sudol](imgs/user-sudol.png "user-sudol")

> [!IMPORTANT]
> User flag from `user.txt`: `THM{6Y0TXHz7c2d}`

![admin-checks](imgs/admin-checks.png "admin-checks")

now we can do

```
sudo -u gyles /home/gyles/admin_checks
```

We can exploit this file, in first input we can type anything, but in second we can type `bash` to spawn a shell as gyles, then we can use python3 to stabilize it

```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

![gyles](imgs/gyles.png "gyles")

In /opt there is interesting folder `admin_stuff` that contains `script.sh`

![script](imgs/script.png "script")

Now i check those files mentioned in script.sh

The main_backup.sh is writeable

![backup-priv](imgs/backup-priv.png "backup-priv")

Now i edit main_backup to generate reverse shell as root, the script is run by cronjob every minute. **This privilege escalation stage could be done in various ways.**

![new-bakup](imgs/new-bakup.png "new-bakup")

![root](imgs/root.png "root")

> [!IMPORTANT]
> Root flag from `root.txt`: `THM{fhqbznavfonq}`

# MACHINE PWNED
