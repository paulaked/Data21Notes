user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit():
        user_prompt = False
    else:
        print("please provide your answer as a digit")