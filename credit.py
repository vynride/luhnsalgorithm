from sys import exit


# Prompt user for a card and store it's length
card_number = input("Enter Credit Card Number: ")
num_length = len(card_number)


def main():
    card_check()


def card_check():
    # Exit if card number is not comprised only of int
    for char in card_number:
        if char.isalpha():
            print("INVALID")
            # exit(1)

    # Exit if length of card_number string is invalid
    if num_length not in (13, 15, 16):
        print("INVALID")
        # exit(1)

    else:
        # Check for AMEX
        if num_length == 15:
            if card_number[0] == "3" and (card_number[1] == "4" or card_number[1] == "7"):
                if verify_card():
                    print("AMEX")

                else:
                    print("INVALID")

            else:
                print("INVALID")

        # Check for 16 digit MASTERCARD or VISA
        elif num_length == 16:
            # MASTERCARD
            if card_number[0] == "5" and "1" <= card_number[1] <= "5":
                if verify_card():
                    print("MASTERCARD")

                else:
                    print("INVALID")
            # VISA
            elif card_number[0] == "4":
                if verify_card():
                    print("VISA")

                else:
                    print("INVALID")

            else:
                print("INVALID")

        # Check for 13 digit VISA
        elif num_length == 13:
            if card_number[0] == "4":
                if verify_card():
                    print("VISA")
                else:
                    print("INVALID")

            else:
                print("INVALID")


# Verify card with Luhn's Algorithm
def verify_card():
    # Set initial values to zero
    count_even = 0
    count_odd = 0

    for num in range(num_length - 1, -1, -1):

        # num is even: update count_odd to include num
        if (num_length - (num + 1)) % 2 == 0:
            count_even = count_even + int(card_number[num])

        # num is odd: multiply the value at card_number[num] with 2
        else:
            temp = int(card_number[num]) * 2

            # Ensure num is a single digit
            while temp > 9:
                temp = temp - 9

            count_odd = count_odd + temp

    # Calculate final number
    total = count_odd + count_even

    # Check if total follows Luhn's Algorithm
    if (total % 10) == 0:
        return True

    return False


main()
