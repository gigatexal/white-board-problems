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
    take input strings like "elm", "flower" etc and convert to string of numbers. for elm this would be "356", 
    converting the input string to lower case before processing the input
    find "356" in target string of numbers in this case: find "356" in "3569377"
    repeat for all words in input list
    return all that fit

the above solution is O(1) map lookup * O(length of the word) * n number of words O(nxm)?
"""
MAPPER: dict[str, str] = {
            'a':'2',
            'b':'2',
            'c':'2',
            'd':'3',
            'e':'3',
            'f':'3',
            'g':'4',
            'h':'4',
            'i':'4',
            'j':'5',
            'k':'5',
            'l':'5',
            'm':'6',
            'n':'6',
            'o':'6',
            'p':'7',
            'q':'7',
            'r':'7',
            's':'7',
            't':'8',
            'u':'8',
            'v':'8',
            'w':'9',
            'x':'9',
            'y':'9',
            'z':'9'
}

def convert_word_to_number(word: str, mapping=MAPPER)->str:
    processed_word: str = ''.join([mapping[letter] for letter in word.lower()])
    return processed_word

def substring_exists(needle: str, haystack: str)->bool:
    return needle in haystack

if __name__ == '__main__':
    search_space: str = "3569377"
    words = ['elm','FLOWER','flOWERS','foobar','flow']
    words_filtered = [word for word in words if substring_exists(needle=convert_word_to_number(word), haystack=search_space)]
    print(words_filtered)

