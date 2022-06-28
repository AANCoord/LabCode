
# Problem 2-6
def rhytm():
    count = 0
    while count < 10:
        if count % 2 == 0:
            print("Rhythm")
        else:
            print("Blues")
        count += 1

# Problem 7
def squares():

    print(f"Number  Squares")
    for num in range(10):
        print(f"{num}       {num**2}")

#Problem 10
def guessing_game():
    correct_answer = 31
    while guessing:
        answer = int(input("Give me a number: "))

        if answer < correct_answer:
            print("Too Low")
        elif answer > correct_answer:
            print("Too high")
        else:
            print("Correct Number!")
            guessing = False

def main():
    rhytm()
    squares()
    guessing_game()


if __name__ == "__main__":
    main()