import auth


def register_flow():
    print("\n--- User registration ---")
    u = input("Create a username: ")
    p = input("Create a password: ")

    success, message = auth.save_user(u, p)
    print(message)


def login_flow():
    print("\n--- Login ---")
    u = input("Username: ")
    p = input("Password: ")

    if auth.verify_credentials(u, p):
        print(f"\nWelcome! @{u.strip().lower()}")
        print("Access granted to the secure system.")
    else:
        print("\nAccess denied. Invalid credentials.")

def main():
    print("=== DEFENSIVE AUTH SYSTEM v2.0 ===")
    print("1. Login..")
    print("2. Register New User")
    option = input("Select an option (1/2): ").strip()

    if option == "1":
        login_flow()
    elif option == "2":
        register_flow()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()