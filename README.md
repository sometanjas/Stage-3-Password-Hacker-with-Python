**Project: Password Hacker with Python - Stage 3**

Source: https://hyperskill.org/projects/80

Source of this stage: https://hyperskill.org/projects/80/stages/444/implement

My code: https://github.com/sometanjas/Stage-3-Password-Hacker-with-Python/blob/master/Password%20Hacker%20with%20Python/task/hacking/hack.py

**Description**

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
