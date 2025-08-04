def greet(name):
    """
    Greets the user with the provided name.
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet(user_name)