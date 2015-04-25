magicNumber = 26

#This is a comment
"""
This is a longer comment
"""

z = 5
class B(object):
    x = 10
    def z(self):
        print("fuck you")
def x():
    "This is an optional description of a function aka documentation Strong aka docString"
    for n in range(101):
        if n is magicNumber:
            # To add a non String along with a String need to seperate with a comma (,) eg print("fuck", 5)
            print('The magic number is ', n)
            #Use break to save memory so the program does not have to run the loop when it does not need to
            break
        else: 
            print(n)


def y( whatever ):
    if z is 5:
        global words 
        words = 50
        print(words)
words = 10
y(10)

print()

#homeWork - print out all numbers betweenn 1..100 that are divisible by 4 
test = range(100)
def divisible4(rng):
    for f in rng:
        if f != 0:
            if f % 4 is 0:
                print(f)

divisible4(test)    