
def locate_cards(cards, query):
    position = 0
    while True:
        if cards[position]==query:
            return position
        position += 1
        if len(cards) == position:
            return -1

tests = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
print(locate_cards(**test['input'])==test['output'])

#alternate solution using for loop and avoiding enumarate method 
def locate_cards(cards, query):
  pos = 0
  for i in cards:
    if i == query:
      return i,pos
    pos += 1

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7

#implementing using enumearate method in for loop
def locate_cards(cards, query):
    for i, card in enumerate(cards):
        if card == query:
            print(f"Element {query}, found at location {i}")
            return f"Element {query}, found at location {i}"

tests = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 'Element 7, found at location 3'
}

print(locate_cards(**tests['input']) == tests['output'])
