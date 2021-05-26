# Version 2 Functioon asks for type of number being inputed

# Functions go here
def num_check(question, error, num_type, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()

# Main Routine
# looped for testing
while 1 == 1:
    # Asks user for amount of trials
    trial_error = "<error> Please enter an interger above 0"
    num_trials = num_check("What is the numebr of trials? ", trial_error, int, 0)

    # Sets number too an interger without decimal  } Changed in
    # num_trials = int(num_trials)                 } new version

    # Outputs the number of trials (For testing)
    print("Number of trials", num_trials)
    print()
    break