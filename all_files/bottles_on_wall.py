# Ninety-nine bottles of milk on the wall, ninety-nine bottles of milk. take one down pass it around, ninety-eight bottles of milk on the wall.
import inflect
import pandas as pd
import numpy as np
p = inflect.engine()
for i in range(int(input("Enter a number: ")), 0, -1):
    if i > 1:
        print(f"{(p.number_to_words(i)).capitalize()} bottles of milk on the wall, {p.number_to_words(i)} bottles of milk. take one down pass it around, {p.number_to_words(i-1)} bottles of milk on the wall.")
        i -= 1
        continue
    print("One bottle of milk on the wall, one bottle of milk. Take it down pass it around, no more bottles of milk on the wall.")

mydict = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
mmnh = pd.DataFrame(mydict, index=[23, 24, 25, 26])
# print(mmnh)
