import random


def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def string_checker(user_response, valid_ans):
    while True:

        # Get user response and make sure its lowercase
        user_response = user_response.lower()

        for item in valid_ans:
            # check if the user response is a word in the lst
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of a item in the list.

            elif user_response == item[0]:

                return item

        return "invalid"


want_instructions = yes_no("would you like to see the instructions enter yes or no ")

if want_instructions == "yes":
    print('''
***** Game *****
This game will be a math quiz that you will have to answer!
You will be given a certin amount of rounds to play and your score will be shown at the end
          ''')



start = input("Press <enter> to begin")

print("Round 1")
print()
num1 = random.randint

num2 = random.randint

ops = ["-", "+", "*", "/"]

# Select a random operator
selected_operator = random.choice(ops)

print(selected_operator)

# todo save below "outcome/answer" and "equation" in variables
equation = f"{num1} {ops} {num2} = ?"
answer = 0

if selected_operator == "+":
    answer = num1 + num2
elif selected_operator == "-":
    answer = num1 - num2
elif selected_operator == "*":
    answer = num1 * num2
elif selected_operator == "|":
    answer = num1 / num2



points = 0
highest_points = float('-inf')
lowest_points = float('inf')
quiz_history = []
question_answerd = 0
question_correct = 0











