"""
implement binary search

return index: int or None
index: is the index in the original list of the target
return None if not found
"""

def exists(l: list, target)->bool:
    midpoint: int = len(l) // 2
    if target > l[midpoint]:
        # print(f"{target=} is larger than the {midpoint=}, so now the list is: {l[midpoint:]}")
        return exists(l=l[midpoint:], target=target)
    if target < l[midpoint]:
        # print(f"{target=} is smaller than the {midpoint=}, so now the list is: {l[0:midpoint]}")
        return exists(l=l[0:midpoint], target=target) 
    elif target == l[midpoint]:
        # print(f"{target=} and {midpoint=}, so now the list is: {l[midpoint:]}")
        return True
    else:
        return False


def BinarySearch(l: list, target)->int|None:
    index: int = -1 
    if len(l) == 1:
        return 0
    midpoint: int = len(l) // 2







    

