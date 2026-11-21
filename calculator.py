"""
=============================================================================
Project 01: Interactive Calculator & Unit Converter
InternCircle Internship Assignment
=============================================================================
A beginner-friendly Python CLI application that provides:
1. Basic Arithmetic Operations (+, -, *, /, %, ^)
2. Unit Conversions (km to miles, Celsius to Fahrenheit, meters to feet, kg to lbs)
3. Currency Conversions (USD, INR, EUR, GBP)
4. Robust input validation using while loops
5. Calculation history tracker
=============================================================================
"""

import sys

# Global list to store session history
history_log = []


# =============================================================================
# 1. HELPER FUNCTIONS FOR INPUT VALIDATION (USING WHILE LOOPS)
# =============================================================================

def get_valid_float(prompt: str) -> float:
    """Prompt the user for a numeric value using a while loop until valid."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("⚠️  Invalid input! Please enter a valid number (e.g. 10, 3.14).")


def get_non_zero_float(prompt: str) -> float:
    """Ensure divisor is not zero to prevent ZeroDivisionError."""
    while True:
        val = get_valid_float(prompt)
        if val == 0:
            print("⚠️  Error: Division by zero is not allowed. Please enter a non-zero number.")
        else:
            return val


# =============================================================================
# 2. ARITHMETIC FUNCTIONS
# =============================================================================

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b (b guaranteed non-zero)."""
    return a / b


def modulus(a: float, b: float) -> float:
    """Calculate remainder of a divided by b."""
    return a % b


def power(a: float, b: float) -> float:
    """Calculate a raised to power b."""
    return a ** b


def run_arithmetic_calculator():
    """Interactive Arithmetic Calculator submenu."""
    while True:
        print("\n" + "=" * 50)
        print("         ➕ ARITHMETIC CALCULATOR ➖")
        print("=" * 50)
        print("  [1] Addition (+)")
        print("  [2] Subtraction (-)")
        print("  [3] Multiplication (*)")
        print("  [4] Division (/)")
        print("  [5] Modulus / Remainder (%)")
        print("  [6] Power / Exponentiation (^)")
        print("  [0] Back to Main Menu")
        print("=" * 50)

        choice = input("Select an operation (0-6): ").strip()

        if choice == "0":
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("⚠️  Invalid choice! Please select an option from 0 to 6.")
            continue

        num1 = get_valid_float("Enter first number: ")

        if choice == "1":
            num2 = get_valid_float("Enter second number: ")
            result = add(num1, num2)
            op = "+"
        elif choice == "2":
            num2 = get_valid_float("Enter second number: ")
            result = subtract(num1, num2)
            op = "-"
        elif choice == "3":
            num2 = get_valid_float("Enter second number: ")
            result = multiply(num1, num2)
            op = "*"
        elif choice == "4":
            num2 = get_non_zero_float("Enter second number (divisor): ")
            result = divide(num1, num2)
            op = "/"
        elif choice == "5":
            num2 = get_non_zero_float("Enter second number (divisor): ")
            result = modulus(num1, num2)
            op = "%"
        elif choice == "6":
            num2 = get_valid_float("Enter exponent power: ")
            result = power(num1, num2)
            op = "^"

        record = f"{num1} {op} {num2} = {result}"
        history_log.append(record)

        print("\n" + "-" * 35)
        print(f"  Result: {record}")
        print("-" * 35)

        again = input("\nPerform another calculation? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break


# =============================================================================
# 3. UNIT CONVERTER FUNCTIONS
# =============================================================================

def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km * 0.621371


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles / 0.621371


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9.0 / 5.0) + 32.0


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32.0) * 5.0 / 9.0


def kg_to_pounds(kg: float) -> float:
    """Convert kilograms to pounds (lbs)."""
    return kg * 2.20462


def pounds_to_kg(pounds: float) -> float:
    """Convert pounds (lbs) to kilograms."""
    return pounds / 2.20462


def meters_to_feet(meters: float) -> float:
    """Convert meters to feet."""
    return meters * 3.28084


def feet_to_meters(feet: float) -> float:
    """Convert feet to meters."""
    return feet / 3.28084


def run_unit_converter():
    """Interactive Unit Converter submenu."""
    while True:
        print("\n" + "=" * 50)
        print("           📏 UNIT CONVERTER 🌡️")
        print("=" * 50)
        print("  [1] Kilometers ➔ Miles")
        print("  [2] Miles ➔ Kilometers")
        print("  [3] Celsius ➔ Fahrenheit")
        print("  [4] Fahrenheit ➔ Celsius")
        print("  [5] Meters ➔ Feet")
        print("  [6] Feet ➔ Meters")
        print("  [7] Kilograms (kg) ➔ Pounds (lbs)")
        print("  [8] Pounds (lbs) ➔ Kilograms (kg)")
        print("  [0] Back to Main Menu")
        print("=" * 50)

        choice = input("Select a conversion (0-8): ").strip()

        if choice == "0":
            break

        if choice not in [str(i) for i in range(1, 9)]:
            print("⚠️  Invalid choice! Please select an option from 0 to 8.")
            continue

        if choice == "1":
            val = get_valid_float("Enter distance in kilometers: ")
            res = km_to_miles(val)
            record = f"{val:.2f} km = {res:.4f} miles"
        elif choice == "2":
            val = get_valid_float("Enter distance in miles: ")
            res = miles_to_km(val)
            record = f"{val:.2f} miles = {res:.4f} km"
        elif choice == "3":
            val = get_valid_float("Enter temperature in Celsius (°C): ")
            res = celsius_to_fahrenheit(val)
            record = f"{val:.2f} °C = {res:.2f} °F"
        elif choice == "4":
            val = get_valid_float("Enter temperature in Fahrenheit (°F): ")
            res = fahrenheit_to_celsius(val)
            record = f"{val:.2f} °F = {res:.2f} °C"
        elif choice == "5":
            val = get_valid_float("Enter length in meters: ")
            res = meters_to_feet(val)
            record = f"{val:.2f} m = {res:.4f} ft"
        elif choice == "6":
            val = get_valid_float("Enter length in feet: ")
            res = feet_to_meters(val)
            record = f"{val:.2f} ft = {res:.4f} m"
        elif choice == "7":
            val = get_valid_float("Enter weight in kilograms: ")
            res = kg_to_pounds(val)
            record = f"{val:.2f} kg = {res:.4f} lbs"
        elif choice == "8":
            val = get_valid_float("Enter weight in pounds: ")
            res = pounds_to_kg(val)
            record = f"{val:.2f} lbs = {res:.4f} kg"

        history_log.append(record)

        print("\n" + "-" * 35)
        print(f"  Converted: {record}")
        print("-" * 35)

        again = input("\nPerform another unit conversion? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break


# =============================================================================
# 4. CURRENCY CONVERTER FUNCTIONS
# =============================================================================

# Benchmark exchange rates (relative to 1 USD)
EXCHANGE_RATES_TO_USD = {
    "USD": 1.00,
    "INR": 86.50,
    "EUR": 0.95,
    "GBP": 0.79,
    "CAD": 1.40,
    "AED": 3.67
}

def convert_currency(amount: float, from_curr: str, to_curr: str) -> float:
    """Convert amount between supported currencies using USD as base."""
    rate_from = EXCHANGE_RATES_TO_USD[from_curr]
    rate_to = EXCHANGE_RATES_TO_USD[to_curr]
    # Convert to USD base first, then to target currency
    amount_in_usd = amount / rate_from
    return amount_in_usd * rate_to


def run_currency_converter():
    """Interactive Currency Converter submenu."""
    currencies = list(EXCHANGE_RATES_TO_USD.keys())

    while True:
        print("\n" + "=" * 50)
        print("          💱 CURRENCY CONVERTER 💵")
        print("=" * 50)
        print("Supported Currencies:")
        for idx, curr in enumerate(currencies, 1):
            print(f"  [{idx}] {curr}")
        print("  [0] Back to Main Menu")
        print("=" * 50)

        # Get 'from' currency
        while True:
            from_choice = input(f"Select source currency (1-{len(currencies)}) or 0 to exit: ").strip()
            if from_choice == "0":
                return
            if from_choice.isdigit() and 1 <= int(from_choice) <= len(currencies):
                from_curr = currencies[int(from_choice) - 1]
                break
            print("⚠️  Invalid selection! Please choose a valid currency index.")

        # Get 'to' currency
        while True:
            to_choice = input(f"Select target currency (1-{len(currencies)}) or 0 to exit: ").strip()
            if to_choice == "0":
                return
            if to_choice.isdigit() and 1 <= int(to_choice) <= len(currencies):
                to_curr = currencies[int(to_choice) - 1]
                break
            print("⚠️  Invalid selection! Please choose a valid currency index.")

        # Get amount with while loop validation (must be positive)
        while True:
            amount = get_valid_float(f"Enter amount in {from_curr}: ")
            if amount < 0:
                print("⚠️  Amount cannot be negative. Please enter a positive value.")
            else:
                break

        converted = convert_currency(amount, from_curr, to_curr)
        record = f"{amount:,.2f} {from_curr} = {converted:,.2f} {to_curr}"
        history_log.append(record)

        print("\n" + "-" * 40)
        print(f"  Conversion: {record}")
        print("-" * 40)

        again = input("\nPerform another currency conversion? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break


# =============================================================================
# 5. CALCULATION HISTORY
# =============================================================================

def view_history():
    """Display calculation history for current session."""
    print("\n" + "=" * 50)
    print("           📜 RECENT CALCULATION HISTORY")
    print("=" * 50)
    if not history_log:
        print("  (No calculations performed yet in this session.)")
    else:
        for idx, item in enumerate(history_log, 1):
            print(f"  [{idx}] {item}")
    print("=" * 50)
    input("\nPress Enter to return to the Main Menu...")


# =============================================================================
# 6. MAIN APPLICATION MENU
# =============================================================================

def print_main_banner():
    """Display project header banner."""
    print("\n" + "=" * 65)
    print("      🚀 INTERACTIVE CALCULATOR & UNIT CONVERTER (CLI) 🚀")
    print("                   InternCircle Project 01")
    print("=" * 65)


def main():
    """Main application loop with menu selection."""
    print_main_banner()

    while True:
        print("\n" + "─" * 45)
        print("                  MAIN MENU")
        print("─" * 45)
        print("  [1] ➕ Arithmetic Calculator (+, -, *, /, %, ^)")
        print("  [2] 📏 Unit Converter (km/miles, °C/°F, m/ft, kg/lbs)")
        print("  [3] 💱 Currency Converter (USD, INR, EUR, GBP, CAD)")
        print("  [4] 📜 View Calculation History")
        print("  [5] ❌ Exit Program")
        print("─" * 45)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            run_arithmetic_calculator()
        elif choice == "2":
            run_unit_converter()
        elif choice == "3":
            run_currency_converter()
        elif choice == "4":
            view_history()
        elif choice == "5":
            print("\n" + "=" * 50)
            print("  Thank you for using Interactive Calculator & Unit Converter!")
            print("  InternCircle Project 01 • Built with Python")
            print("=" * 50 + "\n")
            sys.exit(0)
        else:
            print("⚠️  Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
