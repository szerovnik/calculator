x = int(raw_input("Pick anumber between 1 and 100: "))

for i in range(0, x):

    if (i % 3 == 0):
        print "{0} fizz".format(i)
    elif (i % 5 == 0):
        print "{0} buzz".format(i)
    elif (i % 3 == 0 and i % 5 == 0):
        print "{0} fizzbuzz".format(i)

    else:
        print "Tvoje stevilo je {param}.".format(param=i)