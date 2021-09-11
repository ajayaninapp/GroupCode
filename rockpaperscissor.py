import random

winning_options = {1: (2, 1, "Player"), 2: (3, 2, "Player"), 3: (1, 3, "Player"), 4: (1, 2, "CPU"), 5: (2, 3, "CPU"),
                   6: (3, 1, "CPU"), 7: (1, 1, "Tie"), 8: (2, 2, "Tie"), 9: (3, 3, "Tie")}
options = {"rock": 1, "paper": 2, "scissors": 3}
scores = {"Player": 0, "CPU": 0, "Tie": 0}
play_again = "yes"
round_winner = None
history = {1: []}

no_of_rounds = int(input("Enter the number of Rounds : "))
for i in range(0, no_of_rounds):
    user_input = user_choice = (input("Player choice (rock, paper, scissors): ")).lower()
    user_input = options[user_input]
    cpu_input = cpu_choice = random.choice(list(options.keys()))
    print("CPU choice : {}".format(cpu_input))
    cpu_input = options[cpu_input]
    for j in winning_options:
        if winning_options[j][0] == user_input and winning_options[j][1] == cpu_input:
            round_winner = winning_options[j][2]
            scores[round_winner] = scores[round_winner] + 1
        history[i + 1] = [user_choice, cpu_choice, round_winner]
print("Player Score : {}\nCPU Score    : {}".format(scores["Player"], scores["CPU"]))
if scores["Player"] > scores["CPU"]:
    print("Winner of the series is Player")
elif scores["Player"] < scores["CPU"]:
    print("Winner of the series is CPU")
else:
    print("The Series is Tied")
round_history = int(input("Enter the round whose information is needed (0 to exit): "))
while round_history != 0:
    print("Player Choice : {}\nCPU Choice    : {}\nRound Winner  : {}".format(history[round_history][0],
                                                                              history[round_history][1],
                                                                              history[round_history][2]))
    round_history = int(input("Enter the round whose information is needed (0 to exit): "))