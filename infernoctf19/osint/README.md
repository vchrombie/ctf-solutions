## OSINT

```
New Developer (50)

A friend of a friend of a friend who is known for leaking info was recently hired at a game company. What can you find in their GitHub profile?

https://github.com/iamthedeveloper123

Author: nullpxl
```
The given GitHub profile has a few repositories created recently. Cloned the recent added repos and saw `.bashrc2` of dotfiles repo was being executed in the bash script of `bash2048`. Upon looking upon the script, got a pastebin link which has the flag.


```
Whistle Blower (270)

After playing some 2048 you come across an interesting email exchange... What could it lead to?

Author : nullpxl

File: employment_status.mbox
```
The given file is a mailbox file which has a conversation. The crux of the convo is the iamthedeveloper123 is gonna leak the whole information. And a hint was given in the name of 'infosec twitter'.

Searched in twitter about this and got a [tweet](https://twitter.com/imdeveloper123/status/1210483808639709185) which said he leaked info on [https://iamthedeveloper123.weebly.com/](https://iamthedeveloper123.weebly.com/). But the blog said site was taken down recently. Searched around [Wayback Machine](https://web.archive.org/web/) and got a recent [snapshot](https://web.archive.org/web/20191224223734/https://iamthedeveloper123.weebly.com/) which has the flag.