#question 2 task 1
def length_of_name(name):
    return len(name) >= 2

def user_name(prompt):
    while True:
        name = input(prompt).strip()
        if length_of_name(name):
            return name
        else:
            print("You're name must be 2 characters long.")

def main():
    first_name = user_name("Enter your first name: ")
    last_name = user_name("Enter your last name: ")
    print(f"You're first name is '{first_name}' and your last name is '{last_name}'.")

if __name__ == "__main__":
    main()