import random
while True:
    print("""
    please choose one of them...
    1 . stone
    2 . paper
    3 . scissor
    """)
    user_entered_value = input("Press enter number in order to game will be start...\n")
    if user_entered_value.lower() == "quit":
        break
    actual_value = int(user_entered_value)
    random_value = random.choice("123")
    actual_random_value = int(random_value)
    print(random_value)
    if user_entered_value.isdigit():
        if 0 < int(actual_value) < 4 :
            if actual_value == actual_random_value:
                print("Both are equal!")
            elif actual_value == 1 and actual_random_value == 3:
                print("You win!")
            elif actual_value == 2 and actual_random_value == 1:
                print("You win!")
            elif actual_value == 3 and actual_random_value == 2:
                print("You win!")
            else:
                print("You lose!")




    