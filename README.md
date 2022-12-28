# GuessingGame2 (workshop exercise)

This is a variation of the first GuessingGame app. It is also a terminal program, however, this time it is the computer
that tries to guess users number. When the app is run the rules are presented:

```
Computer: Think of a number between 0 and 1000, and I will try to guess it in 10 tries!
Click ENTER to continue:

Computer: My guess number 1, is "500"
Is it correct, too small, or too big? Choose 1 for "correct", 2 for "too small", 3 for "too big" or type in a phrase. 
```

When the user decides on a numer, they will have to answer computers questions as shown above. It can obviously be
cheated. However, if the user truthful, computer will always guess the number in 10 tries. The program ends when the
user says that the guess is correct, or when there are already 10 attempts. In the second case there would be the following console output:
```
Computer: My guess number 10, is "999"
Is it correct, too small, or too big? Choose 1 for "correct", 2 for "too small", 3 for "too big" or type in a phrase. 2

Computer: NOOO! You must have been cheating!
```