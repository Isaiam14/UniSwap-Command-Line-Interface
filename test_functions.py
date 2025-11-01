import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user import User
from item import Item 
from storage import save_items, load_items, save_users, load_users

def test_user_save():
    user1 = User("u001", "Isai Amaya", "iamayadi@umd.edu")
    user2 = User("u002", "Matthew Patrick", "mdp@umd.edu")

    users = [user1, user2]

    test_file = "test/test_users.json"


    save_users(users, test_file)
    loaded_users = load_users(test_file)
    assert len(loaded_users) == 2
    assert loaded_users[0].name == "Isai Amaya"
    assert loaded_users[1].email == "mdp@umd.edu"

    os.remove(test_file)

    print("You have passed the test_user_save test!")

def test_item_save():
    item1 = Item("i001", "Vintage UMD T-Shirt", "Clothing", "Used","u001", is_traded = True)
    item2 = Item("i002", "Mini Fridge", "Appliances", "Good", "u001")

    items = [item1, item2]
    test_file = "test/test_items.json"
    save_items(items, test_file)
    
    loaded_items = load_items(test_file)

    assert len(loaded_items) == 2

    assert loaded_items[1].name == "Mini Fridge"

    assert loaded_items[0].is_traded is True
    os.remove(test_file)

    print("You have passed the test_item_save test!")

if __name__ == "__main__":
    test_item_save()
    test_user_save()
