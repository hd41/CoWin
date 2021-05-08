from helper.CowinRequests import *
from helper.CowinScheduler import *
import config


def print_bold(string):
    print("\033[1m" + string + "\033[0m")


def check_slots():
    while True:
        print("*" * 50)
        print("Please select any method to check for vaccination slots: ")
        print("1. Find slots by states and district.")
        print("2. Find slots by pincode.")
        print("(Type 'q' to quit)")
        choice = input("Enter your choice: ")
        if choice == '1':
            CowinRequests.get_states()
            state_input = input("Enter state you want to select: ")
            if int(state_input) > 37 or int(state_input) < 1:
                print("{} is not a valid state id. Try again ...".format(state_input))
                continue
            CowinRequests.get_districts_by_state_id(state_input)
            district_input = input("Enter district you want to find slots in: ")
            CowinRequests.get_slots_by_district_id(district_input)
        elif choice == '2':
            pincode_input = input("Enter the pincode you want to find slots in: ")
            CowinRequests.get_slots_by_pincode(pincode_input)
        elif choice == 'q' or choice == 'Q' or choice.lower() == 'quit':
            break
        else:
            print_bold("There is no choice like '" + choice + "'.")


def main():
    print("Welcome to slot finder for COVID-19 vaccine")
    while True:
        print("A. Find slots.")
        print("B. Make a scheduler.")
        choice = input("Enter your choice: ")
        if choice == 'A' or choice == 'a':
            check_slots()
        elif choice == 'B' or choice == 'b':
            CowinScheduler.schedule()
        elif choice == 'q' or choice == 'Q' or choice.lower() == 'quit':
            break
        else:
            print_bold("Make a valid choice")
    print_bold("Successfully able to quit.")


if __name__ == '__main__':
    main()
