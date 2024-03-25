# cli.py
from helper import (
    list_users,
    find_user_by_name,
    find_user_by_id,
    add_new_user,
    list_movies,
    find_movie_by_title,
    add_new_movie,
    exit_program
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_users()
            input("Press ENTER to Continue")
        elif choice == "2":
            find_user_by_name()
            input("Press ENTER to Continue")
        elif choice == "3":
            find_user_by_id()
            input("Press ENTER to Continue")
        elif choice == "4":
            add_new_user()
            input("Press ENTER to Continue")
        elif choice == "5":
            list_movies()
            input("Press ENTER to Continue")
        elif choice == "6":
            find_movie_by_title()
            input("Press ENTER to Continue")
        elif choice == "7":
            add_new_movie()
            input("Press ENTER to Continue")
        elif choice == "8":
            exit_program()
        else:
            print("Invalid choice")

def menu():
    print("1. List all users")
    print("2. Find user by name")
    print("3. Find user by id")
    print("4. Enroll new user")
    print("5. List all movies")
    print("6. Find movie by title")
    print("7. Add new movie")
    print("8. Exit the program")
    print("Please select an option:")

if __name__ == "__main__":
    main()
