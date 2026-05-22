from manager.manager_logic import *

def menu():
    while True:
        print("\n===== Password Manager =====")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. List Sites")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            site = input("Site: ").strip()
            user = input("Username: ").strip()
            pwd = input("Password (blank = auto): ").strip()

            if not site or not user:
                print("❌ Site & Username required")
                continue

            print("✅ Saved:", add_password(site, user, pwd if pwd else None))

        elif choice == "2":
            site = input("Site: ").strip()
            user, pwd = get_password(site)

            if user:
                print("Username:", user)
                print("Password:", pwd)
            else:
                print("❌ Not found")

        elif choice == "3":
            site = input("Site: ").strip()
            print("Deleted" if delete_password(site) else "Not found")

        elif choice == "4":
            print("Sites:", list_sites())

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()