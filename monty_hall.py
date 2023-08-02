import random

def monty_hall_simulation(num_trials):
    stick_wins = 0
    switch_wins = 0

    for _ in range(num_trials):
        doors = [1, 2, 3]
        prize_door = random.choice(doors)
        player_choice = random.choice(doors)

        # Monty Hall reveals a door with a goat that is not the player's choice or the prize door
        doors.remove(player_choice)
        if player_choice != prize_door:
            doors.remove(prize_door)
        revealed_goat_door = random.choice(doors)

        # Player switches to the other unopened door
        player_choice = [door for door in doors if door != revealed_goat_door][0]

        # Check if player wins by sticking or switching
        if player_choice == prize_door:
            switch_wins += 1
        else:
            stick_wins += 1

    return stick_wins, switch_wins

if __name__ == "__main__":
    num_trials = int(input("Enter the number of trials: "))

    stick_wins, switch_wins = monty_hall_simulation(num_trials)

    print(f"Stick wins: {stick_wins} ({stick_wins/num_trials:.2f} probability)")
    print(f"Switch wins: {switch_wins} ({switch_wins/num_trials:.2f} probability)")
