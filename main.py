from user import User 
from item import Item 
from storage import save_items, save_users, load_items, load_users

"""main.py is a CLI

A CLI is a type of user interface that allows you to interact with a program by typing commands into the terminal.

I implemented this Command Line Interface for my UniSwap application. 
"""


def generate_user_id(users):
    """Args:
        users(list): Existing users
    Returns:
        str: New user ID"""
    #Simple function that generates the user of the current user
    return f"u{1000 + len(users)}"





def generate_item_id(items):

    """Args:
        items(list): Existing items
    Returns:
        str: New item ID"""
    #Simple function that generates the item id 
    return f"i{1000 + len(items)}"

def add_user(users):

    """Tells the user to enter user details and adds another User to the list
    
    Args:
        users(list): List of current users"""
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    if not name or not email:
        print("Please enter a name and a valid email.")
        return

    user_id = generate_user_id(users)
    user = User(user_id, name, email)
    users.append(user)
    print(f"User '{name} ' added with ID {user_id}")

def add_item(items, users):
    """Tells the user to add an item associated with the user"""
    if not users:
        print("Registered user not found. Please add a user first.")
        return

    print("Choose owner: ")

    for idx, user in enumerate(users):
        print(f"{idx+1}. {user.name} ({user.email})")
    try:
        owner_choice = int(input("Enter number: ")) - 1
        owner = users[owner_choice]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return 
    
    name = input("Item name: ").strip()

    category = input("Category (e.g. clothing, electronic, supplies): ").strip()
    
    condition = input("Condition (e.g. new, used, fair): ").strip()
    if not name or not category or not condition:
        print("These fields are required.")
        return


    item_id = generate_item_id(items)
    item = Item(item_id, name, category,condition, owner.user_id)
    items.append(item)
    print(f"Item '{name}' added with ID {item_id}")

def list_items(items):
    """Prints all items currently in the system. 
    Args:
        items(list): List of items"""
    if not items:
        print("No items found.")
    else:
        for item in items:
            print(f"-{item}")

def list_users(users):
    """Prints all the users registered.
    
    Args:
        users(list): List users
        """
    if not users:
        print("No users found.")
    else: 
        for user in users:
            print(f"-{user}")
        
def search_items(items):

    """Searches items by keyword or category.
    
    Args: 
        items(list): List of ites to search."""
    term = input("Search keyword or category: ").strip().lower()
    results = []
    for item in items:
        if term in item.name.lower() or term in item.category.lower():
            results.append(item)
    if not results:
        print("No items were found that matched your search.")
    else:
        print("Search results: ")
        for item in results:
            print(f"- {item}")

def main():
    """Main loop for the UniS"""
    users = load_users()
    items = load_items()

    while True:
        print("\n=== UniSwap ===")
        print("1. Add user")
        print("2. Add item")
        print("3. List users")
        print("4. List items")
        print("5. Search items")

        print("6. Make a Uniswap")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_user(users)

        elif choice == "2":
            add_item(items,users)
        elif choice == "3":
            list_users(users)
        elif choice == "4":

            list_items(items)
        elif choice == "5":
            search_items(items)
        elif choice == "6":
            make_swap(items,users)
        elif choice == "7":
            save_users(users)

            save_items(items)

            print("Thank you. Data saved. Comeback and UniSwap later :) ")
            break

        else:
            print("Invalid. Please try again.")

def make_swap(items, users):

    """This is the swap system between users. The useres can exchange or swap items. 
    
    Args:
        items(list): List of available items. 
        users(list): List of users"""
    available_items = [item for item in items if not item.is_traded]
    if len(available_items) < 2:
        print("Not enough available items to do a swap.")
        return

    print("Choose the item you want to receive: ")
    for idx, item in enumerate(available_items):
        print(f"{idx+1}. {item.name} (Owned by: {item.owner_id})")

    try:
        target_index = int(input("Enter number: ")) - 1
        target_item = available_items[target_index]
    except (IndexError, ValueError):
        print("Invalid selection.")
        return

    #This will only show items from different owners
    my_items = [item for item in available_items if item.owner_id != target_item.owner_id]
    if not my_items:
        print("No items available to offer from other users")
        return 

    print("\nChoose one of your items to exchange them:")
    for idx, item in enumerate(my_items):
        print (f"{idx+1}. {item.name} (Owned by: {item.owner_id})")

    try:
        offer_index = int(input("Enter number: ")) - 1
        offered_item = my_items[offer_index]
    except(IndexError, ValueError ):
        print("Invalid selection.")
        return

    #This is to confirm the swap with the other seller 
    confirm = input(f"\nConfirm swap '{offered_item.name}' for '{target_item}' Are you sure you want to swap? (y/n): ").lower()
    if confirm == 'y':
        target_item.is_traded = True

        offered_item.is_traded = True
        print("The Uniswap has been successfull! Both items were marked as traded.")
    else:
        print("Swap has been canceled.")




if __name__ == "__main__":
    main()





    





