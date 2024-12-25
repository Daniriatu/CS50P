def main():
    usr_input = input("Greeting: ")
    dollor = value(usr_input)
    print(f"${dollor}")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
