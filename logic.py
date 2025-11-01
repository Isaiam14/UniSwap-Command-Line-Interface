#This is a pure logic function that can be tested. 

def simulate_swap(item1, item2):
    """This function marks two items as traded if the item is not already traded."""

    if item1.is_traded or item2.is_traded:
        return False

    item1.is_traded = True 
    item2.is_traded = True

    return True