###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
code = digits[:3]
# print(code)
NotMatch = True

print("Welcome to code beaker !!!! Let's see whether you can break the code or not The code has been generated. Please Enter you three digit code")

while NotMatch:
    # Another hint:
    guess = list(input("What is your guess? "))

    guess = [int(x) for x in guess]
    # print(guess)

    compare =[ i for i, j in zip(code, guess) if i == j ]
    # print(compare)
    w = len(compare)
    common = 0
    if w == 3:
      print("perfect match")
      NotMatch= False
    elif w==2 or w==1:
        print("match")
    else:

        for i in code:
            for j in guess:
                if i==j:
                    common= common+1
        if common > 0:
            # print(common)
            print("close")
        else:
            print("none")






#
# close = 0
# for i in digits:
#     for j in guess:
#         if i==j:
#             close= close+1
# print(close)
#
#
#
#
#
#  def result(L):








# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
