def healthCalculator(age, applesAte, cigarettes):
    answer = (100 - age) + (applesAte * 3.5) - (cigarettes * 2)
    print(answer)
    
andreData = [26, 2, 0]
healthCalculator(andreData[0], andreData[1], andreData[2])

#Or you can Unpack it like this
healthCalculator(*andreData)