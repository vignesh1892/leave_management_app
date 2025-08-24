import requests
from utils import logger,BASE_URL

def show_menu():
    print("\n===== Leave Management System =====")
    print("1. Add Leave")
    print("2. View All Leave Categories")
    print("0. Exit")
    choice = input("Enter choice: ")
    return choice.strip()

def print_leaves(leaves):
    if not leaves:
        print("No leave categories found.")
        return

    print("\n{:<5} {:<20}".format("ID", "Name"))
    print("-" * 30)
    for c in leaves:
        print("{:<5} {:<20}".format(c.get("id", "-"), c.get("name", "-")))

def main():
    while True:
        choice = show_menu()

        try:
            if choice == "1":
                desc = input("Enter description: ")
                empname = input("Enter Name: ")
                date = input("Enter date (YYYY-MM-DD): ")
                lev_id = input("Enter leave_id (or leave blank): ")
                lev_id = int(lev_id) if lev_id else None
                payload = {"description": desc, "empname": empname, "date": date, "leave_id": lev_id}

                try:
                    r = requests.post(f"{BASE_URL}/add_leave", json=payload)
                    r.raise_for_status()
                    print(r.json())
                    logger.info(f"Applied leaves: {payload}")
                except requests.exceptions.RequestException as req_err:
                    logger.error(f"Request error while applying leaves: {req_err}")
                    print("Failed to apply leaves. Check logs for details.")

            elif choice == "2":
                try:
                    r = requests.get(f"{BASE_URL}/get_leaves")
                    r.raise_for_status()
                    leaves = r.json()
                    print_leaves(leaves)
                    logger.info(f"Fetched {len(leaves)} leaves")
                except requests.exceptions.RequestException as req_err:
                    logger.error(f"Request error while fetching leaves: {req_err}")
                    print("Failed to fetch leaves. Check logs for details.")
            elif choice == "0":
                print("Exiting...")
                logger.info("User exited the program")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as ve:
            logger.error(f"Invalid input: {ve}")
            print("Invalid input. Please enter correct values.")

        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            print("An unexpected error occurred. Check logs for details.")

if __name__ == "__main__":
    main()
