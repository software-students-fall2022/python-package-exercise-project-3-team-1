import team1ArithmeticTrainer.functions as functions
def run():
    while True:
        question = functions.generate_question()
        functions.print_prompt(question[0], question[1], question[2])
        ans = input("Enter your answer: ")
        while not (ans.isnumeric()):
            print("You must enter an integer")
            ans = input("Enter your answer: ")
        ans = int(ans)
        if ((question[0] == "sqr_root" or question[0] == "cube_root") and ans == question[2]):
            print("Correct")
        elif ((question[0] == "sqr_root" or question[0] == "cube_root") and ans != question[2]):
            print("Incorrect")
        elif (ans == question[3]):
            print("Correct")
        else:
            print("Incorrect")
        again = input("Another question? (y/n): ")
        if(again != "y"):
            break