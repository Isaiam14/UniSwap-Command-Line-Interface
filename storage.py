import json
from user import User
from item import Item

def save_users(users, filename = "data/users.json"):
    """Save the list of Users object to a JSON file
    
    Args:
        users(list of User): List of User objects to save.
        filename(str): Path to the output JSON file.  """
    with open(filename, "w") as f:
        json.dump([user.to_dict() for user in users], f, indent = 4)



def load_users(filename = 'data/users.json'):
    """Loads the USer Objects from the JSON file.
    
    Args:
        filename(str): Path to the JSON file. Defaults to "data/users.json". 
        
    Returns: 
    list of User"""
    try: 
        with open (filename, "r") as f:
            data = json.load(f)
            return [User.from_dict(entry) for entry in data]
    except FileNotFoundError:
        return []

def save_items(items, filename = "data/items.json"):

    """Saves a lost of Item Objects into a JSON file
    
    Args:
        items(list of Item): List of item objects to save.
        """
    with open (filename, "w") as f:
        json.dump([item.to_dict() for item in items], f, indent = 4)

def load_items(filename = 'data/items.json'):

    """Load item obejcts from JSON
    
    Args:
        filename(str): path to the JSON file
        
    Returns: 
        list of Item: A list of Item obejcts loaded from the file"""
    try: 
        with open (filename, "r") as f:
            data = json.load(f)
            return [Item.from_dict(entry) for entry in data]
    except FileNotFoundError:
        return []