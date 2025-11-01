class Item:
    """Represents an item listed in UniSwap"""

    def __init__(self, item_id, name, category, condition, owner_id, is_traded = False):
        """
        Initialize an Item object.
        
        Args:
            item_id(str): Unique identifier for the item.
            name(str): Name of the item.
            category(str): Category(What category the item pertains)
            condition(str): Description of the items condition(Good, new, used)
            owner_id(str): The user_id of the items owner.
            is_traded(bool): Whether the item has been traded or not. It will always default to false"""
        self.item_id = item_id
        self.category =  category
        self.name = name 
        self.owner_id = owner_id
        self.condition = condition
        self.is_traded = is_traded

    def to_dict(self):
        """This function converts item data to dict """

        return{
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "owner_id": self.owner_id,
            "is_traded": self.is_traded,
            "condition": self.condition
        }
    

    @staticmethod
    def from_dict(data):
        """This function reconstruct an Item object from a dict"""
        return Item(**data)

    def __str__(self):

        """Returns a readable string.
        
        Returns:
            str: Formatted item display"""
        status = "Traded" if self.is_traded else "Available"
        return f"[{self.item_id}] {self.name} ({self.category}) - {self.condition} | Owner: {self.owner_id} | {status}"