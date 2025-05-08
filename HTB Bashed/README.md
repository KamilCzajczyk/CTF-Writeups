# Bashed CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Bashed** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/118). 
---

we see open port 80

![scn](imgs/scn.png "scn")

from feroxbuster we see some hidden folders 

![fr](imgs/fr.png "fr")

if we head to /dev and then click on phpbash.php we see some webshell

![dv](imgs/dv.png "dv")

we can execute commands as www-data

![www](imgs/www.png "www")

we see 2 users in /home

![hm](imgs/hm.png "hm")

we can use reverse-shell to gain access in shell

by looking at the sudo -l output we see that we can run bash as scriptmanager 

![sd](imgs/sd.png "sd")

```
sudo -u scriptmanager bash
```

![sc](imgs/sc.png "sc")

we can now read user flag

![ud](imgs/ud.png "ud")

we can run pspy64 to see what is executed, we see that file test.py is run every few minutes

![ps](imgs/ps.png "ps")

we can also modify this file, we can add malicious script that will copy bash with SUID bit

![mal](imgs/mal.png "mal")

after waiting for a short while we can inspect /tmp folder and we see a rootbash

now we execute 

```
/tmp/rootbash -p
```

![rt](imgs/rt.png "rt")

now we have access as root and we can grab root flag

# MACHINE PWNED
