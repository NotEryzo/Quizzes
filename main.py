# # Letter grades task


# # Percentage to Letter Grade Function
# def getLetterGrade(percentage):
#     if 100 >= percentage >= 85:
#         output = "A"
#     elif 84 >= percentage >= 70:
#         output = "B"
#     elif 69 >= percentage >= 60:
#         output = "C"
#     elif 59 >= percentage >= 50:
#         output = "D"
#     elif 49 >= percentage >= 0:
#         output = "F"
#     else:
#         output = print("That is not between 0 - 100!")
#     return output

# # Input Percentages 
# print("Percentage grade to Letter grade program")
# print("\nInput percentage grades")
# Engper = int(input("Enter percentage grade for English: "))
# Socialper = int(input("Enter percentage grade for Social Studies: "))
# Mathper = int(input("Enter percentage grade for Social Mathematics: "))
# Sciper = int(input("Enter percentage grade for Science: "))

# # Ouput Letter Grades
# print("\nLetter Grades")
# print(f"English Letter Grade: {getLetterGrade(Engper)}")
# print(f"Social Studies Letter Grade: {getLetterGrade(Socialper)}")
# print(f"Mathematics Letter Grade: {getLetterGrade(Mathper)}")
# print(f"Science Letter Grade: {getLetterGrade(Sciper)}")


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
    