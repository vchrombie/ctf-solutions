## Forensics

```
Easy Peasy

Points: 100

Description: My friend sent me this file and he tells me that something is hidden in it. Can you help him find it?

Author: g4rud4

File attached: chall.jpg
```

The flag is stored in the given photo which can be extracted using the [steghide](https://github.com/StefanoDeVuono/steghide) tool. The passphrase is needed tho.

The author name of the file is in the format base64, need to convert and that is the passphrase to extract the flag.