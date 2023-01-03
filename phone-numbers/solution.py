"""
-------------------------
|       |  ABC  |  DEF  |
|   1   |   2   |   3   |
-------------------------
|  GHI  |  JKL  |  MNO  |
|   4   |   5   |   6   |
-------------------------
| PQRS  |  TUV  | WXYZ  |
|   7   |   8   |   9   |
-------------------------

given that and a vanity number like

1-800-flowers which the flowers bit would translate to 3569377 for the full number being 1-800-3569377

given a list of numbers after the 1-800- part e.g. 3569377 and a list of possible words like "elm", "flower", "flowers", "apples", "pears", "trucks", "fastcars" etc

where the given words are between 1 and 7 letters inclusive as that is the max length for a valid phone number.

- find all the words that could fit within the target number -- note: candidates need not be the exact length they could be any length 1 to 7 inclusive as was said

In the above example elm, flower, flowers all fit but the others do not. 
"""

"""
algo:
    map letters to integers store as string
    take input strings like "elm", "flower" etc and convert to string of numbers. for elm this would be "356".
    find "356" in target string of numbers in this case: find "356" in "3569377"
    repeat for all words in input list
    return all that fit
"""


