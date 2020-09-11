import random
a=True
while a:
    winning_no = random.randint(1, 150)
    guess_no = int(input('guess a number between 1 to 150: '))
    if  winning_no == guess_no:
       print('you win!')

    elif winning_no>guess_no:print('guess number is to low')
    else:
        print('guessed number is to high')
    choice=input('if u want to continue press Y\n or if u want to exit press N ')
    if choice.lower()=='y':
        a=True
    elif choice.lower()=='n':
        a=False



# Without using random function

flag=79
a=True
time=1
while a:
    guess_no=int(input('enter a guessed number: '))
    if guess_no==flag:
        print('you have to win in ',time,'attempt')
    elif guess_no>flag:
        print('Number is to high')
    else:print('Number is to low')
    time=time+1
    choice=input('if you want to continue press Y\n or if you want to exit press N ')
    if choice.lower()=='y':
        a = True
    elif choice.lower()=='n':
        a=False