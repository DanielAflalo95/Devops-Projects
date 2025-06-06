import random

def generate_lotto_combinations():
    while True:
        user_input = input("How many combinations do you want to generate?: ")
        try:
            amount = int(user_input)
            print("$$$ Generating numbers $$$")
            break
        except ValueError:
            print("Please enter a number")

    if amount > 30:
        print("Cannot generate more than 30 combinations at once!")
        print("Generating the maximum amount of combinations now...")
        amount = 30

    for combo in range(1, amount + 1):
        numbers = list(range(1, 38))
        strongnumbers = list(range(1, 8))
        normal = []

        for _ in range(6):
            pick = random.choice(numbers)
            normal.append(pick)
            numbers.remove(pick)

        strong = random.choice(strongnumbers)

        print(f"\n📦 Combo #{combo}: {', '.join(map(str, sorted(normal)))} | ⭐ Strong: {strong}")

    print("\n$$$ !!Good Luck!! $$$")

generate_lotto_combinations()
