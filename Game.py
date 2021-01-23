from random import randint
from random import choice
import getpass


# Intro and Welcome to the game


def Intro():
    print("Welcome to Mastermind!")
    print("Developed by Anh Huy Nguyen")
    print("COMP 1046 Object-Oriented Programming")
    print("-------------------------------------------")


class GameControl():
    def gameOptions():  # print the game options
        print("                 Menu        ")
        print("(A) Original Mastermind for 2 Players")
        print("(B) Original Mastermind for 1 Player")
        print("(C) Mastermind44 for 4 Players")
        choice = True
        while choice:  # The while loop will run as long as the conditional expression evaluates to True.
            choice = input("Choose your option: ")
            if choice == "a":
                print("\n(A)")
                break   # implement break for stop while and exit loop
            elif choice == "b":
                print("\n(B)")

                break   # implement break for stop while and exit loop
            elif choice == "c":
                print("\n(C)")
                break   # implement break for stop while and exit loop
            elif choice != "":
                # if not choice will return and exit loop
                print("\nNot Valid Choice Try again")
    Intro()
    gameOptions()
    print("What would you like to do?")  # choose what would you like to do
    option = input("")
    if option == "p":
        print("(p)")  # play the game
    elif option == "q":
        print("(q)")  # quit the game
        exit()
    else:
        print("Good bye")  # exit the game
        exit()


class Mastermind_2pl():
    def feedback(blackPegs, whitePegs):  # feedback method
        # declare variable black pegs to feedback
        feedback1 = str(blackPegs) + " BLACK PEGS"
        # declare variable white pegs to feedback
        feedback2 = str(whitePegs) + " WHITE PEGS"

        if blackPegs == 1:
            feedback1 = feedback1[:-1]

        if whitePegs == 1:
            feedback2 = feedback2[:-1]

        # This is to take out the "S" if the number of white pegs or black pegs is singular

        feedback = feedback1 + " — " + feedback2 + "\n"
        return print(feedback)

    colours = ["R", "G", "Y", "W", "B"]  # add option list for colours
    play = "Y"
    while play == "Y":
        # This sets up the program so that later on the player can the game play again

        CodeMaker = []
        # pick up the code from the list above and hide other player
        CodeMaker = getpass.getpass("Please enter your code:\n")
        print("Enter your code again: ")
        # pick up the code from the list above and hide other player
        CodeMaker = getpass.getpass("")
        print("The code was stored")
        print("Welcome Supermind. You can now start to play by guessing the code.Enter a guess by providing four characters and press Enter.")

        # start the game

        win = False
        for g in range(5):  # You only get 5 guesses

            evaluateWin = False
            while evaluateWin == False:
                evaluateWin = True
                # You assume the user input is valid until you find out otherwise
                guessLimit = input("INPUT guess: ").upper()
                if len(guessLimit) != len(CodeMaker):  # catch exception for choices of colours
                    print("You have to type in 4 colours.")
                    evaluateWin = False
                else:
                    for i in range(4):  # you just can choose 4 colours
                        if guessLimit[i] not in colours:
                            print("Unexpected character. Please try again.")
                            evaluateWin = False
                            break

            guessLimit = list(guessLimit)  # store guessList

            blackPegs = 0
            whitePegs = 0
            for i in range(4):
                if guessLimit[i] == CodeMaker[i]:
                    blackPegs += 1
                    guessLimit[i] += "PEG!"

            for i in range(4):
                if guessLimit[i] in CodeMaker and guessLimit[i] != CodeMaker[i]:
                    whitePegs += 1
                    CodeMaker[CodeMaker.index(guessLimit[i])] += "PEG!"

            for i in range(4):
                if len(CodeMaker[i]) > 1:
                    CodeMaker[i] = (CodeMaker[i])[0]

            if blackPegs == 4:
                win = True
                break
            else:
                if g < 6:  # feedback for the guess
                    feedback(blackPegs, whitePegs)

        if win == True:
            print("You win! The code is " + "".join(CodeMaker) + ".")

        else:
            print("Sorry — the code was " + "".join(CodeMaker) + ". You lose.")

        print()
        play = input("Play again? (Y/N) ").upper()  # play again or not
        while play != "Y" and play != "N":
            print("Please respond with the letter 'Y' or 'N' only.")
        break


class Game():
    print("Welcome Tom Turbo, you need to create a code that consists of four pegs. Eeach peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack. Specify the code by specifying four characters where each character indicates a colour as above. For example, WWRG represents the code White-White-Red-Green. You need to enter the code twice. No character is shown on the screen so Supermind cannot see it.")

    def feedback(blackPegs, whitePegs):  # feedback method
        # declare variable black pegs to feedback
        feedback1 = str(blackPegs) + " BLACK PEGS"
        # declare variable white pegs to feedback
        feedback2 = str(whitePegs) + " WHITE PEGS"

        if blackPegs == 1:
            feedback1 = feedback1[:-1]

        if whitePegs == 1:
            feedback2 = feedback2[:-1]

        # This is to take out the "S" if the number of white pegs or black pegs is singular

        feedback = feedback1 + " — " + feedback2 + "\n"
        return print(feedback)

    colours = ["G", "R", "Y", "B", "W"]  # add colours list
    print("You will then be awarded one or more black or white pegs.")
    print("A black peg means right colour, right position.")
    print("A white peg means right colour, wrong position.")
    print("You have 12 guesses. Good luck!")

    play = "Y"  # start to play game
    while play == "Y":
        # This sets up the program so that later on the player has the option to play again

        current_guess = []  # Add random choices into list
        for i in range(4):
            current_guess.append(choice(colours))
            # This randomly selects the code from the colours list

        evaluateWin = False
        for g in range(12):  # You only get 12 guesses

            validated = False
            while validated == False:
                validated = True
                # You assume the user input is valid until you find out otherwise
                playerLimit = input("INPUT guess: ").upper()
                if len(playerLimit) != len(current_guess):
                    print("You have to type in 4 colours.")
                    validated = False
                else:
                    for i in range(4):      # you just can choose 4 colours
                        if playerLimit[i] not in colours:
                            print("Unexpected character. Please try again.")
                            validated = False
                            break

            playerLimit = list(playerLimit)  # store guess list

            blackPegs = 0
            whitePegs = 0
            for i in range(4):
                if playerLimit[i] == current_guess[i]:
                    blackPegs += 1
                    playerLimit[i] += "PEG!"
                    current_guess[i] += "PEG!"

            for i in range(4):
                if playerLimit[i] in current_guess and playerLimit[i] != current_guess[i]:
                    whitePegs += 1
                    current_guess[current_guess.index(
                        playerLimit[i])] += "PEG!"

            for i in range(4):
                if len(current_guess[i]) > 1:
                    current_guess[i] = (current_guess[i])[0]

            if blackPegs == 4:
                win = True
                break
            else:  # feedback for the guess
                if g < 13:
                    feedback(blackPegs, whitePegs)

        if evaluateWin == True:
            print("You win! The code is " + "".join(current_guess) + ".")

        else:
            print("Sorry — the code was " +
                  "".join(current_guess) + ". You lose.")
        break  # end the game

