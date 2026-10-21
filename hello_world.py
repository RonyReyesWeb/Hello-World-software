"""Hello World — a friendly greeting program.

Prints the classic message, then greets the user by name
in English and Spanish.
"""
from datetime import datetime


def time_of_day_greeting(hour):
    """Return a greeting that matches the hour (0-23)."""
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    return "Good evening"


def main():
    # The classic first line every programmer writes
    print("Hello World")

    name = input("What's your name? ").strip() or "friend"
    greeting = time_of_day_greeting(datetime.now().hour)
    print(f"{greeting}, {name}!")

    # Same welcome in two languages
    for word in ["Welcome", "Bienvenido"]:
        print(f"{word}, {name}!")


if __name__ == "__main__":
    main()
