import wisdom as wisdom


def main():
    while True:
        question = wisdom.generate_question()
        wisdom.print_prompt(question[0], question[1], question[2])
        ans = int(input("Enter Your Answer: "))
        if (ans == question[3]):
            print("Correct")
        else:
            print("Incorrect")

if __name__ == "__main__":
    main()
