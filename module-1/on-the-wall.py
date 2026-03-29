# Samuel Dirr
# Assignment 1.3
# CSD 325
# Program: On the Wall

def countdown_bottles(bottle_count):
    """Count down bottles of beer from the starting number to 1."""
    """This is just one massive loop"""
    for bottles in range(bottle_count, 0, -1):
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print("Take one down, pass it around,")

            if bottles - 1 == 1:
                print("1 bottle of beer on the wall.\n")
            else:
                print(f"{bottles - 1} bottles of beer on the wall.\n")

        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around,")
            print("0 bottles of beer on the wall.\n")


def main():
    """Main function for program"""
    while True:
        try:
            bottle_count = int(input("How many bottles of beer are on the wall? "))

            if bottle_count < 1:
                print("Please enter a number greater than 0.\n")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    countdown_bottles(bottle_count)
    print("Time to buy more beer.")


if __name__ == "__main__":
    main()