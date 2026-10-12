
# STUDENT EXPENSE TRACKER

# Display project title
print("===== STUDENT EXPENSE TRACKER =====")

# Enter monthly budget
budget = float(input("Enter monthly budget: Rs. "))

# Empty list to store expenses
expenses = [] 

# Display menu up to 100 times
for i in range(100): # REFERENCE FROM CHATGPT

    print("\n===== MAIN MENU =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Budget Summary")
    print("4. Exit")

    # Take user's choice
    choice = int(input("Enter your choice: "))

    # Option 1: Add expense
    if choice == 1:
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: Rs. "))

        # Check valid amount
        if amount > 0:
            expenses.append([category, amount])
            print("Expense added successfully!")
        else:
            print("Invalid amount!")

    # Option 2: View expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses recorded!")
        else:
            print("\n===== YOUR EXPENSES =====")

            # Display all expenses
            for expense in expenses:
                print(expense[0], "- Rs.", expense[1])

    # Option 3: Budget summary
    elif choice == 3:

        # Calculate total expenses
        total = 0
        for expense in expenses:
            total = total + expense[1]

        # Calculate remaining budget
        remaining = budget - total

        print("\n===== BUDGET SUMMARY =====")
        print("Number of Expenses:", len(expenses))
        print("Monthly Budget: Rs.", budget)
        print("Total Expenses: Rs.", total)
        print("Remaining Budget: Rs.", remaining)

        # Check budget
        if remaining < 0:
            print("Warning! Budget exceeded!")
        else:
            print("You are within your budget!")

    # Option 4: Exit
    elif choice == 4:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")
