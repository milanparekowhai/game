

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


want_instructions = yes_no("would you like to ssee the in structions enter yes or no ")

if want_instructions == "yes":
    print("***** Game *****"
          "this game will be a math quiz that you will have to anser!"
          "you will be given a certin amount of rounds to play and your score will be shown at the end")










