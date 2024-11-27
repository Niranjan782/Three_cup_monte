                                            #This is a basic progam of Three Cup Monte

from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess=''

    while guess not in ['0','1','2']:
        guess=input("pick a number [0,1,,2]\n")
    return int(guess)


def check_guess(mylist,guess):
    if mylist[guess]=='0':
        print("Correct!!!")
    else:
        print("Wrong!!")
        print(mylist)

#intial list

mylist=['','o','']

#shuffled List

mixed_list=shuffle_list(mylist)

#user guess
guess=player_guess()

#check guess

check_guess(mixed_list,guess)