"""from magic_eight_ball import get_eight_ball_response
question = input ("Ask the magic Eight Ball question: ")

try:
    if not question.strip():
        raise ValueError("question can not be empty")
    answer = get_eight_ball_response()
    print(f"\nMagic Eight Ball Says: {answer}")
except ValueError as error:
    print(f"Input error: {error}")"""

balance = 5000.00
print("Welcome to the class Bank")
while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw money")
        print("4. Exit")

        option = input("Choose an option")
        match option:
            case "1":
                print(f"Your balance is £{balance:.2f}")
            case "2":
                try:
                    amount = float(input("Enter amount to deposit: £"))
                    if amount <=0:
                        raise ValueError("Amount must be greater than Zero.")
                    balance += amount
                    print(f"deposit successful")
                    print(f"New balance {balance:.2f}")
                except ValueError as error:
                    print("Error: ", error)

            case "3":
                try:
                    amount = float(input("Enter amount to Withdraw: £"))
                    if amount <=0:
                        raise ValueError("Amount must be greater than Zero.")
                    if amount > balance:
                        raise ValueError("Insufficient balance")

                    balance -= amount
                    print("Withdrawal successful")
                    print(f"New balance £{balance:.2f}")
                    
                except ValueError as error:
                    print("Error: ", error)

                
            case "4":
                print("Good bye!")
                break
            case _:
                print ("Invalid option. Please choose 1,2,3 or 4")

            