# Nocturnal CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Nocturnal** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/Nocturnal). 
---

we see open ports 22 and 80

![scn](imgs/scn.png "scn")

we see some login form 

![lg](imgs/lg.png "lg")

i created the user tt:tt 

we see a file upload service, i tried to upload reverse shell but we can only upload documents like pdf or odt

![up](imgs/up.png "up")

if we take a look at the link to a file we see a parameter username, so we might have some IDOR

![u](imgs/u.png "u")

![fzz](imgs/fzz.png "fzz")

i tried to FUZZ the username parameter and i found other usernames like: admin, amanda and tobias

admin has no files 

![fz](imgs/fz.png "fz")

we see some file in amanda account called privacy.odt, we can try to donwload this file

![am](imgs/am.png "am")

![ama](imgs/ama.png "ama")

![p](imgs/p.png "p")

we found some private message with password for user amanda, i tried to login to ssh but i didnt seem to work, but we can login as amanda to dashboard

now we have access to admin panel

![pn](imgs/pn.png "pn")

we can take a look at source code of the file 

![sc](imgs/sc.png "sc")

we can use creating backup function to get some remote code execution we can use %0A for new-line and %09 for tab to bypass the filter

![ft](imgs/ft.png "ft")

![id](imgs/id.png "id")

now we can create payload to execute reverse shell (we need to swap spaces to %09)

![rs](imgs/rs.png "rs")

it worked we have consistent access 

![rss](imgs/rss.png "rss")

we see some sqlite database that we can investigate using sqlite3

![db](imgs/db.png "db")

```
$ sqlite3 /var/www/nocturnal_database/nocturnal_database.db
> .tables
> select * from users;
```

![sql](imgs/sql.png "sql")

we found some users and hashes, we can try to crack it using crackstation

![cr](imgs/cr.png "cr")

we found tobias password, we can try to change user to tobias with this password

it worked we have access as tobias and we can grab user flag

![us](imgs/us.png "us")

after running pspy64 we see that php command is executed as root, it means that there is another server running

```
/usr/bin/php -S 127.0.0.1:8080
```

![ps](imgs/ps.png "ps")

to gain access to this server we need to forward port to our local machine

![pf](imgs/pf.png "pf")

```
 ssh -L 8888:127.0.0.1:8080 tobias@10.10.11.64
```

now we can access localhost:8888 to see another page: ISPConfig

![is](imgs/is.png "is")

we can scan the port with nmap 

```
nmap -p 8888 -sCV 127.0.0.1
```

![nm](imgs/nm.png "nm")

we can login as admin using tobias password

admin:slowmotionapocalypse

![ad](imgs/ad.png "ad")

if we google: `ispconfig exploit` we see some python code that might help us get a root shell `https://github.com/bipbopbup/CVE-2023-46818-python-exploit/blob/main/exploit.py`

![go](imgs/go.png "go")

we can then copy it to our machine and execute

```
python3 exploit.py http://127.0.0.1:8888 admin passwd
```

![ex](imgs/ex.png "ex")

now we have root shell and root flag

# MACHINE PWNED 
