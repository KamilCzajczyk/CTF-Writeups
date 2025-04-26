# Dreaming CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Dreaming** CTF challenge on [TryHackMe](https://tryhackme.com/room/dreaming). 
---

we see open ports 22 and 80

![scn](imgs/scn.png "scn")

main page is apache default page

![ap](imgs/ap.png "ap")

we need to perform directory scanning with feroxbuster

![fr](imgs/fr.png "fr")

we found some `pluck-4.7.13`

we try to access it

![dr](imgs/dr.png "dr")

by clicking on admin we can find login page

![lgg](imgs/lgg.png "lgg")

i randomly guessd password : password

now we see some admin panel  

![lg](imgs/lg.png "lg")

i also found some pluck file upload exploit here `https://www.exploit-db.com/exploits/49909`

![db](imgs/db.png "db")

we need to download the file and run the command

```
python3 49909.py 10.10.81.102 80 password /app/pluck-4.7.13
```

![py](imgs/py.png "py")

after running the script we got link to our shell

```
http://10.10.81.102:80/app/pluck-4.7.13/files/shell.phar
```

we got access to p0wnyshell

![sh](imgs/sh.png "sh")

we see other users death, lucien, morpheus

![hm](imgs/hm.png "hm")

there is something interesting in /opt

![op](imgs/op.png "op")

in /opt/test.py we found some plain-text password

![ts](imgs/ts.png "ts")

i used simple reverse shell to switch to terminal, then i tried to login as lucien with password that i found

![rs](imgs/rs.png "rs")

it worked we have first flag

![f1](imgs/f1.png "f1")

we see some history of commands, most notable is mysql connection which we can simply recreate

![his](imgs/his.png "his")

```
mysql -u lucien -p[REDACTED]
```

![dbb](imgs/dbb.png "dbb")

we can take a look inside library database

![de](imgs/de.png "de")

we also see sudo -l output, we can run some python script as death

![sdl](imgs/sdl.png "sdl")

we cant look directly into this script, but we see a script with the same name in /opt directory, we

![cd](imgs/cd.png "cd")

script takes data from database that we have seen, data isnt sanitized so we could input additional row to databse with malicious content

```
> use library;
> insert into dreams (dreamer, dream) values (";/bin/bash","");
```

now when the script runs it will execute something like : `echo ; /bin/bash` and we should get shell as death

```
sudo -u death /usr/bin/python3 /home/death/getDreams.py
```

![in](imgs/in.png "in")

i did something wrong and it works but we need to use exit to see the result of the commands run as death

![w](imgs/w.png "w")

i made it work by using reverse shell command, now we have stable access as death

![rss](imgs/rss.png "rss")

we can grab another credentials from getDreams.py file and connect via ssh 

![cr](imgs/cr.png "cr")

in /home/morpheus we see some python script that creats backup

![hmm](imgs/hmm.png "hmm")

after installing pspy64 we see that there is a proccess that runs the script

![ps](imgs/ps.png "ps")

we can edit the function /usr/lib/python3.8/shutil.py 

![ln](imgs/ln.png "ln")

![ls](imgs/ls.png "ls")

script uses copy2() so we can add our malicious code to it and create reverse shell to get access as morpheus, now we need to wait 

![code](imgs/code.png "code")

we can grab last flag

![r](imgs/r.png "r")

this user can sudo su without password so we got root access

![ssl](imgs/ssl.png "ssl")

# MCHINE PWNED
