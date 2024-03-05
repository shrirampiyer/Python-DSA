max_size = 100
hash_table = [None] * 100 
def hash(key, value):
  hash_val = 0
  for i in key:
    hash_val += ord(i)
  hash_table.insert(hash_val//100, value)

def retrieve(key):
  hash_val = 0
  for i in key:
    hash_val += ord(i)
  return hash_table[hash_val//100]

hash('shriram','shrirampiyerthepatriot@gmail.com')
print(retrieve('shriram'))  
