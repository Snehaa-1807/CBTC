import random
def play_again():
  """Asks the user if they want to play another round."""
  answer = input("Do you want to play again? (y/n): ").lower()
  return answer == 'y'

def determine_winner(user_choice, computer_choice):
  """Determines the winner based on user and computer choices."""
  # Tie condition
  if user_choice == computer_choice:
    return "Tie"
  # Win conditions
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "Win"
    else:
      return "Lose"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "Win"
    else:
      return "Lose"
  elif user_choice == "scissors":
    if computer_choice == "paper":
      return "Win"
    else:
      return "Lose"
  else:
    return "Invalid Input"

def main():
  user_score = 0
  computer_score = 0

  while True:
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
      print("Invalid choice. Please try again.")
      continue
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(user_choice, computer_choice)
    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    if result == "Win":
      print("You Win!")
      user_score += 1  
    elif result == "Lose":
      print("You Lose!")
      computer_score += 1  
    else:
      print("It's a Tie!")

    if user_score > 0 or computer_score > 0:
      print(f"Your score: {user_score}")
      print(f"Computer score: {computer_score}")

    if not play_again():
      break

  print("Thanks for playing!")
if __name__ == "__main__":
  main()