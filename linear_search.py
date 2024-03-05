
def locate_cards(cards, query):
    for i in cards:
        if cards[i] == query:
            print( f"Element {cards[i]}, found at location {i}")
            return f"Element {cards[i]}, found at location {i}"
    
cards = [1,2,3,4,5,6,7,8,9,10]
query = 9

locate_cards(cards, query)