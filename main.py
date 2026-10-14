from datetime import date

def calculate_simple_interest(principal, rate, time):
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Values cannot be negative.")

    interest = principal * rate * time / 100
    return interest, principal + interest


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def calculate_receipt_total(items):
    if not items:
        raise ValueError("At least one item is required.")

    total = 0.0

    for name, price, quantity in items:
        if not name.strip():
            raise ValueError("Item name cannot be empty.")

        if price < 0 or quantity <= 0:
            raise ValueError("Invalid price or quantity.")

        total += price * quantity

    return total


def calculate_age(birth_year, current_year):
    if birth_year < 1 or birth_year > current_year:
        raise ValueError("Invalid birth year.")

    return current_year - birth_year


def simple_interest():
    """Calculate simple interest."""
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (%): "))
        time = float(input("Enter the time in years: "))

        if principal < 0 or rate < 0 or time < 0:
            print("Error: Values cannot be negative.")
            return

        interest, total = calculate_simple_interest(
            principal, rate, time
        )

        print(f"Simple interest: {interest:.2f}")
        print(f"Total amount: {total:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers.")


def temperature_converter():
    """Convert Celsius to Fahrenheit or Fahrenheit to Celsius."""
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose a conversion: ")

    try:
        temperature = float(input("Enter the temperature: "))

        if choice == "1":
            result = celsius_to_fahrenheit(temperature)
            print(f"Temperature: {result:.2f} °F")

        elif choice == "2":
            result = fahrenheit_to_celsius(temperature)
            print(f"Temperature: {result:.2f} °C")

        else:
            print("Invalid conversion choice.")

    except ValueError:
        print("Error: Please enter a valid temperature.")


def receipt_calculator():
    """Calculate the total cost of items."""
    try:
        number_of_items = int(input("How many items are you purchasing? "))

        if number_of_items <= 0:
            print("Error: Enter at least one item.")
            return

        total = 0.0

        for item_number in range(1, number_of_items + 1):
            print(f"\nItem {item_number}")

            name = input("Enter item name: ").strip()
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))

            if not name:
                print("Error: Item name cannot be empty.")
                return

            if price < 0 or quantity <= 0:
                print("Error: Price cannot be negative "
                      "and quantity must be positive.")
                return

            item_total = calculate_receipt_total([
                (name, price, quantity)
            ])

            total += item_total

            print(f"{name}: {item_total:.2f}")

        print(f"\nReceipt total: {total:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers.")


def age_calculator():
    """Calculate age using the birth year."""
    try:
        current_year = date.today().year
        birth_year = int(input("Enter your birth year: "))

        if birth_year > current_year:
            print("Error: Birth year cannot be in the future.")
            return

        if birth_year < 1:
            print("Error: Enter a valid birth year.")
            return

        age = calculate_age(birth_year, current_year)

        print(f"Your age is approximately {age} years.")

    except ValueError:
        print("Error: Enter a valid year.")


def display_menu():
    """Display the toolkit menu."""
    print("\n" + "=" * 35)
    print("       PYUTILITY TOOLKIT")
    print("=" * 35)
    print("1. Simple Interest Calculator")
    print("2. Temperature Converter")
    print("3. Receipt Calculator")
    print("4. Age Calculator")
    print("5. Exit")
    print("=" * 35)


def main():
    """Run the CLI toolkit."""
    print("Welcome to PyUtility Toolkit!")

    while True:
        display_menu()

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            simple_interest()

        elif choice == "2":
            temperature_converter()

        elif choice == "3":
            receipt_calculator()

        elif choice == "4":
            age_calculator()

        elif choice == "5":
            print("Thank you for using PyUtility Toolkit!")
            break

        else:
            print("Invalid option. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()