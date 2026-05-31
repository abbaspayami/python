import random

def game():
    game_count = 0
    player_winner = 0
    computer_winner = 0
    def play_game():
        nonlocal player_winner
        nonlocal computer_winner
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
            return play_game()

        random_value =  random.choice("123")
        actual_random_value = int(random_value)

        actual_user_value = int(user_entered_value)

        def decide_winner(player , computer_value):
            nonlocal player_winner
            nonlocal computer_winner
            print(f"your choice is: {player} \nrandom choice is: {computer_value}")
            if player == computer_value:
                return "Both are equal!"
            elif player == 1 and computer_value == 3:
                player_winner +=1
                return "You win!"
            elif player == 2 and computer_value == 3:
                player_winner  +=1
                return "You win!"
            elif player == 3 and computer_value == 2:
                player_winner  +=1
                return "You win!"
            else:
                computer_winner +=1
                return "You lose!"
        game_return = decide_winner(actual_user_value, actual_random_value)
        print(game_return)
        nonlocal game_count
        game_count += 1

        print(f"{game_count} games played")
        print(f"Player has won {player_winner} times")
        print(f"Computer has won {computer_winner} times")
        return play_game()

    return play_game

play = game()
play()
