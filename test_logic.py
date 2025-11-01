import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from item import Item 
from logic import simulate_swap

def test_simulate_swap():
    #This function will create two tradable items 
    item1 = Item("i001", "Monitor", "Electronics", "Good", "u001")

    item2 = Item("i002", "Night Stand", "Furniture", "Fair", "u002")

    #This should allow the swap and mark both as traded
    result = simulate_swap(item1, item2)
    assert result is True 

    assert item1.is_traded
    assert item2.is_traded

    """If the user attempts to trade an already traded item, it will fail, which is what this test is looking for"""

    item3 = Item("i003", "Camera", "Electronics", "Used", "u003", is_traded = True)
    result = simulate_swap(item1, item3)
    
    assert result is False
    assert item3.is_traded is True



    print("You passed the test!")

if __name__ == "__main__":
    test_simulate_swap()

