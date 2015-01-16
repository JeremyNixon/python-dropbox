arr = []
weird = 0
number = 20
while(weird == 0):
    indicator = 1
    for i in range(1,20):
        if number % i != 0:
            indicator = 0
    if indicator == 1:
        weird = 1
        print number
    number+= 20
    print number