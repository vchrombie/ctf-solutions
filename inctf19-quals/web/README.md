## Web Exploitation

```
Cookie's everywhere !!

Points: 100

Description: Can u spot the difference...

Challenge link - http://3.112.230.177/

Author : Captain-kay
```

**Solution**:

The flag is stored in parts in the cookies with the session name `_THE_FLAG_IS`. Refresh the page if you don't see anything. There are 15 such parts. You get a different cookie each time you refresh the page.

The cookies are stored as MD5 hash. This can be cracked using the online crackers like [MD5 Online](https://www.md5online.org/md5-decrypt.html) or you can use [s0md3v/Hash-Buster](https://github.com/s0md3v/Hash-Buster). 

The 15 parts are cracked and re-arranged in the format of the flag, `inctf{_}`.