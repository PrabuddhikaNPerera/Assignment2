#Student Name : Prabuddhika Panawalage
#Student ID : 10609924

def inputNumber(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 2:
                print("Error: The number must be greater than of equal 2.") # Check if the number is greater than or equal 2
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    #Define variables
    numberofplayers = 0
    playerNames = []

    #Welcome message
    print("Welcome to WordChain!")

    # Get number of players
    numberofplayers = inputNumber("Enter the number of players (minimum 2): ")
    print (numberofplayers)






main()