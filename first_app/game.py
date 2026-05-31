import random

from pip._internal.utils import retry


# def game():
#     print("""
#         Please enter number :
#         1) stone:
#         2) paper:
#         3) scissors:
#     """)
#     user_entered_value =  input("Please enter number : ")
#     if user_entered_value.lower() == "quit":
#         print("Goodbye!")
#         return
#
#     random_value =  random.choice("123")
#     actual_random_value = int(random_value)
#     print(actual_random_value)
#     if user_entered_value.isdigit():
#         actual_user_value = int(user_entered_value)
#         if 0 < int(actual_user_value) < 4:
#             if actual_user_value == actual_random_value:
#                 print("Both are equal!")
#             elif actual_user_value == 1 and actual_random_value == 3:
#                 print("You win!")
#             elif actual_user_value == 2 and actual_random_value == 1:
#                 print("you loss!")
#             elif actual_user_value == 3 and actual_random_value == 2:
#                 print("You win!")
#             else:
#                 print("You lose!")
#         return game()
# game()

# make that better

game_count = 0
def game():
    print("""
        Please enter number : 
        1) stone:
        2) paper:
        3) scissors:
    """)
    user_entered_value =  input("Please enter number : ")
    if user_entered_value.lower() == "quit":
        print("Goodbye!")
        return

    if user_entered_value not in ["1", "2", "3"]:
        print("Please enter number from 1 to 3")
        return game()

    random_value =  random.choice("123")
    actual_random_value = int(random_value)

    actual_user_value = int(user_entered_value)

    def decide_winner(player , computer_value):
        print(f"your choice is {player} random choice is {computer_value}")
        if player == computer_value:
            return "Both are equal!"
        elif player == 1 and computer_value == 3:
            return "You win!"
        elif player == 2 and computer_value == 1:
            return "you loss!"
        elif player == 3 and computer_value == 2:
            return "You win!"
        else:
            return "You lose!"
    game_return = decide_winner(actual_user_value, actual_random_value)
    print(game_return)
    global game_count
    game_count += 1

    print(f"{game_count} games played")
    return game()

game()
