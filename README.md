**Project: Password Hacker with Python - Stage 3, 4 and 5**

Source: https://hyperskill.org/projects/80

Stage 3: [link](https://github.com/sometanjas/Stage-3-Password-Hacker-with-Python/blob/master/Password%20Hacker%20with%20Python/task/hacking/hack.py)  
Stage 4: [branch](https://github.com/sometanjas/stage-3-4-5-password-hacker-with-python/tree/stage-4)  
Stage 5: [branch](https://github.com/sometanjas/stage-3-4-5-password-hacker-with-python/tree/stage-5)  


**Description: Stage 3**

Source of this stage: https://hyperskill.org/projects/80/stages/444/implement

Looks like you can already call yourself a hacker! However, the situation gets more complicated: the admin improves the server and our simple brute force attack is no longer working. 
Well, this shouldn't hold you back: you can provide your program with a prepared dictionary of typical passwords (it was generated using a database with over a million real-life passwords).

That's not all: the admin decided to outsmart us and changed the case of some letters in the new password so that we could not crack it using the password dictionary. 
Let's outsmart the admin and try all possible combinations of upper and lower case for each letter for all words of the password dictionary. 
We won't have to try too much since for a 6-letter word you'll get only 64 possible combinations.

Now not only do you have to try each element of the dictionary but you also need to change the case of some letters to find the correct password. 
And when you've entered the correct password, the server will greet you with "Connection success!".

This has increased the time of hacking greatly, so using brute force is probably not an option. 
Use the dictionary of standard passwords, and do not forget to try changing the cases of different letters. 
For example, there is the word ‘qwerty’ in the dictionary, but the cunning admin sets it to ‘qWeRTy’. Your program should make it possible to hack such passwords, too.

**Description: Stage 4**

Source of this stage: https://hyperskill.org/projects/80/stages/445/implement

The server is becoming smarter along with your hacking program. Now the admin has implemented a security system by login and password. In order to access the site with admin privileges, you need to know the admin's login and password. Fortunately, we have a dictionary of different logins and a very interesting vulnerability. You need to improve your program once again to hack the new system.

Also, now the admin has made a complex password that is guaranteed to be absent in the databases since it's randomly generated from several characters.

The server now uses JSON to send messages.

**Description: Stage 5**

Source of this stage: https://hyperskill.org/projects/80/stages/446/implement

Your program has successfully hacked the new system! However, you've been spotted: the admin noticed your first failed attempts, found the vulnerability and made a patch. You should overcome this patch and hack the system again. It’s not easy being a hacker!

The admin has improved the server: the program now catches the exception and sends a simple ‘wrong password’ message to the client even when the real password starts with current symbols.

But here's the thing: the admin probably just caught this exception. We know that catching an exception takes the computer a long time, so there should be a delay in the server response when this exception takes place. You can use it to hack the system: count the time period in which the response comes and find out which starting symbols work out for the password.


