baskets = [
  ["Cat", "and", "dog", "bites"],
  [
    "Yahoo",
    "news",
    "claims",
    "a",
    "cat",
    "mated",
    "with",
    "a",
    "dog",
    "and",
    "produced",
    "viable",
    "offspring",
  ],
  ["Cat", "killer", "likely", "is", "a", "and", "big", "dog"],
  [
    "Professional",
    "free",
    "advice",
    "on",
    "dog",
    "training",
    "puppy",
    "training",
  ],
  ["Cat", "and", "kitten", "training", "and", "behavior"],
  ["Dog", "&", "Cat", "provides", "dog", "training", "in", "Eugene", "Oregon"],
  [
    "Dog, and, cat",
    "is",
    "a",
    "slang",
    "term",
    "used",
    "by",
    "police",
    "officers",
    "for",
    "a",
    "male–female",
    "relationship",
  ],
  [
    "Shop",
    "for",
    "your",
    "show",
    "dog",
    "grooming",
    "and",
    "pet",
    "cat",
    "supplies",
  ],
]

def preprocess_dataset():
  global baskets
  temp_baskets = []
  
  for i in range(len(baskets)):
    for j in range(len(baskets[i])):
      baskets[i][j] = baskets[i][j].lower()
  
  for basket in baskets:
    temp_basket = sorted(set(basket))
    temp_baskets.append(temp_basket)
  baskets = temp_baskets