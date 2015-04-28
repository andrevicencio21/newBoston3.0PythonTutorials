loopsDone = 0
while True:
    try:
        number = int(input("What's your favourtite number hoss?\n"))
        print(18/number)
        break
    except ValueError: #this only handles value error
        print("Make your you enter a number!\n")
    except ZeroDivisionError: #this only handles Zero division error
        print("please don't enter Zero!\n")
    except: # Handles every type of error but not recommended because your not sure about the source of the problem
        break
    finally: # no matter what this bit of code gets executed!
        loopsDone += 1
        print(loopsDone, "loops done")
        
        
        