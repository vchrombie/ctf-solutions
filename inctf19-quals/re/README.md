## Reverse Engineering

```
Python_revN

Points: 300

Description: Python is cool. And this is Python 3.

Author: Mr_UnKnOwN

File attached: sol_patched.py
```

**Solution**:

The the flag was converted into some format and they have given the value, `check`. So, I need to write a script to reverse the whole process and get the value.

There were two funtions push() and sage() which were applied in a particular fashion, `ALL=sage(push(x))`, where `x` is the flag input encoded to hex.

The push() generates another string from the hex encoded flag string which has a unique encoding type[(type.index(i)+3)%total_types]. All I need to do is replace +3 with -3. I wrote the unpush() function.

The sage() takes this string from push() and generated a list by slicing the string into parts of step 4, encode as hex and converting them into int. I reversed it, converted to string and decode hex. I wrote the unsage() function.

Apply the two functions in the required order and decode using from hex which gives you the flag.