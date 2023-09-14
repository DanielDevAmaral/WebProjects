


def main():
    print('''This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:
    ''')
    print('''
    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.
    ''')


    score = 0
    
    score += esteem_positive(
        "1. I feel that I am a person of worth, at least on an equal plane with others.")
    score += esteem_positive(
        "2. I feel that I have a number of good qualities.")
    score += esteem_negative(
        "3. All in all, I am inclined to feel that I am a failure.")
    score += esteem_positive(
        "4. I am able to do things as well as most other people.")
    score += esteem_negative(
        "5. I feel I do not have much to be proud of.")
    score += esteem_positive(
        "6. I take a positive attitude toward myself.")
    score += esteem_positive(
        "7. On the whole, I am satisfied with myself.")
    score += esteem_negative(
        "8. I wish I could have more respect for myself.")
    score += esteem_negative(
        "9. I certainly feel useless at times.")
    score += esteem_negative(
        "10. At times I think I am no good at all.")

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def esteem_positive(question):
    print(question)

    anwser = input("   Enter D, d, a, or A: ")

    if anwser == "D":
        score = 0
    elif anwser == "d":
        score = 1
    elif anwser == "a":
        score = 2
    elif anwser == "A":
        score = 3

    return score

def esteem_negative(question):
    print(question)
    anwser = input("   Enter D, d, a, or A: ")

    if anwser == "D":
        score = 3
    elif anwser == "d":
        score = 2
    elif anwser == "a":
        score = 1
    elif anwser == "A":
        score = 0

    return score

# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()