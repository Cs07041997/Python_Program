import random
class Gambler:

    bet_amount=1
    def gamblerProblem():
        stake = int(input("Enter the stake Amount: "))
        goal = int(input("Enter the amount you want to win: "))
        bet_made = int(input("Enter The number of bets you want to want to make: "))
        no_of_times_won=0
        no_of_times_lost=0
        no_of_bets_made=0

        while(stake >=0 and stake <= goal and no_of_bets_made < bet_made):
            no_of_bets_made += 1
            gambler_choice = random.random()  #generate a random floating-point number in the range (0.0, 1.0)

            if gambler_choice>0.5:
                no_of_times_won += 1
                stake=stake+1
            else:
                no_of_times_lost+=1
                stake=stake-1

        print("Number of times won", no_of_times_won)
        print("percentage of win", (no_of_times_won/bet_made)*100)
        print("percentage of loss", (no_of_times_lost/bet_made)*100)
        print("Number of Bets Made", no_of_bets_made)


    gamblerProblem()

