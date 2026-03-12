# CodePartTwo CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **CodePartTwo** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/CodePartTwo). 
---

we see open porst 22 and 8000

![scn](imgs/scn.png "scn")

we see a webpage, we can do few things: register, login and download 

![pg](imgs/pg.png "pg")

if we click download we see some source code that might be connected to our website

we can login via login page

![lg](imgs/lg.png "lg")

and we can register new user

![rg](imgs/rg.png "rg")

after logging in we see a dashboard with code editor

![ce](imgs/ce.png "ce")

we can try to execute some simple code (it works !)

![ex](imgs/ex.png "ex")


going back to source code 

![s1](imgs/s1.png "s1")

![s2](imgs/s2.png "s2")

we see that this code is not very secure, there are few flaws like:

- weak password hashing with MD5

- hardcoded secret_key

- possible database disclosure

- possible Remote Code Execution via /run_code, 

```
result = js2py.eval_js(code)
```

this method allows JavaScript code to be executed within the Python interpreter, this vulnerability is described in `CVE-2024-28397` (we know about js2py version from requirements.txt)

we can read more about it here:

```
https://cvefeed.io/vuln/detail/CVE-2024-28397
```

we can also find links to public exploits 

![cv](imgs/cv.png "cv")

i used exploit from this github repo

```
https://github.com/Marven11/CVE-2024-39205-Pyload-RCE
```

![gh](imgs/gh.png "gh")

here is the part of malicious code where we insert command to execute

![ghh](imgs/ghh.png "ghh")

we can test RCE by using ping command, we modify the malicious code and supply `ping -c1 10.10.X.X` command

![pn](imgs/pn.png "pn")

we also need to setup listener, I will use tcpdump

![dm](imgs/dm.png "dm")

we see hits to our machine, so malicious code was executed, now we can craft a reverse shell command

![rs](imgs/rs.png "rs")

now we have shell access

![rss](imgs/rss.png "rss")

we remember about some user.db file from source code but we can also use linpeas to find this file

![db](imgs/db.png "db")

now we can use sqlite3 to browse the database

![sq](imgs/sq.png "sq")

we found some password hashes that we can crack

![cr](imgs/cr.png "cr")

now we can login as marco via ssh and grab user flag

![us](imgs/us.png "us")

by using linpeas we see that we can run sudo on `/usr/local/bin/npbackup-cli`

![sq](imgs/sq.png "sq")

to read root flag we will use npbackup as sudo

first we need to edit config file to inlude the path that we want to backup like /root

![na](imgs/na.png "na")

then we run this command to create a backup

```
sudo /usr/local/bin/npbackup-cli --backup --config-file=npbackup.conf
```

![bc](imgs/bc.png "bc")

we need to remember the snapshot id, now we need to dump the file that we wanted to see using command

```
sudo /usr/local/bin/npbackup-cli --config-file=npbackup.conf --snapshot-id SNAPID --dump /root/root.txt
```

![dp](imgs/dp.png "dp")

now we have root flag

# MACHINE PWNED
