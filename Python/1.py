
number1 = int(input ("Please input the first number: "))

number2 = int(input ("Please input the second number: "))

Func = raw_input("What do you want to do : +, -, * or / ?")

if Func == "+":
    Result = number1 + number2
    print "The result is: " + str(number1) + " + " + str(number2) + " = " + str(Result)
elif Func == "-":
    Result = number1 - number2
    print "The result is: " + str(number1) + " - " + str(number2) + " = " + str(Result)
elif Func == "*":
    Result = number1 * number2
    print "The result is: " + str(number1) + " * " + str(number2) + " = " + str(Result)
elif Func == "/":
    Result = number1 / number2
    print "The result is: " + str(number1) + " / " + str(number2) + " = " + str(Result)
else:
    print "Looks like as something wrong, try agian later"

	
