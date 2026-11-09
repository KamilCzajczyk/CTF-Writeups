# Helix CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Helix** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/Helix). 
---

we see open ports 22 and 80

![nm](imgs/nm.png "nm")

main www page

![www](imgs/www.png "www")

we can enumerate subdomians with ffuf 

![fl](imgs/fl.png "fl")

we found `flow`, we need do add to /etc/hosts 


we can check this subdomain, we see some nifi instance, we can also check app version 

![nifi](imgs/nifi.png "nifi")

this nifi version is vulnerable to RCE, we can use this script to gain shell access `https://github.com/sbouabid-sec/CVE-2023-34468-POC`

![poc](imgs/poc.png "poc")

we got hit with shell as nifi

![nc](imgs/nc.png "nc")

in `/opt/nifi-1.21.0/support-bundles` we can find operator private key

![ket](imgs/key.png "key")

now we have access as operator, we can grab user flag and also some image and pdf files

![us](imgs/us.png "us")

image represents simple instruction for reactor

![png](imgs/png.png "png")

we can use `pdf2john.pl` script to prepare pdf password for cracking with john 

![jh](imgs/jh.png "jh")

now cracking with john

![jhh](imgs/jhh.png "jhh")

now we can open the pdf, we have full operator manual, the most important chapters are 6 and 7

![p6](imgs/p6.png "p6")

![p8](imgs/p8.png "p8")

we can take look at open ports with ss, we can forward them with ssh to our machine, 8081 and 4840 are the most interesting

![ss](imgs/ss.png "ss")

on port 8081 there is a web panel with plant status

![norm](imgs/norm.png "norm")

we can also see that we can run sudo on some maint-console which probably is the maintenance window that will be open when we correctly manipulate reactor parameters

![sd](imgs/sd.png "sd")

we now that we can manipulate the parameters in UA to change the status of the reactor

![ua](imgs/ua.png "ua")

we see that privileged maintenance window is OPEN

![pv](imgs/pv.png "pv")

now we can get root shell with sudo and root flag

![rt](imgs/rt.png "rt")

# MACHINE PWNED