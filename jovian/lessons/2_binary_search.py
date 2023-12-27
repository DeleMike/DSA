"""When solving problems try to come up with some edge cases apart from the general case
Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card 
containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
"""

test_cases = [{
    'input_params': {'cards': [], 'query': 0},
    'output': -1,
}]

tests = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2,
                         2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3,
                         2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}
]


def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        # if we have found query, we need to find its first value
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    """Binary Search Implementation

    Args:
        cards (list): List of cards
        query (int): card number to search

    Returns:
        int: position of query. if it does not exist, it returns -1
    """
    # set the two pointers to the beginning and end of array
    low, high = 0, len(cards) - 1
    
    
    while low <= high:
        # get the mid point - floor decimal points
        mid = (low + high) // 2
        mid_value = cards[mid]
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1
           
    return -1

for test in tests:
    print(locate_card(**test['input']) == test['output'])
