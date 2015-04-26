def addNumber(*args):
    total = 0
    for a in args:
        total += a
    print(total)

addNumber(3, 5, 6, 40)

#it's common pratice to use *args even tho it could be many variable names
    