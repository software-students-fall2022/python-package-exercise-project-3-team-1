import random

def checkPerfectSquare(num):
    if num>0:
        for i in range(num+1):
            for j in range(num+1):
                if i*j==num and i==j:
                    return i
    return -1


def checkPerfectCube(num):
    if num>0:
        for i in range(num+1):
            for j in range(num+1):
                for k in range(num+1):
                    if i*j*k==num and i==j and j==k:
                        return i
    return -1

    
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def sqr_root(a):
    return a ** 0.5


def cube_root(a):
    return a ** (1/3)


def modulus(a, b):
    return a % b


def generate_question():
    """Generate a random question."""
    question = random.choice([add, subtract, multiply, divide, sqr_root, modulus,cube_root])
    if question == add:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = add(a, b)
        return question, a, b, ans
    elif question == subtract:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = subtract(a, b)
        return question, a, b, ans
    elif question == multiply:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        ans = multiply(a, b)
        return question, a, b, ans
    elif question == divide:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = divide(a, b)
        return question, a, b, ans
    elif question == sqr_root:
        a = random.randint(1, 100)
        sentinel=checkPerfectSquare(a)
        while sentinel==-1:
            a=random.randint(1,100)
            sentinel=checkPerfectSquare(a)
        ans = sqr_root(a)
        return question, a, ans
    elif question == modulus:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = modulus(a, b)
        return question, a, b, ans
    elif question == cube_root:
        a = random.randint(1, 100)
        sentinel=checkPerfectCube(a)
        while sentinel==-1:
            a=random.randint(1,100)
            sentinel=checkPerfectCube(a)
        ans = cube_root(a)
        return question, a, b, ans


def print_prompt(question, a, b):
    print("What is the answer to the following question?")
    if question == add:
        print(f"{a} + {b} = ")
    elif question == subtract:
        print(f"{a} - {b} = ")
    elif question == multiply:
        print(f"{a} * {b} = ")
    elif question == divide:
        print(f"{a} / {b} = ")
    elif question == sqr_root:
        print(f"√{a} = ")
    elif question == modulus:
        print(f"{a} % {b} = ")
    elif question == cube_root:
        print(f"∛{a} = ")