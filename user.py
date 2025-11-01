#One of the projects core classes

#Create the user class with functions


class User:
    """This class initialzies the user, essentially represents a user in UniSwap"""


    def __init__(self, user_id, name, email):

        """Initializes the User Object
        
        Args:
        user_id(str): Unique identifier for the user.
        
        name(str): The users name.
        
        email(str): The users email address. """


        self.user_id = user_id
        self.name = name
        self.email = email
    
    def to_dict(self):
 
        """This function converts user data to dictionary format (JSON)"""
        """Returns:
            dict: Dictionary representation of the user."""
        return{
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email

        }
    
    @staticmethod

    def from_dict(data):
        """Creates a User object from the dictionary.
        
        Args:
            data(dict): Dictionary with user data.
        Returns:
            User: A new User object"""


        return User(data["user_id"], data["name"], data["email"])

    def  __str__(self):
        """Returns:
            str: Formatted user display."""
        return f"{self.name} ({self.email})"