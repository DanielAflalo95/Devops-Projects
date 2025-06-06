import json
import sys

# Load users information from JSON
def load_users():
    with open("users.json", "r") as file:
        data = json.load(file)
        return data["users"]

users = load_users()

# Saving the user information to the JSON file after actions
def save_users(users):
    with open("users.json", "w") as file:
        json.dump({"users": users}, file, indent=4)

# --- Function: Login ---
def login():
    print("Hello, Welcome to the ATM machine")
    for attempts in range(3):
        name_input = input("Enter your full name: ").strip().lower()
        if name_input in users:
            print(f"Welcome {users[name_input]['name']}!")
            return name_input
        else:
            print("User not found, please try again.")
    print("Too many failed attempts. Exiting...")
    sys.exit()

# --- Function: PIN Check ---
def pin_check(current_user):
    user_data = users[current_user]
    pin = user_data["pin"]
    for attempts in range(3):
        try:
            password = int(input("Please enter your 4-digit PIN code: "))
        except ValueError:
            print("PIN must be a number.")
            continue
        if password == pin:
            print("Valid PIN code.")
            return user_data
        else:
            print(f" Wrong PIN. You have {2 - attempts} attempt(s) left.")
    print("You have failed all 3 attempts. Exiting ATM Application!")
    sys.exit()

# The actual ATM action menu for doing specific actions
def action_menu(user_data):
    while True:
        print("\nWhat would you like to do?")
        print("[W] Withdraw")
        print("[D] Deposit")
        print("[C] Check Balance")
        print("[P] Pin Change")
        print("[L] Show Last 3 Actions")
        print("[Q] Quit")

        choice = input("Insert your choice: ").lower()

        if choice == "w":
            withdraw(user_data, users)
        elif choice == "d":
            deposit(user_data, users)
        elif choice == "c":
            check(user_data)
        elif choice == "p":
            pin_change(user_data, users)
        elif choice == "l":
            last_actions(user_data, users)
        elif choice == "q":
            print("Exiting ATM system, Have a good day!")
            sys.exit()
        else:
            print("Invalid choice, please try again...")


def check(user_data):
    print(f"\nYour current balance is: {user_data['balance']} NIS")
    action = {"type": "Balance Check"}
    user_data["last actions"].append(action)
    user_data["last actions"] = user_data["last actions"][-3:]
    save_users(users)

# Gives the user the option to deposit money or to quit to the main menu
def deposit(user_data, users):
    while True:
        amount_input = input("\nPlease insert the amount you want to deposit, or type 'Q' to quit: ").lower()

        if amount_input == "q":
            return
        try:
            amount = int(amount_input)
            if amount > 0 and any(amount % x == 0 for x in (20, 50, 100, 200)):
                user_data['balance'] += amount
                action = {"type": "Deposit", "amount": amount}
                user_data["last actions"].append(action)
                user_data["last actions"] = user_data["last actions"][-3:]
                save_users(users)
                print(f"Deposit successful. New balance: {user_data['balance']} NIS")
                return #after successful deposit
            else:
                print(" Invalid amount. Must be a multiple of 20, 50, 100 or 200.")
        except ValueError:
            print(" Please enter a valid number.")

#Gives the user the option to withdraw or to quit to the main menu
def withdraw(user_data, users):
    while True:
        amount_input = input("\nPlease insert the amount you want to withdraw, or type 'Q' to quit: ").lower()

        if amount_input == "q":
            return

        try:
            amount = int(amount_input)

            if amount <= user_data['balance']:
                if amount > 0 and any(amount % x == 0 for x in (20, 50, 100, 200)):
                    user_data['balance'] -= amount
                    action = {"type": "Withdraw", "amount": amount}
                    user_data["last actions"].append(action)
                    user_data["last actions"] = user_data["last actions"][-3:]
                    save_users(users)
                    print("Withdrawal successful. Please take your money.")
                    print(f"New balance: {user_data['balance']} NIS")
                    return  # Exit after successful withdrawal
                else:
                    print(" Invalid amount. Must be a multiple of 20, 50, 100 or 200.")
            else:
                print(f" You can't withdraw more than your current balance ({user_data['balance']} NIS).")

        except ValueError:
            print(" Please enter a valid number.")

def pin_change(user_data, users):
    pin = user_data["pin"]
    for attempts in range(3):
        try:
            password = int(input("Please enter your 4-digit PIN code: "))
        except ValueError:
            print("PIN must be a number.")
            continue

        if password == pin:
            print("Valid PIN code.")
            for attempts in range(3):
                firstpin = input("Please enter your new PIN code: ").strip()
                secondpin = input("Please enter your new PIN code again: ").strip()

                if not (firstpin.isdigit() and secondpin.isdigit()):
                    print("PIN must contain numbers only!")
                    continue

                if len(firstpin) != 4 or len(secondpin) != 4:
                    print("PIN must be exactly 4 digits!")
                    continue

                if firstpin != secondpin:
                    print("PINs do not match. Try again.")
                    continue

                # All checks passed:
                user_data["pin"] = int(firstpin)
                print("✅ Your PIN code was changed successfully!")
                action = {"type": "pin change"}
                user_data["last actions"].append(action)
                user_data["last actions"] = user_data["last actions"][-3:]
                save_users(users)
                return user_data

            print("You failed to set a valid PIN in 3 attempts.")
            return user_data
        else:
            print(f"Wrong PIN. You have {2 - attempts} attempt(s) left.")

    print("You have failed all 3 attempts. Exiting ATM Application!")
    sys.exit()


def last_actions(user_data, users):
    print("\n🧾 Last 3 actions:")
    for action in reversed(user_data["last actions"]):
        if action is None:
            continue
        elif "amount" in action:
            print(f"{action['type'].capitalize()} - {action['amount']} NIS")
        else:
            print(f"{action['type'].capitalize()}")


# --- Main Program Flow ---
current_user = login()
user_data = pin_check(current_user)
action_menu(user_data)