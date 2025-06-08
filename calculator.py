def show_menu():
    print("\n" + "="*30)
    print("     ✨ SIMPLE CALCULATOR ✨")
    print("="*30)
    print("1️⃣  Addition")
    print("2️⃣  Subtraction")
    print("3️⃣  Multiplication")
    print("4️⃣  Division")
    print("5️⃣  Exit")
    print("="*30)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️  Invalid number. Try again.")

def calculator():
    while True:
        show_menu()
        choice = input("👉 Select option (1-5): ").strip()

        if choice == '5':
            print("👋 Exiting... Stay sharp!")
            break

        elif choice in {'1', '2', '3', '4'}:
            num1 = get_number("🔢 Enter first number: ")
            num2 = get_number("🔢 Enter second number: ")

            if choice == '1':
                result = num1 + num2
                operation = '+'
            elif choice == '2':
                result = num1 - num2
                operation = '-'
            elif choice == '3':
                result = num1 * num2
                operation = '*'
            elif choice == '4':
                if num2 == 0:
                    print("🚫 Error: Division by zero is undefined.")
                    continue
                result = num1 / num2
                operation = '/'

            print(f"✅ Result: {num1} {operation} {num2} = {result}")

        else:
            print("❌ Invalid input. Please choose a number between 1 and 5.")

# Run the calculator
calculator()
