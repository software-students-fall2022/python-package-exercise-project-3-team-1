import functions as functions
def main():
    while True:
        question = functions.generate_question()
        functions.print_prompt(question[0], question[1], question[2])
        ans = int(input("Enter Your Answer: "))
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

if __name__ == "__main__":
    main()
