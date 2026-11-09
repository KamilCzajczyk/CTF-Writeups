# Reactor CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Reactor** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/Reactor). 
---

we see open porst 22 and 3000

![nm](imgs/nm.png "nm")

main www page, thereis no interesting directories and subdomains, so probably there is something wrong with outdated versions of frameworks

![www](imgs/www.png "www")

additional scan with whatweb, website could be exploitable by react2shell because of nextjs headers

![wb](imgs/wb.png "wb")

we can confirm the react2shell with a scanner

![scn](imgs/scn.png "scn")

we got hit with reverse shell 

![rs](imgs/rs.png "rs")

we see some `reactor.db` database that could have some useful data

![db](imgs/db.png "db")

we got some hashes

![sq](imgs/sq.png "sq")

we can crack the hashes with crackstation

![cr](imgs/cr.png "cr")

now we have access as user and we can grab user flag

![us](imgs/us.png "us")

linpeas shows that the node is running with inspect flag

![ins](imgs/ins.png "ins")

we can forward the port via ssh and confirm the inspector

![js](imgs/js.png "js")

by accessing the chrome://inspect we see our application is available due to port forwarding, we can proceed to inspect

![chr](imgs/chr.png "chr")

now we can run commands on the system

![dev](imgs/dev.png "dev")

we can copy /bin/bash with SUID bit flag to gain root shell

now we have root access

![rt](imgs/rt.png "rt")

# MACHINE PWNED
