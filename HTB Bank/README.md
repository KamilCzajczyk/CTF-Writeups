# Bank CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Bank** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/Bank). 
---

we see open porst 22, 53 and 80

![scn](imgs/scn.png "scn")

we need to add `bank.htb` to /etc/hosts

now we can access the `login.php`

![lg](imgs/lg.png "lg")


from gobuster we see hidden directories: `/uploads`, `/assets`, `/inc` and `/balance-transfer`

![dr](imgs/dr.png "dr")

we see listing of files, one of them is smaller than others

![bt](imgs/bt.png "bt")

we can cat the file to get some credentials

![pw](imgs/pw.png "pw")

now we can login to some dashboard

![ds](imgs/ds.png "ds")

in Support we see some file upload

![sp](imgs/sp.png "sp")

by looking at the source code we can see a comment saying that we could upload .htb files that will be executed as php, we can craft php reverse-shell and save it as .htb

![cm](imgs/cm.png "cm")

![ht](imgs/ht.png "ht")

now we can click the generated link to gain shell as www-data

![lk](imgs/lk.png "lk")

![www](imgs/www.png "www")

we see the user chris and we need to gain access as him to get user flag

![hm](imgs/hm.png "hm")

after running linpeas we see that we have write access to /etc/passwd so we can create our own root user

![lep](imgs/lep.png "lep")

![pp](imgs/pp.png "pp")

first we generate the password 

```
openssl passwd -6 "pass"
```

then we use echo to add record to /etc/passwd

```
echo 'haxor:hash:0:0:Hacker:/root:/bin/bash' >> /etc/passwd
```

![rt](imgs/rt.png "rt")

there is also easier way, we see unknown SUID binary

![su](imgs/su.png "su")

we can just run this binary to gain root access 

```
/var/htb/bin/emergency
```

![rtt](imgs/rtt.png "rtt")

# MACHINE PWNED
