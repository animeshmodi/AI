import random

def monty_hall(num_simulations):
  """
  Simulates the Monty Hall problem for a given number of simulations.

  Args:
      num_simulations: The number of simulations to run.

  Returns:
      A tuple containing the win counts for switching and staying.
  """
  wins_switch = 0
  wins_stay = 0
  for _ in range(num_simulations):
    # Place the car behind a random door (1, 2, or 3)
    car_door = random.randint(1, 3)

    # Player chooses a random door
    player_choice = random.randint(1, 3)

    # Host reveals a goat behind a different door (not the car or player's choice)
    available_doors = set([1, 2, 3]) - {car_door, player_choice}
    host_reveals = random.choice(list(available_doors))

    # Option 1: Switch doors
    remaining_door = list(available_doors - {host_reveals})[0]
    if remaining_door == car_door:
      wins_switch += 1

    # Option 2: Stay with initial choice
    if player_choice == car_door:
      wins_stay += 1

  return wins_switch, wins_stay

if __name__ == "__main__":
  num_simulations = 10000  # Change this to desired number of simulations
  wins_switch, wins_stay = monty_hall(num_simulations)

  print(f"Wins by switching: {wins_switch}/{num_simulations} ({wins_switch/num_simulations:.2f})")
  print(f"Wins by staying: {wins_stay}/{num_simulations} ({wins_stay/num_simulations:.2f})")
