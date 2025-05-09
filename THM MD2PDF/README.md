# MD2PDF CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **MD2PDF** CTF challenge on [TryHackMe](https://tryhackme.com/room/md2pdf). 
---

we see open ports 22, 80 and 5000

![scn](imgs/scn.png "scn")

we can access the page on port 80, we see markdown to pdf converter

![cv](imgs/cv.png "cv")

we can try to input some html tags to see the result (it is possible to use html tags in markdown)

i tried

```
<b>ttt</b>
<i>ttt</i>
ttt
```

![tg](imgs/tg.png "tg")

it works

![r](imgs/r.png "r")

from ferobuster scan we see directory /admin

![ad](imgs/ad.png "ad")

if we try to access /admin we see error saying that this page can only be seen by accessing localhost:5000

![er](imgs/er.png "er")

we can use iframe tag to see the content of /admin 

```
<iframe src="http://localhost:5000/admin"></iframe>
```

![if](imgs/if.png "if")

it works and we see the flag

![fg](imgs/fg.png "fg")

# FLAG OBTAINED
