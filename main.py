# Magic 8 Ball Assignment

import random

# Random Responce Function 
def randomResponce():
    num = random.randint(1, 5)
    if num == 1:
        return "Without a Doubt."
    elif num == 2:
        return "As I see it, yes."
    elif num == 3:
        return "Concentrate and ask again."
    elif num == 4:
        return "Don't count on it."
    elif num == 5:
        return "Outlook not so good."

# Check Question function

def checkQuestion(question):
    if question == "":
        return "Please ask a question..."
    elif question == "does a magic 8 ball actually work?":
        return "How dare you doubt me!"
    elif question == "is javascript awesome?":
        return "Of Course"
    else:
        return ""

# Input
while True:
    print("\nMain Menu")
    print("1. Ask me a question")
    print("2. Exit")
    choice = int(input("Enter a number (1-2): "))

    # Output

    if choice == 1:
        askQuestion = input("What is your question?: ").lower()
        response = checkQuestion(askQuestion)
        if response == "":
            print(randomResponce())
        else:
            print(response)

    elif choice == 2:
        break
    else:
        print("Please enter a number between 1-2.")
    