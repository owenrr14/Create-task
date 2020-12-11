
import random

# List of NFL players that the game can chose from
# Lists also have hits attached to each player to help the user guess the player
TomBrady = ["Tom Brady", "He had 198 players selected before him", "He went to Michigan Collage", "He was a backup until the started got hurt", "He won 5 Super Bowls", "He was drafted by the Patriots"]
JoeMontana = ["Joe Montana", "He was selected 82nd overall in the 1979 NFL Draft", "He went at Notre Dame for Collage", "He is known as Joe Cool", "He was one of the best quarterbacks ever", "He won 4 Super Bowls wit the 49ers"]
PaytonManning = ["Payton Manning", "He was selected 1st overall in 1998 NFL Draft", "He suffered a herniated disc in 2011", "He went to the University of Tennessee", "He is in Many Nationwide commercials", "He played for the Colts and Broncos"]
OdellBeckhamJr = ["Odell Beckham Jr", "He was selected #12 overall in the 2014 NFL Draft", "He fought a kicking net", "He was traded to the browns for the 2019 season", "He made the most infamous one handed catches ever"]
TedyBruschi = ["Tedy Bruschi", "He wore #54 for the New England Patriots", "He went into the Collage football hall of fame in 2013 for Arizona collage", "He played linebacker his entire carrier", "He is well know at Roseville high", "He has a weight room named after him at Roseville High"]
OJSimpson = ["OJ Simpson", "He played running back for USC", "He got drafted #1 overall in the 1969 draft", "He is a convicted felon for murder", "He is known as The Juice", "He played for the Buffalo Bills and 49ers"]
MarkSanchez = ["Mark Sanchez", "He played QB for USC", "He was drafted #5 overall by the Jets", "He played for a total of 6 teams over 10 seasons", "He got to back to back AFC championship games", "He was most famous for being in the Butt Fumble play"]
AntonioBrown = ["Antonio Brown", "He was drafted #195 overall in 2010", "He went to the Michigan St.", "He was cut by the Raiders before ever playing a snap for them", "He played for the Steelers for most of his career", "He was suspended for 8 weeks before signing with the Buccaneers"]
AdamVinatieri = ["Adam Vinatieri", "He went undrafted and Played in NFL Europe for the first year of his career", "He played for the Patriots and the Colts", "He kicked 2 Superbowl winning field goals", "He has the most points ever by an NFL player", "Oldest player in the NFL"]
MarshawnLynch = ["Marshawn Lynch", "He was drafted by the Bills in 2007", "He was traded to the Seahawks after suffering a minor preseason injury", "He loves Skittles", "He caused the Beastquake", "He is known as Beast Mode"]

# player_list contains the names of the above players for randomized picking
player_list = ["TomBrady", "JoeMontana", "PaytonManning", "OdellBeckhamJr", "TedyBruschi", "OJSimpson", "MarkSanchez", "AntonioBrown", "AdamVinatieri", "MarshawnLynch"]


def random_player():
    # random_player() looks at the list of players and sets it to a variable to be used later
    # random_player() also gets rid of the player from the list so it does not repeat when you play again
    player = (random.choice(player_list))
    player_list.remove(player)
    return player


def find_player():
    # find_player() assigns the variable from random_player() to the list of the corresponding player list
    player = random_player()
    rplayer = ""

    if player == "TomBrady":
        rplayer = TomBrady

    if player == "JoeMontana":
        rplayer = JoeMontana

    if player == "PaytonManning":
        rplayer = PaytonManning

    if player == "OdellBeckhamJr":
        rplayer = OdellBeckhamJr

    if player == "TedyBruschi":
        rplayer = TedyBruschi

    if player == "OJSimpson":
        rplayer = OJSimpson

    if player == "MarkSanchez":
        rplayer = MarkSanchez

    if player == "AntonioBrown":
        rplayer = AntonioBrown

    if player == "AdamVinatieri":
        rplayer = AdamVinatieri

    if player == "MarshawnLynch":
        rplayer = MarshawnLynch

    return rplayer


def formality(guess):
    # formality() takes the guess and answer from main and gets rid of capitals, spaces and periods
    # when it compares the two so it is easier for the user to guess the player
    guess = guess.lower()
    if " " in guess:
        guess = guess.replace(" ", "")
    if "." in guess:
        guess = guess.replace(".", "")
    return guess


def welcome():
    # welcome() describes how the game is played
    print()
    print("Welcome to NFL Player Quiz!")
    print("You goal is to guess the NFL player that the hint corresponds to.")
    print("Guesses must include full names.")
    print("If the guess is wrong, you will get a new hint.")
    print("If you don't have a guess, hit enter.")
    print()
    # Asks the player if they are ready to continue
    input(str("Ready? Hit enter to start"))
    print()
    main()


def main():
    # main() initializes the important variables before running the game
    count = 1
    # mplayer is set to the random player with their list that was selected before
    mplayer = find_player()
    game = True
    while game:
        # The print statement below prints the first hint but as the game goes on count will be increased
        # So it will print the 2nd, then 3rd, etc.
        print(mplayer[count])
        guess = input(str("Guess a player: "))
        print()
        # Runs formality() to check if the guess was correct
        if formality(guess) == formality(mplayer[0]):
            # If the guess was correct it stops the game and asks them to play again
            print("You guessed the player!")
            game = False
            if not player_list:
                print()
                print("You have ran out of players to guess")
                print("If you want to play again, hit the rerun button")
            else:
                play_again = input(str("Do you want to play again? Y/N "))
                if play_again.upper() == "Y":
                    print()
                    main()
                elif play_again.upper() == "N":
                    print("Bye Bye!")
        else:
            # If the guess was wrong, it tells them and adds one to the count so it can print the next hint
            count += 1
            if count == 6:
                game = False
                # If the count ever exceeds the amount of hints it tells the player
                # That they have failed and asks to play again
                if not player_list:
                    print()
                    print("You have ran out of players to guess")
                    print("If you want to play again, hit the rerun button")
                else:
                    print("You never guessed the player, you lose.")
                    play_again = input(str("Do you want to play again? Y/N "))
                    if play_again.upper() == "Y":
                        print()
                        main()
                    elif play_again.upper() == "N":
                        print("Bye Bye!")
            else:
                print("Try again")
                print()


if __name__ == "__main__":
    welcome()
