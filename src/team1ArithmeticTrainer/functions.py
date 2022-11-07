import random

def addition(self, minLim, maxLim):
    numOne = random.randInt(minLim, maxLim)
    numTwo = random.randInt(minLim, maxLim)
    solution = numOne + numTwo
    answer = input("What is" + str(numOne) + " + " + str(numTwo) + ":")
    if(int(answer) == (numOne + numTwo)):
        print("Correct!")
    else:
        print("Incorrect, the answer is: " + str(solution))
def subtraction(self, minLim, maxLim):
    return 0
def multiplication(self, minLim, maxLim):
    num1=random.randint(minLim,maxLim)
    num2=random.randint(minLim,maxLim)
    answer=num1*num2
    answer = input("What is" + str(num1) + " * " + str(num2) + ":")
    userInput=input()
    try:
        if int(userInput)==answer:
            return True
        else:
            return False
    except:
        return "Invalid"
def squareRoot(self, minLim, maxLim):
    return 0
def divion(self, minLim, maxLim):
    return 0
def modulus(self, minLim, maxLim): 
    return 0